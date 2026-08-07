Hvordan fungerer store språkmodeller?
=======================================

Store språkmodeller er en type *generativ KI* som vi lærte om i forrige kapittel.
En type enkle språkmodeller som mange har brukt er smarte tastaturer på mobiltelefoner.
Disse foreslår neste ord basert på teksten du har skrevet så langt.
Modellene er trent opp på tekster hentet fra internett, og forslagene er de mest sannsynlige ordene utfra mønstrene som modellen har lært fra tekstene.
Forslaget er *betinget* av teksten du har skrevet, og denne teksten kalles *konteksten*.

.. figure:: ../images/IMG_2787.jpg
    :align: center
    :width: 50%
    :alt: Skjermbilde med et tastatur der det er skrevet "Jeg vil ha en kopp". Forslag til fortsettelse er "te", "kaffe" og en emoji.

    Forslag til fortsettelser av teksten "Jeg vil ha en kopp".

.. figure:: ../images/IMG_2788.jpg
    :align: center
    :width: 50%
    :alt: Skjermbilde med et tastatur der det er skrevet "Jeg vil ha et glass". Forslag til fortsettelse er "vin", "med" og en emoji.

    Forslag til fortsettelser av teksten "Jeg vil ha et glass".

Store språkmodeller er mye mer avanserte enn smarte tastaturer, men de fungerer grunnleggende sett på samme måte.
En språkmodell er en matematisk modell som bygger opp svaret ett ord av gangen, betinget av *konteksten*.
Hvert ord trekkes med litt tilfeldighet.
Modellen stopper når den "mener" svaret er fullstendig.


Hva er konteksten?
------------------

Når vi snakker om store språkmodeller, bruker vi ofte *kontekst* om alt det vi gir modellen som input.
Input kan være et spørsmål eller instruksjon, men også dokumenter, bilder eller andre ting vi laster opptil modellen.
Alle store språkmodeller har et *kontekstvindu*, som har en begrenset størrelse.
Informasjonen vi vil at modellen skal behandle må få plass i kontekstvinduet.
Hvis vi har mer informasjon enn det som får plass i kontekstvinduet, kan systemet som styrer språkmodellen bruke ulike teknikker for å lage utdrag eller sammendrag av informasjonen.
Språkmodellen har ikke tilgang til informasjon som ikke er i konteksten.
Den kan heller ikke "huske" informasjon fra tidligere samtaler.
