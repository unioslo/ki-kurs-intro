API tilgang
============


API (Application Programming Interface) er en teknisk "bro" som lar ulike programvarer snakke med hverandre.
Med API-tilgang til GPT UiO kan du koble språkmodellene til egne applikasjoner eller tredjepartsverktøy som for eksempel en agent.

Hvordan fungerer det med lokale LLM-er?
-----------------------------------------

UiO og NTNU tilbyr språkmodeller som kjører på egne servere i Norge (lokale språkmodeller). 
    
Ved å bruke API-nøkler kan du:

* Koble disse sikre, lokale modellene til KI-verktøy du allerede bruker (såfremt verktøyet tillater det)
* Integrere KI-funksjonalitet i interne systemer
* Sette opp automatikk som benytter LLMen, f.eks i programmeringsspråk som Python eller R

Det er veldig viktig å forstå at API tilgang til de lokale LLMene *ikke* automatisk betyr at du kan behandle personsensitiv informasjon eller annen konfidensiell informasjon trygt.
Det kommer helt an på hvilken applikasjon bruker, og om du har kontroll på at denne applikasjonen ikke sender informasjon ut til tredjepartssystemer.


.. canvas-tabs:: Eksempler på bruk

    .. canvas-tab:: Utrygg bruk

        Du har koblet opp en lokal språkmodell til en agentisk kode assistent. 
        Agenten kommuniserer med en utenlands server, og sender for eksempel logger eller annen data systemet anser som relevant fra din maskin til den utenlandske serveren.
        Med andre ord: selv om du benytter en lokal språkmodell, så sendes allikevel informasjon ut. 

    .. canvas-tab:: Trygg bruk

        Et forskningsprosjekt kan bruke API-et til å analysere konfidensielle dokumenter med en lokal LLM, 
        ved hjelp av egenutviklet lokal KI applikasjon som ikke sender noe data ut fra systemet. 
        All data blir trygt værende på maskinen du kjører agenten på (f.eks. din laptop) og på UiOs/NTNUs infrastruktur.

    
Hvordan være (nesten) helt trygg
---------------------------------

Om du vil være (nesten) helt trygg, så kan benytte en lokal LLM og kjøre agenten i en virtuell maskin (VM) eller i en container uten nettverkstilgang. 
Om du velger aktivt hvilke filer du flytter over inn i VMen eller containeren sikrer du en høy grad av kontroll. 