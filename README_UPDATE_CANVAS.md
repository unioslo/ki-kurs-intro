# Canvas API Skript - Dokumentasjon

**OPPDATERT Juni 2026**: Skriptet er omskrevet for å støtte ny modul-basert mappestruktur og håndtere duplikate filnavn på tvers av moduler.

Skriptet `div-support-filer/update_canvas_pages.py` kan automatisk oppdatere Canvas-sider basert på de genererte HTML-filene.

## Viktige endringer fra tidligere versjon

- ✅ **Støtte for modul-basert mappestruktur**: HTML-filer nå i `module1/`, `module2/`, etc.
- ✅ **Håndtering av duplikate filnavn**: Samme filnavn (f.eks. `oppsummering.html`) kan finnes i flere moduler
- ✅ **Relative stier i mapping**: Mapping bruker nå `module2/oppsummering.html` i stedet for bare `oppsummering.html`
- ✅ **Ny kommando for moduloppretting**: `--create-module` for å opprette moduler med egendefinerte navn
- ✅ **Forbedret enkeltsideoppdatering**: `--page` kan nå ta både filnavn og full sti

## Funksjonalitet

Skriptet gjør følgende:
- Leser HTML-filer fra `_build/html/module*/` (ved lokal oppdatering) eller `html/module*/` (ved deploy fra GitHub)
- Henter ut `<h1>` tittel fra hver HTML-fil og bruker denne som sidetittel i Canvas
- Canvas genererer automatisk page URL basert på sidetittelen (f.eks. "Hva er KI?" → `hva-er-ki`)
- Henter ut hovedinnholdet og fjerner `<h1>` elementer og navigasjon (siden Canvas legger til tittel automatisk)
- Oppdaterer Canvas-sider via REST API basert på page ID mapping
- Kan bygge opp mapping mellom HTML-filer og Canvas page IDs
- Støtter deploy fra GitHub html-pages branch
- Støtter dry-run mode for å se hva som vil bli oppdatert uten å gjøre endringer
- **Automatisk bildehåndtering**: Finner alle bilder i HTML, laster dem opp til Canvas, og oppdaterer `<img>` tags med Canvas URLer
- **Automatisk håndtering av interne lenker**: Konverterer Sphinx cross-references til Canvas page URLs
- **Modulhåndtering**: Filer i `moduleN/` blir automatisk tilordnet Module N

## Sette opp API-nøkkel

For å bruke skriptet trenger du en Canvas API-nøkkel:

1. Gå til https://uio.instructure.com/profile/settings
2. Scroll ned til "Approved Integrations"
3. Klikk "+ New Access Token"
4. Generer og kopier nøkkelen
5. Sett miljøvariabelen:
   ```bash
   export CANVAS_API_TOKEN="din_token_her"
   ```

## Mappesstruktur

Skriptet forventer HTML-filer i modul-undermapper:

```
_build/html/
    module1/
        generativ_ki.html
        kunstig_intelligens.html
        oppsummering.html
    module2/
        store_spraakmodeller.html
        oppsummering.html          # Samme filnavn, men annen modul
    module3/
        instruksjoner.html
        oppsummering.html          # Samme filnavn, men annen modul
    ...
```

**Moduloppdeling**: Filer i `moduleN/` blir automatisk tilordnet Module N når du bruker `--add-to-modules`.

## Opprette moduler

Før du kan bruke `--add-to-modules`, må modulene eksistere i Canvas. Du kan opprette dem manuelt i Canvas eller bruke skriptet:

```bash
# Opprett modul 1 med egendefinert navn
python div-support-filer/update_canvas_pages.py --create-module 1 --module-name "Grunnbegreper i kunstig intelligens"

# Opprett modul 2
python div-support-filer/update_canvas_pages.py --create-module 2 --module-name "Hvordan fungerer språkmodeller"

# Opprett modul 3
python div-support-filer/update_canvas_pages.py --create-module 3 --module-name "Hvordan bruke KI på en god måte?"

# osv...
```

## Page ID Mapping System

Skriptet bruker en mapping-fil (`div-support-filer/page_id_mapping.json`) for å koble HTML-filer til Canvas page IDs. Dette gjør oppdateringene stabile selv når sidetitler eller URLs endres.

### Mapping-filens struktur (NY STRUKTUR)

```json
{
  "module1/generativ_ki.html": {
    "page_id": 395872,
    "url": "generativ-ki",
    "title": "Generativ KI",
    "module_id": 233819,
    "module_name": "Grunnbegreper i kunstig intelligens"
  },
  "module2/oppsummering.html": {
    "page_id": 409300,
    "url": "oppsummering-kapittel-2",
    "title": "Oppsummering kapittel 2",
    "module_id": 233820,
    "module_name": "Hvordan fungerer språkmodeller"
  },
  "module3/oppsummering.html": {
    "page_id": 409301,
    "url": "oppsummering-kapittel-3",
    "title": "Oppsummering kapittel 3",
    "module_id": 233811,
    "module_name": "Hvordan bruke KI på en god måte?"
  }
}
```

**Merk**: Nøklene bruker nå relative stier (`moduleN/filnavn.html`) i stedet for bare filnavn. Dette gjør det mulig å ha samme filnavn i flere moduler.

### Generere mapping første gang

```bash
# Bygg HTML lokalt først
make html

# Generer mapping fra lokale filer
python div-support-filer/update_canvas_pages.py --generate-mapping
```

**Hva skjer under genereringen:**

1. Skanner alle HTML-filer i `_build/html/module*/`
2. Henter ut `<h1>` tittel fra hver fil (denne blir sidetittelen i Canvas)
3. Konverterer tittel til forventet Canvas URL (med norske tegn: æ→ae, ø→o, å→a)
4. Henter alle Canvas-sider som er del av moduler
5. Matcher HTML-filer til Canvas-sider basert på URL-matching
6. Ved duplikater (f.eks. `avslutning-2`, `avslutning-5`) velges den med høyest suffiksnummer
7. Lagrer mapping til `page_id_mapping.json` med relative stier som nøkler

### Når må du regenerere mapping?

Du må regenerere mappingen når:
- Du legger til nye episoder/sider
- Du endrer `<h1>` taggen i en HTML-fil (fordi Canvas genererer ny URL basert på sidetittelen fra `<h1>`)
- Du har opprettet nye sider i Canvas som skal kobles til HTML-filer
- Du har omorganisert mappestrukturen (f.eks. flyttet filer mellom moduler)

**OBS:** Vanlige innholdsoppdateringer (endringer i brødtekst, ikke i `<h1>` tittel) krever IKKE regenerering av mapping.

## Brukseksempler

### Oppdatere alle sider

```bash
# Oppdater alle sider (bare innhold, ingen modulendringer)
python div-support-filer/update_canvas_pages.py

# Oppdater alle sider OG legg dem til i riktige moduler
python div-support-filer/update_canvas_pages.py --add-to-modules
```

### Oppdatere en enkelt side

**Hvis filnavnet er unikt på tvers av moduler:**
```bash
python div-support-filer/update_canvas_pages.py --page generativ_ki.html
```

**Hvis samme filnavn finnes i flere moduler (f.eks. `oppsummering.html`):**
```bash
# Spesifiser full sti
python div-support-filer/update_canvas_pages.py --page module2/oppsummering.html
```

**Hvis du bare skriver filnavnet og det finnes duplikater:**
```bash
python div-support-filer/update_canvas_pages.py --page oppsummering.html
```
Skriptet vil da liste opp alle treff og be deg spesifisere full sti:
```
Error: Multiple files found with name 'oppsummering.html':
  - module2/oppsummering.html
  - module3/oppsummering.html
  - module4/oppsummering.html

Please specify the full path, e.g.: --page module2/oppsummering.html
```

### Oppdatere alle sider i en modul

```bash
# Oppdater alle sider i modul 2 og legg dem til i modulen
python div-support-filer/update_canvas_pages.py --module 2 --add-to-modules
```

### Oppdater med spesifikk page ID (mest stabilt)

```bash
python div-support-filer/update_canvas_pages.py --page-id 395872 --page module1/generativ_ki.html
```

### Dry-run (se hva som ville bli oppdatert)

```bash
python div-support-filer/update_canvas_pages.py --dry-run
python div-support-filer/update_canvas_pages.py --add-to-modules --dry-run
python div-support-filer/update_canvas_pages.py --page module2/oppsummering.html --dry-run
```

### Liste alle sider med mapping-info

```bash
python div-support-filer/update_canvas_pages.py --list-pages
```

## Bildehåndtering

Skriptet håndterer automatisk bilder i HTML-filene:

### Hvordan det fungerer

1. **Finner bilder**: Skanner HTML-innholdet etter `<img>` tags
2. **Sjekker eksisterende**: Hopper over bilder som allerede er lastet opp til Canvas
3. **Løser filstier**: Håndterer relative stier (f.eks. `../_images/bilde.png`)
4. **Laster opp til Canvas**: Følger Canvas sin offisielle 3-stegs opplastingsworkflow
5. **Oppdaterer HTML**: Erstatter bildestier med Canvas URLer i riktig format

### Canvas bildeformat

Bilder blir konvertert fra:
```html
<img src="../_images/ChatGPT_howLLMswork.png" alt="LLM text generation" style="width: 60%;" />
```

Til Canvas-format:
```html
<img src="https://uio.instructure.com/courses/63248/files/3757441/preview"
     alt="LLM text generation"
     data-api-endpoint="https://uio.instructure.com/api/v1/courses/63248/files/3757441"
     data-api-returntype="File"
     data-ally-user-updated-alt="LLM text generation"
     width="60%" />
```

### Hvor lagres bildene?

- Bilder lagres i en egen mappe `course_images` i Canvas
- Hvis samme filnavn eksisterer, blir det overskrevet automatisk
- Bildene blir tilgjengelige for hele kurset

## Håndtering av interne lenker (NYTT)

Skriptet konverterer automatisk Sphinx cross-references til Canvas page URLs.

**Eksempel**: Hvis du i en RST-fil har:
```rst
Se :ref:`Hicks <Hicks>` for mer informasjon.
```

Dette blir til en HTML-lenke som peker til `episode6_3.html#Hicks`. Skriptet konverterer automatisk denne til:
```html
<a href="/courses/63248/pages/kilder#Hicks">Hicks</a>
```

hvor `kilder` er Canvas URL-en for siden som inneholder referansen.

## Workflows

### Arbeidsflyt 1: Første gangs oppsett etter omstrukturering

**Kun nødvendig hvis du har slettet alle moduler og starter på nytt:**

```bash
# 1. Opprett moduler med egendefinerte navn
python div-support-filer/update_canvas_pages.py --create-module 1 --module-name "Grunnbegreper i kunstig intelligens"
python div-support-filer/update_canvas_pages.py --create-module 2 --module-name "Hvordan fungerer språkmodeller"
# ... osv for alle 8 moduler

# 2. Slett gammel mapping (hvis den eksisterer)
rm div-support-filer/page_id_mapping.json

# 3. Generer ny mapping basert på ny mappestruktur
python div-support-filer/update_canvas_pages.py --generate-mapping

# 4. Oppdater alle sider og legg dem til i moduler
python div-support-filer/update_canvas_pages.py --add-to-modules
```

### Arbeidsflyt 2: Daglig oppdatering av innhold

```bash
# 1. Rediger RST-filer i source/moduleN/

# 2. Bygg HTML lokalt
make html

# 3. Test endringene i _build/html/

# 4. Oppdater Canvas (enten alle eller enkeltside)
python div-support-filer/update_canvas_pages.py                              # Alle sider
python div-support-filer/update_canvas_pages.py --page module2/oppsummering.html  # Enkeltside

# 5. Commit og push til GitHub
```

### Arbeidsflyt 3: Legge til ny side

```bash
# 1. Opprett ny RST-fil i source/moduleN/

# 2. Bygg HTML
make html

# 3. Oppdater Canvas (vil opprette ny side automatisk)
python div-support-filer/update_canvas_pages.py --page moduleN/ny_side.html --add-to-module N

# 4. Regenerer mapping for å inkludere den nye siden
python div-support-filer/update_canvas_pages.py --generate-mapping
```

## Feilsøking

### Problem: "Multiple files found with name 'X'"

**Årsak**: Du prøver å oppdatere en fil som finnes i flere moduler med bare filnavnet.

**Løsning**: Spesifiser full sti:
```bash
python div-support-filer/update_canvas_pages.py --page module2/oppsummering.html
```

### Problem: "No mapping found for X"

**Årsak**: Filen finnes ikke i mapping-filen.

**Løsning**: Regenerer mapping:
```bash
python div-support-filer/update_canvas_pages.py --generate-mapping
```

### Problem: Mapping virker utdatert

**Årsak**: Mappestrukturen eller filnavnene har endret seg siden siste mapping.

**Løsning**: Slett og regenerer mapping:
```bash
rm div-support-filer/page_id_mapping.json
python div-support-filer/update_canvas_pages.py --generate-mapping
```

### Problem: Moduler eksisterer ikke

**Årsak**: Du prøver å bruke `--add-to-modules` men modulene finnes ikke i Canvas.

**Løsning**: Opprett modulene først med `--create-module`:
```bash
python div-support-filer/update_canvas_pages.py --create-module 1 --module-name "Modulnavn"
```

## Notater

- Skriptet er produsert av KI og testet for grunnleggende operasjoner
- Skriptet bruker `<h1>` taggen fra HTML-filen som sidetittel i Canvas
- Canvas genererer automatisk page URL basert på sidetittelen (du kan ikke velge URL manuelt)
- HTML-filene renses for `<h1>` elementer og navigasjon før opplasting til Canvas
- Page ID er stabilt og endres ikke når tittel/URL endres - derfor bruker vi page ID mapping
- Skriptet kan kjøres fra både root-mappen og `div-support-filer/` mappen
- Mapping-filen må regenereres hvis du legger til nye sider eller endrer `<h1>` titler
- Ved tidsnød: Du kan gjøre manuelle endringer i Canvas, men husk å oppdatere RST-filene i GitHub etterpå
- **NYTT**: Relative stier i mapping gjør det mulig å ha samme filnavn i flere moduler
- **NYTT**: Interne Sphinx cross-references blir automatisk konvertert til Canvas page URLs
