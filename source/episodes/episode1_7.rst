KI-agenter
===============

Vi har allerede snakket om neste begrep, nemlig KI-agenten. 
Mens KI-assistenten egentlig ikke er så mye mer enn en KI med spesifikke instruksjoner på hvordan den skal oppføre seg, 
så er KI agenten gjerne en avansert KI-assistent som i tillegg kan utføre *handlinger* i andre IT-systemer. 
KI-agenten nøyer seg ikke med å fortelle deg hvordan du løser en oppgave, den utfører oppgaven for deg. 

Agenter er laget for en eller flere spesifikke formål. 
En agent kan for eksempel hente informasjon fra andre systemer som internett eller en database, 
den kan kanskje bestille togbiletter for deg, eller slå av en datamaskin som har symptomer på å være under angrep utenfra. 
Eller helt andre ting avhengig av hva som er formålet med akkurat den agenten.

.. uio-colorbox-3:: 

    Hvis jeg ber henholdsvis en KI-assistent og en KI-agent om hjelp til å skrive en e-post vil 
    
    .. canvas-tabs:: 

        .. canvas-tab:: KI-assistenten

            forfatte et tekst forslag for meg 

            Eksempel: Microsoft Chat

        .. canvas-tab:: KI-agenten

            forfatte et tekst forslag for meg, legge til relevante filer, legge til adressanter, og sende e-posten for meg

            Eksempel: Microsoft Copilot


.. canvas-tabs::

    .. canvas-tab:: KI-chat

        En generell chat-tjeneste som svarer utfra det du spør den om. 

        * Gir deg forslag, svar og utkast til innhold
        * Produserer kun tekst (eller bilder, lyd, etc.)
        * Du må selv utføre handlingene basert på forslagene


    .. canvas-tab:: KI-assistent

        En KI-chat med en forhåndsdefinert *rolle* eller *personlighet*.

    .. canvas-tab:: KI-agent

        * Kan utføre handlinger på vegne av deg
        * Har tilgang til verktøy (for eksempel internettsøk) og systemer (for eksempel dit filsystem)
        * Kan samhandle med eksterne tjenester (som for eksempel et bestillingssystem, e-post eller annet)



Risiko knyttet til KI-agenter
------------------------------

Det er mye høyere risiko involvert med agenter sammenlignet med en ren chat eller assistent tjeneste. 
Begge har de samme svakheter og begrensninger alle KI-systemer har som genererer tekst basert på en språkmodell (troverdighet, hallusinasjon, ikke fakta basert, ikke reproduserbart).
Du skal lære om dette i neste episode.
Men fordi en agent samhandler med andre digitale systemer i den "virkelige" verden, kan konsekvensene av en feil bli betydelig større. 
Spesielt hvis man lar agenten operere autonomt, det vil si uten at et menneske godkjenner eller kontrollerer handlingen.


.. uio-info::

    På UiO har vi foreløpig ikke mange agentiske KI verktøy skrudd på i våre IT-verktøy. 
    
    Det er flere grunner til det
    
    * teknologien er ny og ikke alle verktøy (som f.eks. arkiveringsverktøy eller annet) har agenter integrert enda
    * det kan være økte kostnader knyttet til aktivering av agent funksjonalitet i tredjeparts verktøy som Microsoft
    * vi er varsomme med å skru på agent funksjonalitet fordi det er større risiko knyttet til dette kraftige verktøyet, og opplæring er nødvendig for å begrense risikoen.

    Eksempler på KI-agenter

    * `Microsoft Copilot <https://copilot.microsoft.com/>`_ (men ikke Microsoft Chat som er en enkel chat løsning uten agent funksjonalitet)
    * Agentiske kode-verktøy som `Claude Code <https://claude.com/product/claude-code>`_ , `opencode <https://opencode.ai/>`_ og `codex <https://openai.com/codex/>`_. 
