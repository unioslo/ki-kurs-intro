Hvordan fungerer språkmodeller?
==========================================

I denne delen av kurset skal du lære mer om hvordan store språkmodeller (LLM-er) fungerer, og hvorfor denne forståelsen er viktig når du bruker dem.

En type enkle språkmodeller som mange har brukt, er smarte tastaturer på mobiltelefoner.
De foreslår neste ord basert på teksten du har skrevet så langt.
Modellene er trent opp på tekster hentet fra internett, og forslagene er de mest sannsynlige ordene utfra mønstrene som modellen har lært fra tekstene.
Vi kan si at forslaget er betinget av teksten du har skrevet, som vi kaller *konteksten*.

Selv om store språkmodeller er mye mer avanserte enn smarte tastaturer, fungerer de grunnleggende sett på samme måte.
De bygger opp teksten et ord av gangen, betinget av konteksten du gir den.
Konteksten kan være en instruksjon eller spørsmål.
Men ofte legger vi til ekstra kontekst, for eksempel ved å laste opp filer.
Mange KI-systemer som for eksempel chat-tjenesten MS Copilot kan også hente relevant informasjon fra internett, som deretter brukes som kontekst.

Store språkmodeller trenes altså på tekster fra internett.
Men det er mange tekster de ikke har tilgang til.
For eksempel har de ikke tilgang til informasjon som krever innlogging, eller som er bak en betalingsmur.
De har også begrenset tilgang til trykte kilder. Dette skaper begrensninger for hva modellene kan lære.

Dette gir ulikt utslag for ulike bruksområder. 
For eksempel er det for visse fagområder lite informasjon på nett, og da vil naturligvis også språkmodellen ha lite informasjon om disse områdene.
Det betyr at modellene har tilgang til mindre eller kanskje ingen informasjon på noen områder!

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Forstå at LLM-er konstruerer tekst basert på statistiske mønstre
* Forklare hvorfor LLM-er ikke er pålitelige kunnskapsbaser
* Gjenkjenne når en LLM kan gi feil informasjon
* Forstå betydningen av tilfeldighet i KI-svar

.. uio-colorbox-3:: Fordypning

    .. uio-detail:: Hva er kontekst?

        blahblah
