Episode 5: Prompting og prompt engineering
===========================================

.. contents::
   :local:
   :depth: 2

Oversikt
--------

I denne episoden lærer du hvordan du skriver gode instruksjoner (prompts) til KI-verktøy for å få best mulige resultater.

Temaer som dekkes
~~~~~~~~~~~~~~~~~

* Hva er en prompt?
* Grunnleggende prinsipper for god prompting
* Teknikker for å forbedre resultater
* Vanlige feil og hvordan unngå dem
* Praktiske eksempler

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Skrive klare og effektive prompts
* Bruke ulike prompt-teknikker for forskjellige oppgaver
* Iterere og forbedre prompts basert på resultatene
* Gjenkjenne vanlige feil i prompting

**Estimert tid:** 12 minutter

Hva er en prompt?
~~~~~~~~~~~~~~~~~

En **prompt** er instruksjonen eller spørsmålet du gir til en KI-modell. Det er din måte å kommunisere med KI-en på.

.. tabs::

   .. tab:: Enkel prompt

      **Eksempel:**

      .. code-block:: text

         Hva er klimaendringer?

      **Resultat:**

      Du får et generelt svar om klimaendringer.

   .. tab:: Detaljert prompt

      **Eksempel:**

      .. code-block:: text

         Forklar klimaendringer på en enkel måte for en 10-åring.
         Bruk 3-4 setninger og unngå faguttrykk.

      **Resultat:**

      Du får et svar tilpasset målgruppen og lengden du ba om.

   .. tab:: Kontekst-rik prompt

      **Eksempel:**

      .. code-block:: text

         Jeg skal skrive en e-post til alle ansatte om nytt møterom-
         bookingsystem. Målgruppen er administrativt ansatte ved UiO
         som ikke er teknisk kyndige. Tonen skal være vennlig og
         informativ, ikke formell. Kan du hjelpe meg med et utkast?

      **Resultat:**

      Du får et svar som er tilpasset din spesifikke situasjon.

.. note::

   **Hovedregel:** Jo mer spesifikk og detaljert prompten din er, jo bedre blir resultatet.

Prinsipper for god prompting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: 1. Vær spesifikk

      **Dårlig prompt:**

      .. code-block:: text

         Skriv en e-post.

      **Bedre prompt:**

      .. code-block:: text

         Skriv en e-post til mine kolleger hvor jeg informerer om
         at møterommet Gaia er stengt for vedlikehold uke 15.
         Tonen skal være vennlig men profesjonell.

      **Hvorfor bedre?**

      Den spesifiserer hva e-posten skal handle om, hvem den er til, og hvilken tone den skal ha.

   .. tab:: 2. Gi kontekst

      **Dårlig prompt:**

      .. code-block:: text

         Lag et møtereferat.

      **Bedre prompt:**

      .. code-block:: text

         Basert på disse notatene fra møtet, lag et møtereferat:
         [dine notater her]

         Strukturer referatet med:
         - Deltakere
         - Agenda
         - Beslutninger
         - Oppgaver (hvem skal gjøre hva)

      **Hvorfor bedre?**

      Du gir både innholdet (notatene) og strukturen du ønsker.

   .. tab:: 3. Spesifiser format

      **Dårlig prompt:**

      .. code-block:: text

         Gi meg informasjon om UiOs fakulteter.

      **Bedre prompt:**

      .. code-block:: text

         Lag en tabell med UiOs 8 fakulteter.
         Kolonner: Navn, Forkortelse, Antall studenter (omtrent)
         Sorter alfabetisk etter navn.

      **Hvorfor bedre?**

      Du får et strukturert svar som er lett å bruke videre.

   .. tab:: 4. Definer rollen

      **Dårlig prompt:**

      .. code-block:: text

         Hvordan kan jeg forbedre min skriving?

      **Bedre prompt:**

      .. code-block:: text

         Du er en erfaren kommunikasjonsrådgiver. Jeg jobber
         administrativt ved et universitet og skal ofte skrive
         formelle brev og e-poster. Gi meg 5 konkrete tips til
         hvordan jeg kan forbedre min administrative skriving.

      **Hvorfor bedre?**

      Ved å gi KI-en en rolle, får du svar som er mer relevant for din situasjon.

Nyttige prompt-teknikker
~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Chain of thought (Tankekjede)

      **Teknikk:**

      Be KI-en "tenke høyt" eller "forklare steg for steg".

      **Eksempel:**

      .. code-block:: text

         Forklar trinn for trinn hvordan jeg kan
         organisere et sommerarrangement for 50 personer.

      **Fordel:**

      * Får mer gjennomtenkte svar
      * Enklere å følge resonnementet
      * Bedre for komplekse oppgaver

   .. tab:: Few-shot prompting (Gi eksempler)

      **Teknikk:**

      Gi eksempler på hva du vil ha.

      **Eksempel:**

      .. code-block:: text

         Jeg skal skrive titler til nyhetssaker. Her er eksempler
         på stilen jeg ønsker:

         - "Nytt tilbud: Gratis språkkurs for ansatte"
         - "Viktig: Endringer i møterom-booking fra 1. april"
         - "Påminnelse: Personalseminar 15. mai"

         Skriv en tittel for denne saken:
         "Vi får nytt IT-system for reiseregninger neste måned"

      **Fordel:**

      * Får svar i ønsket stil
      * Lettere enn å forklare stilen med ord

   .. tab:: Rollespill

      **Teknikk:**

      Be KI-en ta rollen som en bestemt type ekspert.

      **Eksempel:**

      .. code-block:: text

         Du er en erfaren prosjektleder ved et norsk universitet.
         Jeg skal lede mitt første prosjekt og er nervøs.
         Gi meg dine beste råd for å lykkes.

      **Fordel:**

      * Får perspektiv fra en bestemt rolle
      * Mer fokuserte svar

   .. tab:: Strukturert output

      **Teknikk:**

      Be om svaret i et bestemt format.

      **Eksempel:**

      .. code-block:: text

         Oppsummer dette møtereferatet i følgende format:

         BESLUTNINGER:
         -
         -

         OPPGAVER:
         - [Person]: [oppgave] - [frist]

         NESTE MØTE:
         [dato og tid]

         [ditt møtereferat her]

      **Fordel:**

      * Får svar klart til bruk
      * Konsistent format

   .. tab:: Iterativ prompting

      **Teknikk:**

      Bygg videre på svarene i en samtale.

      **Eksempel:**

      .. code-block:: text

         Første prompt:
         "Skriv et utkast til e-post om nytt bookingsystem"

         Oppfølging 1:
         "Gjør den mer konsis, maks 3 avsnitt"

         Oppfølging 2:
         "Legg til en setning om hvor de kan få hjelp"

      **Fordel:**

      * Gradvis forbedring
      * Lettere enn å skrive perfekt prompt med én gang

Praktiske eksempler for administrativt arbeid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: E-post og kommunikasjon

      **Eksempel 1: Omformulere til vennligere tone**

      .. code-block:: text

         Denne e-posten føles litt for stram:

         "Møtet er flyttet. Nytt tidspunkt er 14:00.
         Møt presis."

         Omformuler til en vennligere og mer profesjonell tone.

      **Eksempel 2: Forenkle fagspråk**

      .. code-block:: text

         Denne teksten bruker for mye fagsjargong:

         [din tekst]

         Omskriv den slik at ikke-eksperter forstår den,
         men behold den viktige informasjonen.

   .. tab:: Oppsummering

      **Eksempel 1: Oppsummere møtenotater**

      .. code-block:: text

         Oppsummer disse møtenotatene i punktform.
         Trekk ut:
         1. Viktigste beslutninger
         2. Hvem skal gjøre hva
         3. Frister som ble nevnt

         Notater:
         [dine notater her]

      **Eksempel 2: Lage sammendraget av langt dokument**

      .. code-block:: text

         Les dette dokumentet og gi meg:
         - En setning med hovedbudskapet
         - 3-5 kulepunkter med viktigste punkter
         - Anbefalinger/konklusjon

         [dokument her]

   .. tab:: Planlegging

      **Eksempel 1: Lage agenda**

      .. code-block:: text

         Lag en agenda for et 1-times planleggingsmøte
         for sommerarrangement. Vi må diskutere:
         - Dato og sted
         - Budsjett
         - Mat og drikke
         - Program/aktiviteter
         - Påmelding

         Sett av fornuftig tid til hvert punkt.

      **Eksempel 2: Sjekkliste**

      .. code-block:: text

         Lag en sjekkliste for hva jeg må huske når
         jeg arrangerer et seminar for 30 personer
         på et eksternt sted. Inkluder alt fra booking
         til oppfølging etter arrangementet.

   .. tab:: Språk og oversettelse

      **Eksempel 1: Oversette og tilpasse**

      .. code-block:: text

         Oversett denne teksten til engelsk.
         Målgruppen er internasjonale studenter,
         så bruk enkelt språk:

         [norsk tekst]

      **Eksempel 2: Finne riktig terminologi**

      .. code-block:: text

         Hva er den korrekte norske oversettelsen av
         disse engelske universitetsbegrepene?

         - Dean
         - Faculty board
         - Course coordinator

         Gi meg både norsk og en kort forklaring.

Vanlige feil og hvordan unngå dem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Feil 1: For vage prompts

      **Problem:**

      .. code-block:: text

         "Skriv noe om møter"

      **Resultat:** Generelt, ubrukelig svar.

      **Løsning:**

      .. code-block:: text

         "Skriv 5 tips for hvordan jeg kan gjøre våre
         ukentlige teammøter mer effektive. Vi er en gruppe
         på 8 personer som møtes i 1 time."

   .. tab:: Feil 2: For mange krav på én gang

      **Problem:**

      .. code-block:: text

         "Skriv en e-post om det nye systemet, lag også
         en FAQ, en guide, og en presentasjon, og oversett
         alt til engelsk"

      **Resultat:** Overfladisk behandling av alt.

      **Løsning:**

      Del opp i separate prompts - én oppgave om gangen.

   .. tab:: Feil 3: Ikke gi nok kontekst

      **Problem:**

      .. code-block:: text

         "Hva synes du om dette?"
         [uten å forklare hva "dette" er]

      **Resultat:** KI-en gjetter hva du mener.

      **Løsning:**

      .. code-block:: text

         "Jeg har skrevet et utkast til invitasjon for
         et personalseminar. Kan du vurdere om tonen
         er passende og om all viktig info er med?

         [ditt utkast]"

   .. tab:: Feil 4: Forvente perfeksjon med én gang

      **Problem:**

      Bli frustrert hvis første svar ikke er perfekt.

      **Løsning:**

      Bruk iterativ prompting:

      .. code-block:: text

         1. Start med grunnleggende prompt
         2. "Kan du gjøre den kortere?"
         3. "Legg til et avsnitt om hvor de får hjelp"
         4. "Endre tonen til å være mer formell"

Tips for å bli bedre til prompting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   **Slik lærer du god prompting:**

   1. **Eksperimenter**
      - Prøv ulike måter å formulere spørsmål på
      - Se hva som gir best resultat
      - Lek deg med ulike teknikker

   2. **Lagre gode prompts**
      - Når du finner en prompt som fungerer godt, lagre den
      - Bygg opp en samling du kan gjenbruke
      - Del med kolleger

   3. **Iterer**
      - Første svar er sjelden perfekt
      - Følg opp og rafiner
      - Det er helt greit å justere underveis

   4. **Lær av andre**
      - Se på eksempler på prompts online
      - Spør kolleger hva som fungerer for dem
      - Del egne erfaringer

   5. **Vær spesifikk om hva som er galt**
      - I stedet for "Dette var ikke bra", si
      - "Dette var for langt, gjør det kortere" eller
      - "Tonen var for formell, jeg trenger mer avslappet språk"

.. exercise::

   **Praktisk øvelse: Forbedre prompts**

   Her er noen dårlige prompts. Hvordan ville du forbedret dem?

   1. "Skriv noe fint"
   2. "Hjelp meg"
   3. "Hva med den tingen?"
   4. "Lag en liste"

   .. solution::

      **Mulige forbedringer:**

      1. **Original:** "Skriv noe fint"
         **Forbedret:** "Skriv en gratulasjon til en kollega som har jobbet her i 25 år. Tonen skal være varm og personlig, ca 100 ord."

      2. **Original:** "Hjelp meg"
         **Forbedret:** "Jeg skal lede mitt første møte neste uke med 6 kolleger. Kan du gi meg konkrete tips for hvordan jeg forbereder meg og leder møtet profesjonelt?"

      3. **Original:** "Hva med den tingen?"
         **Forbedret:** "Jeg har skrevet denne e-posten om endringer i lunsjordningen. Kan du sjekke om budskapet er klart og om jeg har glemt noe viktig? [e-post her]"

      4. **Original:** "Lag en liste"
         **Forbedret:** "Lag en liste over 10 ting jeg må huske på når jeg arrangerer et jubileumsseminar for 50 ansatte. Inkluder både planlegging, gjennomføring og oppfølging."

Eksempel: Fra dårlig til god prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La oss se et komplett eksempel på hvordan en prompt kan forbedres:

.. tabs::

   .. tab:: Versjon 1 - Dårlig

      .. code-block:: text

         Skriv om møter

      **Problem:** Altfor vagt. Hva slags tekst? Om hva med møter?

   .. tab:: Versjon 2 - Bedre

      .. code-block:: text

         Skriv tips om møter

      **Problem:** Fortsatt vagt. Tips til hvem? Hva slags møter? Hvor mange tips?

   .. tab:: Versjon 3 - Mye bedre

      .. code-block:: text

         Skriv 5 tips for effektive møter

      **Problem:** Bedre, men mangler kontekst. Hvilke typer møter? Hvem er målgruppen?

   .. tab:: Versjon 4 - God!

      .. code-block:: text

         Jeg leder ukentlige teammøter med 6 kolleger i
         administrativ stilling. Møtene er ofte kaotiske
         og ineffektive. Gi meg 5 konkrete, praktiske tips
         for hvordan jeg kan gjøre møtene bedre.

         Fokuser på:
         - Forberedelse
         - Struktur under møtet
         - Oppfølging

      **Hvorfor god:** Spesifikk kontekst, tydelig mål, definert struktur.

Oppsummering
~~~~~~~~~~~~

.. note::

   **Nøkkelpunkter for god prompting:**

   1. **Vær spesifikk** - Jo mer detaljer, jo bedre svar
   2. **Gi kontekst** - Forklar situasjonen og formålet
   3. **Spesifiser format** - Si hvordan du vil ha svaret strukturert
   4. **Bruk eksempler** - Vis hva du mener hvis mulig
   5. **Iterer** - Første forsøk er sjelden perfekt
   6. **Eksperimenter** - Test ulike tilnærminger
   7. **Vær tålmodig** - God prompting er en ferdighet som utvikles over tid

.. exercise::

   **Oppgave: Skriv din egen prompt**

   Tenk på en faktisk oppgave du har i ditt arbeid denne uken. Skriv en god prompt for å få hjelp med denne oppgaven.

   Sjekk at du har inkludert:
   - [ ] Spesifikk beskrivelse av hva du vil ha
   - [ ] Kontekst (hvem er målgruppen, hva er formålet)
   - [ ] Ønsket format eller struktur
   - [ ] Tone eller stil
   - [ ] Eventuelle begrensninger (lengde, kompleksitetsnivå, osv.)

   Prøv prompten i et KI-verktøy og iterer til du er fornøyd!

.. note::

   **Gratulerer!** Du har nå fullført hoveddelen av KI-introduksjonskurset. I siste episode oppsummerer vi det viktigste og gir tips til videre læring.
