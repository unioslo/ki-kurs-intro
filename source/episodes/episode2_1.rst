Trening og kontekst
=====================

En type enkle språkmodeller som mange har brukt er smarte tastaturer på mobiltelefoner.
De foreslår neste ord basert på teksten du har skrevet så langt.
Modellene er trent opp på tekster hentet fra internett, og forslagene er de mest sannsynlige ordene utfra mønstrene som modellen har lært fra tekstene.
Forslaget er *betinget* av teksten du har skrevet, og denne betingelsen kalles *konteksten*.

Selv om store språkmodeller er mye mer avanserte enn smarte tastaturer, fungerer de grunnleggende sett på samme måte.
De bygger opp teksten et ord av gangen, betinget av konteksten du gir den.
Konteksten kan være en instruksjon, et spørsmål, nettsider eller filer du laster opp.

Store språkmodeller trenes på tekster fra internett, men det er mange tekster de ikke har tilgang til.
For eksempel har de ikke tilgang til informasjon som krever innlogging, eller som er bak en betalingsmur.
De har også begrenset tilgang til trykte kilder. Dette skaper begrensninger for hva modellene kan lære.

Dette gir ulikt utslag for ulike bruksområder.
For eksempel er det for visse fagområder lite informasjon på nett, og da vil naturligvis også språkmodellen ha lite informasjon om disse områdene.


Hva er konteksten?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Når vi snakker om store språkmodeller, bruker vi ofte *kontekst* om alt det vi gir modellen som input.
Det kan være et spørsmål eller instruksjon, men også for eksempel dokumenter, bilder eller andre ting i vi laster opptil modellen.
Alle store språkmodeller har et *kontekstvindu*, som har en begrenset størrelse.
Informasjonen vi vil at modellen skal behandle må få plass i kontekstvinduet.
Hvis vi har mer informasjon enn det som får plass i kontekstvinduet, kan systemet som styrer språkmodellen bruke ulike teknikker for å lage utdrag eller sammendrag av informasjonen.
Språkmodellen har ikke tilgang til informasjon som ikke er i konteksten.
Den kan heller ikke "huske" informasjon fra tidligere samtaler.

