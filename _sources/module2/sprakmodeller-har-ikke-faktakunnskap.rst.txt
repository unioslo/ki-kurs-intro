Språkmodeller har ikke faktakunnskap
==============================================

Store språkmodeller er trent til å generere tekst som er troverdig, og som ligner på tekstene de er trent opp på.
De har likevel ikke noe forhold til sannhet [:ref:`Hicks <Hicks>`] og har derfor ikke sikker kunnskap om hva som er sant. 

Noen ganger spiller det liten rolle hvilket neste ord språkmodellen velger. 
Andre ganger er valget helt avgjørende for om svaret blir riktig eller feil.

Tenk deg at modellen skal fullføre setningen: «Fargen på huset er …»
Mulige fortsettelser kan være «rød», «blå» eller «grå».
I en slik setning er det ikke åpenbart hvilket ord som er «riktig» eller «best», fordi flere alternativer passer. 
Det er heller ikke veldig viktig hvilket som velges.

Men hvis du spør modellen: «Hva er hovedstaden i Norge?»
Da forventer du et korrekt svar. 
Her blir det viktig hvilket ord modellen foreslår. 

I begge tilfellene velger modellen det mest sannsynlige ordet basert på mønstre i tekst den har lært fra, og ikke kunnskap.
Forventer du et kunnskapssvar eller faktasvar, er det derfor fare for feil. 
Dette gjelder særlig hvis treningsgrunnlaget er mangelfullt eller skjevt.


.. uio-dont:: Manipulering (Språkmodell-forgiftning)

   At språkmodeller ikke har sikker kunnskap om hva som er fakta, gjør dem sårbare for bevisst manipulering av treningsdata.
   Denne typen manipulering kalles ofte «språkmodell-forgiftning».  Aktører kan legge ut misvisende informasjon for at modellene skal bli trent på den.
   Dermed kan modellene gi svar som er manipulert og ikke stemmer overens med virkeligheten.

   Et eksempel er da BBC-journalisten Thomas Germain manipulerte blant annet ChatGPT og Gemini til å svare at han var kåret til mester i pølsespising. [:ref:`Germain <Germain>`]
   En ganske ufarlig type manipulering, men som allikevel tydeliggjør modellenes svakhet. 

   Et mer alvorlig eksempel er et forsøk av den svenske forskeren Almira Osmanovic Thunström.
   Hun undersøkte om KI-tjenester ville spre medisinske påstander fra åpenbart fabrikkerte artikler.
   Derfor publiserte hun to fabrikkerte artikler om en fiktiv diagnose i arkivet preprints.org.
   Etter kort tid begynte KI-tjenester å vise til den fiktive diagnosen. [:ref:`Stokel-Walker <Stokel-Walker>`]

.. uio-reflect:: Test deg selv

   Hvorfor kan en språkmodell sine svare inneholde feil, selv om svaret høres troverdig ut?

   .. uio-answer:: Klikk på meg for mulig svar

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk.
      Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant.
      Derfor kan den produsere feil informasjon med samme selvtillit som riktig informasjon.


   
