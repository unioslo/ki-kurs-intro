Episode 5: Prompting og prompt engineering
==========================================

Prinsipper for god prompting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. canvas-tabs::

   .. canvas-tab:: 1. Vær spesifikk

      **Dårlig prompt:**

      .. code-block:: text

         Skriv en e-post.

      **Bedre prompt:**

      .. code-block:: text

         Skriv en e-post til mine kolleger hvor jeg informerer om
         at møterommet Gaia er stengt for vedlikehold uke 15.
         Tonen skal være vennlig men profesjonell.

      **Hvorfor bedre?**

      Den spesifiserer hva e-posten skal handle om, hvem den er til, og hvilken tone den skal ha.

   .. canvas-tab:: 2. Gi kontekst

      **Dårlig prompt:**

      .. code-block:: text

         Lag et møtereferat.

      **Bedre prompt:**

      .. code-block:: text

         Basert på disse notatene fra møtet, lag et møtereferat:
         [dine notater her]

         Strukturer referatet med:
         - Deltakere
         - Agenda
         - Beslutninger
         - Oppgaver (hvem skal gjøre hva)

      **Hvorfor bedre?**

      Du gir både innholdet (notatene) og strukturen du ønsker.

   .. canvas-tab:: 3. Spesifiser format

      **Dårlig prompt:**

      .. code-block:: text

         Gi meg informasjon om UiOs fakulteter.

      **Bedre prompt:**

      .. code-block:: text

         Lag en tabell med UiOs 8 fakulteter.
         Kolonner: Navn, Forkortelse, Antall studenter (omtrent)
         Sorter alfabetisk etter navn.

      **Hvorfor bedre?**

      Du får et strukturert svar som er lett å bruke videre.

   .. canvas-tab:: 4. Definer rollen

      **Dårlig prompt:**

      .. code-block:: text

         Hvordan kan jeg forbedre min skriving?

      **Bedre prompt:**

      .. code-block:: text

         Du er en erfaren kommunikasjonsrådgiver. Jeg jobber
         administrativt ved et universitet og skal ofte skrive
         formelle brev og e-poster. Gi meg 5 konkrete tips til
         hvordan jeg kan forbedre min administrative skriving.

      **Hvorfor bedre?**

      Ved å gi KI-en en rolle, får du svar som er mer relevant for din situasjon.
