Episode 3: Kan du stole på generativ KI?
=========================================

.. contents::
   :local:
   :depth: 2

Oversikt
--------

I denne episoden lærer du hvordan du kan kvalitetssikre output fra generativ KI og hva du må tenke på når du bruker disse verktøyene.

Temaer som dekkes
~~~~~~~~~~~~~~~~~

* Når kan du stole på generativ KI?
* Hvordan kvalitetssikre innhold fra LLM-er
* Beste praksis for bruk av KI-verktøy
* Vanlige feil og hvordan unngå dem
* Personvern og datasikkerhet

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Vurdere når generativ KI er pålitelig og når den ikke er det
* Bruke strategier for å kvalitetssikre KI-generert innhold
* Forstå personvernhensyn ved bruk av generativ KI
* Unngå vanlige feil ved bruk av KI-verktøy

**Estimert tid:** 10 minutter

Når kan du stole på generativ KI?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generativ KI er ikke enten "pålitelig" eller "upålitelig" - det avhenger av hva du bruker den til.

.. canvas-tabs::

   .. canvas-tab:: Høy risiko - MÅ verifiseres

      **Situasjoner hvor du ALLTID må sjekke output:**

      * **Fakta og tall** - befolkningstall, datoer, statistikk
      * **Lover og regler** - lovparagrafer, regelverket ved UiO
      * **Referanser** - kildehenvisninger, studier, publikasjoner
      * **Kontaktinformasjon** - telefonnumre, e-postadresser, åpningstider
      * **Tekniske detaljer** - programvare-kommandoer, konfigurasjon
      * **Medisinske/juridiske råd** - Bruk profesjonelle kilder i stedet
      * **Kritisk kommunikasjon** - Viktige e-poster til ledelse, eksterne

      **Hvorfor?**

      Her kan hallusinering få alvorlige konsekvenser - feilinformasjon kan skade tilliten, føre til feil beslutninger, eller bryte lover/regler.

   .. canvas-tab:: Medium risiko - Bør sjekkes

      **Situasjoner hvor du bør være kritisk:**

      * **Forslag til prosedyrer** - Verifiser mot faktiske retningslinjer
      * **Historisk informasjon** - Sjekk viktige detaljer
      * **Tekniske forklaringer** - Bekreft med fagressurser
      * **Oppgaveplanlegging** - Vurder om forslagene er realistiske
      * **Oppsummeringer** - Sammenlign med originaldokumentet

      **Hvorfor?**

      Feil her kan føre til ineffektivitet, misforståelser, eller bortkastet tid.

   .. canvas-tab:: Lav risiko - Kan brukes mer fritt

      **Situasjoner hvor KI er tryggere å bruke:**

      * **Brainstorming og idémyldring** - Kreative prosesser uten fasitsvar
      * **Formulere tekst du selv har kontekst på** - Du vet hva som er riktig
      * **Språklig forbedring** - Grammatikk, tonefall, struktur
      * **Oppsummere tekst DU har gitt** - Basert på din input, ikke hallusinert
      * **Lage utkast** - Som utgangspunkt for videre arbeid
      * **Lære nye konsepter** - Når du følger opp med verifiserte kilder

      **Hvorfor?**

      Her er du i kontroll, eller konsekvensene av feil er lave.

Hvordan kvalitetssikre KI-generert innhold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Her er konkrete strategier for å sikre kvaliteten på det du får fra generativ KI:

.. canvas-tabs::

   .. canvas-tab:: 1. Kildekritikk

      **Behandle KI-output som ukjent kilde:**

      * Ville du stolt på denne informasjonen fra en tilfeldig person på gaten?
      * Er dette noe du kan verifisere?
      * Har du fagkunnskap til å vurdere om det virker riktig?

      **Verifiser alltid:**

      * Sjekk fakta mot pålitelige kilder (UiO.no, lovdata.no, osv.)
      * Søk opp referanser - eksisterer de faktisk?
      * Sammenlign med offisiell dokumentasjon

   .. canvas-tab:: 2. Be om kilder

      **Bruk strategiske spørsmål:**

      * "Kan du gi meg kilder for denne påstanden?"
      * "Hvor kommer denne informasjonen fra?"
      * "Kan du peke meg til offisiell dokumentasjon?"

      **Merk:**

      Selv når LLM-en gir "kilder", kan disse være hallusinerte! Sjekk alltid at kildene faktisk eksisterer.

      **Bedre tilnærming:**

      Søk selv etter informasjonen på pålitelige nettsider, og bruk KI-en til å hjelpe deg forstå eller oppsummere det du finner.

   .. canvas-tab:: 3. Kryss-sjekk

      **Sammenlign flere verktøy:**

      * Spør samme spørsmål til ChatGPT, Claude, og Copilot
      * Hvis de gir ulike svar, er dette et rødt flagg
      * Bruk tradisjonell søk (Google, UiO.no) for å verifisere

      **Sjekk mot dokumentasjon:**

      * Interne prosedyrer ved UiO
      * Offisielle nettsider
      * Lover og regler
      * Faglige kilder

   .. canvas-tab:: 4. Bruk din egen ekspertise

      **Stol på din kunnskap:**

      * Hvis noe føles feil, er det sannsynligvis feil
      * Bruk din fagkunnskap og erfaring
      * Vær spesielt skeptisk til svært spesifikke eller detaljerte påstander

      **Eksempel:**

      Hvis KI-en påstår at "alle møtereferater ved UiO skal sendes til Arkivverket innen 24 timer", og dette høres rart ut - så er det sannsynligvis feil.

   .. canvas-tab:: 5. Test og iterasjon

      **Stille spørsmålet på nytt:**

      * Omformulere spørsmålet ditt
      * Hvis du får helt ulike svar, er ikke KI-en pålitelig for dette spørsmålet
      * Konsistente svar er (litt) mer troverdige - men fortsatt ikke garantert korrekte

      **Eksempel:**

      * "Hva er søknadsfristen for X?"
      * "Når må søknaden om X leveres?"
      * "Har du informasjon om tidsfrister for X?"

      Hvis du får tre ulike datoer, vet du at du må finne informasjonen på en annen måte.

.. canvas-exercise::

   **Praktisk øvelse: Kvalitetssikring**

   Tenk deg at du har bedt en LLM om hjelp med følgende oppgaver. Hvordan ville du kvalitetssikret hvert svar?

   1. "Skriv et utkast til e-post hvor jeg informerer om møtetidspunkt"
   2. "Hva sier universitetsloven om arbeidskontrakter?"
   3. "Hjelp meg å strukturere disse møtenotatene" (du har limt inn notatene)
   4. "Generer ideer til et sommerarrangement for ansatte"

   .. canvas-solution::

      1. **E-post-utkast:**
         - Les grundig gjennom
         - Sjekk at alle fakta (tid, sted, dato) stemmer
         - Vurder om tonen passer
         - Legg til personlig touch

      2. **Universitetsloven:**
         - **VERIFISER ALT!** Sjekk på lovdata.no
         - LLM-er hallusinerer ofte lovtekster
         - Bruk i stedet: Søk på lovdata.no og be KI-en forklare det du finner
         - Kontakt HR hvis det er viktig

      3. **Strukturere notater:**
         - Sammenlign med originalnotatene dine
         - Sjekk at ingenting viktig er utelatt
         - Bekreft at tolkninger stemmer
         - Relativt trygt siden du ga konteksten

      4. **Idémyldring:**
         - Relativt trygt - ingen fasitsvar
         - Bruk ideene som inspirasjon
         - Vurder selv hva som passer for deres kultur
         - Tilpass til budsjett og ressurser

Personvern og datasikkerhet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Et kritisk aspekt ved bruk av generativ KI er personvern og beskyttelse av sensitiv informasjon.

.. warning::

   **ALDRI del sensitiv informasjon med offentlige KI-verktøy!**

.. canvas-tabs::

   .. canvas-tab:: Hva du IKKE skal dele

      **Del ALDRI dette med ChatGPT, Claude, Copilot (gratis versjoner) eller andre offentlige KI-verktøy:**

      * **Personopplysninger** - Fødselsnummer, personnummer, navn + kontaktinfo
      * **Konfidensielle dokumenter** - Interne strategier, ikke-publiserte planer
      * **Sensitive personalsaker** - Informasjon om ansattes helse, økonomi, etc.
      * **Forskningsdata** - Upubliserte data, særlig persondata
      * **Studentinformasjon** - Karakterer, personlige data, sensitivt om studenter
      * **Sikkerhetsinformasjon** - Passord, API-nøkler, systemdetaljer
      * **Kontraktsinfo** - Detaljer fra konfidensielle avtaler
      * **Økonomidata** - Budsjetter, lønnsinfo, sensitive økonomiske data

      **Hvorfor?**

      Når du skriver noe i ChatGPT eller lignende, kan informasjonen bli brukt til trening av modellen eller bli lagret. Det er ikke lenger privat.

   .. canvas-tab:: Anonymisering er ikke nok

      **Vær forsiktig selv med anonymisert data:**

      * Det er lett å gjenidentifisere personer fra "anonymiserte" tekster
      * Kombinasjoner av detaljer kan avsløre identitet
      * Vær spesielt forsiktig med små grupper

      **Eksempel på risiko:**

      "Fakultetet har en kvinnelig professor i astrofysikk som jobber med mørk materie" kan være nok til å identifisere en person.

      **Bedre tilnærming:**

      Skriv helt generiske eksempler: "En person ved et fakultet..." uten spesifikke detaljer.

   .. canvas-tab:: Godkjente verktøy ved UiO

      **Hva kan du bruke?**

      * Sjekk UiOs oversikt over godkjente KI-tjenester (dekkes i neste episode)
      * Noen verktøy har avtaler som beskytter data bedre
      * Organisasjonslisensieter har ofte bedre personverngarantier
      * Spør IT-avdelingen hvis du er usikker

      **Generell regel:**

      Hvis du er i tvil om noe er greit å dele - IKKE del det. Spør heller IT-avdelingen eller din leder først.

   .. canvas-tab:: Praktiske tips

      **Slik kan du jobbe trygt:**

      1. **Bruk generiske eksempler:**
         - I stedet for ekte navn, bruk "Person A", "Person B"
         - I stedet for ekte tall, bruk representative eksempler
         - Behold strukturen, fjern identifiserbar info

      2. **Skriv fra scratch:**
         - Be KI-en hjelpe deg lage noe nytt, i stedet for å dele eksisterende dokumenter
         - "Lag et møtereferat-mal" i stedet for å dele ekte referater

      3. **Dobbeltsjekk før du sender:**
         - Les alltid gjennom før du trykker "send"
         - Er det noe her som ikke burde deles?
         - Ville du vært komfortabel med at hele verden kunne lese dette?

.. canvas-question::

   **Hvorfor er det ikke nok å anonymisere data før du deler det med en LLM?**

   .. canvas-answer::

      Fordi selv "anonymiserte" data kan brukes til å identifisere personer, spesielt når flere detaljer kombineres. I tillegg vet du ikke hvordan dataene blir lagret eller brukt av KI-leverandøren. Det er tryggere å bruke helt generiske eksempler uten ekte data.

      Vanlige feil og fallgruver
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. canvas-tabs::

   .. canvas-tab:: Feil 1: Blind tillit

      **Feilen:**

      Å kopiere KI-output direkte uten å lese gjennom eller sjekke det.

      **Konsekvenser:**

      * Feilinformasjon spres
      * Profesjonelle konsekvenser hvis feil oppdages
      * Tap av tillit

      **Løsning:**

      Alltid les, forstå og verifiser før du bruker output.

   .. canvas-tab:: Feil 2: Dele sensitiv info

      **Feilen:**

      Lime inn konfidensielle dokumenter eller persondata i KI-verktøy.

      **Konsekvenser:**

      * Brudd på personvernlovgivningen (GDPR)
      * Sikkerhetsrisiko for organisasjonen
      * Kan få personlige og juridiske konsekvenser

      **Løsning:**

      Aldri del ekte sensitiv data. Bruk generiske eksempler i stedet.

   .. canvas-tab:: Feil 3: Avhengighet

      **Feilen:**

      Slutte å tenke selv og overlate all skriving/analyse til KI-en.

      **Konsekvenser:**

      * Tap av faglige ferdigheter
      * Lavere kvalitet over tid
      * Mindre kritisk tenkning

      **Løsning:**

      Bruk KI som verktøy, ikke erstatning. Du er eksperten - KI-en er assistenten.

   .. canvas-tab:: Feil 4: Feil bruksområde

      **Feilen:**

      Bruke LLM-er til oppgaver de ikke egner seg for (f.eks. slå opp eksakte prosedyrer).

      **Konsekvenser:**

      * Feil informasjon
      * Bortkastet tid
      * Frustrasjon

      **Løsning:**

      * For fakta: Bruk søkemotorer, offisielle nettsider, databaser
      * For kreativ hjelp: Bruk LLM-er
      * For prosedyrer: Sjekk intern dokumentasjon først

Beste praksis - oppsummering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   **Gylne regler for bruk av generativ KI:**

   1. **Verifiser alltid fakta** - Ikke stol blindt på output
   2. **Beskytt personvern** - Aldri del sensitiv informasjon
   3. **Du er ansvarlig** - Det er ditt navn på dokumentet, ikke KI-ens
   4. **Bruk kritisk tenkning** - Høres noe rart ut? Det er sannsynligvis feil
   5. **Bruk riktig verktøy** - LLM for kreativitet, databaser for fakta
   6. **Les alt før du bruker det** - Ingen copy-paste uten gjennomlesning
   7. **Vær transparent** - Hvis du bruker KI-assistanse, vurder om det bør nevnes
   8. **Hold deg oppdatert** - Sjekk UiOs retningslinjer regelmessig

.. canvas-exercise::

   **Refleksjonsoppgave**

   Tenk på en konkret situasjon hvor du kunne brukt generativ KI i ditt arbeid denne uken:

   * Hva ville du brukt den til?
   * Hvilke kvalitetssikringstiltak ville du tatt?
   * Er det noen personvernhensyn du må ta?
   * Hvordan ville du verifisert at output var korrekt?

   Dette er refleksjonsøvelse uten fasit - målet er å tenke gjennom hvordan du kan bruke KI på en trygg og ansvarlig måte.

.. note::

   I neste episode skal vi se på konkrete KI-tjenester som er tilgjengelige ved UiO, og hvordan du får tilgang til dem.
