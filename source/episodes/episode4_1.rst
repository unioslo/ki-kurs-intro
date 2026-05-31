
GPT UiO
========

GPT UiO er UiOs personverntrygge KI-chat. 

I GPT UiO kan du velge mellom flere ulike språkmodeller - altså hvilken «hjerne» tjenesten bruker.  
Modellene har forskjellig størrelse og kapabilitet (som støtte av bilder) og bruksområder, 
men en spesielt viktig forskjell mellom modellene er om de kjører i skyen (OpenAI sine GPT modeller i Microsoft Azure skyen) eller *lokalt*.
Med *lokalt* mener vi på servere som eies og driftes av UiO eller vår samarbeidspartner NTNU.

Mens alle modellene, både de i skyen og de som lokalt sikrer at GDPR reglene følges, er du ekstra godt beskyttet om du velger de lokale modellene.
Det er da går *ingen* data til skyen, alt forblir på UiO eller NTNU sine systemer.

Noen av de lokale modellene kan i tillegg håndtere opp til `røde data <https://www.uio.no/tjenester/it/sikkerhet/lsis/tillegg/lagring/infoklasser.html>`_.


.. uio-viktig::
   
   * Velger du en lokal språkmodell, har du ekstra kontroll over dataene dine og kan være trygg på at ingenting lastes opp i skyen.  
   * Velger du en skybasert modell, behandles inn- og utdata midlertidig av Microsoft Azure OpenAI innenfor GDPR-kompatible regioner (Europa).

   Uavhengig av om du bruker en lokal eller skybasert modell, lagres all logg samt inn- og utdata kun på UiOs servere. Ditt brukernavn deles ikke med Microsoft.
   Derfor er GPT UiO GDPR-kompatibel. 

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

API (Application Programming Interface) er en teknisk "bro" som lar ulike programvarer snakke med hverandre.
Med API-tilgang til GPT UiO kan du koble språkmodellene til egne applikasjoner eller tredjepartsverktøy som for eksempel en agent.

.. uio-info:: Avansert bruk

   API oppkobling er en litt mer avansert KI-bruk og er ikke for alle. 
   Du kan derfor hoppe over denne delen om API tilgang ikke er relevant for deg.

Kode-agenter som for eksempel Codex, OpenCode eller Claude Code er eksempler på en type agenter.
Vi nevner disse spesielt fordi de er så mye mer enn bare programmeringshjelpere. 
De kan hjelpe med alt fra dokumentgenerering og dataanalyse til integrering av ulike programvaresystemer, helt uten at du må skrive kode selv. 
Tenk på dem som tekniske assistenter som bygger bro mellom administrative behov og automatisering, noe som sparer tid og reduserer manuelt arbeid.

Ofte vil en gitt kode-agent ha et standardoppsett meg en egen språkmodell som kjører i en skytjeneste. 
For eksempel kommer Codex med en av OpenAI sine GPT modeller som standard, og for å bruke den må du ha konto hos OpenAI.
Men de fleste har også mulighet til å koble opp andre språkmodeller via API. 
Man kan altså bytte motoren i agenten, slik vi forklarte i episode 1. 

Språkmodeller på UiO og NTNU
+++++++++++++++++++++++++++++

For å ivareta datasikkerhet og personvern skal man på UiO benytte `godkjente KI-tjenester <https://www.uio.no/tjenester/it/ki/>`_. 
Kode-agentene med sitt standardoppsett ivaretar ikke disse hensynene. 

Men på UiO tilbyr vi språkmodeller via GPT UiO som kjører på egne servere i Norge (lokale LLMer). 
Kobler du agenten opp mot en av disse modellene er personvern og datasikkerhet mye bedre ivaretatt. 

Det er veldig viktig å forstå at API tilgang til de lokale LLMene *ikke* automatisk betyr at du kan behandle personsensitiv informasjon eller annen konfidensiell informasjon trygt.
Det kommer helt an på hvilken applikasjon bruker, og om du har kontroll på at denne applikasjonen ikke sender informasjon ut til tredjepartssystemer.


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



