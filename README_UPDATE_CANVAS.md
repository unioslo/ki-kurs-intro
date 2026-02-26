# Canvas API Skript - Dokumentasjon

Skriptet `div-support-filer/update_canvas_pages.py` kan automatisk oppdatere Canvas-sider basert på de genererte HTML-filene.

## Funksjonalitet

Skriptet gjør følgende:
- Leser HTML-filer fra `_build/html/episodes/` (ved lokal oppdatering) eller `html/episodes/` (ved deploy fra GitHub html-pages branch)
- Henter ut `<h1>` tittel fra hver HTML-fil og bruker denne som sidetittel i Canvas
- Canvas genererer automatisk page URL basert på sidetittelen (f.eks. "Hva er KI?" → `hva-er-ki`)
- Henter ut hovedinnholdet og fjerner `<h1>` elementer og navigasjon (siden Canvas legger til tittel automatisk)
- Oppdaterer Canvas-sider via REST API basert på page ID mapping
- Kan bygge opp mapping mellom HTML-filer og Canvas page IDs
- Støtter deploy fra GitHub html-pages branch (henter HTML fra `html/episodes/` i html-pages branch)
- Støtter dry-run mode for å se hva som vil bli oppdatert uten å gjøre endringer
- **Automatisk bildehåndtering**: Finner alle bilder i HTML, laster dem opp til Canvas, og oppdaterer `<img>` tags med Canvas URLer

## Bildehåndtering

Skriptet håndterer automatisk bilder i HTML-filene:

### Hvordan det fungerer

1. **Finner bilder**: Skanner HTML-innholdet etter `<img>` tags
2. **Sjekker eksisterende**: Hopper over bilder som allerede er lastet opp til Canvas
3. **Løser filstier**: Håndterer relative stier (f.eks. `../_images/bilde.png`) både for lokale filer og GitHub-filer
4. **Laster opp til Canvas**: Følger Canvas sin offisielle 3-stegs opplastingsworkflow
5. **Oppdaterer HTML**: Erstatter bildestier med Canvas URLer i riktig format

### Canvas bildeformat

Bilder blir konvertert fra dette formatet:
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

### Output-informasjon

For hver fil med bilder vil du se:
```
Processing: episode2_2.html
  Found 1 image(s) to process
    • Uploading: ../_images/ChatGPT_howLLMswork.png
      Local path: /path/to/_images/ChatGPT_howLLMswork.png
      ✓ Uploaded: ChatGPT_howLLMswork.png (file_id: 3757441)
      Canvas URL: https://uio.instructure.com/courses/63248/files/3757441/preview
  Image summary: 1 uploaded, 0 skipped
```

### Viktige notater

- Alt-tekst fra originale `<img>` tags blir bevart
- Width/height attributter blir bevart
- Bilder som allerede er på Canvas blir automatisk hoppet over
- Fungerer både med lokale filer og filer fra GitHub
- Dry-run mode viser hvilke bilder som ville blitt lastet opp uten å faktisk gjøre det

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

## Page ID Mapping System

Skriptet bruker en mapping-fil (`div-support-filer/page_id_mapping.json`) for å koble HTML-filer til Canvas page IDs. Dette gjør oppdateringene stabile selv når sidetitler eller URLs endres.

### Mapping-filens struktur

```json
{
  "episode1_0.html": {
    "page_id": 395816,
    "url": "hva-er-ki-og-generativ-ki-2",
    "title": "Hva er KI og generativ KI?",
    "module_id": 233819,
    "module_name": "Hva er KI og generativ KI?"
  }
}
```

### Generere mapping første gang

Du har to alternativer for å generere mappingen:

#### Alternativ 1: Fra lokale HTML-filer (krever lokal bygging)

```bash
# Bygg HTML lokalt først
make html

# Generer mapping fra lokale filer
python div-support-filer/update_canvas_pages.py --generate-mapping
```

#### Alternativ 2: Fra GitHub html-pages branch (anbefalt - ingen lokal bygging nødvendig)

```bash
# Generer mapping direkte fra GitHub (anbefalt)
python div-support-filer/update_canvas_pages.py --generate-mapping --from-github
```

Dette alternativet:
- Henter HTML-filer fra GitHub html-pages branch (fra `html/episodes/`)
- Krever IKKE at du bygger HTML lokalt først
- Passer om du ikke vil kjøre `make html` lokalt

**Hva skjer under genereringen:**

1. Leser alle HTML-filer (enten fra `_build/html/episodes/` eller `html/episodes/` i GitHub)
2. Henter ut `<h1>` tittel fra hver fil (denne blir sidetittelen i Canvas)
3. Konverterer tittel til forventet Canvas URL (med norske tegn: æ→ae, ø→o, å→a)
4. Henter alle Canvas-sider som er del av moduler
5. Matcher HTML-filer til Canvas-sider basert på URL-matching
6. Ved duplikater (f.eks. `avslutning-2`, `avslutning-5`) velges den med høyest suffiksnummer
7. Lagrer mapping til `page_id_mapping.json`

### Når må du regenerere mapping?

Du må regenerere mappingen når:
- Du legger til nye episoder/sider
- Du endrer `<h1>` taggen i en HTML-fil (fordi Canvas genererer ny URL basert på sidetittelen fra `<h1>`)
- Du har opprettet nye sider i Canvas som skal kobles til HTML-filer

**OBS:** Vanlige innholdsoppdateringer (endringer i brødtekst, ikke i `<h1>` tittel) krever IKKE regenerering av mapping.

## Hvordan Canvas URLs og sidetitler fungerer

**Viktig:** Canvas genererer automatisk page URLs basert på sidetittelen du setter, og du kan ikke manuelt velge en annen URL.

Skriptet gjør følgende:
1. Henter ut `<h1>` taggen fra hver HTML-fil (f.eks. `<h1>Hva er KI og generativ KI?</h1>`)
2. Bruker denne som sidetittel når Canvas-siden oppdateres
3. Canvas genererer så automatisk en page URL basert på denne tittelen

Canvas sin URL-generering følger disse reglene:
- Konverterer til lowercase
- Norske tegn: æ→ae, ø→o, å→a
- Fjerner spesialtegn
- Erstatter mellomrom og bindestreker med enkelt bindestrek
- Legger til suffiksnummer hvis URL finnes fra før (f.eks. `-2`, `-3`)

Eksempel: `<h1>Hva er KI?</h1>` → sidetittel: "Hva er KI?" → Canvas URL: `hva-er-ki-2`

Dette betyr at hvis du endrer `<h1>` taggen i en HTML-fil, vil både sidetittelen og URL-en i Canvas endres neste gang du oppdaterer siden.

## Brukseksempler

### Oppdatere alle sider fra lokale HTML-filer

```bash
make deploy-from-local
```

eller

```bash
python div-support-filer/update_canvas_pages.py
```

Dette oppdaterer alle sider basert på HTML-filene i `_build/html/episodes/` (lokale filer) og mappingen i `page_id_mapping.json`.

For hver HTML-fil:
1. Henter ut `<h1>` taggen (blir sidetittel i Canvas)
2. Canvas genererer automatisk URL basert på tittelen
3. Oppdaterer siden ved hjelp av page ID fra mapping-filen

### Deploy fra GitHub html-pages branch

```bash
make deploy-from-github
```

eller

```bash
python div-support-filer/update_canvas_pages.py --from-github
```

Dette gjør følgende:
1. Sjekker om du er i main branch
2. Henter HTML-filer fra GitHub html-pages branch (fra `html/episodes/` i den branchen)
3. Viser siste commit på html-pages branch og build-tidspunkt
4. Spør om bekreftelse
5. Oppdaterer alle Canvas-sider med innhold fra html-pages branch

**Merk:** Når du bruker `--from-github`, hentes HTML-filene fra `html/episodes/` i html-pages branch (ikke fra lokale `_build/html/episodes/`). Dette sikrer at du deployer de samme HTML-filene som GitHub Actions har bygget.

### Dry-run (se hva som ville bli oppdatert)

**Fra lokale filer:**
```bash
make deploy-from-local-dry-run
```

eller

```bash
python div-support-filer/update_canvas_pages.py --dry-run
```

**Fra GitHub:**
```bash
make deploy-from-github-dry-run
```

eller

```bash
python div-support-filer/update_canvas_pages.py --from-github --dry-run
```

Dry-run viser hva som ville bli oppdatert uten å faktisk gjøre endringer i Canvas.

### Liste alle sider med mapping-info

```bash
python div-support-filer/update_canvas_pages.py --list-pages
```

Viser en tabell med:
- HTML filename
- Canvas page ID
- Module name
- Page title
- Expected URL

### Oppdater en enkelt side

**Fra lokale filer:**
```bash
python div-support-filer/update_canvas_pages.py --page episode1_0
```

**Fra GitHub:**
```bash
python div-support-filer/update_canvas_pages.py --page episode1_0 --from-github
```

### Oppdater med spesifikk page ID

```bash
python div-support-filer/update_canvas_pages.py --page-id 395816 --page episode1_0
```

**Merk:** `--page-id` fungerer kun med lokale filer (ikke med `--from-github`).

## Workflows

### Arbeidsflyt 1: Kun GitHub (anbefalt - ingen lokal bygging)

Denne flyten er passer hvis du ikke vil bygge HTML lokalt:

**Første gangs oppsett:**
```bash
# Generer mapping fra GitHub (kun én gang)
python div-support-filer/update_canvas_pages.py --generate-mapping --from-github
```

**Deretter, hver gang du vil oppdatere Canvas:**
1. Rediger RST-filer i `source/episodes/` og commit til GitHub
2. Vent på at GitHub Actions bygger html-pages branch (tar noen minutter)
3. Deploy fra GitHub:
   ```bash
   make deploy-from-github
   # eller med dry-run først:
   make deploy-from-github-dry-run
   ```
4. Bekreft deploy

**Når må du regenerere mapping:**
- Når du legger til nye sider
- Når du endrer `<h1>` titler i RST-filer

### Arbeidsflyt 2: Lokal bygging og oppdatering

Denne flyten er best hvis du vil teste HTML lokalt før du oppdaterer Canvas:

**Første gangs oppsett:**
```bash
# Bygg HTML lokalt
make html

# Generer mapping fra lokale filer (kun én gang)
python div-support-filer/update_canvas_pages.py --generate-mapping
```

**Deretter, hver gang du vil oppdatere Canvas:**
1. Rediger RST-filer i `source/episodes/`
2. Bygg HTML lokalt: `make html`
3. Test endringene i `_build/html/`
4. Oppdater Canvas:
   ```bash
   make deploy-from-local
   # eller med dry-run først:
   make deploy-from-local-dry-run
   ```
   (eller bruk direkte: `python div-support-filer/update_canvas_pages.py` / `python div-support-filer/update_canvas_pages.py --dry-run`)
5. Commit og push til GitHub

## Notater

- Skriptet er produsert av KI og testet for grunnleggende operasjoner
- Skriptet bruker `<h1>` taggen fra HTML-filen som sidetittel i Canvas
- Canvas genererer automatisk page URL basert på sidetittelen (du kan ikke velge URL manuelt)
- HTML-filene renses for `<h1>` elementer og navigasjon før opplasting til Canvas
- Page ID er stabilt og endres ikke når tittel/URL endres - derfor bruker vi page ID mapping
- Skriptet kan kjøres fra både root-mappen og `div-support-filer/` mappen
- Når du bruker `--from-github`, hentes HTML fra `html/episodes/` i GitHub html-pages branch
- Når du ikke bruker `--from-github`, hentes HTML fra lokale `_build/html/episodes/`
- Mapping-filen må regenereres hvis du legger til nye sider eller endrer `<h1>` titler
- Ved tidsnød: Du kan gjøre manuelle endringer i Canvas, men husk å oppdatere RST-filene i GitHub etterpå
