Episode 2: Hvordan fungerer språkmodeller?
==========================================

.. contents::
   :local:
   :depth: 2

Temaer som dekkes
~~~~~~~~~~~~~~~~~

* Språkmodeller er ikke kunnskapsbaser
* Hvordan LLM-er genererer tekst
* Statistisk sannsynlighet og tilfeldighet
* Begrensninger ved LLM-er
* Hvorfor LLM-er kan "hallusinere"

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Forstå at LLM-er konstruerer tekst basert på statistiske mønstre
* Forklare hvorfor LLM-er ikke er pålitelige kunnskapsbaser
* Gjenkjenne når en LLM kan gi feil informasjon
* Forstå betydningen av tilfeldighet i KI-svar

**Estimert tid:** 10 minutter

LLM-er er IKKE kunnskapsbaser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dette er kanskje den viktigste forståelsen du kan ha om språkmodeller:

.. warning::

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

