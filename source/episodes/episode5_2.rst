Episode 5: Prompting og prompt engineering
==========================================

Nyttige prompt-teknikker
~~~~~~~~~~~~~~~~~~~~~~~~

.. canvas-tabs::

   .. canvas-tab:: Chain of thought (Tankekjede)

      **Teknikk:**

      Be KI-en "tenke høyt" eller "forklare steg for steg".

      **Eksempel:**

      .. code-block:: text

         Forklar trinn for trinn hvordan jeg kan
         organisere et sommerarrangement for 50 personer.

      **Fordel:**

      * Får mer gjennomtenkte svar
      * Enklere å følge resonnementet
      * Bedre for komplekse oppgaver

   .. canvas-tab:: Few-shot prompting (Gi eksempler)

      **Teknikk:**

      Gi eksempler på hva du vil ha.

      **Eksempel:**

      .. code-block:: text

         Jeg skal skrive titler til nyhetssaker. Her er eksempler
         på stilen jeg ønsker:

         - "Nytt tilbud: Gratis språkkurs for ansatte"
         - "Viktig: Endringer i møterom-booking fra 1. april"
         - "Påminnelse: Personalseminar 15. mai"

         Skriv en tittel for denne saken:
         "Vi får nytt IT-system for reiseregninger neste måned"

      **Fordel:**

      * Får svar i ønsket stil
      * Lettere enn å forklare stilen med ord

   .. canvas-tab:: Rollespill

      **Teknikk:**

      Be KI-en ta rollen som en bestemt type ekspert.

      **Eksempel:**

      .. code-block:: text

         Du er en erfaren prosjektleder ved et norsk universitet.
         Jeg skal lede mitt første prosjekt og er nervøs.
         Gi meg dine beste råd for å lykkes.

      **Fordel:**

      * Får perspektiv fra en bestemt rolle
      * Mer fokuserte svar

   .. canvas-tab:: Strukturert output

      **Teknikk:**

      Be om svaret i et bestemt format.

      **Eksempel:**

      .. code-block:: text

         Oppsummer dette møtereferatet i følgende format:

         BESLUTNINGER:
         -
         -

         OPPGAVER:
         - [Person]: [oppgave] - [frist]

         NESTE MØTE:
         [dato og tid]

         [ditt møtereferat her]

      **Fordel:**

      * Får svar klart til bruk
      * Konsistent format

   .. canvas-tab:: Iterativ prompting

      **Teknikk:**

      Bygg videre på svarene i en samtale.

      **Eksempel:**

      .. code-block:: text

         Første prompt:
         "Skriv et utkast til e-post om nytt bookingsystem"

         Oppfølging 1:
         "Gjør den mer konsis, maks 3 avsnitt"

         Oppfølging 2:
         "Legg til en setning om hvor de kan få hjelp"

      **Fordel:**

      * Gradvis forbedring
      * Lettere enn å skrive perfekt prompt med én gang
