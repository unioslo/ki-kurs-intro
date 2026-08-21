Modellenes skjevheter
=====================

Vi har tidligere lært at det er en iboende egenskap ved språkmodeller at de *finner på ting*.
En annen iboende egenskap er at språkmodellen har innebygde *skjevheter*. 
Det kan være mange typer skjevheter. Vi skal ta for oss noen her. 

Skjevhet som følge av manglende treningsdata
---------------------------------------------------
Store språkmodeller trenes som sagt på tekster fra internett, men det er mange tekster de ikke har tilgang til.
For eksempel har de ikke tilgang til informasjon som krever innlogging, eller som er bak en betalingsmur.
De har også begrenset tilgang til trykte kilder.
Dette skaper begrensninger for hva modellene kan lære og gir ulikt utslag for forskjellige bruksområder. 
Ett eksempel på dette er at modellene kan være svake på helt spesifikk fagkunnskap i et gitt forskningsdomene.


Skjevhet som speiler skjevheter i samfunnet
---------------------------------------------

En annen type skjevhet stammer fra ulikheter i samfunnet vårt, og gjenspeiles derfor også i den digitale informasjonen vi produserer.
Dette kan dreie seg om skjevheter knyttet til etnisitet, kjønn, religion eller annet og er veldig viktig å være klar over når man behandler forslag og tekst fra en språkmodell. 

.. uio-colorbox-3:: Eksempel på skjevheter i treningsdata

  Anta at en språkmodell er trent på mange gamle stillingsannonser der «leder» oftere omtales som «han» enn «hun».
  Når du ber modellen skrive en tekst om «en typisk leder», vil den da ha høyere sannsynlighet for å bruke ord som «han», «mann» og mannsnavn.
  
  Modellen har ikke meninger om kjønn, den gjennskaper bare mønstrene som allerede fantes i tekstene den ble trent på.


Bekreftelsesskjevhet (bekreftelsesbias)
----------------------------------------

Dagens språkmodeller har en tendens til å være enige med deg.
Dette kan føre til at språkmodellen gir deg *rett i* noe som ikke er rett.

For å unngå bekreftelsesskjevhet kan du snu på spørsmålet, altså også spørre om det motsatte.
