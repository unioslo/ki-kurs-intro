
Hva er generativ KI?
====================
Når vi snakker om KI i hverdagen er det som oftest generativ KI vi tenker på. Generativ KI er en type kunstig intelligens som skaper nytt innhold i stedet for bare å analysere eller klassifisere det som finnes. Den kan produsere tekst, bilder, lyd, video eller kode som ikke eksisterte før. Når du for eksempel spør ChatGpT UiO om å oppsummere en artikkel for deg er det generativ KI som genererer svaret for deg basert på mønstre den har lært. Det spesielle med denne type KI er at den skaper noe nytt og ikke bare kopierer. For å lære bruker KI-systemet det som kalles maskinlæring. Frem til nå har de fleste datamaskiner blitt instruert til hvordan en oppgave skal løses med forhåndsdefinerte regler. Maskinlæring er en metode der maskinen lærer fra data i stedet, og der systemet finner mønstre på egen hånd.

Det finnes forskjellige måter å dele inn kunstig intelligens i ulike typer. Et vanlig skille går mellom *generativ*, *diskriminativ* og *prediktiv* kunstig intelligens. 
Alle tre er ulike former for *maskinlæring*, som betyr at algoritmene trenes opp ved å lære fra data. Forskjellen er hva slags type oppgave de er laget for. Klikk på fanene under for å se noen forskjeller mellom de tre typene.

.. canvas-tabs::

	.. canvas-tab:: Generativ KI

		Generativ kunstig intelligens er programmer som lager (genererer) nytt innhold.
		Det er ofte tekst eller bilder vi bruker generativ KI til å lage.
		Men generativ KI kan også lage andre typer data, for eksempel tabeller.
		Generativ KI trenes opp på store mengder data av den typen den skal generere.

		I dette kurset skal vi for det meste ta for oss generativ KI.
		ChatGPT, Copilot og NotebookLM er eksempler på generativ kunstig intelligens som kan lage både tekst og bilder.

	.. canvas-tab:: Diskriminativ KI

		Diskriminativ kunstig intelligens er programmer som kan skille mellom ulike typer innhold.
		Det kan for eksempel være et program som kan se om et bilde er av en hund, en katt eller et annet dyr.
		Eller oppgaven kan være å klassifisere tekster etter tema, slik som spamfiltre.
		Selvkjørende biler trenger diskriminativ KI blant annet for å oppdage ting og mennesker rundt seg.

	.. canvas-tab:: Prediktiv KI

		Prediktiv kunstig intelligens prøver å forutsi utfallet av en hendelse.
		Værmelding er et velkjent eksempel på at det kan være nyttig å forutsi hva som kommer til å skje.
		Prediktiv kunstig intelligens leter etter mønstre i data som kan si noe om sannsynligheten for hendelser.

Oppsummert: Generativ KI er en type KI som kan *skape* nytt innhold, i stedet for bare å analysere eller klassifisere eksisterende informasjon.

.. uio-colorbox-3:: Fordypning
   
    .. uio-detail:: Hva er maskinlæring?
      
		Mennesker kan lære av erfaring.
		I maskinlæring lærer programmet av data (eller forsøker å gjøre det).
		Den stadig økende mengden tilgjengelige data har ført til sterkt økende interesse for maskinlæring.
		Maskinlæring er et sett av statistiske metoder som kan brukes til å trekke ut informasjon fra data.

		Maskinlæring skiller seg fra tradisjonell programmering i hvordan vi løser problemer.
		Et tradisjonelt program bruker en algoritme på noen inndata (input) for å produsere et resultat (output), som vist på figuren
		:ref:`figure-tradisjonelt_program`.

		.. _figure-tradisjonelt_program:
		.. figure:: ../images/tradisjonelt_program.svg
		   :align: center
		   :width: 100%
		   :alt:
		   		En figur som illustrerer et tradisjonelt program.
				Midt på er det en datamaskin.
				Til venstre er det to piler inn mot datamaskinen, som viser input og en algoritme.
				Til høyre er det en pil ut fra datamaskinen, som viser output.

		   Tradisjonell programmering

		Med maskinlæring er algoritmen ukjent, og det er nettopp den vi ønsker å lære.
		I veiledet læring har vi et sett med treningsdata og tilhørende ønskede utdata.
		Hvis oppgaven er å merke bilder, så kan utdataene være merkelappen til bildet, som for eksempel "hund" eller "katt".
		Fra dette vil vi lære en algoritme eller funksjon som kan produsere de ønskede utdataene fra de gitte inndataene.
		Figuren :ref:`figure-maskinlaring` illustrerer denne forskjellen.

		.. _figure-maskinlaring:
		.. figure:: ../images/maskinlaring.svg
		   :align: center
		   :width: 100%
		   :alt: 
		   		En figur som illustrerer maskinlæring.
				Midt på er det en datamaskin.
				Til venstre er det to piler inn til datamaskinen, merket "input: treningsdata" og "ønsket output".
				Til høyre er det en pil ut fra datamaskinen merket "algoritme".

		   Maskinlæring
