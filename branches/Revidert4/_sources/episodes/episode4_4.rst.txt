
GPT UiO personlige API-nøkler
==============================

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
