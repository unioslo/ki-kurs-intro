Språkmodeller finner på ting
================================================

Siden store språkmodeller ikke har kunnskap, kan de finne på ting som ikke stemmer.
Det kalles ofte *hallusinering*, men har egentlig ingenting med menneskelig hallusinering å gjøre.
Derfor er det noen som foretrekker å kalle det *konfabulering* når språkmodeller finner på ting.

Eksempler på hallusinering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Språkmodeller kan finne på eller blande sammen ting på forskjellige måter.
Her er noen eksempler, det finnes flere.

* **Feil fakta**: Modellen oppgir feil datoer, tall eller navn.
* **Oppdiktede referanser**: Modellen lager titler på artikler eller bøker som ikke finnes.
* **Blandede personer**: Modellen blander sammen biografier fra ulike personer.

.. uio-info:: Eksempel

   "Studien av Hansen et al. (2023) publisert i Nature viste at …", der både studien og forfatterne er oppfunnet.
   Det kan også være en tittel som høres troverdig ut, fordi temaet er innenfor fagområdet til en virkelig forfatter.

Hvorfor skjer det?
~~~~~~~~~~~~~~~~~~~~~~

Det er mange årsaker til hallusinering:

1. *Modellen vil alltid gi et svar*, den sier ikke "jeg vet ikke".
2. *Mønstre fra trening*, modellen har lært hvordan svar "skal se ut".
3. *Manglende faktasjekk*, modellen har ikke kunnskap.
4. *Overgeneralisering*, modellen kombinerer mønstre fra ulike kilder.
5. *Utdaterte treningsdata*, modellen vet ikke hva som har skjedd etter den ble trent.

.. uio-info:: Viktig å forstå:

   Hallusinering er ikke en "bug" som kan fikses fullstendig.
   Det er en iboende egenskap ved hvordan språkmodeller fungerer.

Hallusinering med selvtillit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Det er et stort problem at LLM-er ofte hallusinerer med stor *selvsikkerhet*.
De sier ikke: "Jeg er usikker, men …".
I stedet presenterer de feilinformasjon med samme overbevisning som riktig informasjon.
Derfor kan du *ikke* stole på at et svar er riktig bare fordi det fremstår selvsikkert.
Du må alltid sjekke fakta med en pålitelig kilde.

Hva med internett-søk?
~~~~~~~~~~~~~~~~~~~~~~

Mange store språkmodeller har nå mulighet til å søke på internett for å få oppdatert informasjon.
Men det garanterer ikke at svaret er riktig.
Det er fordi LLM-en fortsatt må *tolke* og *oppsummere* informasjonen den finner, og det gjør den på samme måte som alltid – ved å generere tekst basert på mønstre.
Modellen kan derfor fortsatt hallusinere selv om den har tilgang til korrekt informasjon fra nettet.

Et eksempel på hallusinering er en sak fra Politihøgskolen. [Svarstad]_
Der ble feilinformasjon generert av Copilot brukt som saksgrunnlag.
Copilot fant ikke opplysningene som brukeren spurte etter, og fant derfor på et svar.

.. uio-reflect:: Refleksjon

   Hva kunne Politihøyskolen gjort for å unngå feilen som skjedde i saken over?
   
   .. uio-answer::
   
      Det viktigste å huske, er å alltid sjekke faktaopplysninger med en pålitelig kilde.
      Hvis det ikke mulig å finne kilden, er opplysningen ofte feil.

.. uio-reflect:: Refleksjon

   Hvorfor kan en språkmodell gi feilinformasjon selv om svaret høres veldig troverdig ut?

   .. uio-answer::

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk.
      Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant.
      Derfor kan den produsere feilinformasjon med samme selvtillit som riktig informasjon.

.. uio-source::

   .. [Svarstad] Jørgen Svarstad, «Politihøgskolen brukte falske KI-tall: — Jeg legger meg flat», 26. februar 2026, https://www.khrono.no/politihogskolen-brukte-falske-ki-tall-jeg-legger-meg-flat/1040462.
