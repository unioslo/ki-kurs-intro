Episode 2: Hvordan fungerer språkmodeller?
==========================================

Hva er "hallusinering"?
~~~~~~~~~~~~~~~~~~~~~~~

Når LLM-er genererer informasjon som høres troverdig ut, men som er feil, kaller vi det "hallusinering" (eller "confabulation" på fagspråket).

.. canvas-tabs::

   .. canvas-tab:: Eksempler på hallusinering

      **Typiske situasjoner:**

      * **Oppdiktede referanser**: Modellen lager titler på artikler som ikke finnes
      * **Feil fakta**: Oppgir feil datoer, tall eller navn
      * **Blandede personer**: Blander sammen biografier fra ulike personer
      * **Oppfunnet programvare**: Beskriver funksjoner som ikke eksisterer
      * **Feil prosedyrer**: Beskriver arbeidsprosesser som ikke stemmer

      **Eksempel:**

      "Studien av Hansen et al. (2023) publisert i Nature viste at..." - der både studien og forfatterne kan være oppfunnet.

   .. canvas-tab:: Hvorfor skjer det?

      **Årsaker til hallusinering:**

      1. **Modellen vil alltid gi et svar** - Den sier ikke "jeg vet ikke"
      2. **Mønstre fra trening** - Den har lært hvordan svar "skal se ut"
      3. **Manglende faktasjekk** - Den verifiserer ikke mot noen database
      4. **Overgeneralisering** - Den kombinerer mønstre fra ulike kilder
      5. **Utdatert treningsdata** - Modellen vet ikke hva som har skjedd etter den ble trent

      **Viktig å forstå:**

      Hallusinering er ikke en "bug" som kan fikses fullstendig - det er en iboende egenskap ved hvordan språkmodeller fungerer.

   .. canvas-tab:: Hallusinering med selvtillit

      **Det mest problematiske:**

      LLM-er hallusinerer ofte med stor **selvsikkerhet**. De sier ikke:

      * "Jeg er usikker, men..."
      * "Dette kan være feil, men..."
      * "Jeg vet ikke sikkert, men..."

      I stedet presenterer de feil informasjon med samme overbevisning som riktig informasjon.

      **Derfor:**

      Du kan IKKE stole på om et svar er korrekt basert på hvor selvsikkert det fremstår.

.. canvas-question::

   **Hvorfor kan en språkmodell gi feil informasjon selv om svaret høres veldig troverdig ut?**

   .. canvas-answer::

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk. Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant. Derfor kan den produsere feil informasjon med samme selvtillit som riktig informasjon.
