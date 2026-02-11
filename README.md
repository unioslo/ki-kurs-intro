# ki-kurs-intro

## test - web edits - does it need signed commits, or is this considered signed?
New test after added signing in settings

Alt innhold er KI-generert. Innholdet er foreløpig kun for å ha noe relevant innhold for å få på plass automatiseringen av html genereringen. 

Kurssidene bygges automatisk og kan sees her: https://unioslo.github.io/ki-kurs-intro
OBS: Funksjonaliteten er laget for canvas for å laste opp html i _build som "Sider" i canvas. Kildekoden bruker mye av canvas sine innebygde [Designelementer](https://www.uio.no/for-ansatte/arbeidsstotte/sta/canvas/veiledninger/utnytt-mulighetene/designelementer.html) Dette ser ikke bra ut i https://unioslo.github.io/ki-kurs-intro som forventer sphinx tema. 


### Hvordan bruke i Canvas

Innholdet bygges automatisk med Actions - se konfigurasjon i ```.gitlab/workflows/static_pages.yml```. Html filene finner du i Actions artifacts. Gå inn på siste Action og klikk på den. Du ser artifacts neders, som du kan laste ned. 

<img width="500"  alt="Screenshot 2026-02-02 at 18 35 59" src="https://github.com/user-attachments/assets/03fa8c0f-7318-44fc-99e8-6cc18ee4c9c5" />

Html filene finner du i:  ```artifact/episodes``` når du har unzippet den nedlastede artifacts zip fila. 

Da må du manuelt åpne hver fil, og copy-paste innholdet til Canvas. 

1. Lage en ny side og gi den en tittel - f.eks. samme tittel som `<h1>` elemented i html-en du skal kopiere inn
2. Klikk på `<``>`iconet for å laste inn rå html.
3. Copy html fra artifacts, paste inn i Siden
4. Lagre
5. Legg til Siden i en Modul. 

### Tekstinnholdet
Brukt følgende prompt for å generere innhold med Claude Code: 

Populate the source/episodes folder with the content that I want. This is an AI introduction course for administrativ staffat the University of Oslo. The course is in Norwegian. It should be a course that the participants go through digitally by themselves, and should take no more than 45 minutes. The topics I want to cover are: 

1. What is AI and what is generative AI - what are language models
2. LLMs are not a knowledge source, but construct contents/sentences based on what is statistically most probable with some added randomness
3. Can you trust what comes out of generative AI? Quality control, understand the contents
4. What AI services do we have at UiO https://www.uio.no/tjenester/it/ki/
5. Try prompting and simple prompt engineering
6. Other things you think are essential in an intro course in AI tools for administrative staff at UiO.  
