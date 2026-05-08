Språkmodellen - LLMen
=========================

Når vi snakker om KI-tjenester som UiO GPT eller Microsoft Copilot, er **språkmodellen** (LLM - Large Language Model) hovedingrediensen - selve "motoren" eller "hjernen" i tjenesten.

En *språkmodell* er en KI-modell av typen *generativ KI* som har trent på enorme mengder tekst, og dermed lært seg mønstre i språk som gjør den i stand til å "forstå" og produsere tekst.

.. uio-colorbox-3::

    I dette kurset fokuserer vi på *språkmodeller*, men det meste vi skal lære gjelder også for andre typer generativ KI som produserer bilder, video eller audio i stedet for tekst.



En språkmodell er ingenting alene
----------------------------------

Men en språkmodell kan ikke brukes direkte,den må være del av et helt system.

Tenk på språkmodellen som en motor i en bil. Motoren alene kan ikke kjøre deg noe sted, du trenger hjul, karosseri, et ratt, sete, pedaler osv. For at du skal kunne benytte deg av motoren eller språkmodellen trenger du også: 

* **Chat-grensesnitt** - så du kan kommunisere med modellen
* **Brukerautentisering** - så systemet vet hvem du er
* **Sikkerhetslag** - som filtrerer ut upassende innhold
* **Lagring** - for å huske samtalehistorikk
* **API-er** - for å integrere med andre verktøy


Bregepet "KI-tjenester" eller "KI-verktøy" brukes når vi refererer til hele pakken, og ikke bare språkmodellen.  
I KI-tjenester kan du ofte velge hvilken KI-modell du benytter. KI-tjenesten er den samme, men motoren kan byttes ut. 


.. uio-colorbox-3:: Eksempler på KI-modell versus KI-tjenesten

    .. canvas-tabs::

        .. canvas-tab:: KI-modellen

            * GPT-5.4 (fra OpenAI)
            * Claude Opus 4.7 (fra Anthropic)
            * Gemini 3.1 (fra Google)

        .. canvas-tab:: KI-tjenesten

            * ChatGPT
            * Claude Code
            * Gemini Google

