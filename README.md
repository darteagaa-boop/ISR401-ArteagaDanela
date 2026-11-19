# ISR401-ArteagaDanela

Repositorio personal de **Danela Dayana Arteaga Alava** para la asignatura
**Ingeniería de Requerimientos (ISR-401)**, 4.º nivel, Paralelo B,
Universidad Técnica Estatal de Quevedo.

Docente: Gleiston Cicerón Guerrero Ulloa, PhD.

## Contenido

| Carpeta | Actividad | Archivo principal |
|---|---|---|
| `FORM-TL-01/` | Taller de tipos de requisitos (actividad formativa, Semana 1) | `FORM-TL-01/main.tex` |
| `TA-IND-01/` | Trabajo individual: IEEE 29148 y tipos de requisitos de Apple Music (sumativa) | `TA-IND-01/main.tex` |
| `EV-PRAC-01/` | Evaluación de la Unidad I (prueba práctica, transcripción fiel) | `EV-PRAC-01/main.tex` |

Archivos de `FORM-TL-01/`:

- `main.tex`: documento fuente en LaTeX.
- `referencias.bib`: referencias bibliográficas (estilo IEEE con `biblatex`).

Archivos de `TA-IND-01/`:

- `main.tex`: documento fuente en LaTeX.
- `referencias.bib`: referencias bibliográficas (estilo IEEE con `biblatex`).
- `figuras/`: capturas propias de Apple Music (`captura-inicio.jpg`, `captura-biblioteca.jpg`, `captura-reproductor.jpg`).

Archivos de `EV-PRAC-01/`:

- `main.tex`: transcripción fiel de la prueba escrita a mano.
- `main.pdf`: PDF compilado desde `main.tex`.
- `evidencias/`: fotografías de las hojas originales (`hoja-01.jpg` a `hoja-04.jpg`), que no se incluyen en el PDF.

## Cómo compilar

### Compilador y orden de comandos

Compilador: `pdflatex`, con `biber` para la bibliografía. Cada actividad se
compila desde su carpeta. Por ejemplo, desde la raíz del repositorio:

```bash
cd FORM-TL-01        # o: cd TA-IND-01
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

El resultado es `main.pdf` dentro de la carpeta de cada actividad.

### Dependencias

- Distribución LaTeX: TeX Live 2022 o posterior, o MiKTeX actualizado.
- Clase: `IEEEtran`.
- Paquetes: `fontenc`, `inputenc`, `babel` (idioma `spanish`), `lmodern`,
  `microtype`, `csquotes`, `amsmath`, `amssymb`, `booktabs`, `float`,
  `tabularx`, `array`, `longtable`, `graphicx`, `url`, `hyperref` y `biblatex`
  con el estilo `ieee` (paquete `biblatex-ieee`).
- Gestor de bibliografía: `biber`.

En Overleaf: subir la carpeta de la actividad completa (incluida `figuras/` si existe), elegir el compilador
pdfLaTeX y compilar, y Overleaf ejecuta `biber` automáticamente.

### Compilar EV-PRAC-01

EV-PRAC-01 no tiene bibliografía, así que no usa `biber`. Desde la raíz del repositorio:

```bash
cd EV-PRAC-01
pdflatex main.tex
pdflatex main.tex
```

El resultado es `EV-PRAC-01/main.pdf`. Usa la clase `IEEEtran` y los paquetes `fontenc`,
`inputenc`, `babel` (idioma `spanish`), `lmodern`, `microtype`, `booktabs`, `float`, `array`,
`longtable`, `url` y `hyperref`.
