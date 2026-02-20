
LLM-er er IKKE kunnskapsbaser
==============================

Dette er kanskje den viktigste forståelsen du kan ha om språkmodeller:

.. uio-dont::

   **Store språkmodeller er IKKE databaser med fakta. De er statistiske modeller som genererer tekst basert på mønstre de har lært.**

La oss sammenligne med noe du kjenner:

.. canvas-tabs::

   .. canvas-tab:: Kunnskapsbase (f.eks. Wikipedia)

      **Slik fungerer det:**

      * Informasjon er lagret som strukturerte data
      * Når du søker, henter systemet frem eksakt informasjon
      * Informasjonen er (ideelt sett) verifisert og referert
      * Du får samme svar hver gang på samme spørsmål
      * Hvis informasjonen ikke finnes, får du ingen treff

      **Eksempel:**

      Søker du "befolkning i Norge 2024", får du det eksakte tallet som er lagret.

   .. canvas-tab:: Språkmodell (f.eks. ChatGPT)

      **Slik fungerer det:**

      * Ingen informasjon er direkte "lagret" som fakta
      * Modellen har lært mønstre fra millioner av tekster
      * Når du stiller et spørsmål, genererer den ny tekst som ligner på mønstre den har sett
      * Du kan få ulike svar på samme spørsmål
      * Modellen vil alltid forsøke å gi et svar, selv om den ikke "vet" svaret

      **Eksempel:**

      Spør du "befolkning i Norge 2024", konstruerer modellen et svar basert på mønstre fra lignende spørsmål den har sett - og kan gi feil tall.
