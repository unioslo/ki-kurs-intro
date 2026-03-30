
GPT UiO
=======================

GPT UiO er UiOs personverntrygge KI-chat. GPT UiO tilbyr en rekke forskjellige språkmodeller, både OpenAI sine GPT modeller som kjører i skyen, og språkmodeller som kjører på servere som UiO eller vår samarbeidspartner NTNU eier og drifter (lokale språkmodeller). 
I begge tilfeller lagres all logg- og inn- og utdata på UiOs servere, og ditt brukernavn blir ikke utlevert.

Når du velger en av de lokale språkmodellene har du ekstra kontroll på dataene og kan være trygg på at ingenting lastes opp "i skyen". 
Hvis du velger en av OpenAI sine modeller må du være oppmerksom på at inn- og utdata blir behandlet midlertidig av Microsoft Azure OpenAI innenfor GDPR-kompatible regioner.

Til forskjell fra ChatGPT som har en rekke andre tjenester knyttet til seg som f.eks. internettsøk, så er GPT UiO kun en enkel chat tjeneste (enn så lenge). 
Det betyr at den kun bruker en språkmodell til å genere tekst, og har ikke annen funksjonalitet som f.eks. å gjøre internettsøk, hente ut informasjon fra andre systemer, eller utføre handlinger som for eksempel opprette/endre filer.

GPT UiO har allikevel en *assistent* funksjonalitet. Med den kan man lage egne instruksjoner som ligger som et ekstra lag i tillegg til instruksjonene i chatten, man kan laste opp filer, slik at når man gjør spørringer, 
så vil modellen lete gjennom filene og finne relevant informasjon som den benytter i svaret, og man kan velge en spesifikk modell som assistenten benytter. 
Assistenten kan deles med andre, og låses eller våre åpen for redigering. 


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

   .. raw:: html

      <p><a href="https://www.uio.no/tjenester/it/ki/gpt-uio/index.html" target="_blank">GPT UiO</a></p>



.. uio-colorbox-3:: Fordypning


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


.. uio-colorbox-3:: Fordypning

   .. uio-detail:: Hva er API tilgang?

      API (Application Programming Interface) er en teknisk "bro" som lar ulike programvarer snakke med hverandre.
      Med API-tilgang til GPT UiO kan du koble språkmodellene til egne applikasjoner eller tredjepartsverktøy som for eksempel en agent.

      **Hvordan fungerer det med lokale LLM-er?**

      UiO og NTNU tilbyr språkmodeller som kjører på egne servere i Norge (lokale språkmodeller). 
            
      Ved å bruke API-nøkler kan du:

      * Koble disse sikre, lokale modellene til KI-verktøy du allerede bruker (såfremt verktøyet tillater det)
      * Integrere KI-funksjonalitet i interne systemer
      * Sette opp automatikk som benytter LLMen, f.eks i programmeringsspråk som Python eller R

      Det er veldig viktig å forstå at API tilgang til de lokale LLMene *ikke* automatisk betyr at du kan behandle personsensitiv informasjon eller annen konfidensiell informasjon trygt.
      Det kommer helt an på hvilken applikasjon bruker, og om du har kontroll på at denne applikasjonen ikke sender informasjon ut til tredjepartssystemer.

      **Eksempel på utrygg bruk**
      Du har koblet opp en lokal språkmodell til en agentisk kode assistent. 
      Agenten kommuniserer med en utenlands server, og sender for eksempel logger eller annen data systemet anser som relevant fra din maskin til den utenlandske serveren.
      Med andre ord: selv om du benytter en lokal språkmodell, så sendes allikevel informasjon ut. 

      **Eksempel på trygg bruk:** Et forskningsprosjekt kan bruke API-et til å analysere konfidensielle dokumenter med en lokal LLM, 
      ved hjelp av egenutviklet lokal KI applikasjon som ikke sender noe data ut fra systemet. 
      All data blir trygt værende på maskinen du kjører agenten på (f.eks. din laptop) og på UiOs/NTNUs infrastruktur.

      **Hvordan være (nesten) helt trygg**
      Om du vil være (nesten) helt trygg, så kan benytte en lokal LLM og kjøre agenten i en virtuell maskin (VM) eller i en container uten nettverkstilgang. 
      Om du velger aktivt hvilke filer du flytter over inn i VMen eller containeren sikrer du en høy grad av kontroll. 