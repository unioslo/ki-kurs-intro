
GPT UiO
========

GPT UiO er UiOs personverntrygge KI-chat. 

I GPT UiO kan du velge mellom flere ulike språkmodeller - altså hvilken «hjerne» tjenesten bruker.  
Modellene forskjellig kapabilitet (som støtte av bilder) og bruksområder, men en spesielt viktig forskjell mellom modellene er om de kjører i skyen (OpenAI sine GPT modeller i Microsoft Azure skyen) og modeller som kjører lokalt på servere som eies og driftes av UiO eller vår samarbeidspartner NTNU.
Modellene som kjører hos UiO eller NTNU er klassifisert til å håndtere opp til `røde data <https://www.uio.no/tjenester/it/sikkerhet/lsis/tillegg/lagring/infoklasser.html>`_.

.. uio-colorbox-3:: Fordypning

   .. uio-detail:: Velge en annen modell enn standard

      .. figure:: ../images/gpt-modell-meny.png                                                                                                                  
            :align: center                                                                                                                                         
            :width: 75%                                                                                                                                            
            :alt: Meny i GPT som viser de forskjellige språkmodellene man kan velge blant                                        
                                                                                                                                                               
      Klikk på nedover-pilen for å se hvilke språkmodeller du kan velge mellom


   .. uio-detail:: Eksempel på språkmodeller i GPT UiO

      .. figure:: ../images/gpt-uio-modeller.png                                                                                                                 
            :align: center                                                                                                                                         
            :width: 75%                                                                                                                                            
            :alt: Meny i GPT som viser de forskjellige språkmodellene man kan velge blant                                        
                                                                                                                                                               
      Her ser du listen over de forskjellige språkmodellen som GPT UiO tilbyr. Listen oppdateres når nye modeller eller versjoner blir tilgjengelig.
      De røde boksene viser at noen av modellene kjører lokalt på NTNU. De andre kjører i Microsoft Azure skyen.

Velger du en lokal språkmodell, har du ekstra kontroll over dataene dine og kan være trygg på at ingenting lastes opp i skyen.  
Velger du en skybasert modell, behandles inn- og utdata midlertidig av Microsoft Azure OpenAI innenfor GDPR-kompatible regioner.

Uavhengig av om du bruker en lokal eller skybasert modell, lagres all logg samt inn- og utdata kun på UiOs servere. Ditt brukernavn deles ikke med Microsoft.
Derfor er GPT UiO GDPR-kompatibel. 



GPT UiO KI-assistenter
------------------------

GPT UiO har en egen *assistent*-funksjon. Med denne kan du opprette faste instruksjoner som legges som et ekstra lag oppå det du skriver i selve chatten.  

Når du lager assistenten kan du kan blant annet:

- laste opp filer, slik at modellen kan søke i dem og bruke relevant informasjon i svarene sine  
- velge en spesifikk språkmodell som assistenten skal benytte  

Assistenten kan deles med andre, og kan enten låses for redigering eller gjøres åpen slik at flere kan endre den.


.. uio-colorbox-3:: Fordypning

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


GPT UiO personlige API-nøkler
-------------------------------

Med personlige API-nøkler kan du koble GPT UiOs språkmodeller til andre applikasjoner, både egenutviklede løsninger og tredjepartsapplikasjoner som støtter dette.

Eksempler på bruk av API-nøkler:

1. **Interne og/eller egenutviklede systemer ved UiO**

   API-nøkkelen legges inn i konfigurasjonen til et internt system (for eksempel et fagsystem eller webverktøy), som så kan sende tekst til GPT UiO og vise svarene direkte i løsningen.


2. **Eksterne verktøy brukeren selv kobler til**

   API-nøkkelen legges inn i et eksternt verktøy (for eksempel et notat-, analyse- eller kodeverktøy) som støtter «egen API-nøkkel», og verktøyet bruker da GPT UiO til tekstgenerering eller analyse.   
   Sikkerhet og databehandling avhenger både av GPT UiO og det eksterne verktøyet.



.. uio-dont:: Viktig!
   
   * Del aldri API-nøkkelen din offentlig eller i kode som ligger åpent.  
   * Behandle nøkkelen som et passord, og oppbevar den sikkert (for eksempel i miljøvariabler eller en hemmelighets‑/secret‑tjeneste).


Nøkkelpunkter
--------------

* UiO sin personvernvennlig chat tjeneste
* Tilgang til OpenAI's GPT modeller
* Tilgang til åpne modeller som kjører i Norge og hvor ingen data forlater UiO eller vår samarbeidspartner NTNU
* Støtter opptil røde data
* Personlige API nøkler for integrasjon mot andre applikasjoner
* Du trenger kun din UiO brukerkonto for å få tilgang
* Gratis for ansatte og studenter ved UiO

.. uio-source::  Lenke til UiOs nettsider

   `GPT UiO <https://www.uio.no/tjenester/it/ki/gpt-uio/index.html>`_



