"""Cálculos de TA-IND-02: tabulación de Kano, votación de 100 puntos y
correlación de rangos de Spearman entre MoSCoW y la votación.
Uso, desde la carpeta TA-IND-02:  python datos/calculos.py
Solo usa la biblioteca estándar de Python 3."""
import csv
from collections import Counter, defaultdict
from pathlib import Path

D = Path(__file__).resolve().parent
TABLA_KANO = ['QAAAO', 'RIIIM', 'RIIIM', 'RIIIM', 'RRRRQ']  # filas: funcional, columnas: disfuncional
ORDEN_MOSCOW = ['Must', 'Should', 'Could', "Won't"]


def leer(nombre):
    with open(D / nombre, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def escribir(nombre, encabezado, filas):
    with open(D / nombre, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(encabezado)
        w.writerows(filas)


def rangos(valores, descendente=False):
    """Rango 1 = primero. Los empates reciben el rango promedio."""
    idx = sorted(range(len(valores)), key=lambda i: valores[i], reverse=descendente)
    r = [0.0] * len(valores)
    i = 0
    while i < len(idx):
        j = i
        while j + 1 < len(idx) and valores[idx[j + 1]] == valores[idx[i]]:
            j += 1
        promedio = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[idx[k]] = promedio
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / (sxx * syy) ** 0.5


# 1. Kano: categoría de cada respuesta y categoría final por mayoría
kano = leer('kano_respuestas.csv')
caracteristicas = {c['caracteristica']: c for c in leer('caracteristicas_kano.csv')}
conteo = defaultdict(Counter)
for fila in kano:
    cat = TABLA_KANO[int(fila['respuesta_funcional']) - 1][int(fila['respuesta_disfuncional']) - 1]
    assert cat == fila['categoria_kano'], f"Categoría mal tabulada en {fila}"
    conteo[fila['caracteristica']][cat] += 1
filas_kano = []
for c in sorted(conteo):
    mas = conteo[c].most_common()
    empate = len(mas) > 1 and mas[0][1] == mas[1][1]
    final = '/'.join(k for k, v in mas if v == mas[0][1]) if empate else mas[0][0]
    filas_kano.append([c, caracteristicas[c]['requisito'], caracteristicas[c]['nombre']]
                      + [conteo[c][k] for k in 'AOMIRQ'] + [final])
escribir('resultados_kano.csv', ['caracteristica', 'requisito', 'nombre', 'A', 'O', 'M', 'I', 'R', 'Q', 'categoria_final'], filas_kano)

# 2. Votación de 100 puntos
votos = leer('votacion.csv')
participantes = sorted({v['participante'] for v in votos})
puntos = defaultdict(dict)
for v in votos:
    puntos[v['requisito']][v['participante']] = int(v['puntos'])
for p in participantes:
    total_p = sum(puntos[r][p] for r in puntos)
    assert total_p == 100, f"{p} repartió {total_p} puntos"
moscow = leer('moscow.csv')
ids = [m['requisito'] for m in moscow]
totales = [sum(puntos[r].values()) for r in ids]
rango_voto = rangos(totales, descendente=True)
escribir('resultados_votacion.csv', ['requisito'] + participantes + ['total', 'rango_votacion'],
         [[r] + [puntos[r][p] for p in participantes] + [t, rv] for r, t, rv in zip(ids, totales, rango_voto)])

# 3. Spearman entre MoSCoW y votación (rangos promedio en los empates)
nivel = [ORDEN_MOSCOW.index(m['categoria']) for m in moscow]
rango_moscow = rangos(nivel)
rho = pearson(rango_moscow, rango_voto)
n = len(ids)
d2 = [(a - b) ** 2 for a, b in zip(rango_moscow, rango_voto)]
rho_simple = 1 - 6 * sum(d2) / (n * (n ** 2 - 1))
kano_de = {f[1]: f[-1] for f in filas_kano}
escribir('resultados_comparacion.csv',
         ['requisito', 'categoria_moscow', 'rango_moscow', 'total_votacion', 'rango_votacion', 'd2', 'categoria_kano'],
         [[r, m['categoria'], rm, t, rv, dd, kano_de.get(r, '')]
          for r, m, rm, t, rv, dd in zip(ids, moscow, rango_moscow, totales, rango_voto, d2)])

print('Kano (categoría final por característica):')
for f in filas_kano:
    print(f'  {f[0]} {f[1]:6} {f[-1]}  A={f[3]} O={f[4]} M={f[5]} I={f[6]} R={f[7]} Q={f[8]}')
print(f'Spearman MoSCoW vs votación (Pearson sobre rangos, con empates): rho = {rho:.4f}')
print(f'Referencia, fórmula simplificada sin corregir empates: {rho_simple:.4f}')
print(f'Suma de d^2 = {sum(d2):.2f}, n = {n}')
