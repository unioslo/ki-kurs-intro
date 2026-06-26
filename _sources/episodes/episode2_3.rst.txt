Språkmodeller har ikke faktakunnskap
==============================================

Språkmodeller har ikke noe forhold til sannhet [Hicks]_.
Store språkmodeller er trent til å generere tekst som er troverdig, og som ligner på tekstene de er trent opp på.
Språkmodellene har ikke sikker kunnskap om hva som er sant, de regner bare på hvilke ord som er mest sannsynlige.

Hvis en språkmodell skal fullføre setningen «Hovedstaden i Norge var…», så er noen mulige fortsettelser «Bergen», «Kristiania» og «Oslo».
Alle disse stedene har vært hovedstaden i Norge.
Hvis du spør modellen hva som er hovedstaden i Norge, svarer den sannsynligvis «Oslo».
Men det er en viss fare for at modellen svarer feil.
Det er særlig risiko for feil svar på spørsmål om tall, som for eksempel datoer og årstall.


.. uio-dont:: Manipulering (LLM poisoning)

   Store språkmodeller kan være sårbare for bevisst manipulering, såkalt "LLM poisoning".
   Aktører kan for eksempel legge ut misvisende informasjon for at modellene skal bli trent på den.
   Dermed kan modellene gi svar som er manipulert og ikke stemmer overens med virkeligheten.

   Et eksempel er da BBC-journalisten Thomas Germain manipulerte blant annet ChatGPT og Gemini til å svare at han var kåret til mester i pølsespising. [Germain]_

   Et annet eksempel er et forsøk av den svenske forskeren Almira Osmanovic Thunström.
   Hun undersøkte om KI-tjenester ville spre medisinske påstander fra åpenbart fabrikkerte artikler.
   Derfor publiserte hun to fabrikkerte artikler om en fiktiv diagnose i arkivet preprints.org.
   Etter kort tid begynte KI-tjenester å vise til den fiktive diagnosen. [Stokel-Walker]_

.. uio-reflect:: Refleksjon

   Hvorfor kan en språkmodell gi feilinformasjon selv om svaret høres veldig troverdig ut?

   .. uio-answer::

      Fordi språkmodellen genererer tekst basert på statistiske mønstre den har lært, ikke basert på faktasjekk.
      Den har lært hvordan troverdige svar "ser ut", men vet ikke forskjellen på sant og usant.
      Derfor kan den produsere feilinformasjon med samme selvtillit som riktig informasjon.


   