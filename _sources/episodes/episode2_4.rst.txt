Språkmodeller finner på ting
================================================

Siden store språkmodeller ikke har kunnskap, kan de finne på ting som ikke stemmer.
Noen kaller det *hallusinering* når språkmodeller finner på ting, men vi kan gjerne bare si at de *finner på ting*.

Språkmodeller kan finne på eller blande sammen ting på forskjellige måter.
Her er noen eksempler: 

* *Feil fakta*: Modellen oppgir feil datoer, tall eller navn.
* *Oppdiktede referanser*: Modellen lager titler på artikler eller bøker som ikke finnes.
* *Forveksling*: Modellen blander sammen ulike personer.

Det er et stort problem at LLM-er ofte finner på ting med stor *selvsikkerhet*.
De sier ikke: "Jeg er usikker, men …".
I stedet presenterer de feilinformasjon med samme overbevisning som riktig informasjon.
Derfor kan du *ikke* stole på at et svar er riktig bare fordi det fremstår selvsikkert.
Du må alltid sjekke fakta med en pålitelig kilde.

Hvorfor skjer det?
~~~~~~~~~~~~~~~~~~~~~~

Det er mange årsaker til at modellene finner på ting:

1. *Modellen vil alltid gi et svar*, den sier ikke "jeg vet ikke".
2. *Mønstre fra trening*, modellen har lært hvordan svar "skal se ut".
3. *Manglende faktasjekk*, modellen har ikke kunnskap.
4. *Overgeneralisering*, modellen kombinerer mønstre fra ulike kilder.
5. *Utdaterte treningsdata*, modellen vet ikke hva som har skjedd etter den ble trent.

.. uio-viktig:: Viktig å forstå

   At språkmodeller finner på ting er ikke en feil som kan fikses fullstendig.
   Det er en iboende egenskap ved hvordan språkmodeller fungerer.

Hva med internett-søk?
~~~~~~~~~~~~~~~~~~~~~~

Mange store språkmodeller har nå mulighet til å søke på internett for å få oppdatert informasjon.
Men det garanterer ikke at svaret er riktig.
Det er fordi LLM-en fortsatt må *tolke* og *oppsummere* informasjonen den finner.
Det gjør den på samme måte som alltid, ved å generere tekst basert på mønstre.
Modellen kan derfor fortsatt finner på ting selv om den har tilgang til korrekt informasjon fra nettet.

.. uio-info:: Eksempel

   Et eksempel på at modeller finner på ting er en sak fra Politihøgskolen. [Svarstad]_
   Der ble feilinformasjon generert av Microsoft Copilot brukt som saksgrunnlag.
   Politihøgskolen skulle bestemme hvor mye tid undervisere skulle få til forberedelse.
   De forsøkte å bruke Copilot for å hente informasjon om forberedelsestid på andre universiteter og høyskoler.
   Copilot fant ikke opplysningene som brukeren spurte etter på nettet, og fant derfor på et svar.

.. uio-reflect:: Refleksjon

   Hva kunne Politihøyskolen gjort for å unngå feilen som skjedde i saken over?

   .. uio-answer::

      Det viktigste å huske, er å alltid sjekke faktaopplysninger med en pålitelig kilde.
      Hvis det ikke er mulig å finne kilden, er opplysningen ofte feil.

.. uio-source::

   .. [Svarstad] Jørgen Svarstad, «Politihøgskolen brukte falske KI-tall: — Jeg legger meg flat», 26. februar 2026, https://www.khrono.no/politihogskolen-brukte-falske-ki-tall-jeg-legger-meg-flat/1040462.
