Generativ KI
==============
Når vi snakker om KI i hverdagen, mener vi som regel generativ KI. UiO GPT, Copilot og NotebookLM er eksempler på dette.
Generativ kunstig intelligens kalles «generativ» fordi den lager nytt innhold basert på det den har lært fra før. Du skriver inn en
instruksjon og systemet genererer et forslag til svar eller innhold.

Generativ KI bygger på det som kalles maskinlæring. Det betyr at systemet lærer av store mengder data og finner mønstre uten at mennesker forteller det nøyaktig hva det skal se etter.

Det finnes flere typer KI. I dette kurset skal du lære mest om store språkmodeller, som en en type generativ KI.
Store språkmodeller er selve motoren i mange KI-tjenester du bruker. 

.. uio-colorbox-3:: 

	Generativ, disktriminativ og prediktiv KI 

	.. canvas-tabs::

		.. canvas-tab:: Generativ KI

			En KI-chat som genererer et møtereferat basert på dine møtenotater

		.. canvas-tab:: Diskriminativ KI

			Diskrimitativ KI sorterer og gjenkjenner ting som allerede finnes. 
			Eksempel: KI system som kan identifisere om et fotografi er av en hund eller en katt

		.. canvas-tab:: Prediktiv KI
			
			Prediktiv kunstig intelligens leter etter mønstre i data som kan si noe om sannsynligheten for hendelser.

			Eksempel: værmeldingen

.. uio-colorbox-3:: Fordypning for de nysgjerrige

    .. uio-detail:: Maskinlæring

		Mennesker lærer ved erfaring. Maskinlæring er det samme prinsippet, bare for dataprogrammer. I stedet for å lære av erfaring,
		lærer programmet av data.
		Når vi har store mengder data tilgjengelig, for eksempel tekst, bilder eller tall, kan vi bruke
		maskinlæring til å finne mønstre og sammenhenger som det er vanskelig eller tidkrevende for mennesker å oppdage selv. 

		Maskinlæring skiller seg fra tradisjonell programmering i hvordan den løser problemer. 

 		Tradisjonell programmering foregår slik: 

		- Et menneske lager klare regler: «Hvis X skjer, gjør Y».
		- Programmet får input, og bruker reglene på den.
		- Programmet gir deg resultatet.
		
		Eksempel på tradisjonell programering: 
		Et program som regner ut studiepoeng basert på antall beståtte emner og vekting per emne.

		I maskinlæring er algoritmen ukjent, og det vi ønsker å lære.
		Maskinlæring løser en problem slik:

		- Vi har mange eksempler på input (data)  
 		- Vi leverer en instruksjon på ønsket resultat (output) 
		- I stedet for å skrive reglene selv, lar vi systemet lære reglene ut fra eksemplene.

		Eksempel:
		Hvis vi vil at et system skal kjenne igjen om et bilde viser en hund eller en katt, kan vi gi det tusenvis av bilder som allerede er merket som «hund» eller «katt».
		Systemet lærer da en regel (en algoritme) som kan gjette riktig merkelapp for nye bilder det aldri har sett før.




Gammel  versjon

Når vi snakker om KI i hverdagen er det som oftest generativ KI vi tenker på.
ChatGPT, Copilot og NotebookLM er eksempler på generativ KI.

Det kalles *generativ kunstig intelligens* fordi den *genererer* (lager) helt nytt innhold som for eksempel tekst, bilde eller lyd. 
En annen type KI er *diskriminativ*  kunstig intelligens som klassifiserer det som finnes fra før. 
Generativ og diskriminativ KI er èn måte å bryte opp hva kunstig intelligens er. 
I denne klassifiseringen har vi i tillegg *prediktiv* kunstig intelligens som har som mål å *prediktere* (beregne/forutse) en sannsynlig utvikling av gitt data. 

.. uio-colorbox-3:: 

	Eksempler på generativ, disktriminativ og prediktiv KI 

	.. canvas-tabs::

		.. canvas-tab:: Generativ KI

			En KI-chat som genererer et møtereferat basert på dine møtenotater

		.. canvas-tab:: Diskriminativ KI

			En KI som kan identifisere om et fotografi er av en hund eller en katt

		.. canvas-tab:: Prediktiv KI
			
			Her er et klassisk eksempel værmeldingen.


Alle tre bygger på det som kalles *maskinlæring*. Maskinlæring er en metode der teknologien lærer fra store mengder date, og der systemet finner mønstre på egen hånd.
Forskjellen på dem er hva slags type oppgave de er laget for.
Du kan lære mer om maskinlæring og hva som skiller diskriminativ og prediktiv KI fra generativ KI under "Fordypning".

I dette kurset vil du hovedsakelig lære om generativ kunstig intelligens, som bygger på store språkmodeller og derfor genererer tekst.
Du vil også lære litt om KI til bildegenererig, som er en annen type generativ KI, spesialisert på bilder. 


.. uio-colorbox-3:: Fordypning for de nysgjerrige

    .. uio-detail:: Diskriminativ KI

		Diskriminativ kunstig intelligens er programmer som kan skille mellom ulike typer innhold.
		Det kan for eksempel være et program som kan se om et bilde er av en hund, en katt eller et annet dyr.
		Eller oppgaven kan være å klassifisere tekster etter tema, slik som spamfiltre.
		Selvkjørende biler trenger diskriminativ KI blant annet for å oppdage ting og mennesker rundt seg.

    .. uio-detail:: Prediktiv KI

		Prediktiv kunstig intelligens prøver å forutsi utfallet av en hendelse.
		Værmelding er et velkjent eksempel på at det kan være nyttig å forutsi hva som kommer til å skje.
		Prediktiv kunstig intelligens leter etter mønstre i data som kan si noe om sannsynligheten for hendelser.

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
