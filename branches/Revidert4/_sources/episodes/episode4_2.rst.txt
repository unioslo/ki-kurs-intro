
GPT UiO
========

GPT UiO er UiOs personverntrygge KI-chat.

I GPT UiO kan du velge mellom flere ulike språkmodeller - altså hvilken «hjerne» tjenesten bruker.
Modellene har forskjellig størrelse, funksjoner (som støtte av bilder) og bruksområder.
En spesielt viktig forskjell mellom modellene er om de kjører i skyen (OpenAI sine GPT-modeller i Microsoft Azure skyen) eller *lokalt*.
Med *lokalt* mener vi på servere som eies og driftes av UiO eller vår samarbeidspartner NTNU.

Mens alle modellene, både de i skyen og de som lokalt sikrer at GDPR reglene følges, er du ekstra godt beskyttet om du velger de lokale modellene.
Det er da går *ingen* data til skyen, alt forblir på UiO eller NTNU sine systemer.

Noen av de lokale modellene kan i tillegg håndtere opp til `røde data`_.

.. _røde data: https://www.uio.no/tjenester/it/sikkerhet/lsis/tillegg/lagring/infoklasser.html

.. uio-viktig::

   * Velger du en lokal språkmodell, har du ekstra kontroll over dataene dine og kan være trygg på at ingenting lastes opp i skyen.
   * Velger du en skybasert modell, behandles inn- og utdata midlertidig av Microsoft Azure OpenAI innenfor GDPR-kompatible regioner (Europa).

   Uavhengig av om du bruker en lokal eller skybasert modell, lagres all logg samt inn- og utdata kun på UiOs servere. Ditt brukernavn deles ikke med Microsoft.
   Derfor er GPT UiO GDPR-kompatibel.
