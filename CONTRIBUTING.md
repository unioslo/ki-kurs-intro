# Contributing Guide

## Lokal utviklingsmiljø / Local Development Environment

### 1. Klon repositoriet / Clone the repository

```bash
git clone https://github.com/unioslo/ki-kurs-intro.git
cd ki-kurs-intro
```

### 2. Sett opp Python virtual environment

```bash
# Opprett virtual environment
python3 -m venv .venv

# Aktiver virtual environment
source .venv/bin/activate  # macOS/Linux
# eller
.venv\Scripts\activate     # Windows
```

### 3. Installer Python-avhengigheter

```bash
pip install -r requirements.txt
```

### 4. Installer systembiblioteker for PDF-generering (valgfritt)

PDF-generering krever eksterne systembiblioteker. Dette er **valgfritt** - du kan jobbe med HTML uten disse.

#### macOS (Homebrew)

```bash
brew install cairo pango gdk-pixbuf libffi

# Reinstaller WeasyPrint for å linke mot systembibliotekene
pip install --force-reinstall --no-cache-dir weasyprint
```

#### Ubuntu/Debian

```bash
sudo apt-get install build-essential python3-dev python3-pip \
    libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info
```

#### Fedora/RHEL/CentOS

```bash
sudo dnf install python3-devel cairo pango gdk-pixbuf2 libffi-devel
```

#### Windows

Se [WeasyPrint Windows installasjon](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows).

**GTK3 Runtime** må installeres først, deretter:

```bash
pip install weasyprint
```

### 5. Bygg dokumentasjonen

```bash
# Bygg HTML (standard)
make html

# Bygg PDF (krever systembiblioteker)
make simplepdf
```

**Output:**
- HTML: `_build/html/`
- PDF: `_build/simplepdf/Grunnkurs KI.pdf`

## Arbeidsflyt / Workflow

### Mappestruktur (Oppdatert Juni 2026)

Innholdsfilene er organisert i moduler:

```
source/
  module1/        # Episode 1: Oppsummering av kurset
  module2/        # Episode 2: Grunnbegreper i kunstig intelligens
  module3/        # Episode 3: Hvordan fungerer språkmodeller?
  module4/        # Episode 4: Hvordan trygt bruke KI?
  module5/        # Episode 5: Etikk, bærekraft, opphavsrett og personvern
  module6/        # Episode 6: KI-tjenester ved UiO
  module7/        # Episode 7: Treningsoppgaver
  module8/        # Episode 8: Oppsummering
  index.rst       # Hovedindeks
```

**Viktig:** Filnavn bruker bindestreker (`-`) i stedet for understreker (`_`) og følger Canvas URL-konvensjoner:
- `kunstig-intelligens.rst` (ikke `kunstig_intelligens.rst`)
- Norske tegn: `å` → `a`, `æ` → `ae`, `ø` → `o`

### Endre innhold

1. Rediger filer i `source/moduleN/` (der N er modulnummer 1-8)
2. Bygg HTML: `make html`
3. Se resultatet i en nettleser:
   ```bash
   open _build/html/index.html  # macOS
   # eller
   xdg-open _build/html/index.html  # Linux
   # eller
   start _build/html/index.html  # Windows
   ```

### Legge til ny side

Når du legger til en ny RST-fil:

1. **Opprett filen** i riktig modul med Canvas-style navn:
   ```bash
   # Eksempel: Ny side i modul 2
   touch source/module2/ny-side.rst
   ```

2. **Bruk Canvas URL-format** for filnavn:
   - Bindestreker i stedet for mellomrom
   - Små bokstaver
   - `å` → `a`, `æ` → `ae`, `ø` → `o`

3. **Legg til i index.rst**:
   ```rst
   .. toctree::
      :maxdepth: 1
      :caption: Episode 2: ...
   
      module2/kunstig-intelligens
      module2/ny-side              # Legg til her
   ```

4. **Bygg og test**: `make html`

### Deploy til Canvas

Se [README_UPDATE_CANVAS.md](README_UPDATE_CANVAS.md) for fullstendig dokumentasjon om Canvas-oppdatering.

**Viktige kommandoer:**

```bash
# Oppdater én side
python div-support-filer/update_canvas_pages.py --page module2/kunstig-intelligens.html

# Hvis samme filnavn finnes i flere moduler, spesifiser full sti:
python div-support-filer/update_canvas_pages.py --page module2/oppsummering-kapittel-2.html

# Oppdater alle sider
python div-support-filer/update_canvas_pages.py

# Oppdater alle sider og legg til i moduler
python div-support-filer/update_canvas_pages.py --add-to-modules

# Dry-run (se hva som ville blitt oppdatert)
python div-support-filer/update_canvas_pages.py --dry-run
```

**Før første gangs bruk:**
1. Sett Canvas API-nøkkel: `export CANVAS_API_TOKEN="din_token"`
2. Generer mapping: `python div-support-filer/update_canvas_pages.py --generate-mapping`

## Vanlige problemer / Troubleshooting

### PDF-bygging feiler med "cannot load library 'libgobject-2.0-0'"

**Problem:** WeasyPrint kan ikke finne systembiblioteker.

**Løsning:** 
1. Installer systembiblioteker (se steg 4 over)
2. Reinstaller WeasyPrint:
   ```bash
   pip install --force-reinstall --no-cache-dir weasyprint
   ```

### "No module named 'sphinx'"

**Problem:** Virtual environment er ikke aktivert eller avhengigheter ikke installert.

**Løsning:**
```bash
source .venv/bin/activate  # Aktiver virtual environment
pip install -r requirements.txt
```

### Endringer vises ikke

**Problem:** Sphinx bruker caching.

**Løsning:**
```bash
make clean
make html
```

## GitHub Actions CI/CD

GitHub Actions bygger automatisk HTML-versjon ved push til enhver branch. Publiseres til GitHub Pages:

- **Main branch**: `https://unioslo.github.io/ki-kurs-intro/`
- **Andre branches**: `https://unioslo.github.io/ki-kurs-intro/branches/<branch-navn>/`

**Merk:** GitHub Actions bygger **kun HTML**, ikke PDF. PDF-bygging må gjøres lokalt.

Workflow-fil: `.github/workflows/static_pages.yml`

### GitHub Pages Settings

Gå til repository Settings → Pages og sørg for:
- **Source**: Deploy from a branch
- **Branch**: `gh-pages` / `/ (root)`

## Ressurser

- [Sphinx dokumentasjon](https://www.sphinx-doc.org/)
- [reStructuredText (RST) guide](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [WeasyPrint dokumentasjon](https://doc.courtbouillon.org/weasyprint/)
