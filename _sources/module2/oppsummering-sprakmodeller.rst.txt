Oppsummering kapittel 2
========================

I dette kapittelet har du lært hvordan store språkmodeller lager tekst og hvilke svakheter den har når den gjøre dette.
Før du går videre til kapittel 3 kan du teste hva du har lært.

.. uio-reflect:: Test deg selv

    Diskuter selv eller med en kollega

    1. Hva er store språkmodeller og hvordan fungerer de?
    2. Hva er kontekst og hva gjør du for å gi språkmodellen god nok kontekst?
    3. Nevn noen av de viktigste svakhetene ved store språkmodeller og hva kan du gjøre for å imøtekomme dem?

Repetisjon
--------------------------------------------------------------------

* **Store språkmodeller** er matematiske modeller som som bygger opp svaret ett ord av gangen, betinget av
  konteksten du gir den.
  Store språkmodeller generere med andre ord tekster basert på statistiske mønstre, fremfor kunnskap.

* **Kontekst** er alt vi gir modellen som informasjon når vi snakker med den.
 
* **Store språkmodeller har ikke noe forhold til sannhet** og har derfor ikke sikker kunnskap om hva som er
  sant. De er trent til å generere tekst som er troverdig, og som ligner på tekstene de er trent opp på. Det
  gjør modellene sårbare for bevisst manipulering av treningsdata. Aktører kan legge ut misvisende informasjon
  for at modellene skal bli trent på den. Dermed kan modellene gi svar som er manipulert og ikke stemmer overens
  medvirkeligheten.

* Fordi store språkmodeller ikke har faktakunnskap, kan de **finne på ting som ikke stemmer**. Det kan være
  feil fakta, oppdiktede referanser eller forvekslinger.

* **Språkmodellen har ikke hukommelse i seg selv**.
  Når du skriver en ny instruksjon, sender chat-systemet hele den tidligere samtalen sammen med den
  nye instruksjonen til språkmodellen. 
  Lange samtaler kan "forvirre" modellen, slik at den gir dårligere svar. Derfor er det viktig
  å starte en ny samtale om du skifter tema.

* **Språkmodellen har innebygde skjevheter**. Det kan være skjevhet som følge av manglende treningsdata,
  skjevhet som speiler skjevheter i samfunnet eller bekreftelsesskjevhet.

Neste kapittel
--------------

Nå som du forstår hvordan språkmodeller fungerer og hva begrensningene deres er,
skal du i neste kapittel lære hvordan du bruker KI trygt og effektivt i praksis.
