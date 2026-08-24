Lag gode instruksjoner
=========================

Språkmodellen er god til å gjette hva svaret bør inneholde, men den kan ikke lese tankene dine.
Med noen få grep kan du hjelpe språkmodellen til å gi svar du blir mer fornøyd med.
Bruk gjerne alle disse prinsippene når du skriver instruksjonen din.

Her ser du noen enkle eksempler på instruksjoner som kan bli bedre, og forslag til hvordan du kan forbedre dem.

1. Gi kontekst
******************

.. uio-do-dont:: 

    .. uio-dont:: Mangelfull

        Forklar forskjellen på KI og maskinlæring.
    
    .. uio-do:: Bedre


        Forklar kort forskjellen på KI og maskinlæring, tilpasset administrativt ansatte ved et universitet som ikke har teknisk bakgrunn.
        Tenk at forklaringen skal brukes i et 5-minutters innlegg på et personalmøte, der målet er at kollegene skal forstå begrepene på et overordnet nivå - ikke tekniske detaljer.


        **Hva gjør denne bedre?**

        Du forteller språkmodellen litt hva som er bakgrunnen og/eller konteksten til teksten du ber den produsere.

2. Spesifiser format
***********************

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Lag et møtereferat av disse notatene: [dine notater]
    
    
    .. uio-do::  Bedre
        
        Basert på mine notater fra møtet, lag et møtereferat. Strukturer referatet med deltakere, agenda, beslutninger og oppgaver. Mine notater: [dine notater].

        **Hva gjør denne bedre?**

        Siden du har spesifisert formatet vil du trenge mindre redigering i etterkant. Språkmodellen vil kunne sortere og skille ut teksten basert på strukturen du ber om. 

    
3. Definer en rolle
***********************

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Sjekk denne teksten: [din tekst]


    .. uio-do:: Bedre


        Du er en norskspråklig språkvasker i universitetssektoren.
        Gå gjennom teksten nedenfor og gi forslag til forbedringer. 
       
        - Påpek skrivefeil og grammatikk
        - Behold innholdet faglig uendret
      
        Teksten: 
        [din tekst]

        **Hva gjør denne bedre?** 
        
        Språkmodeller har sett tekst fra veldig mange roller og sjangre. 
        Fortell modellen hvilken rolle den skal innta, så får du mer relevante og fokuserte svar.


4. Gi eksempler
***********************

.. uio-do-dont::

    .. uio-dont:: Mangelfull

        Skriv en tittel til en nyhetssak om at vi får nytt system for reiseregninger.


    .. uio-do:: Bedre

        Jeg skal skrive titler til interne nyhetssaker for ansatte ved Universitetet i Oslo.

        Her er eksempler på stilen jeg ønsker:

        - «Nytt tilbud: Gratis språkkurs for ansatte»
        - «Viktig: Endringer i møterom-booking fra 1. april»
        - «Husk: Frist for registrering av arbeidstid nærmer seg»

        Skriv en kort tittel i samme stil for denne saken: Vi får nytt IT-system for reiseregninger neste måned.

        Krav til tittelen:

        - Maks 90 tegn
        - Skal være informativ og nøktern
        - Målgruppe: alle ansatte


        ### Hva gjør denne bedre? 
        
        **Hva gjør denne bedre?** 

        Her gir du eksempler på stilen eller formatet du ønsker. 
        Dette er ofte lettere enn å forklare stilen med ord.
        Denne teknikken kalles gjerne "Few-shot instruksjon"

