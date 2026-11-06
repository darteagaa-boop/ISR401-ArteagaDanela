# ISR401-ArteagaDanela

Repositorio personal de **Danela Dayana Arteaga Alava** para la asignatura
**Ingeniería de Requerimientos (ISR-401)**, 4.º nivel, Paralelo B,
Universidad Técnica Estatal de Quevedo.

Docente: Gleiston Cicerón Guerrero Ulloa, PhD.

## Contenido

| Carpeta | Actividad | Archivo principal |
|---|---|---|
| `FORM-TL-01/` | Taller de tipos de requisitos (actividad formativa, Semana 1) | `FORM-TL-01/main.tex` |

Archivos de `FORM-TL-01/`:

- `main.tex`: documento fuente en LaTeX.
- `referencias.bib`: referencias bibliográficas (estilo IEEE con `biblatex`).

## Cómo compilar

### Compilador y orden de comandos

Compilador: `pdflatex`, con `biber` para la bibliografía. Desde la raíz del
repositorio:

```bash
cd FORM-TL-01
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

El resultado es `FORM-TL-01/main.pdf`.

### Dependencias

- Distribución LaTeX: TeX Live 2022 o posterior, o MiKTeX actualizado.
- Clase: `IEEEtran`.
- Paquetes: `fontenc`, `inputenc`, `babel` (idioma `spanish`), `lmodern`,
  `microtype`, `csquotes`, `amsmath`, `amssymb`, `booktabs`, `float`,
  `tabularx`, `array`, `longtable`, `url`, `hyperref` y `biblatex`
  con el estilo `ieee` (paquete `biblatex-ieee`).
- Gestor de bibliografía: `biber`.

En Overleaf: subir `main.tex` y `referencias.bib`, elegir el compilador
pdfLaTeX y compilar; Overleaf ejecuta `biber` automáticamente.
