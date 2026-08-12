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
- ✅ **Forside (front page)**: `--front-page` bygger `source/forside.rst` og oppdaterer Canvas-forsiden via det dedikerte `/front_page`-endepunktet; `--fetch-front-page` laster ned den nåværende Canvas-forsiden for å hjelpe med å lage RST-en
- ✅ **Lokalt genererte kapittelikoner**: `build_icons.py` lager «Kapitler»-ikonene lokalt fra `source/forside.rst` (kortenes tittel/rekkefølge/farge). `--upload-icons` regenererer og laster dem opp til Canvas-mappen `Ikonskaper-ikoner`

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
- **Forside**: Bygger `source/forside.rst` og oppdaterer Canvas-forsiden via `/front_page`-endepunktet (`--front-page`)
- **Kapittelikoner**: Genererer «Kapitler»-ikonene lokalt fra `source/forside.rst` og laster dem opp (`--upload-icons`)

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

## Forside (front page)

Kursets forside er en egen Canvas-wiki-side som ligger utenfor alle moduler. Kilden er `source/forside.rst`, som Sphinx bygger til `forside.html` i roten av HTML-bygget (ikke under `module*/`, så den blir ikke feid med i modulsidene). Den pushes via Canvas' dedikerte `/front_page`-endepunkt – ingen `page_id` eller mapping-oppføring trengs.

```bash
# Bootstrap: last ned den nåværende Canvas-forsiden for å lage forside.rst
python update_canvas_pages.py --fetch-front-page              # -> forside_canvas.html
python update_canvas_pages.py --fetch-front-page my_dump.html # valgfritt filnavn

# Bygg source/forside.rst (make html) og push til Canvas-forsiden
python update_canvas_pages.py --front-page
python update_canvas_pages.py --front-page --dry-run
```

`--front-page` kjører samme innholdspipeline som vanlige sider (bildeopplasting, nedlastingslenker, interne kryssreferanser, kapittelkort) og oppdaterer forsiden. Den **regenererer også kapittelikonene** fra `forside.rst` først (se under), slik at ikonene alltid stemmer med kortene. For å få de oppdaterte ikonene til Canvas må du i tillegg kjøre `--upload-icons`.

## Kapittelkort (`uio-chapter-card`)

Direktivet `uio-chapter-card` lager et klikkbart kapittel-**felt i full bredde**: én bred ikon-SVG med kapittelnummeret til venstre og tittelen ved siden av, der hele feltet lenker til kapittelets første Canvas-side. Nummeret og tittelen er «bakt inn» i selve ikonet – det er **ingen egen overskriftstekst eller beskrivelse** under ikonet lenger. På forsiden stables feltene i full bredde inne i «Kapitler»-boksen.

**Bruk i RST:**
```rst
.. uio-chapter-card::
   :title: Grunnbegreper i kunstig intelligens
   :icon_filename: ikon1.svg
   :icon_color: #7ED321
   :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3
```

### `source/forside.rst` er kilden (single source of truth)

Ikonene genereres lokalt av `build_icons.py` direkte fra `uio-chapter-card`-oppføringene i `source/forside.rst`. Hvert kort beskriver ikonet sitt fullstendig:

- `:title:` → tittelen som skrives inn i ikonet
- `:icon_filename:` → filnavnet ikonet lagres/lastes opp som (må matche navnet i Canvas)
- `:icon_color:` → bakgrunnsfargen på feltet (hex, f.eks. `#7ED321`)
- **kortets posisjon** i «Kapitler»-listen → kapittelnummeret som bakes inn

Endrer du tittel, farge, filnavn eller rekkefølge på et kort, endres ikonet tilsvarende når du regenererer. Det finnes ingen egen kapittel-tabell å holde i synk – `forside.rst` er fasit. Ikonene lages altså **ikke** lenger manuelt i Canvas sin Icon Maker.

### Gruppering med `uio-module-listing`

Bruk `uio-module-listing` for å samle flere kapittelkort i en farget boks med en overskrift. Overskriften angis som argument (f.eks. `Kapitler:`); uten argument brukes `Emnemoduler:`.

```rst
.. uio-module-listing:: Kapitler:

   .. uio-chapter-card::
      :title: Grunnbegreper i kunstig intelligens
      :icon_filename: ikon1.svg
      :icon_color: #7ED321
      :url: https://uio.instructure.com/courses/63248/pages/introduksjon-til-ki-spraket-3

   .. uio-chapter-card::
      :title: Hvordan fungerer språkmodeller?
      :icon_filename: ikon3.svg
      :icon_color: #40BEA6
      :url: https://uio.instructure.com/courses/63248/pages/store-sprakmodeller-3
```

Dette gir ett klikkbart felt per kort (hele feltet er en lenke rundt et ikon i full bredde):
```html
<div class="uio-color-box-3 uio-module-listing">
    <h2>Kapitler:</h2>
    <a href="..." title="..." data-course-type="wikiPages" ... style="display:block; margin-bottom:12px; text-decoration:none;">
        <img style="width:100%; height:auto; display:block;" ... data-icon-file="ikon1.svg" />
    </a>
    <!-- flere felter ... -->
</div>
```

Ved opplasting slås ikonet opp via `data-icon-file`-markøren (som deretter fjernes), mens selve `uio-module-listing`-boksen sendes uendret til Canvas.

**Opsjoner:**

| Opsjon | Beskrivelse |
|--------|-------------|
| `title` | Kapitteltittelen som bakes inn i ikonet (og brukes som `title=` på lenken) |
| `icon_filename` | Filnavnet ikonet lagres/lastes opp som i Canvas (f.eks. `ikon1.svg`). Brukes både lokalt og for oppslag ved opplasting |
| `icon_color` | Bakgrunnsfargen på feltet (hex, f.eks. `#7ED321`). Driver kun ikon-genereringen |
| `url` | Full Canvas-URL feltet lenker til. Utelates den, utledes lenken fra `title` via `page_id_mapping.json` ved opplasting |
| `icon_file_id` | (Valgfritt/avansert) Canvas fil-ID for et ferdig Icon-Maker-ikon. Angis den, bygges Canvas-`<img>`-en direkte fra ID-en uten oppslag – da brukes ikke det lokalt genererte ikonet |

> Merk: `:description:` finnes fortsatt i direktivet av bakoverkompatibilitet, men vises ikke i det nye feltdesignet.

### Generere ikonene (`build_icons.py`)

Ikonene er brede felt (referansestørrelse `700×96`, ca. 7:1) i kapittelfargen, med Lato-fonten innebygd (hentet fra Canvas' opprinnelige Icon-Maker-ikoner), slik at teksten rendres riktig selv når Canvas viser SVG-en som `<img>`. Juster størrelse/font via konstantene øverst i `build_icons.py`.

```bash
# Regenerer source/_static/icons/*.svg fra forside.rst
python build_icons.py
```

`update_canvas_pages.py` kaller de samme funksjonene, så `--front-page` og `--upload-icons` regenererer ikonene automatisk før de bygger/laster opp.

**Slik fungerer det (to faser):**

1. **`make html`**: Direktivet lager den ferdige lenken fra `:url:` (Canvas `data-api-endpoint` utledes ved å bytte `/courses/` → `/api/v1/courses/`) og legger ikonet ut som en `<img style="width:100%">` med markøren `data-icon-file` (filnavn) og `src` mot den lokale kopien i `source/_static/icons/`, slik at forhåndsvisningen viser ikonet.
2. **`update_canvas_pages.py`**: `process_chapter_cards()` slår opp filnavnet i Canvas via `find_canvas_file_by_name()`, bygger den endelige Canvas-`<img>`-en og fjerner markøren. Lenken (hele feltet) røres ikke hvis `:url:` allerede er satt.

> ⚠️ **`make clean html` etter endring av utvidelsen:** Selve feltmarkupen produseres av Sphinx-utvidelsen (`source/_ext/uio_components.py`). Endrer du den koden, tar et vanlig inkrementelt `make html` det ikke med – kjør `make clean html`. Endringer i `forside.rst` eller i selve ikon-SVG-ene bygges normalt.

### Laste ikoner opp til / ned fra Canvas

```bash
# Regenerer ikonene fra forside.rst OG last dem opp til 'Ikonskaper-ikoner'
python update_canvas_pages.py --upload-icons
python update_canvas_pages.py --upload-icons --dry-run

# Last ned eksisterende ikoner fra Canvas (f.eks. for å hente Lato-fonten / eldre ikoner)
python update_canvas_pages.py --download-icons
```

`--upload-icons` bruker `on_duplicate=overwrite`, så hvert ikon beholder sin eksisterende Canvas fil-ID – forsiden (som refererer ikoner via fil-ID) peker dermed på oppdatert innhold uten ny opplasting av selve siden.

> Canvas (og nettleseren) cacher SVG-nedlastinger aggressivt. Ser ikonene fortsatt gamle ut etter opplasting, gjør en hard refresh (Cmd+Shift+R) – selve filen er oppdatert.

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

### Arbeidsflyt 4: Oppdatere forsiden og kapittelikoner

```bash
# 1. Rediger source/forside.rst (tekst, illustrasjon og/eller uio-chapter-card-oppføringer:
#    :title:, :icon_filename:, :icon_color:, :url: og rekkefølgen = kapittelnummer)

# 2. Bygg HTML (bruk clean hvis du nettopp endret Sphinx-utvidelsen)
make html          # eller: make clean html

# 3. Forhåndsvis _build/html/forside.html og et ikon i source/_static/icons/

# 4. Regenerer ikonene og last dem opp til Canvas ('Ikonskaper-ikoner')
python update_canvas_pages.py --upload-icons

# 5. Oppdater selve forsiden på Canvas (regenererer også ikonene lokalt)
python update_canvas_pages.py --front-page

# 6. Commit og push til GitHub
```

Endrer du bare kapittel-tittel/-nummer/-farge/-ikonfil, sørger steg 4–5 for at ikonene stemmer med kortene (`forside.rst` er fasit). Ser ikonene gamle ut etterpå, gjør en hard refresh i nettleseren.

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
| `--front-page` | Bygg `source/forside.rst` → `forside.html` og oppdater Canvas-forsiden (via `/front_page`-endepunktet). Regenererer også kapittelikonene fra `forside.rst`. Respekterer `--dry-run` og `--from-github` |
| `--fetch-front-page [PATH]` | Last ned den nåværende Canvas-forsiden til PATH (standard `forside_canvas.html`) for å hjelpe med å lage `source/forside.rst`. Endrer ikke Canvas |
| `--upload-icons` | Regenerer kapittelikonene fra `source/forside.rst` (tittel/nummer/farge/filnavn) og last dem opp til Canvas-mappen `Ikonskaper-ikoner`. Respekterer `--dry-run` |
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
