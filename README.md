Kurssidene bygges automatisk (det tar noen minutter etter at du har lagret endringene dine) og kan sees her: https://unioslo.github.io/ki-kurs-intro

OBS: Funksjonaliteten er laget for canvas for å laste opp html i _build som "Sider" i canvas. Siden her på github vil ikke være 100 % lik det vi ser i Canvas, men jeg har forsøkt å få det så nært som mulig, for å lette arbeidet. 


# Hvordan jobbe i github og Canvas

Selve kursinnholdet finner du i folderen `source/episodes`

Filene er delt opp slik at de blir passelige "Sider" i Canvas, målet er at man ikke må scrolle for mye per side.

## 1. Naviger til filen du ønsker å editere, og åpne den for editering
<img width="400" height="468" alt="github-unioslo-edit-file" src="https://github.com/user-attachments/assets/f5d7b5fd-b09e-4fad-aa85-f5d3940d2e91" />

## 2. Når du er ferdig, trykk den store grønne "Commit changes" knappen
<img width="400" alt="github-unioslo-commit-change" src="https://github.com/user-attachments/assets/ff770c1a-d3eb-4ab9-8770-9958e0deab3f" />

## 3. Skriv en fornuftig endringsmelding (Commit message). 

Velg ellers default og trykk "Commit changes" for å laste opp endringene i github.com

<img width="300" alt="github-unioslo-commit-message" src="https://github.com/user-attachments/assets/2b49e59a-dee1-4a03-8709-2c7ea44df491" />

## 4. Automatisk bygging av html filene
Når endringen er blitt lastet opp (commited) så starter en automasjon i bakgrunnen - du kan følge med i Actions taben i github. 

Denne automatikken er satt opp til å "bygge" html filer av rst filene. Alle rst filene blir bygget på nytt hver gang en fil er endret (selv de som ikke har noen endringer).

<img width="300" alt="github-unioslo-actions" src="https://github.com/user-attachments/assets/d6c2f096-e5a8-4bd8-a891-e1b337356f2b" />

### Kontroller resultatet
Når denne prosessen er ferdig, kan du kikke på resultatet på github sin egen publiseringløsning: https://unioslo.github.io/ki-kurs-intro - dette er bare "for convenience" for å få en rask sjekk at ting ser bra ut. Dersom du er fornøyd så er du klar for å oppdatere innholdet i Canvas - se punkt 5. 

## 5. Oppdater Canvas

Html-filene lagres i en egen branch i github [html-pages](https://github.com/unioslo/ki-kurs-intro/tree/html-pages)

<img width="300" alt="github-unioslo-html-pages-branch" src="https://github.com/user-attachments/assets/827ffaf8-4734-47bb-985d-7bde147f1367" />

Du har nå valget mellom å bruke et python skript til å oppdatere filen(e) i Canvas med REST API, eller manuelt oppdatere de ved å copy/paste html-koden for hver fil. 


### 5a. Manuell oppdatering
Naviger til branchen `html-pages`. Du finner de genererte html filene i folderen `html/episodes`.  

1. For hver fil/side du ønsker å ooppdatere, klikk inn på den og klikk på kopier-ikonet. 
<img width="500" alt="github-unioslo-html-raw-copy" src="https://github.com/user-attachments/assets/146a1079-532f-4a79-99d3-8df1408ebea2" />


2. Gå deretter til Canvas, finn riktig side, klikk "Rediger" og videre `</>` knappen nede til høyre under redigeringsboksen. 

<img width="500" alt="canvas-rediger-html" src="https://github.com/user-attachments/assets/c275505e-f74b-4bf3-8630-77c8cdf539bd" />

3. Paste inn html koden du kopierte fra github.
   
4. Lagre

Siden er nå oppdatert i Canvas. 

### 5b. Oppdatering via REST API (for "eksperter")

Du finner python skriptet i `div-support-filer/update_canvas_pages.py`. Du trenger en API nøkkel for å gjøre dette, se instruksjoner i python filen og/eller i [README_UPDATE_CANVAS.md](README_UPDATE_CANVAS.md). 

Kort oppsummert:
- Skriptet oppdaterer Canvas-sider automatisk basert på HTML-filer (lokale eller fra GitHub)
- Bruker en mapping-fil (`page_id_mapping.json`) for å koble HTML-filer til Canvas page IDs
- Støtter deploy fra lokale filer via `make deploy-from-local`
- Støtter deploy fra GitHub html-pages branch via `make deploy-from-github`
- Støtter dry-run mode for å teste uten å gjøre endringer

Se dokumentasjonen for:
- Oppsett av API-nøkkel
- Generering av page ID mapping
- Vanlige workflows og kommandoer
- Troubleshooting og beste praksis  


## Caveat
Dersom man gjør manuelle endringer i Siden på Canvas vil ikke denne endringen eksistere på github. 
Det beste er derfor alltid å gjøre endringen i github, og følge prosessen som forklart her.

**Ved tidspress og behov for direkte endring i Canvas - noter endringene og foreta de ved et senere tidspunkt også i github.**


## Tekstinnholdet opprinnelig generert av Claude Code
Jeg har brukt følgende prompt for å generere start-innhold med Claude Code:

Populate the source/episodes folder with the content that I want. This is an AI introduction course for administrativ staffat the University of Oslo. The course is in Norwegian. It should be a course that the participants go through digitally by themselves, and should take no more than 45 minutes. The topics I want to cover are:

1. What is AI and what is generative AI - what are language models
2. LLMs are not a knowledge source, but construct contents/sentences based on what is statistically most probable with some added randomness
3. Can you trust what comes out of generative AI? Quality control, understand the contents
4. What AI services do we have at UiO https://www.uio.no/tjenester/it/ki/
5. Try prompting and simple prompt engineering
6. Other things you think are essential in an intro course in AI tools for administrative staff at UiO.



---


