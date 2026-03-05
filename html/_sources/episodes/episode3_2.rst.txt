
Hvordan kvalitetssikre KI-generert innhold
===========================================

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

.. uio-task::

   **Praktisk øvelse: Kvalitetssikring**

   Tenk deg at du har bedt en LLM om hjelp med følgende oppgaver. Hvordan ville du kvalitetssikret hvert svar?

   1. "Skriv et utkast til e-post hvor jeg informerer om møtetidspunkt"
   2. "Hva sier universitetsloven om arbeidskontrakter?"
   3. "Hjelp meg å strukturere disse møtenotatene" (du har limt inn notatene)
   4. "Generer ideer til et sommerarrangement for ansatte"

   .. uio-answer::

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
