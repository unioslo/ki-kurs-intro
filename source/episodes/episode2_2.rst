
Hvordan genererer språkmodeller tekst?
================================================

Språkmodeller er matematiske modeller som jobber med tall. Før modellen kan behandle instruksjonen din må den deles opp i mindre biter, kalt *tokens*, og hvert token gjøres så om til et tall.
Instruksjonen din brukes så som kontekst for å generere ny tekst.

1. Basert på konteksten og mønstre den har lært, beregner den sannsynlighetene for neste ord i setningen.
2. Den trekker et ord, med litt tilfeldighet, og legger det til svaret.
3. Den gjentar prosessen for neste ord, og neste ord, osv.
4. Modellen stopper når den "mener" svaret er fullstendig.

.. uio-viktig::

   Modellen "tenker" ikke på om informasjonen er korrekt. Den genererer bare det som er statistisk sannsynlig basert på mønstre.


.. uio-colorbox-3:: Fordypning for de nysgjerrige

   .. uio-detail:: Tokens og tokenisering

      Før språkmodellen kan behandle teksten må den deles opp i mindre biter, kalt tokens.
      Hvert token gjøres om til et tall, fordi datamaskiner regner på tall.
      For eksempel kan ordet "er" representeres av tallet *2781* hvert sted i teksten det står.
      Et token kan være et helt ord, men det kan også være en mindre del av et ord.
      Denne oppdelingen kalles tokenisering, og programmet som gjør oppdelingen kalles en tokeniserer (tokenizer).
      På websiden `Tiktokenizer <https://tiktokenizer.vercel.app/?model=cl100k_base>`__ kan du skrive inn tekst og se hvordan den deles opp i tokens.

   .. uio-detail:: Determinisme/forutsigbarhet

      Språkmodeller kan være deterministiske (forutsigbare) hvis de alltid bruker det mest sannsynlige ordet.
      Men det ville vært ganske kjedelig hvis for eksempel ChatGPT alltid ga samme svar på samme spørsmål.
      Derfor er det med hensikt lagt inn litt tilfeldighet i hvordan modellene svarer.
      I stedet for å velge det mest sannsynlige ordet, trekker modellen det neste ordet basert på sannsynlighetene.
      Det er altså mer sannsynlig å trekke et ord som ofte kommer etter ordene som er generert til nå.

   .. uio-detail:: Tilfeldighet og temperatur

      Vi kan justere hvor "tilfeldig" eller "kreativ" tekst språkmodellen skal generere.
      Den mest brukte innstillingen er *temperatur*. Temperaturen kontrollerer altså hvordan språkmodellen trekker ord fra sannsynlighetsfordelingen.
      Med høy temperatur øker sannsynligheten for å trekke sjeldne ord.

      * **Lav temperatur** (f.eks. 0.2): Mer forutsigbar, velger de mest sannsynlige ordene.
      * **Høy temperatur** (f.eks. 1.5): Mer kreativ, kan velge mindre sannsynlige ord.

      Du kan få dermed ulike svar på samme spørsmål. Noen ganger kan svarene være mer kreative, andre ganger mer "standard". Det er ingen garanti for at samme spørsmål gir samme svar neste gang.

      De fleste vanlige tjenester har en standard temperatur som ikke kan justeres, men noen lar deg sette denne etter behov.


   .. uio-detail:: GPT simulator

      Lek med GPT 2 simulatoren for en forenklet model av hvordan LLMer som GPT fungerer!

      https://poloclub.github.io/transformer-explainer/


.. uio-reflect:: Refleksjon

   Hvorfor kan en språkmodell gi feilinformasjon selv om svaret høres veldig troverdig ut?

   .. uio-answer::

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk.
      Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant.
      Derfor kan den produsere feilinformasjon med samme selvtillit som riktig informasjon.

