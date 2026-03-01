
Begrensninger du bør kjenne til
================================

Vi har sett at LLM-er lærer mønstre fra treningsdata, og at de kan hallusinere - produsere overbevisende men feil informasjon. 
Men det er flere praktiske begrensninger du bør være klar over når du bruker disse verktøyene i hverdagen.

Disse begrensningene handler ikke om at teknologien er "dårlig", men om å forstå *hva slags verktøy* du faktisk bruker. 
En hammer er utmerket til å slå inn spiker, men håpløs til å sage i tre - det handler ikke (nødvendigvis) om kvalitet, men om å bruke riktig verktøy til riktig formål.

På samme måte er det viktig å vite når en LLM er et godt verktøy, og når den mangler viktig informasjon eller kontekst som påvirker svarene du får.

.. figure:: ../images/ChatGPT_usingTheRightTool.png
   :align: center
   :width: 60%
   :alt: LLM using the right tool - placeholder image

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
