Episode 2: Hvordan fungerer språkmodeller?
==========================================

.. contents::
   :local:
   :depth: 2

Oversikt
--------

I denne episoden lærer du hvordan store språkmodeller (LLM) faktisk fungerer, og hvorfor denne forståelsen er viktig når du bruker dem.

Temaer som dekkes
~~~~~~~~~~~~~~~~~

* Språkmodeller er ikke kunnskapsbaser
* Hvordan LLM-er genererer tekst
* Statistisk sannsynlighet og tilfeldighet
* Begrensninger ved LLM-er
* Hvorfor LLM-er kan "hallusinere"

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Forstå at LLM-er konstruerer tekst basert på statistiske mønstre
* Forklare hvorfor LLM-er ikke er pålitelige kunnskapsbaser
* Gjenkjenne når en LLM kan gi feil informasjon
* Forstå betydningen av tilfeldighet i KI-svar

**Estimert tid:** 10 minutter

LLM-er er IKKE kunnskapsbaser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dette er kanskje den viktigste forståelsen du kan ha om språkmodeller:

.. warning::

   **Store språkmodeller er IKKE databaser med fakta. De er statistiske modeller som genererer tekst basert på mønstre de har lært.**

La oss sammenligne med noe du kjenner:

.. canvas-tabs::

   .. canvas-tab:: Kunnskapsbase (f.eks. Wikipedia)

      **Slik fungerer det:**

      * Informasjon er lagret som strukturerte data
      * Når du søker, henter systemet frem eksakt informasjon
      * Informasjonen er (ideelt sett) verifisert og referert
      * Du får samme svar hver gang på samme spørsmål
      * Hvis informasjonen ikke finnes, får du ingen treff

      **Eksempel:**

      Søker du "befolkning i Norge 2024", får du det eksakte tallet som er lagret.

   .. canvas-tab:: Språkmodell (f.eks. ChatGPT)

      **Slik fungerer det:**

      * Ingen informasjon er direkte "lagret" som fakta
      * Modellen har lært mønstre fra millioner av tekster
      * Når du stiller et spørsmål, genererer den ny tekst som ligner på mønstre den har sett
      * Du kan få ulike svar på samme spørsmål
      * Modellen vil alltid forsøke å gi et svar, selv om den ikke "vet" svaret

      **Eksempel:**

      Spør du "befolkning i Norge 2024", konstruerer modellen et svar basert på mønstre fra lignende spørsmål den har sett - og kan gi feil tall.

Hvordan genererer LLM-er tekst?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For å forstå språkmodeller bedre, la oss se på en forenklet forklaring av hvordan de fungerer:

.. canvas-tabs::

   .. canvas-tab:: Trening

      **Hva skjer under treningen:**

      1. Modellen får lese milliarder av ord fra internett, bøker, artikler osv.
      2. Den lærer hvilke ord som ofte kommer etter hverandre
      3. Den lærer mønstre i språk, grammatikk, og hvordan setninger bygges opp
      4. Den lærer sammenhenger mellom begreper og emner

      **Eksempel:**

      Hvis modellen har sett setningen "hovedstaden i Norge er Oslo" tusenvis av ganger, lærer den at "Oslo" er et sannsynlig ord som kommer etter "hovedstaden i Norge er".

   .. canvas-tab:: Generering

      **Hva skjer når du stiller et spørsmål:**

      1. Modellen analyserer din tekst (prompten)
      2. Basert på mønstre den har lært, beregner den hva som er statistisk sannsynlig som neste ord
      3. Den velger et ord (med litt tilfeldighet)
      4. Den gjentar prosessen for neste ord, og neste ord, osv.
      5. Den stopper når den "mener" svaret er fullstendig

      **Viktig:**

      Modellen "tenker" ikke på om informasjonen er korrekt - den genererer bare det som er statistisk sannsynlig basert på mønstre.

   .. canvas-tab:: Temperatur og tilfeldighet

      **Hva er "temperatur"?**

      * En parameter som styrer hvor kreativ/tilfeldig modellen skal være
      * **Lav temperatur** (f.eks. 0.2): Mer forutsigbar, velger de mest sannsynlige ordene
      * **Høy temperatur** (f.eks. 0.8): Mer kreativ, kan velge mindre sannsynlige ord

      **Derfor:**

      * Du kan få ulike svar på samme spørsmål
      * Noen ganger kan svarene være mer kreative, andre ganger mer "standard"
      * Ingen garanti for at samme spørsmål gir samme svar

Et praktisk eksempel
~~~~~~~~~~~~~~~~~~~~

La oss se på et konkret eksempel:

.. code-block:: text

   DU: "Hva er åpningstidene til biblioteket på Blindern?"

**Hva skjer i modellen:**

1. Modellen ser at dette er et spørsmål om åpningstider
2. Den har sett mange lignende spørsmål under trening
3. Den har lært mønsteret: spørsmål om åpningstider → svar med tider
4. Den genererer et svar som *ser ut* som åpningstider

**Problemet:**

Modellen kan konstruere et helt plausibelt svar som "Biblioteket på Blindern er åpent 08:00-20:00 mandag-fredag og 10:00-16:00 i helgene" - selv om dette er fullstendig feil!

.. warning::

   **Modellen "vet" ikke hva åpningstidene faktisk er. Den genererer bare tekst som ligner på svar om åpningstider.**

Hva er "hallusinering"?
~~~~~~~~~~~~~~~~~~~~~~~~

Når LLM-er genererer informasjon som høres troverdig ut, men som er feil, kaller vi det "hallusinering" (eller "confabulation" på fagspråket).

.. canvas-tabs::

   .. canvas-tab:: Eksempler på hallusinering

      **Typiske situasjoner:**

      * **Oppdiktede referanser**: Modellen lager titler på artikler som ikke finnes
      * **Feil fakta**: Oppgir feil datoer, tall eller navn
      * **Blandede personer**: Blander sammen biografier fra ulike personer
      * **Oppfunnet programvare**: Beskriver funksjoner som ikke eksisterer
      * **Feil prosedyrer**: Beskriver arbeidsprosesser som ikke stemmer

      **Eksempel:**

      "Studien av Hansen et al. (2023) publisert i Nature viste at..." - der både studien og forfatterne kan være oppfunnet.

   .. canvas-tab:: Hvorfor skjer det?

      **Årsaker til hallusinering:**

      1. **Modellen vil alltid gi et svar** - Den sier ikke "jeg vet ikke"
      2. **Mønstre fra trening** - Den har lært hvordan svar "skal se ut"
      3. **Manglende faktasjekk** - Den verifiserer ikke mot noen database
      4. **Overgeneralisering** - Den kombinerer mønstre fra ulike kilder
      5. **Utdatert treningsdata** - Modellen vet ikke hva som har skjedd etter den ble trent

      **Viktig å forstå:**

      Hallusinering er ikke en "bug" som kan fikses fullstendig - det er en iboende egenskap ved hvordan språkmodeller fungerer.

   .. canvas-tab:: Hallusinering med selvtillit

      **Det mest problematiske:**

      LLM-er hallusinerer ofte med stor **selvsikkerhet**. De sier ikke:

      * "Jeg er usikker, men..."
      * "Dette kan være feil, men..."
      * "Jeg vet ikke sikkert, men..."

      I stedet presenterer de feil informasjon med samme overbevisning som riktig informasjon.

      **Derfor:**

      Du kan IKKE stole på om et svar er korrekt basert på hvor selvsikkert det fremstår.

.. canvas-question::

   **Hvorfor kan en språkmodell gi feil informasjon selv om svaret høres veldig troverdig ut?**

   .. canvas-answer::

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk. Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant. Derfor kan den produsere feil informasjon med samme selvtillit som riktig informasjon.

      Begrensninger du bør kjenne til
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. canvas-tabs::

   .. canvas-tab:: Utdatert informasjon

      **Problemet:**

      * LLM-er trenes på data fra et bestemt tidspunkt
      * De vet ikke hva som har skjedd etter treningsdataen ble samlet
      * Mange modeller har en "kunnskapsgrense" (cutoff date)

      **Eksempel:**

      En modell trent i 2023 vet ikke hvem som vant fotball-VM i 2024, eller nye lover som ble vedtatt i 2024.

      **Merk:**

      Noen verktøy (som Bing Chat/Copilot) kan søke på internett for oppdatert informasjon - men da bruker de en søkemotor i tillegg til språkmodellen.

   .. canvas-tab:: Manglende kontekst

      **Problemet:**

      * LLM-er kjenner ikke til interne prosedyrer ved UiO (med mindre de fortelles)
      * De vet ikke om spesifikke systemer dere bruker
      * De har ikke tilgang til deres dokumenter eller databaser

      **Eksempel:**

      Spør du "Hvordan registrerer jeg fravær i vårt system?", kan modellen gi et generisk svar om fraværsregistrering - men ikke det spesifikke systemet dere bruker.

      **Løsning:**

      Gi kontekst i prompten: "Vi bruker systemet X ved UiO. Hvordan registrerer jeg fravær?"

   .. canvas-tab:: Språk og kulturforståelse

      **Problemet:**

      * De fleste LLM-er er primært trent på engelsk
      * Norsk fungerer, men kvaliteten kan være noe lavere
      * Norske forhold og kontekst kan være underrepresentert

      **Eksempel:**

      Juridiske eller administrative spørsmål om norske forhold kan få svar basert på amerikanske eller britiske systemer.

      **Tips:**

      * Vær eksplisitt: "i Norge", "ved norske universiteter", "etter norsk lovverk"
      * Sjekk alltid svar om lover, regler og prosedyrer

Hva betyr dette for deg som bruker?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   **Viktigste takeaways:**

   1. **LLM-er er verktøy for å generere tekst** - ikke oppslagsverk for fakta
   2. **Verifiser alltid viktig informasjon** - spesielt fakta, tall, referanser
   3. **Bruk LLM-er til hva de er gode på** - strukturering, formulering, idémyldring
   4. **Vær kritisk** - spesielt når svaret virker veldig detaljert og spesifikt
   5. **Gi god kontekst** - hjelp modellen ved å gi relevant informasjon i prompten

.. canvas-exercise::

   **Refleksjonsoppgave**

   Tenk over følgende situasjoner. I hvilke av disse bør du være EKSTRA forsiktig med å stole på et LLM-svar?

   * Skrive et utkast til en e-post
   * Finne en spesifikk paragraf i universitetsloven
   * Få hjelp til å formulere et budskap på en vennlig måte
   * Sjekke åpningstider for UiO-biblioteket
   * Brainstorme ideer til et arrangement
   * Få oppgitt kontaktinformasjon til en bestemt person
   * Oppsummere et dokument du har limt inn i chatten

   .. canvas-solution::

      **Ekstra forsiktig (verifiser alltid):**

      * Spesifikk paragraf i universitetsloven (kan hallusinere lovtekst)
      * Åpningstider (kan oppfinne tider)
      * Kontaktinformasjon (kan oppfinne eller gi utdatert info)

      **Tryggere å bruke (men fortsatt vær kritisk):**

      * Skrive utkast til e-post (du leser over og godkjenner)
      * Formulere budskap (du kontrollerer innholdet)
      * Brainstorme ideer (kreativ prosess, ikke faktabasert)
      * Oppsummere dokument du ga (basert på tekst du ga, ikke hallusinert)

.. note::

   I neste episode skal vi se nærmere på hvordan du kan kvalitetssikre output fra generativ KI, og hva du må tenke på når du bruker disse verktøyene.
