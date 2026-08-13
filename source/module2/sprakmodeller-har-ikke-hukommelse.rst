Språkmodeller har ikke hukommelse
================================================

Språkmodellen har ikke hukommelse i seg selv. Det er chat-systemet rundt modellen som lagrer samtalen du har hatt.

Hver gang du skriver en ny instruksjon, sender chat-systemet hele den tidligere samtalen sammen med den nye instruksjonen til språkmodellen. 
Dette kalles, som vi har lært, «kontekst».

Språkmodellen lager så et nytt svar basert på hele samtalen og den siste instruksjonen du har gitt.
Det betyr at modellen behandler hele samtalen på nytt for hver eneste instruksjon.

Begrenset kontekstvindu
------------------------

Alle store språkmodeller har et *kontekstvindu*, som har en begrenset størrelse.
Informasjonen vi vil at modellen skal behandle må få plass i kontekstvinduet.
Hvis vi har mer informasjon enn det som får plass i kontekstvinduet, kan systemet bruke ulike teknikker for å lage utdrag eller sammendrag av informasjonen, uten at du som bruker nødvendigvis blir informert.
Det er viktig å være klar over at språkmodellen ikke har tilgang til informasjon som ikke er i konteksten.


Korte samtaler gir bedre svar
------------------------------

Lange samtaler kan "forvirre" modellen, slik at den gir dårligere svar.
Særlig når du bytter tema, er det viktig å starte en ny samtale.
Se for deg at du har stilt KI spørsmål om økonomireglementet til UiO.
Hvis du så stiller spørsmål om hvordan man formaterer figurer i Word, vil modellen svare på spørsmålet i lys av økonomireglementet til UiO.
Det gir ikke mening, og du vil få bedre svar hvis du starter en ny samtale.

Men selv om du ikke skifter tema, kan modellen gi dårligere svar når samtalen blir lengre.
Philippe Laban mfl. fant at språkmodeller svarer best når de får all informasjon i en enkelt instruksjon.  [:ref:`Laban <Laban>`]
En viktig årsak til det var at gale svar fra modellen ble liggende i samtalen.

I tillegg er språkmodellene er dårlig til å skille mellom tekst brukeren har skrevet, og tekst de selv har generert.
Derfor bør du sørge for at gale svar ikke blir liggende i samtalen.

.. uio-do:: Tips

    Rediger spørsmål som du får feil svar på.
    Trykk på rediger-knappen, ✏️, og legg til informasjon som modellen trenger for å svare riktig.
    Revider instruksjonen til du får et svar uten feil.

