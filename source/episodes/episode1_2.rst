Generativ KI
==============

Når vi snakker om KI i hverdagen er det som oftest generativ KI vi tenker på.
ChatGPT, Copilot og NotebookLM er eksempler på generativ KI.

Det kalles *generativ kunstig intelligens* fordi KIen *genererer* (lager) nytt innhold som tekst, bilder eller lyd, 
til forskjell fra for eksempel *diskriminativ*  kunstig intelligens som "bare" klassifiserer det som finnes fra før. 
Et eksempel på sistnevnte er en KI som kan "se" gjennom bilder av katter og hunder, og "si" hvilke som er kattebilder og hvilke som er hundebilder.

Generativ og deskriptiv KI er eksempler på er en måte man deler inn kunstig intelligens på. 
I denne klassifiseringen har vi i tillegg *prediktiv* kunstig intelligens som har som mål å *prediktere* (beregne/forutse) en sannsynlig utvikling av gitt data. 
Her er et klassisk eksempel værmeldingen.

Alle tre er ulike former for *maskinlæring*, som betyr at algoritmene trenes opp ved å lære fra (store mengder) data. 
Forskjellen er hva slags type oppgave de er laget for.
Du kan lese litt mer om makskinlæring og om hva som skiller diskriminativ og prediktiv KI fra generativ KI under "Fordypning" nedenfor.

I dette kurset vil du hovedsakelig lære om generativ kunstig intelligens som bygger på store språkmodeller og derfor genererer tekst.
Du vil også lære litt om KI til bildegenererig, som er en annen type generativ KI, men da spesialisert på bilder. 


.. uio-colorbox-3:: Fordypning

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
