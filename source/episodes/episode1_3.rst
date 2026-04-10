
Store språkmodeller (LLM)?
==================================

Store språkmodeller (LLM) er en spesifikk type generativ KI, som er spesialisert på språk og tekst. Den har trent og "lært" av enorme mengder tekst fra internett, bøker, artikler og andre kilder. Store språkmodeller er selve "motoren" bak tjenester som GPT UiO, NotebookLM og Microsoft Copilot. 

I dette kurset vil du hovedsakelig lære om kunstig intelligens som bygger på store språkmodeller. Du vil også lære litt om KI til bildegenererig. 

Hvordan lager en LLM tekst?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Forslag: Se for deg at du skal bruke KI til å skrive hjelp i planlegging av et møte. Du stilles Chatgpt UIO spørsmålet
"Kan du sette sammen et forslag til agenda for et evalueringsmøte av et prosjekt" 

En LLM genererer tekst ved å beregne hva som er det mest sannsynlige neste ordet basert på konteksten. 
Litt som hjernen din automatisk foreslår "sola" hvis noen sier "I dag skinner ...", gjør LLM-en noe av det samme.
Eller i setningen: "Katten jaget musen fordi *den* var sulten" kan modellen kanskje forstå at "den" refererer til katten, ikke musen.

LLM-er lærer *mønstre* i tekst, ikke *fakta*. 

I tekst som modellen har blitt trent på vil "Norge" og "hovedstad" ha forekommet sammen med "Oslo", og derfor er ordene tett assosiert med hverandre i modellen.  
Derfor vil den generere "Oslo" når du spør hva hovedstaden i Norge er. Men den "vet" ikke egentlig at dette er riktig.
Dersom modellen hadde sett ordet "Stockholm" i stedet, så ville den svart dette. Dette er grunnen til at LLM-er kan gi svært overbevisende, men feil informasjon.

Dette gjør også modellen sårbar for bevisst manipulering.
Aktører kan for eksempel legge ut misvisende informasjon for at modellene skal bli trent på den, 
og dermed gi svar som er manipulert og ikke stemmer overens med virkeligheten.

