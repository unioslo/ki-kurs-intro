Oppsummering kapittel 5
========================
I dette kapittelet har vi lært om de godkjente KI-tjenestene på UiO, hvorfor det er viktig å bruke dem, og hvilke tjenester som passer best til ulike formål.

.. uio-reflect:: Test deg selv

  Diskuter selv eller med en kollega:

  1. Hvilke KI-tjenester er godkjent på UiO?
  2. Hvorfor er det viktig å bruke dem?
  3. Hvilke KI-tjenester vil være nyttig for deg og dine arbeidsoppgaver?


Repetisjon
------------------------------------

Tabellen under gir deg en oversikt over de godkjente KI-tjenestene ved UiO: hva de egner seg til,
hvilken dataklasse de er godkjent for, og om de kjører på UiOs egne IT-systemer eller i skyen.

.. list-table:: UiOs godkjente KI-tjenester
   :header-rows: 1
   :widths: 16 34 18 32
   :class: uio-table

   * - Tjeneste
     - Bruksområde
     - Beskyttelsesgrad
     - Skytjeneste eller UiO-tjeneste
   * - **GPT UiO**
     - KI-chat til tekstarbeid. Du kan velge mellom flere språkmodeller og lage og dele egne KI-assistenter.
     - Opptil 🔴 rød, men bare med en modell som er godkjent for det
     - UiO-tjeneste. Data lagres hos UiO. De største modellene kjører i skyen (OpenAI i Azure), de mindre lokalt hos UiO eller NTNU.
   * - **Autotekst**
     - Transkribering av lyd- og videoopptak, for eksempel møter, forelesninger og intervjuer.
     - Opptil 🔴 rød
     - UiO-tjeneste. Kjører lokalt på UiOs IT-systemer.
   * - **TSD-Autotekst**
     - Transkribering av opptak som er strengt fortrolige, for eksempel helseintervjuer.
     - Opptil ⚫ svart
     - UiO-tjeneste. Kjører i lokalt på UiOs IT-systemer i Tjenester for Sensitive Data (TSD).
   * - **Nettskjema-diktafon**
     - Mobilapp for opptak som sendes trygt og automatisk til transkribering i (TSD-)Autotekst.
     - Opptil ⚫ svart, hvis opptaket er knyttet til et nettskjema i TSD
     - UiO-tjeneste. Bruker UiOs Nettskjema og (TSD-)Autotekst i bakkant.
   * - **Gemini**
     - Generell KI-chat med søk i åpne nettsider. Egnet til faktasøk, bildegenerering og til å lage pdf, presentasjoner og regneark.
     - Opptil 🟡 gul
     - Skytjeneste fra Google. Kjører i Google Cloud, utenfor UiOs systemer. UiO har databehandleravtale.
   * - **Gemini Notebook**
     - KI-assistent for egne dokumenter og kilder. Gir kildetro svar og lager oppsummeringer, quizzer og podkaster.
     - Opptil 🟡 gul
     - Skytjeneste fra Google. Kjører i Google Cloud, utenfor UiOs systemer. UiO har databehandleravtale.
   * - **Microsoft Copilot Chat**
     - Enkel KI-chat med nettsøk. Arbeider med tekst, bilder og video, og har ferdige instruksjonsforslag som hjelper deg i gang.
     - Kun 🟢 grønn
     - Skytjeneste fra Microsoft. Kjører utenfor UiOs systemer. Bruker GPT-modeller fra OpenAI.

.. uio-colorbox-3:: Husk

   Beskyttelsesgraden i tabellen er den *høyeste* dataklassen tjenesten er godkjent for.
   Du skal alltid bruke den tjenesten som dekker behovet ditt, og aldri dele UiO-data med
   KI-tjenester som ikke er godkjent ved UiO.


Neste kapittel
--------------

Du har nå gjennomført grunnkurset i KI! I neste og siste kapittel får du en oppsummering av det viktigste,
og konkrete tips til hvordan du kan ta kunnskapen videre i praksis.
