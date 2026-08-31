Språkmodeller har ikke hukommelse
================================================

Når du bruker en språkmodell, har du kontakt med den gjennom et chat-system.
Språkmodellen selv husker ikke tidligere meldinger i samtalen eller tidligere samtaler du har hatt med den.
Det er det chat-systemet som gjør.
Chat-systemet viser deg samtalen dere har, og sender den videre til språkmodellen.
Det du bør merke deg her, er at hver gang du skriver en ny instruksjon eller et nytt spørsmål i chatten, så sender chat-systemet *hele* samtalen på nytt til språkmodellen.
Det er fordi språkmodellen selv ikke kan huske det du har spurt om.

Det er altså chat-systemet som "husker" det du har skrevet og bygger opp konteksten, mens språkmodellen bare ser på den teksten den får der og da, og beregner sannsynlige neste ord.
Dette er viktig å være klar over fordi lengden på konteksten har betydning for hvor mye av samtalen modellen faktisk "ser".

.. uio-colorbox-3:: Bonusinnhold

    .. uio-detail:: Er det hele samtalen som sendes til språkmodellen?

        Når vi sier at chat-systemet sender *hele samtalen* til språkmodellen er det en forenkling:
        I praksis har chat-systemene forskjellige måter å redusere informasjonen den sender til språkmodellen.
        
        Allikevel: det er aldri bare siste melding av en samtaletråd som sendes til språkmodellen.  
        Avhengig av språkmodellens kapasitet, og chat-systemets automatiske filtreringer blir hele eller deler av de foregående meldingene i samtaletråden sendt sammen med din siste melding.


Ha korte samtaler
-----------------------------------

Lange samtaler kan "forvirre" modellen, slik at den gir dårligere svar.
En grunn til det kan være at hele konteksten ikke får plass.
Ved lange samtaler er det også større sannsynlighet for at teksten inneholder motstridelser eller annet som gjør budskapet utydelig.
Philippe Laban mfl. fant at språkmodeller svarer best når de får all informasjon i en enkelt instruksjon.  [:ref:`Laban <Laban>`]
En viktig årsak til det var at gale svar fra modellen ble liggende i samtalen.

Det er spesielt viktig å starte en ny samtale om du skifter tema.
Se for deg at du har stilt KI spørsmål om økonomireglementet til UiO.
Hvis du så stiller spørsmål om hvordan man formaterer figurer i Word, vil modellen svare på spørsmålet i lys av økonomireglementet til UiO.
Det gir ikke mening, og du vil få bedre svar hvis du starter en ny samtale.

I tillegg er språkmodellene dårlig til å skille mellom tekst brukeren har skrevet, og tekst de selv har generert.
Derfor bør du sørge for at gale svar ikke blir liggende i samtalen.





