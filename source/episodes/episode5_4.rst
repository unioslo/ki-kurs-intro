Episode 5: Prompting og prompt engineering
==========================================

Vanlige feil og hvordan unngå dem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. canvas-tabs::

   .. canvas-tab:: Feil 1: For vage prompts

      **Problem:**

      .. code-block:: text

         "Skriv noe om møter"

      **Resultat:** Generelt, ubrukelig svar.

      **Løsning:**

      .. code-block:: text

         "Skriv 5 tips for hvordan jeg kan gjøre våre
         ukentlige teammøter mer effektive. Vi er en gruppe
         på 8 personer som møtes i 1 time."

   .. canvas-tab:: Feil 2: For mange krav på én gang

      **Problem:**

      .. code-block:: text

         "Skriv en e-post om det nye systemet, lag også
         en FAQ, en guide, og en presentasjon, og oversett
         alt til engelsk"

      **Resultat:** Overfladisk behandling av alt.

      **Løsning:**

      Del opp i separate prompts - én oppgave om gangen.

   .. canvas-tab:: Feil 3: Ikke gi nok kontekst

      **Problem:**

      .. code-block:: text

         "Hva synes du om dette?"
         [uten å forklare hva "dette" er]

      **Resultat:** KI-en gjetter hva du mener.

      **Løsning:**

      .. code-block:: text

         "Jeg har skrevet et utkast til invitasjon for
         et personalseminar. Kan du vurdere om tonen
         er passende og om all viktig info er med?

         [ditt utkast]"

   .. canvas-tab:: Feil 4: Forvente perfeksjon med én gang

      **Problem:**

      Bli frustrert hvis første svar ikke er perfekt.

      **Løsning:**

      Bruk iterativ prompting:

      .. code-block:: text

         1. Start med grunnleggende prompt
         2. "Kan du gjøre den kortere?"
         3. "Legg til et avsnitt om hvor de får hjelp"
         4. "Endre tonen til å være mer formell"
