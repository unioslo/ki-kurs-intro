
Hva er store språkmodeller (LLM)?
==================================

Store språkmodeller (Large Language Models - LLM) er selve "motoren" bak tjenester som ChatGPT, Claude og Gemini. 
Dette er en type generativ KI som er spesialisert på tekst, og som har lært av enorme mengder tekst fra internett, bøker, artikler og andre kilder.

I dette kurset skal vi fokusere på LLMer, og ikke gå nærmere inn på de andre typene generativ KI.


Hvordan genererer en LLM tekst?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En LLM genererer tekst ved å beregne hva som er det mest sannsynlige neste ordet basert på konteksten. 
Litt som hjernen din automatisk foreslår "varmt" eller "kaldt" hvis noen sier "I dag er det veldig...", gjør LLM-en noe av det samme.

Transformer-teknologien
----------------------------------

Moderne LLM-er er bygget på *transformer*-teknologi som gjør at de kan se på hele teksten samtidig og forstå sammenhenger.
For eksempel: i setningen "Katten jaget musen fordi *den* var sulten" kan modellen kanskje forstå at "den" refererer til katten, ikke musen.

Mønstre, ikke kunnskap
----------------------------------

LLM-er lærer *mønstre* i tekst, ikke *fakta*. Hvis modellen har sett at "Oslo" ofte følger etter "hovedstaden i Norge er", vil den generere "Oslo" når du spør - men den "vet" ikke egentlig at dette er riktig. 
Dette er grunnen til at LLM-er kan gi svært overbevisende, men feil informasjon.

.. uio-note:: Oppsummert

   LLM-er genererer tekst ved å beregne sannsynligheten for neste ord basert på mønstre de har lært. 
   Transformer-teknologien gjør at de kan forstå sammenhenger i hele teksten. 
   De lærer mønstre, ikke fakta, og kan derfor produsere overbevisende tekst som likevel er feil.


