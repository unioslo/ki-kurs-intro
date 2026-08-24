Språkmodeller finner på ting
================================================

Fordi store språkmodeller ikke har faktakunnskap, kan de finne på ting som ikke stemmer.
Hvis du har hørt noen si at KI og språkmodeller *hallusinerer*, er det dette de mener.

Språkmodeller kan finne på eller blande sammen ting på forskjellige måter.
Her er noen eksempler: 

* *Feil fakta*: Modellen oppgir feil datoer, tall eller navn.
* *Oppdiktede referanser*: Modellen lager titler på artikler eller bøker som ikke finnes.
* *Forveksling*: Modellen blander sammen ulike personer.

Det er et stort problem at språkmodeller ofte finner på ting med stor *sikkerhet*.
De sier ikke: "Jeg er usikker, men …".
I stedet presenterer de feilinformasjon med samme "overbevisning" som riktig informasjon.
Derfor kan du *ikke* stole på at et svar er riktig bare fordi det fremstår "selvsikkert".
Du må alltid sjekke fakta med en pålitelig kilde.

Hvorfor skjer det?
------------------

Det er mange årsaker til at modellene finner på ting.
Dette er noen av dem:

- Modellene "vil" gjerne gi et svar, de er dårlige til å si "jeg vet ikke".
- Modellene har ikke kunnskap.
- Overgeneralisering, modellene kombinerer mønstre fra ulike kilder.
- Utdaterte treningsdata, modellene vet ikke hva som har skjedd etter de ble trent.


.. uio-viktig:: Viktig å forstå

   At språkmodeller finner på ting er ikke en feil som kan fikses fullstendig.
   Det er en iboende egenskap ved hvordan språkmodeller fungerer.

Hva med internett-søk?
-----------------------

Mange store språkmodeller har nå mulighet til å søke på internett for å få oppdatert informasjon.
Men det garanterer ikke at svaret er riktig.
Det er fordi språkmodellen fortsatt må *tolke* og *oppsummere* informasjonen den finner.
Det gjør den på samme måte som alltid, ved å generere tekst basert på mønstre.
Modellen kan derfor fortsatt finne på ting, selv om den har tilgang til korrekt informasjon fra nettet.


Eksempel fra virkeligheten
----------------------------

Da Politihøyskolen skulle bestemme hvor mye tid undervisere skulle få til å forberede seg til undervisning, 
ble feilinformasjon brukt som saksgrunnlag [:ref:`Svarstad <Svarstad>`]. 
Under forberedelsene til behandling ble nemlig Copilot brukt for å hente informasjon om forberedelsestid på andre universiteter og høyskoler. 
Problemet var at Copilot ikke fant slike opplysninger på nettet, og fant bare derfor på et svar.

.. uio-reflect:: Refleksjon

   Hva kunne Politihøyskolen gjort for å unngå feilen som skjedde i saken over?

   .. uio-answer:: Klikk for mulig svar

      Det viktigste å huske, er å alltid sjekke faktaopplysninger med en pålitelig kilde.
      Hvis det ikke er mulig å finne kilden, er opplysningen sannsynligvis feil.

