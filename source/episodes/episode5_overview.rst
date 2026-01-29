Episode 5: Prompting og prompt engineering
==========================================

.. contents::
   :local:
   :depth: 2

Temaer som dekkes
~~~~~~~~~~~~~~~~~

* Hva er en prompt?
* Grunnleggende prinsipper for god prompting
* Teknikker for å forbedre resultater
* Vanlige feil og hvordan unngå dem
* Praktiske eksempler

Læringsmål
~~~~~~~~~~

Etter denne episoden vil du kunne:

* Skrive klare og effektive prompts
* Bruke ulike prompt-teknikker for forskjellige oppgaver
* Iterere og forbedre prompts basert på resultatene
* Gjenkjenne vanlige feil i prompting

**Estimert tid:** 12 minutter

Hva er en prompt?
~~~~~~~~~~~~~~~~~

En **prompt** er instruksjonen eller spørsmålet du gir til en KI-modell. Det er din måte å kommunisere med KI-en på.

.. canvas-tabs::

   .. canvas-tab:: Enkel prompt

      **Eksempel:**

      .. code-block:: text

         Hva er klimaendringer?

      **Resultat:**

      Du får et generelt svar om klimaendringer.

   .. canvas-tab:: Detaljert prompt

      **Eksempel:**

      .. code-block:: text

         Forklar klimaendringer på en enkel måte for en 10-åring.
         Bruk 3-4 setninger og unngå faguttrykk.

      **Resultat:**

      Du får et svar tilpasset målgruppen og lengden du ba om.

   .. canvas-tab:: Kontekst-rik prompt

      **Eksempel:**

      .. code-block:: text

         Jeg skal skrive en e-post til alle ansatte om nytt møterom-
         bookingsystem. Målgruppen er administrativt ansatte ved UiO
         som ikke er teknisk kyndige. Tonen skal være vennlig og
         informativ, ikke formell. Kan du hjelpe meg med et utkast?

      **Resultat:**

      Du får et svar som er tilpasset din spesifikke situasjon.

.. note::

   **Hovedregel:** Jo mer spesifikk og detaljert prompten din er, jo bedre blir resultatet.

