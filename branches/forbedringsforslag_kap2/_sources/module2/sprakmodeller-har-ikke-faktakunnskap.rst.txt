Språkmodeller har ikke faktakunnskap
==============================================

Språkmodeller har ikke noe forhold til sannhet [:ref:`Hicks <Hicks>`].
Store språkmodeller er trent til å generere tekst som er troverdig, og som ligner på tekstene de er trent opp på.
Men språkmodellene har ikke sikker kunnskap om hva som er sant: som vi har lært beregner de bare hvilke ord som er mest sannsynlige.

Når en språkmodell skal fullføre setningen «Hovedstaden i Norge var…», så er noen mulige fortsettelser «Bergen», «Kristiania» og «Oslo».
Alle disse stedene har vært Norges hovedstade.
Hvis du spør modellen «Hva som er hovedstaden i Norge?», svarer den sannsynligvis «Oslo».
Men det er en viss fare for at den svarer feil, fordi svaret baseres på sannsynlig neste ord, og ikke kunnskap.

Fordi språkmodellene beregner ord basert på tekst de er trent på er de sårbare for bevisst manipulering, såkalt LLM poisning. 

.. uio-dont:: Manipulering (Språkmodell-forgiftning)

   Store språkmodeller kan være sårbare for bevisst manipulering, såkalt "Språkmodell-forgiftning" (LLM poisoning).
   Aktører kan for eksempel legge ut misvisende informasjon for at modellene skal bli trent på den.
   Dermed kan modellene gi svar som er manipulert og ikke stemmer overens med virkeligheten.

   Et eksempel er da BBC-journalisten Thomas Germain manipulerte blant annet ChatGPT og Gemini til å svare at han var kåret til mester i pølsespising. [:ref:`Germain <Germain>`]

   Et annet eksempel er et forsøk av den svenske forskeren Almira Osmanovic Thunström.
   Hun undersøkte om KI-tjenester ville spre medisinske påstander fra åpenbart fabrikkerte artikler.
   Derfor publiserte hun to fabrikkerte artikler om en fiktiv diagnose i arkivet preprints.org.
   Etter kort tid begynte KI-tjenester å vise til den fiktive diagnosen. [:ref:`Stokel-Walker <Stokel-Walker>`]

.. uio-reflect:: Refleksjon

   Hvorfor kan en språkmodell gi feilinformasjon selv om svaret høres veldig troverdig ut?

   .. uio-answer:: Klikk på meg for mulig svar

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk.
      Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant.
      Derfor kan den produsere feilinformasjon med samme selvtillit som riktig informasjon.


   
