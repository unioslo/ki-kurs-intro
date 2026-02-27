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

.. [Hicks] Michael Townsen Hicks, James Humphries, og Joe Slater, «ChatGPT Is Bullshit», *Ethics and Information Technology 26*, nr. 2 (2024): 38, (https://doi.org/10.1007/s10676-024-09775-5), på s. 2.
