
Hvordan genererer LLM-er tekst?
================================

For å forstå språkmodeller bedre, la oss se på en forenklet forklaring av hvordan de fungerer:

.. figure:: ../images/ChatGPT_howLLMswork.png
   :align: center
   :width: 60%
   :alt: LLM text generation illustration


Trening
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En språkmodell trenes før den tas i bruk.
Modellen lærer ikke mens den brukes.
Men noen leverandører av språkmodeller lagrer brukerdata for å trene neste versjon av modellen.
Det skal vi komme tilbake til senere, i delen om personvern og data.

Her er en forenklet oppsummering av hva som skjer når modellen trenes:

* Modellen får lese milliarder av ord fra internett, bøker, artikler osv.
* Den lærer hvilke ord som ofte kommer etter hverandre.
* Den lærer mønstre i språk, grammatikk og hvordan setninger bygges opp.
* Den lærer sammenhenger mellom begreper og emner.

.. uio-info:: Eksempel

   Hvis modellen har sett setningen "hovedstaden i Norge er Oslo" tusenvis av ganger, lærer den at "Oslo" er et sannsynlig ord som kommer etter "hovedstaden i Norge er".

Generering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hva skjer når du stiller et spørsmål:

1. Modellen leser spørsmålet eller instruksjonen din.
2. Basert på mønstre den har lært, beregner den sannsynlighetene for neste ord i setningen.
3. Den trekker et ord, med litt tilfeldighet, og legger det til svaret.
4. Den gjentar prosessen for neste ord, og neste ord, osv.
5. Modellen stopper når den "mener" svaret er fullstendig.

.. uio-info:: Viktig

   Modellen "tenker" ikke på om informasjonen er korrekt. Den genererer bare det som er statistisk sannsynlig basert på mønstre.

Temperatur og tilfeldighet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vi kan justere hvor "tilfeldig" eller "kreativ" tekst språkmodellen skal generere.
Den mest brukte innstillingen er *temperatur*.
De fleste vanlige tjenester har en standard temperatur som ikke kan justeres, men noen lar deg sette denne etter behov.

.. uio-info:: Hva er "temperatur"?

   Temperaturen kontrollerer hvordan språkmodellen trekker ord fra sannsynlighetsfordelingen.
   Med høy temperatur øker sannsynligheten for å trekke sjeldne ord.

   * **Lav temperatur** (f.eks. 0.2): Mer forutsigbar, velger de mest sannsynlige ordene.
   * **Høy temperatur** (f.eks. 1.5): Mer kreativ, kan velge mindre sannsynlige ord.

   Du kan få dermed ulike svar på samme spørsmål. Noen ganger kan svarene være mer kreative, andre ganger mer "standard". Det er ingen garanti for at samme spørsmål gir samme svar neste gang.
