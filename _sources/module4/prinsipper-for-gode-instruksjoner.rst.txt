Prinsipper for gode instruksjoner
===================================

Her ser du noen enkle eksempler på instruksjoner som kan bli bedre.
Språkmodellen er god til å gjette hva svaret bør inneholde, men den kan ikke lese tankene dine.
Med noen få grep kan du hjelpe språkmodellen til å gi svar du blir mer fornøyd med.
Bruk gjerne alle disse prinsippene når du skriver instruksjonen din.

1. Vær spesifikk 
-----------------------

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Skriv en e-post.

    .. uio-do:: Bedre

        Skriv en e-post til mine kolleger om at møterommet Gaia er stengt for vedlikehold i uke 15. Tonen skal være vennlig, men profesjonell.

        **Hva gjør denne bedre?**

        Den gode instruksjonen spesifiserer både hva e-posten skal handle om, hvem målgruppen er, og hvilken tone den skal ha.

2. Gi kontekst
----------------------

.. uio-do-dont:: 

    .. uio-dont:: Mangelfull

        Forklar forskjellen på KI og maskinlæring.
    
    .. uio-do:: Bedre


        Forklar kort forskjellen på KI og maskinlæring, tilpasset administrativt ansatte ved et universitet som ikke har teknisk bakgrunn.
        Tenk at forklaringen skal brukes i et 5-minutters innlegg på et personalmøte, der målet er at kollegene skal forstå begrepene på et overordnet nivå - ikke tekniske detaljer.


        **Hva gjør denne bedre?**

        Du forteller språkmodellen litt hva som er bakgrunnen og/eller konteksten til teksten du ber den produsere.

3. Spesifiser format
----------------------

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Lag et møtereferat av disse notatene: [dine notater]
    
    
    .. uio-do::  Bedre
        
        Basert på mine notater fra møtet, lag et møtereferat. Strukturer referatet med deltakere, agenda, beslutninger og oppgaver. Mine notater: [dine notater].

        **Hva gjør denne bedre?**

        Siden du har spesifisert formatet vil du trenge mindre redigering i etterkant. Språkmodellen vil kunne sortere og skille ut teksten basert på strukturen du ber om. 

    
4. Definer en rolle
--------------------

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Sjekk denne teksten: [din tekst]


    .. uio-do:: Bedre


        Du er en norskspråklig språkvasker i universitetssektoren.

        Gå gjennom teksten nedenfor og:

        - Rett skrivefeil og grammatikk
        - Behold innholdet faglig uendret
        - Foreslå mer formelle formuleringer der teksten virker for uformell for en beskjed til studenter

        Svar med:

        - Revidert tekst
        - Kort liste over de viktigste endringene du har gjort

        Teksten: 
        [din tekst]

        **Hva gjør denne bedre?** 
        
        Språkmodeller har sett tekst fra veldig mange roller og sjangre. Fortell modellen hvilken rolle den skal innta, så får du mer relevante og fokuserte svar.
