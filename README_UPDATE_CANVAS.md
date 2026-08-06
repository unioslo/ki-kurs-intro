# Canvas API Skript - Dokumentasjon

**OPPDATERT August 2026**: Dokumentasjonen er synkronisert med gjeldende versjon av skriptet. Skriptet og mapping-filen ligger nå i repo-roten (`update_canvas_pages.py` og `page_id_mapping.json`).

Skriptet `update_canvas_pages.py` kan automatisk oppdatere Canvas-sider basert på de genererte HTML-filene.

## Viktige endringer fra tidligere versjon

- ✅ **Støtte for modul-basert mappestruktur**: HTML-filer nå i `module1/`, `module2/`, etc.
- ✅ **Håndtering av duplikate filnavn**: Samme filnavn (f.eks. `oppsummering.html`) kan finnes i flere moduler
- ✅ **Relative stier i mapping**: Mapping bruker nå `module2/oppsummering.html` i stedet for bare `oppsummering.html`
- ✅ **Ny kommando for moduloppretting**: `--create-module` for å opprette moduler med egendefinerte navn
- ✅ **Forbedret enkeltsideoppdatering**: `--page` kan nå ta både filnavn og full sti
- ✅ **Automatisk opplasting av nedlastingsfiler**: `:download:`-filer (f.eks. PDF-er) lastes opp til Canvas
- ✅ **Interaktiv ommapping**: `--remap` for å koble umappede filer til eksisterende Canvas-sider
- ✅ **Ikke-interaktiv oppretting**: `--create-new` og `--no-placement-prompt` for kjøring uten spørsmål

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
- **Automatisk håndtering av nedlastingsfiler**: Laster opp `:download:`-filer (PDF-er m.m.) og oppdaterer lenkene
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

Skriptet leter etter HTML-mappen i denne rekkefølgen: `_build/html`, deretter `../_build/html`, deretter `_build`. Kjør derfor gjerne fra repo-roten etter `make html`.

**Moduloppdeling**: Filer i `moduleN/` blir automatisk tilordnet Module N når du bruker `--add-to-modules`.

## Opprette moduler

Før du kan bruke `--add-to-modules`, må modulene eksistere i Canvas. Du kan opprette dem manuelt i Canvas eller bruke skriptet:

```bash
# Opprett modul 1 med egendefinert navn
python update_canvas_pages.py --create-module 1 --module-name "Grunnbegreper i kunstig intelligens"

# Opprett modul 2
python update_canvas_pages.py --create-module 2 --module-name "Hvordan fungerer språkmodeller"

# Opprett modul 3
python update_canvas_pages.py --create-module 3 --module-name "Hvordan bruke KI på en god måte?"

# osv...
```

## Page ID Mapping System

Skriptet bruker en mapping-fil (`page_id_mapping.json`) for å koble HTML-filer til Canvas page IDs. Dette gjør oppdateringene stabile selv når sidetitler eller URLs endres.

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

**Merk**: Nøklene bruker nå relative stier (`moduleN/filnavn.html`) i stedet for bare filnavn. Dette gjør det mulig å ha samme filnavn i flere moduler. Skriptet har også "fuzzy" matching som håndterer Canvas-suffikser (f.eks. `-2`, `-3`) på URLer.

**Merk (skråstrek/plattform)**: Nøklene bruker alltid vanlig skråstrek (`/`), uansett operativsystem. Skriptet normaliserer stiene med `Path.as_posix()`, slik at mapping-filen fungerer likt på Windows, macOS og Linux. Dette er også nødvendig for at interne kryssreferanser (som Sphinx alltid skriver med `/`) skal matche riktig. Ikke rediger nøklene manuelt til omvendt skråstrek (`\`).

### Generere mapping første gang

```bash
# Bygg HTML lokalt først
make html

# Generer mapping fra lokale filer
python update_canvas_pages.py --generate-mapping

# Alternativt: generer mapping fra GitHub html-pages branch (uten lokal bygging)
# ⚠️ Fungerer ikke for øyeblikket – se «Deploy fra GitHub»
python update_canvas_pages.py --generate-mapping --from-github
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

**OBS:** Vanlige innholdsoppdateringer (endringer i brødtekst, ikke i `<h1>` tittel) krever IKKE regenerering av mapping. Når skriptet oppretter nye sider, oppdaterer det dessuten mapping-filen automatisk.

## Brukseksempler

### Oppdatere alle sider

```bash
# Oppdater alle sider (bare innhold, ingen modulendringer)
python update_canvas_pages.py

# Oppdater alle sider OG legg dem til i riktige moduler
python update_canvas_pages.py --add-to-modules
```

### Oppdatere en enkelt side

**Hvis filnavnet er unikt på tvers av moduler:**
```bash
python update_canvas_pages.py --page generativ_ki.html
```

**Hvis samme filnavn finnes i flere moduler (f.eks. `oppsummering.html`):**
```bash
# Spesifiser full sti
python update_canvas_pages.py --page module2/oppsummering.html
```

**Hvis du bare skriver filnavnet og det finnes duplikater:**
```bash
python update_canvas_pages.py --page oppsummering.html
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
python update_canvas_pages.py --module 2 --add-to-modules
```

### Legge en side til en bestemt modul

```bash
# Legg en enkelt side til modul 5 (spør om plassering i modulen)
python update_canvas_pages.py --page module5/ny_side.html --add-to-module 5

# Opprett ny side og legg den nederst i modulen, uten spørsmål
python update_canvas_pages.py --page module5/ny_side.html --create-new --add-to-module 5 --no-placement-prompt
```

### Oppdater med spesifikk page ID (mest stabilt)

```bash
python update_canvas_pages.py --page-id 395872 --page module1/generativ_ki.html
```
**Merk:** `--page-id` krever `--page` for å angi hvilken HTML-fil som skal brukes.

### Interaktiv ommapping av umappede filer

```bash
# Gå gjennom alle umappede filer og koble dem til eksisterende Canvas-sider
python update_canvas_pages.py --remap

# Ommapp én bestemt fil
python update_canvas_pages.py --remap --page module2/oppsummering.html
```

### Dry-run (se hva som ville bli oppdatert)

```bash
python update_canvas_pages.py --dry-run
python update_canvas_pages.py --add-to-modules --dry-run
python update_canvas_pages.py --page module2/oppsummering.html --dry-run
```

### Liste alle sider med mapping-info

```bash
python update_canvas_pages.py --list-pages
```

## Deploy fra GitHub (html-pages branch)

> ⚠️ **FUNGERER IKKE FOR ØYEBLIKKET (August 2026)**: `--from-github` er ikke funksjonell etter at GitHub Actions ble endret. `html-pages`-branchen bygges/oppdateres ikke lenger på samme måte, så deploy og mapping-generering fra GitHub gir ikke riktig resultat. Bruk lokal bygging (`make html`) og lokal oppdatering inntil dette er fikset. Eksemplene under er beholdt som referanse for når funksjonaliteten er gjenopprettet.

Skriptet kan hente ferdig bygde HTML-filer direkte fra `html-pages`-branchen på GitHub, slik at du slipper å bygge lokalt.

```bash
# Deploy alle sider fra GitHub html-pages branch
python update_canvas_pages.py --from-github

# Dry-run av GitHub-deploy
python update_canvas_pages.py --from-github --dry-run

# Deploy én side fra GitHub
python update_canvas_pages.py --from-github --page module2/oppsummering.html

# Hopp over bekreftelsesspørsmålet (kjør automatisk)
python update_canvas_pages.py --from-github --yes
```

Ved GitHub-deploy viser skriptet informasjon om siste commit (dato, hash, melding) og hvilke filer som vil bli deployet, og ber om bekreftelse. Bruk `--yes` for å hoppe over bekreftelsen (nyttig i automatiserte kjøringer).

## Bildehåndtering

Skriptet håndterer automatisk bilder i HTML-filene:

### Hvordan det fungerer

1. **Finner bilder**: Skanner HTML-innholdet etter `<img>` tags
2. **Sjekker eksisterende**: Hopper over bilder som allerede er lastet opp til Canvas (URLer med `instructure.com`)
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
     id="3757441"
     alt="LLM text generation"
     data-api-endpoint="https://uio.instructure.com/api/v1/courses/63248/files/3757441"
     data-api-returntype="File"
     data-ally-user-updated-alt="LLM text generation"
     width="60%" />
```

### Hvor lagres bildene?

- Bilder lagres i en egen mappe `course_images` i Canvas
- Hvis samme filnavn eksisterer, blir det overskrevet automatisk (`on_duplicate=overwrite`)
- Bildene blir tilgjengelige for hele kurset

## Nedlastingsfiler (`:download:`)

Skriptet håndterer også filer lagt inn med Sphinx sin `:download:`-direktiv (f.eks. PDF-er).

### Hvordan det fungerer

1. **Finner nedlastingslenker**: Skanner etter `<a>`-elementer med klassene `reference download`
2. **Sjekker eksisterende**: Hopper over lenker som allerede peker til Canvas
3. **Løser filstier**: Håndterer relative stier (f.eks. `../_downloads/hash/fil.pdf`)
4. **Laster opp til Canvas**: Filene lagres i mappen `course_files` i Canvas
5. **Oppdaterer lenken**: Peker til Canvas' nedlastings-URL og setter Canvas-klassene `instructure_file_link instructure_scribd_file`

## Håndtering av interne lenker

Skriptet konverterer automatisk Sphinx cross-references til Canvas page URLs.

**Eksempel**: Hvis du i en RST-fil har:
```rst
Se :ref:`Hicks <Hicks>` for mer informasjon.
```

Sphinx genererer da en HTML-lenke til en annen side, f.eks. `../module8/kilder.html#hicks`. Skriptet slår opp riktig side i mapping-filen og konverterer lenken til:
```html
<a href="/courses/63248/pages/kilder#hicks">Hicks</a>
```

hvor `kilder` er Canvas URL-en for siden som inneholder referansen. Skriptet prøver først full relativ sti (`module8/kilder.html`) og faller tilbake til bare filnavnet for bakoverkompatibilitet.

## Kapittelkort (`uio-chapter-card`)

Direktivet `uio-chapter-card` lager et Canvas «kapittelkort»: et Icon-Maker-ikon (venstrestilt), en lenket overskrift og en kort beskrivelse.

**Bruk i RST:**
```rst
.. uio-chapter-card::
   :title: Introduksjon til "KI-språket"
   :icon_filename: kap2-ikon.svg
   :icon_file_id: 3954816
   :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
   :description: Kort beskrivelse
```

### Gruppering med `uio-module-listing`

Bruk `uio-module-listing` for å samle flere kapittelkort i en farget boks med en overskrift. Overskriften angis som argument (f.eks. `Kapitler` eller `Emnemoduler`); uten argument brukes `Emnemoduler:`.

```rst
.. uio-module-listing:: Emnemoduler

   .. uio-chapter-card::
      :title: Introduksjon til "KI-språket"
      :icon_filename: kap2-ikon.svg
      :icon_file_id: 3954816
      :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
      :description: Kort beskrivelse

   .. uio-chapter-card::
      :title: KI-tjenester ved UiO
      :icon_filename: kap6-ikon.svg
      :icon_file_id: 3954823
      :url: https://uio.instructure.com/courses/63248/pages/ki-tjenester-ved-uio
      :description: Godkjente verktøy og datasikkerhet
```

Dette gir (hvert kort er selv en `<div class="float-left">`):
```html
<div class="uio-color-box-3 uio-module-listing">
    <h2>Emnemoduler</h2>
    <div class="float-left">
        <div class="float-left"><img ... /></div>
        <h3><a title="..." href="..." ...>Introduksjon til "KI-språket"</a></h3>
        <span>Kort beskrivelse</span>
    </div>
    <!-- flere kort ... -->
</div>
```

Ved opplasting behandles kortene inni som vanlig (ikonet slås opp via `data-icon-file`-markøren, som deretter fjernes), mens selve `uio-module-listing`-boksen sendes uendret til Canvas. Den produserte HTML-en bruker bare Canvas' egne klasser (`uio-color-box-3`, `uio-module-listing`, `float-left`) – ingen egendefinerte klassenavn.

**Opsjoner:**

| Opsjon | Beskrivelse |
|--------|-------------|
| `title` | Overskriftsteksten (og lenketeksten) |
| `icon_filename` | Filnavnet til ikonet i Canvas (f.eks. `kap2-ikon.svg`). Brukes til den lokale forhåndsvisningen, og som reserve-oppslag hvis `icon_file_id` mangler |
| `icon_file_id` | Canvas fil-ID for ikonet (f.eks. `3954816`), tastet inn for hånd. Angis den, bygges Canvas-URL-en direkte fra den ved opplasting – uten API-oppslag |
| `url` | Full Canvas-URL til siden kortet lenker til. Utelates den, utledes lenken fra `title` via `page_id_mapping.json` ved opplasting |
| `description` | Kort beskrivelsestekst under overskriften |

**Slik lager og bruker du et ikon (rekkefølge):**

1. **Lag ikonet i Canvas.** Bruk Canvas sin Icon Maker til å lage ikonet, og lagre det i kursets ikonmappe (`Ikonskaper-ikoner`). Ikonene lages og lastes opp manuelt i Canvas.
2. **Sett filnavn og hent fil-ID-en.** Gi ikonet et gjenkjennelig filnavn (f.eks. `kap2-ikon.svg`). Klikk deretter på ikonfilen i Canvas – URL-en viser ID-en, f.eks. `.../files/folder/Ikonskaper-ikoner?preview=3954816` → fil-ID `3954816`.
3. **Bruk det i direktivet.** Lim filnavnet inn i `:icon_filename:` og fil-ID-en inn i `:icon_file_id:` i `.. uio-chapter-card::`:
   ```rst
   .. uio-chapter-card::
      :title: Introduksjon til "KI-språket"
      :icon_filename: kap2-ikon.svg
      :icon_file_id: 3954816
      :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
      :description: Kort beskrivelse
   ```

**Slik fungerer det (to faser):**

1. **`make html`**: Direktivet lager ferdig `<h3><a>`-lenken fra `:url:` (Canvas `data-api-endpoint` utledes ved å bytte `/courses/` → `/api/v1/courses/`). For ikonet:
   - **Er `:icon_file_id:` satt** (anbefalt), bygges Icon-Maker-`<img>`-en ferdig allerede her, med full Canvas-URL (`src=.../courses/{COURSE_ID}/files/{id}/download`, relativ `data-download-url`, `data-inst-icon-maker-icon` osv.). Ingen opplastingssteg trengs for dette ikonet.
   - **Mangler `:icon_file_id:`**, legges ikonet ut som en plassholder-`<img>` (uten egendefinert klasse) med markøren `data-icon-file` (filnavn) og `src` mot den lokale kopien i `source/_static/icons/`, slik at forhåndsvisningen viser ikonet.
2. **`update_canvas_pages.py`**: `process_chapter_cards()` behandler kun plassholder-ikonene (de med `data-icon-file`): filnavnet slås opp i Canvas via `find_canvas_file_by_name()`, Icon-Maker-`<img>`-en bygges, og markøren fjernes. Kort som allerede har full Canvas-URL fra fase 1 røres ikke. Resultatet (ytre `<div class="float-left">` med et venstrestilt ikon, `<h3><a>` og `<span>`-beskrivelse) matcher den håndskrevne Canvas-HTML-en og bruker bare Canvas' egne klasser.

**Forutsetning – lokale ikoner:** Ikonene ligger i Canvas-mappen `Ikonskaper-ikoner`. For at den lokale `make html`-forhåndsvisningen skal vise dem, last dem ned én gang (og på nytt når nye ikoner legges til):
```bash
python update_canvas_pages.py --download-icons
```
Dette legger SVG-filene i `source/_static/icons/`. Selve Canvas-siden bruker uansett Canvas-referansen som settes ved opplasting.

## Workflows

### Arbeidsflyt 1: Første gangs oppsett etter omstrukturering

**Kun nødvendig hvis du har slettet alle moduler og starter på nytt:**

```bash
# 1. Opprett moduler med egendefinerte navn
python update_canvas_pages.py --create-module 1 --module-name "Grunnbegreper i kunstig intelligens"
python update_canvas_pages.py --create-module 2 --module-name "Hvordan fungerer språkmodeller"
# ... osv for alle 8 moduler

# 2. Slett gammel mapping (hvis den eksisterer)
rm page_id_mapping.json

# 3. Generer ny mapping basert på ny mappestruktur
python update_canvas_pages.py --generate-mapping

# 4. Oppdater alle sider og legg dem til i moduler
python update_canvas_pages.py --add-to-modules
```

### Arbeidsflyt 2: Daglig oppdatering av innhold

```bash
# 1. Rediger RST-filer i source/moduleN/

# 2. Bygg HTML lokalt
make html

# 3. Test endringene i _build/html/

# 4. Oppdater Canvas (enten alle eller enkeltside)
python update_canvas_pages.py                              # Alle sider
python update_canvas_pages.py --page module2/oppsummering.html  # Enkeltside

# 5. Commit og push til GitHub
```

### Arbeidsflyt 3: Legge til ny side

```bash
# 1. Opprett ny RST-fil i source/moduleN/

# 2. Bygg HTML
make html

# 3. Oppdater Canvas (vil opprette ny side automatisk og oppdatere mapping-filen)
python update_canvas_pages.py --page moduleN/ny_side.html --add-to-module N
```

Skriptet spør før det oppretter en ny side. Vil du hoppe over spørsmålene, bruk `--create-new` (auto-oppretting) og eventuelt `--no-placement-prompt` (legg siden nederst i modulen). Når en ny side opprettes, legges den automatisk inn i `page_id_mapping.json` — du trenger normalt ikke regenerere hele mappingen.

## Feilsøking

### Problem: "Multiple files found with name 'X'"

**Årsak**: Du prøver å oppdatere en fil som finnes i flere moduler med bare filnavnet.

**Løsning**: Spesifiser full sti:
```bash
python update_canvas_pages.py --page module2/oppsummering.html
```

### Problem: "No mapping found for X"

**Årsak**: Filen finnes ikke i mapping-filen.

**Løsning**: Regenerer mapping, eller koble filen manuelt med `--remap`:
```bash
python update_canvas_pages.py --generate-mapping
# eller
python update_canvas_pages.py --remap --page moduleN/X.html
```

### Problem: Mapping virker utdatert

**Årsak**: Mappestrukturen eller filnavnene har endret seg siden siste mapping.

**Løsning**: Slett og regenerer mapping:
```bash
rm page_id_mapping.json
python update_canvas_pages.py --generate-mapping
```

### Problem: Moduler eksisterer ikke

**Årsak**: Du prøver å bruke `--add-to-modules` men modulene finnes ikke i Canvas.

**Løsning**: Opprett modulene først med `--create-module`:
```bash
python update_canvas_pages.py --create-module 1 --module-name "Modulnavn"
```

## Oversikt over kommandolinjevalg

| Flagg | Beskrivelse |
|-------|-------------|
| `--page <fil>` | Oppdater kun én side (filnavn eller `moduleN/fil.html`) |
| `--page-id <id>` | Oppdater én side via Canvas page ID (krever `--page`) |
| `--module <N>` | Oppdater kun sider fra modul N |
| `--add-to-modules` | Legg sidene til i riktige moduler etter oppdatering |
| `--add-to-module <N>` | Legg siden til i en bestemt modul |
| `--list-pages` | List alle sider med ID, tittel, URL og modul |
| `--remap` | Interaktivt koble umappede filer til eksisterende Canvas-sider |
| `--from-github` | ⚠️ Fungerer ikke for øyeblikket (se «Deploy fra GitHub»). Hent HTML fra GitHub `html-pages` branch i stedet for lokal `_build/html` |
| `--generate-mapping` | Generer `page_id_mapping.json` (kan kombineres med `--from-github`) |
| `--download-icons` | Last ned ikonene fra Canvas-mappen `Ikonskaper-ikoner` til `source/_static/icons/` (for lokal forhåndsvisning av kapittelkort) |
| `--dry-run` | Vis hva som ville skjedd uten å gjøre endringer |
| `--yes` | Hopp over bekreftelsesspørsmål (GitHub-deploy) |
| `--create-new` | Opprett nye sider automatisk uten å spørre |
| `--no-placement-prompt` | Legg nye sider nederst i modulen uten å spørre om plassering |
| `--create-module <N>` | Opprett en ny modul på posisjon N (krever `--module-name`) |
| `--module-name <navn>` | Navn på ny modul (brukes med `--create-module`) |

## Notater

- Skriptet er produsert av KI og testet for grunnleggende operasjoner
- Skriptet bruker `<h1>` taggen fra HTML-filen som sidetittel i Canvas
- Canvas genererer automatisk page URL basert på sidetittelen (du kan ikke velge URL manuelt)
- HTML-filene renses for `<h1>` elementer og navigasjon før opplasting til Canvas
- Page ID er stabilt og endres ikke når tittel/URL endres - derfor bruker vi page ID mapping
- Skriptet og mapping-filen ligger i repo-roten; kjør skriptet fra roten etter `make html`
- Mapping-filen må regenereres hvis du legger til nye sider eller endrer `<h1>` titler (nye sider som opprettes av skriptet legges inn automatisk)
- Ved tidsnød: Du kan gjøre manuelle endringer i Canvas, men husk å oppdatere RST-filene i GitHub etterpå
- Relative stier i mapping gjør det mulig å ha samme filnavn i flere moduler
- Interne Sphinx cross-references blir automatisk konvertert til Canvas page URLs
- Konfigurasjon i skriptet: `COURSE_ID=63248`, `HTML_BRANCH=html-pages`
