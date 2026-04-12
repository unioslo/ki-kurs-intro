Språkmodeller har ikke hukommelse
================================================

Selve den matematiske språkmodellen har ikke hukommelse.
Det er systemet rundt modellen som husker samtalen du har hatt.
Når du sender en ny instruksjon, sender chat-systemet hele samtalen og den nye instruksjonen til språkmodellen.
Modellen genererer så et nytt svar basert på hele samtalen og den nye instruksjonen.
Det betyr at språkmodellene prosesserer hele samtalen på nytt for hver instruksjon du gir.


Korte samtaler gir bedre svar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lange samtaler kan "forvirre" modellen, slik at den gir dårligere svar.
Særlig hvis du bytter tema er det viktig å starte en ny samtale.
La oss si at du først har stilt noen spørsmål om økonomireglementet til UiO.
Hvis du så stiller spørsmål om hvordan du formaterer figurer i Word, vil modellen svare på spørsmålet i lys av økonomireglementet til UiO.
Det gir ikke mening, og du vil få bedre svar hvis du starter en ny samtale.

Men selv om du ikke skifter tema, kan modellen gi dårligere svar når samtalen blir lengre.
Philippe Laban mfl. fant at språkmodeller svarer best når de får all informasjon i en enkelt instruksjon. [Laban]_
En viktig årsak til det var at gale svar fra modellen ble liggende i samtalen.

Språkmodellene er dårlig til å skille mellom tekst brukeren har skrevet, og tekst de selv har generert.
Derfor bør du sørge for at gale svar ikke blir liggende i samtalen.
Det kan du gjøre ved å redigere spørsmål som du får feil svar på.
Trykk på rediger-knappen, ✏️, og legg til informasjon som modellen trenger for å svare riktig.
Revider instruksjonen til du får et svar uten feil.

Lange samtaler krever mer ressurser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jo lengre en samtale blir, desto mer ressurser bruker systemet, siden modellen må prosesserer hele samtalen på nytt for hver instruksjon.
Ressursene som brukes er for eksempel maskinvare, strøm og vann.
For å spare ressurser, bør du holde samtalene korte.
Start en ny samtale, når samtalen begynner å bli lang.

.. uio-source::

   .. [Laban] Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, og Jennifer Neville, «LLMs Get Lost In Multi-Turn Conversation», arXiv:2505.06120, arXiv, 9. mai 2025, https://doi.org/10.48550/arXiv.2505.06120 på s. 1.
