Episode 2: Hvordan fungerer språkmodeller?
==========================================

Hvordan genererer LLM-er tekst?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For å forstå språkmodeller bedre, la oss se på en forenklet forklaring av hvordan de fungerer:

.. canvas-tabs::

   .. canvas-tab:: Trening

      **Hva skjer under treningen:**

      1. Modellen får lese milliarder av ord fra internett, bøker, artikler osv.
      2. Den lærer hvilke ord som ofte kommer etter hverandre
      3. Den lærer mønstre i språk, grammatikk, og hvordan setninger bygges opp
      4. Den lærer sammenhenger mellom begreper og emner

      **Eksempel:**

      Hvis modellen har sett setningen "hovedstaden i Norge er Oslo" tusenvis av ganger, lærer den at "Oslo" er et sannsynlig ord som kommer etter "hovedstaden i Norge er".

   .. canvas-tab:: Generering

      **Hva skjer når du stiller et spørsmål:**

      1. Modellen analyserer din tekst (prompten)
      2. Basert på mønstre den har lært, beregner den hva som er statistisk sannsynlig som neste ord
      3. Den velger et ord (med litt tilfeldighet)
      4. Den gjentar prosessen for neste ord, og neste ord, osv.
      5. Den stopper når den "mener" svaret er fullstendig

      **Viktig:**

      Modellen "tenker" ikke på om informasjonen er korrekt - den genererer bare det som er statistisk sannsynlig basert på mønstre.

   .. canvas-tab:: Temperatur og tilfeldighet

      **Hva er "temperatur"?**

      * En parameter som styrer hvor kreativ/tilfeldig modellen skal være
      * **Lav temperatur** (f.eks. 0.2): Mer forutsigbar, velger de mest sannsynlige ordene
      * **Høy temperatur** (f.eks. 0.8): Mer kreativ, kan velge mindre sannsynlige ord

      **Derfor:**

      * Du kan få ulike svar på samme spørsmål
      * Noen ganger kan svarene være mer kreative, andre ganger mer "standard"
      * Ingen garanti for at samme spørsmål gir samme svar
