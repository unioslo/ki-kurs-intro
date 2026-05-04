KI-agenter
===============


Til slutt har vi KI-agenten. 
Mens KI-assistenten egentlig ikke er så mye mer enn en KI med spesifikke instruksjoner på hvordan den skal oppføre seg, 
så er KI agenten gjerne en avansert KI-assistent som i tillegg kan utføre *handlinger* i den digitale verden.
KI-agenten nøyer seg ikke med å fortelle deg hvordan du løser en oppgave, den utfører oppgaven for deg. 

Agenter er laget for en eller flere spesifikke formål. 
En agent kan for eksempel hente informasjon fra andre systemer som internett eller en database, 
den kan kanskje bestille togbiletter for deg, eller slå av en datamaskin som har symptomer på å være under angrep utenfra. 
Eller helt andre ting avhengig av hva som er formålet med akkurat den agenten.

.. canvas-tabs:: Hvis jeg ber henholdsvis en KI-assistent og en KI-agent om å bestille en flybillett fra Norwegian for meg så vil

    .. canvas-tab:: KI-assistenten

        *fortelle meg* hvordan bestille billetten

    .. canvas-tab:: KI-agenten

        gå til norwegian.no og *bestille* den for meg. 


Risiko knyttet til KI-agenter
------------------------------

Det er mye høyere risiko involvert med agenter sammenlignet med en ren chat eller assistent tjeneste. 
Begge har de samme svakheter og begrensninger alle KI-systemer har som genererer output basert på en språkmodell (troverdighet, hallusinasjon, ikke fakta basert, ikke reproduserbart).
Men fordi en agent samhandler med andre digitale systemer i den "virkelige" verden, kan konsekvensene av en feil bli betydelig større. 
Spesielt hvis man lar agenten operere autonomt, det vil si uten at et menneske godkjenner eller kontrollerer handlingen.


.. uio-task:: Refleksjonsoppgave

    Tenk deg en fremtid der Universitetet i Oslo har tatt i bruk en agent som skal avdekke og reagere på fusk på eksamen.

    Agenten 

    * leser gjennom eksamensoppgaven, sensorveiledningen og besvarelsen
    * har tilgang til kandidatens tidligere besvarelser
    * har tilgang til reglene for fusk ved Universitetet i Oslo
    * har en innebygget fusk-detektor
    * tar en beslutning om besvarelsen er gyldig eller anses som fusk
    * dersom fusk: annulerer eksamen og utestenger hen fra Universitetet dersom alvorlighetsgraden tilsier det


    Risikoen ved et slikt system er åpenbar: hva om systemet tar feil og feilaktig bedømmer en besvarelse som fusk? 
    Hva kan man gjøre for å redusere denne risikoen? 
    
    .. uio-detail:: Forslag til svar

        * Kunne kjenne til hvordan fusk detektoren fungerer, ingen "black box".
        * Kunne gå vurderingen grundig i sømmene
           * Sikre at det er loggført hva beslutningen er basert på
           * Sikre at en sensor lett kan finne frem til steder i besvarelsen som anses som fusk
        * Ikke under noen omstendighet la agenten faktisk *ta beslutningen selv*, det vil si faktisk annulere eksamen eller utføre andre handlinger som får konsekvenser for kandidaten, uten at et menneske har godkjent handlingen
