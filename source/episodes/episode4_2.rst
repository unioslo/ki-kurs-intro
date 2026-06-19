
GPT UiO
========

GPT UiO er UiOs personverntrygge KI-chat. 

I GPT UiO kan du velge mellom flere ulike språkmodeller - altså hvilken «hjerne» tjenesten bruker.  
Modellene har forskjellig størrelse, funksjoner (som støtte av bilder) og bruksområder. 
En spesielt viktig forskjell mellom modellene er om de kjører i skyen (OpenAI sine GPT-modeller i Microsoft Azure skyen) eller *lokalt*.
Med *lokalt* mener vi på servere som eies og driftes av UiO eller vår samarbeidspartner NTNU.

Mens alle modellene, både de i skyen og de som lokalt sikrer at GDPR reglene følges, er du ekstra godt beskyttet om du velger de lokale modellene.
Det er da går *ingen* data til skyen, alt forblir på UiO eller NTNU sine systemer.

Noen av de lokale modellene kan i tillegg håndtere opp til `røde data`_.

.. _røde data: https://www.uio.no/tjenester/it/sikkerhet/lsis/tillegg/lagring/infoklasser.html

.. uio-viktig::
   
   * Velger du en lokal språkmodell, har du ekstra kontroll over dataene dine og kan være trygg på at ingenting lastes opp i skyen.  
   * Velger du en skybasert modell, behandles inn- og utdata midlertidig av Microsoft Azure OpenAI innenfor GDPR-kompatible regioner (Europa).

   Uavhengig av om du bruker en lokal eller skybasert modell, lagres all logg samt inn- og utdata kun på UiOs servere. Ditt brukernavn deles ikke med Microsoft.
   Derfor er GPT UiO GDPR-kompatibel. 


Så hvilken modell skal du velge?
---------------------------------

De lokale språkmodellen er gode, men de er mye *mindre* enn de som kjører i skyen. 
Det betyr at om oppgaven du skal løse er veldig kompleks, så kan det være at du får bedre kvalitet om du velger en sky-modell.

Vi foreslår at du prøver ut forskjellige modeller, og om du kan nøye deg med en mindre og lokal modell, så velg denne.
Den bruker totalt sett mindre ressurser, slik som strøm, enn de store modellene i skyen. 

Noen relevante spørsmål som kan hjelpe deg med å velge modell:

* Er svaret godt nok med en mindre modell? Bra, gå for den mindre modellen og spar ressurser!
* Ikke god nok kvalitet på svaret? Bytt fra en mindre lokal modell til en større skymodell.
* Trenger du ekstra beskyttelse på dataene dine? Velg en lokal modell som støtter opp til røde data.
* Skal du behandle bilder i tillegg til tekst? Velg en modell som støtter bilder.


.. uio-colorbox-3:: Fordypning for de nysgjerrige

   .. uio-detail:: Velge en annen modell enn standard

      .. figure:: ../images/gpt-modell-meny.png                                                                                                                  
            :align: center                                                                                                                                         
            :width: 75%                                                                                                                                            
            :alt: Meny i GPT som viser de forskjellige språkmodellene man kan velge blant                                        
                                                                                                                                                               
      Klikk på nedover-pilen for å se hvilke språkmodeller du kan velge mellom


   .. uio-detail:: Eksempel på språkmodeller i GPT UiO

      .. figure:: ../images/gpt-uio-modeller.png                                                                                                                 
            :align: center                                                                                                                                         
            :width: 75%                                                                                                                                            
            :alt: Meny i GPT som viser de forskjellige språkmodellene man kan velge blant                                        
                                                                                                                                                               
      Her ser du listen over de forskjellige språkmodellen som GPT UiO tilbyr. Listen oppdateres når nye modeller eller versjoner blir tilgjengelig.
      De røde boksene viser at noen av modellene kjører lokalt på NTNU. De andre kjører i Microsoft Azure skyen.




