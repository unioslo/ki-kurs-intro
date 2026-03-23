
Tilgjengelige tjenester
=======================

.. uio-source:: Oppdatert liste over tjenester

   **Viktig:** Sjekk alltid https://www.uio.no/tjenester/it/ki/ for oppdatert informasjon.


GPT UiO
-------------

GPT UiO er UiOs personverntrygge KI-chat. Til forskjell fra ChatGPT som har en rekke andre tjenester knyttet til seg som f.eks. internettsøk, så er GPT UiO kun en enkel chat tjeneste (enn så lenge). 
Det betyr at den kun bruker en språkmodell til å genere et tekstsvar, og utfører ikke handlinger som f.eks. å gjøre internettsøk eller hente informasjon fra andre systemer. 

GPT UiO har allikevel en *assistent* funksjonalitet. Med den kan man lage egne instruksjoner som ligger som et ekstra lag i tillegg til instruksjonene i chaten, man kan laste opp filer, slik at når man gjør spørringer, 
så vil modellen lete gjennom filene og finne relevant informasjon som den benytter i svaret, og man kan velge en spesifikk modell som assistenten benytter. 
Assistenten kan deles med andre, og låses eller våre åpen for redigering. 

GPT UiO tilbyr en rekke forskjellige språkmodeller, inkludert språkmodeller som kjører på servere som UiO eller vår samarbeidspartner NTNU eier og drifter. 
Dette gjør at man har ekstra kontroll på all data og kan være trygg på at ingenting lastes opp "i skyen".

Med personlige API nøkler kan du knytte GPT sine språkmodeller opp mot andre applikasjoner, enten de du selv har skrevet, eller applikasjoner fra andre leverandører (om de støtter dette).


**Nøkkelpunkter**

* UiO sin personvernvennlig chat tjeneste
* Tilgang til OpenAI's GPT modeller
* Tilgang til modeller som kjører i Norge og hvor ingen data forlater UiO eller vår samarbeidspartner NTNU
* Tilgang til språkmodeller trent på norsk 
* Støtter opptil røde data
* Personlige API nøkler for integrasjon mot andre applikasjoner
* Du trenger kun din UiO brukerkonto for å få tilgang
* Gratis for ansatte og studenter ved UiO

.. uio-source:: Dokumentasjon

   `GPT UiO <https://www.uio.no/tjenester/it/ki/gpt-uio/index.html>`_




.. uio-colorbox-3::

   **Fordypning**

   .. uio-detail:: Eksempel på assistent til bruk i administrasjon og i undervisning


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


.. uio-colorbox-3::

   **Fordypning**

   .. uio-detail:: Hva er API tilgang?

      API (Application Programming Interface) er en teknisk "bro" som lar ulike programvarer snakke med hverandre.
      Med API-tilgang til GPT UiO kan du koble språkmodellene til egne applikasjoner eller tredjepartsverktøy.

      **Hvordan fungerer det med lokale LLM-er?**

      UiO og NTNU tilbyr språkmodeller som kjører på egne servere i Norge. Ved å bruke API-nøkler kan du:

      * Koble disse sikre, lokale modellene til KI-verktøy du allerede bruker
      * Såfremt KI-verktøyet ikke kommuniserer utad (f.eks. gjør internett søk, eller sender informasjon til utenlandske sky tjenester):
         * Behandle sensitive data trygt
         * Integrere KI-funksjonalitet i interne systemer uten å gå på kompromiss med personvern

      **Eksempel:** Et forskningsprosjekt kan bruke API-et til å analysere konfidensielle dokumenter med en lokal LLM, 
      ved hjelp av egendefinert lokal KI applikasjon - alt mens dataene blir værende innenfor UiOs/NTNUs infrastruktur.

NotebookLM
-------------
NotebookLM er en KI-drevet assistent fra Google spesialisert for å arbeide med dokumenter. 

I NotebookLM bygger man seg først en egen "kunnskapshub" som inneholder dokumenter og lenker til nettsteder, eller til og med lydopptak fra forelesninger. 
Dette er grunnlaget NotebookLM benytter for å generere svar på spørsmål, eller produkter som oppsummeringer i tekst eller audio, quizer eller presentasjoner. 
NotebookLM har med andre ord en hel del spennende funksjonaliteter. 

NotebookLM er tro mot kildene du benytter, og du kan derfor oppleve å få mer presise svar enn for eksempel ved bruk av gpt.uio.no. 
Skal du jobbe med dokumenter anbefaler vi at du prøver dette produktet!

**Nøkkelpunkter**

* KI tjeneste fra Google
* Benytter Google sin Gemini språkmodell
* Spesialisert på arbeid mot dokumenter
* Du må ha Google Workspace konto gjennom UiO for å få tilgang
* Databehandleravtale på plass
* Gratis for ansatte og studenter ved UiO
* *Tjenesten skal kun brukes med UiO konto* - sjekk at du er logget inn med UiO konto og ikke din egen private Google konto!

.. uio-dont:: Viktig

   * Når du arbeider med dokumenter er det viktig at du har kontroll på opphavsretten til materialet: Ikke last opp dokumenter du ikke har rettigheter til å dele.
   * Ikke last opp dokumenter som inneholder sensitiv informasjon. NotebookLM er kun godkjent for opptil gule data.

.. uio-source:: Dokumentasjon

   Les om `NotebookLM på UiO sine nettsider <https://www.uio.no/tjenester/it/ki/notebooklm/>`_. 
   
   Her finner du nyttig og viktig informasjon om vilkår for bruk og veiledning for å komme igang med NotebookLM: 


Autotekst
-----------

Autotekst er en tjeneste utviklet av UiO som transkriberer tale til tekst ved hjelp av OpenAI sin automatiske språkgjenkjenningsmodell Whisper.
Tjenesten kjører i sin helhet på UiOs servere, og støtter derfor opp til røde data. 

Autotekst kan benyttes til å transkribere opptak av møter, av forelesninger eller av intervjuer for å nevne noen bruksområder. 
Man kan benytte Nettskjema-diktafon appen for automatisk transkribering, eller laste opp lydfiler fra f.eks. Panopto eller Zoom. 

Whisper er god på norsk, takket være Nasjonalbibliotekets norsk-trente Whisper modell. 


**Nøkkelpunkter**

* Tale til tekst, sikkert behandlet på UiO
* Opptak kan sendes direkte til Autotekst via Nettskjema-diktafon appen 
* Kan behandle opptil sorte data hvis tjenesten kjører i Tjenester for Sensitiv Data
* Kan lage en oppsummering i tillegg til transkripsjonen, nyttig for eksempel som et utgangspunkt til et møtereferat
* Du trenger kun din UiO brukerkonto for å få tilgang

.. uio-source:: Dokumentasjon

   * `Autotekst <https://www.uio.no/tjenester/it/lyd-video/autotekst/index.html>`_
   * `Nettskjema-diktafon <https://www.uio.no/tjenester/it/adm-app/nettskjema/hjelp/diktafon.html>`_

Microsoft Copilot (Business/Enterprise)
-----------------------------------------

Dette er Microsoft sin egen tjeneste, og den kjører i sin helhet på utenlandske servere. UiO har Databehandleravtale med Microsoft, 
og dette sikrer at data ikke lekkes utenfor organisasjonen, og ikke blir benyttet til å trene modeller videre. 
Men fordi data sendes til utenlandske servere er tjenesten kun godkjent for grønne data (åpne data.) Du må derfor være spesielt forsiktig når du benytter tjenesten. 
Vær nøye med å ikke dele personsensitiv eller konfidensiell informasjon med Microsoft Copilot. 

I Microsoft Copilot fungerer som en vanlig chat-tjeneste med tilgang til internett søk. 
Bildegenerering basert på tekst er også mulig, og i tillegg har den verktøy for diverse oppgaver relatert til undervising. 


.. uio-dont:: Viktig

   Ingen personopplysninger eller annen informasjon som ikke er åpent tilgjengelig må lastes opp i Microsoft Copilot.

**Nøkkelpunkter**

* Integrert med Microsoft 365
* Kan brukes i Word, Outlook, Teams, PowerPoint
* Bildegenerering
* Verktøy relatert til undervisning
* Kun godkjent for grønne data
* Databehandleravtale på plass
* Du trenger kun din UiO brukerkonto for å få tilgang