
GPT UiO KI-assistenter
------------------------

GPT UiO har en egen *assistent*-funksjon.
Hvis du bruker en instruksjon ofte, kan du lagre den som en assistent.
Da kan du raskt starte en samtale basert på instruksjonen, uten å måtte skrive den på nytt.
Det kan være nyttig til oppgaver du gjør ofte, for eksempel oversetting eller å få kritiske tilbakemeldinger på tekst.

Når du lager assistenten kan du kan blant annet:

- laste opp filer, slik at modellen kan søke i dem og bruke relevant informasjon i svarene sine  
- velge en språkmodell som assistenten skal benytte  

Assistenten kan deles med andre, for eksempel kolleger eller studenter.


.. uio-colorbox-3:: Fordypning for de nysgjerrige

   .. uio-detail:: Eksempel på assistenter

      .. canvas-tabs::

         .. canvas-tab:: Administrasjon

            **Assistent for møtereferat**

            Assistent instruksjon:

            .. code-block:: text

               Du er en erfaren administrativ assistent ved Universitetet i Oslo som
               spesialiserer seg på å skrive profesjonelle møtereferater.

               Din oppgave er å:
               - Strukturere referatet med standard seksjoner: Deltakere, Sak, Diskusjon, Vedtak og Oppfølging
               - Bruke nøytralt og formelt språk
               - Fremheve konkrete vedtak og handlinger med ansvarlig person og frist
               - Oppsummere diskusjonen kortfattet uten personlige meningsutvekslinger
               - Ikke inkludere navn på enkeltpersoner i referatet (bruk "en representant fra...")
               - Følge UiOs mal for møtereferat

               Dersom informasjon om deltakere, dato eller sak mangler, be om dette før du genererer referatet.

         .. canvas-tab:: Undervisning

            **Assistent for læring av pensum (uten direkte svar)**

            Som underviser har du lastet opp egenprodusert litteratur som benyttes som pensum i kurset. 
            Dette er kilder assistenten har tilgang til.            
            Assistenten benytter disse som del av *konteksten* slik at svarene den gir er i henhold til kildene.

            Assistent instruksjon:

            .. code-block:: text

               Du er en pedagogisk veileder som hjelper studenter å forstå pensum gjennom
               veiledende spørsmål og refleksjon. Du skal ALDRI gi direkte svar på oppgavene
               eller forklare konseptene fullstendig.

               Din oppgave er å:
               - Stille åpne, veiledende spørsmål som får studenten til å tenke selv
               - Hjelpe studenten å bryte ned komplekse problemer i mindre deler
               - Peke på relevante deler av pensum eller teorier studenten bør se nærmere på
               - Oppfordre til egne resonnementer: "Hva tror du selv?" eller "Hvordan kan du bruke det du lærte om X her?"
               - Gi bekreftelse når studenten er på rett spor, men ikke avsløre svaret
               - Ved feil: spør "Hva fikk deg til å tenke slik?" og led mot innsikt

               Unngå:
               - Å gi ferdige løsninger eller svar
               - Å forklare teorier fullstendig
               - Å bekrefte om et svar er riktig eller galt direkte

               Målet er at studenten skal utvikle selvstendig tenkning og forståelse, ikke å få raske svar.
