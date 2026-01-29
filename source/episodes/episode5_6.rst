Episode 5: Prompting og prompt engineering
==========================================

Eksempel: Fra dårlig til god prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La oss se et komplett eksempel på hvordan en prompt kan forbedres:

.. canvas-tabs::

   .. canvas-tab:: Versjon 1 - Dårlig

      .. code-block:: text

         Skriv om møter

      **Problem:** Altfor vagt. Hva slags tekst? Om hva med møter?

   .. canvas-tab:: Versjon 2 - Bedre

      .. code-block:: text

         Skriv tips om møter

      **Problem:** Fortsatt vagt. Tips til hvem? Hva slags møter? Hvor mange tips?

   .. canvas-tab:: Versjon 3 - Mye bedre

      .. code-block:: text

         Skriv 5 tips for effektive møter

      **Problem:** Bedre, men mangler kontekst. Hvilke typer møter? Hvem er målgruppen?

   .. canvas-tab:: Versjon 4 - God!

      .. code-block:: text

         Jeg leder ukentlige teammøter med 6 kolleger i
         administrativ stilling. Møtene er ofte kaotiske
         og ineffektive. Gi meg 5 konkrete, praktiske tips
         for hvordan jeg kan gjøre møtene bedre.

         Fokuser på:
         - Forberedelse
         - Struktur under møtet
         - Oppfølging

      **Hvorfor god:** Spesifikk kontekst, tydelig mål, definert struktur.
