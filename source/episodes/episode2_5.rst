
Begrensninger du bør kjenne til
================================

.. canvas-tabs::

   .. canvas-tab:: Utdatert informasjon

      **Problemet:**

      * LLM-er trenes på data fra et bestemt tidspunkt
      * De vet ikke hva som har skjedd etter treningsdataen ble samlet
      * Mange modeller har en "kunnskapsgrense" (cutoff date)

      **Eksempel:**

      En modell trent i 2023 vet ikke hvem som vant fotball-VM i 2024, eller nye lover som ble vedtatt i 2024.

      **Merk:**

      Noen verktøy (som Bing Chat/Copilot) kan søke på internett for oppdatert informasjon - men da bruker de en søkemotor i tillegg til språkmodellen.

   .. canvas-tab:: Manglende kontekst

      **Problemet:**

      * LLM-er kjenner ikke til interne prosedyrer ved UiO (med mindre de fortelles)
      * De vet ikke om spesifikke systemer dere bruker
      * De har ikke tilgang til deres dokumenter eller databaser

      **Eksempel:**

      Spør du "Hvordan registrerer jeg fravær i vårt system?", kan modellen gi et generisk svar om fraværsregistrering - men ikke det spesifikke systemet dere bruker.

      **Løsning:**

      Gi kontekst i prompten: "Vi bruker systemet X ved UiO. Hvordan registrerer jeg fravær?"

   .. canvas-tab:: Språk og kulturforståelse

      **Problemet:**

      * De fleste LLM-er er primært trent på engelsk
      * Norsk fungerer, men kvaliteten kan være noe lavere
      * Norske forhold og kontekst kan være underrepresentert

      **Eksempel:**

      Juridiske eller administrative spørsmål om norske forhold kan få svar basert på amerikanske eller britiske systemer.

      **Tips:**

      * Vær eksplisitt: "i Norge", "ved norske universiteter", "etter norsk lovverk"
      * Sjekk alltid svar om lover, regler og prosedyrer
