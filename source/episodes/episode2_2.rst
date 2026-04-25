LLM-er har *ikke* kunnskap
==============================

Store språkmodeller er altså *statistiske* modeller som genererer tekst basert på mønstre de har lært.
De er trent til å generere tekst som er *troverdig*, og som ligner på tekstene de er trent opp på.
Språkmodellene har ikke *sikker kunnskap* om hva som er *sant*, de regner bare på hvilke ord som er mest *sannsynlige*.

Hvis en språkmodell skal fullføre setningen «Jeg vil ha et glass…», så er noen mulige fortsettelser «vann» og «melk».
Men det fins ikke nødvendigvis bare ett riktig svar, bare sannsynligheter.
Og hvis en setning bare har én riktig fortsettelse, så har ikke språkmodeller *sikker kunnskap* om det.
Språkmodeller har ikke noe forhold til sannhet [Hicks]_.

.. uio-dont:: Eksempel på dårlig bruk

   Spør du "Hva var befolkning i Norge i 2024", genererer modellen et svar basert på mønstre fra lignende spørsmål den har sett, og kan gi feil tall.

.. uio-info:: Manipulering (LLM poisoning)

   Store språkmodeller kan være sårbare for bevisst manipulering, såkalt "LLM poisoning".
   Aktører kan for eksempel legge ut misvisende informasjon for at modellene skal bli trent på den.
   Dermed kan modellene gi svar som er manipulert og ikke stemmer overens med virkeligheten.

   Et eksempel er da BBC-journalisten Thomas Germain manipulerte blant annet ChatGPT og Gemini til å svare at han var kåret til mester i pølsespising. [Germain]_

   Et annet eksempel er et forsøk av den svenske forskeren Almira Osmanovic Thunström.
   Hun undersøkte om KI-tjenester ville spre medisinske påstander fra åpenbart fabrikkerte artikler.
   Derfor publiserte hun to fabrikkerte artikler om en fiktiv diagnose i arkivet preprints.org.
   Etter kort tid begynte KI-tjenester å vise til den fiktive diagnosen. [Stokel-Walker]_

.. uio-source::

   .. [Hicks] Michael Townsen Hicks, James Humphries, og Joe Slater, «ChatGPT Is Bullshit», *Ethics and Information Technology 26*, nr. 2 (2024): 38, (https://doi.org/10.1007/s10676-024-09775-5), på s. 2.

   .. [Germain] Thomas Germain, «I Hacked ChatGPT and Google's AI - and It Only Took 20 Minutes», BBC, 18. februar 2026, https://www.bbc.com/future/article/20260218-i-hacked-chatgpt-and-googles-ai-and-it-only-took-20-minutes

   .. [Stokel-Walker] Chris Stokel-Walker, «Scientists Invented a Fake Disease. AI Told People It Was Real», Nature 652, nr. 8110 (2026): 559–61, https://doi.org/10.1038/d41586-026-01100-y
