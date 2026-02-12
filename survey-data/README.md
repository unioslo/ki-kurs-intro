# Survey Data - Grunnkurs i generativ KI

This folder contains synthetic survey data for evaluating the effectiveness of the AI introduction course.

## Overview

- **100 participants**
- **Pre-course and post-course measurements**
- **8 questions covering knowledge, attitudes, and usage**

## Survey Questions

### Q1: Forståelse av AI-begreper (1-5)
*Hvor godt vil du si at du forstår grunnleggende begreper innen kunstig intelligens?*
- 1 = Ingen kunnskap
- 2 = Litt
- 3 = Moderat
- 4 = Godt
- 5 = Svært godt

### Q2: Komfort med AI-verktøy (1-5)
*Hvor komfortabel er du med å ta i bruk KI-verktøy i ditt daglige arbeid?*
- 1 = Ikke komfortabel i det hele tatt
- 2 = Litt ubehagelig
- 3 = Nøytral
- 4 = Ganske komfortabel
- 5 = Meget komfortabel

### Q3: Hyppighet av AI-bruk (1-5)
*Hvor ofte bruker du KI-baserte verktøy eller funksjoner i arbeidet ditt i dag?*
- 1 = Aldri
- 2 = Sjeldent (mindre enn månedlig)
- 3 = Noen ganger (månedlig)
- 4 = Ofte (ukentlig)
- 5 = Daglig

### Q4: Oppfatning av AI (flervalg A-E)
*Hvilke av disse beskriver best din oppfatning av KI i dine arbeidsoppgaver i dag? Velg opptil 3.*
- A) Vil gjøre arbeidet mer effektivt
- B) Er relevant, men jeg mangler ferdigheter
- C) Skaper bekymring rundt personvern/etikk
- D) Ville være nyttig, men vi mangler verktøy/infrastruktur
- E) Ikke relevant for min rolle

### Q5: Komfort med etikk/personvern (1-5)
*I hvilken grad er du enig i påstanden: «Jeg føler meg komfortabel med å vurdere etiske og personvernsrelaterte problemstillinger knyttet til bruk av KI i mitt arbeid.»*
- 1 = Helt uenig
- 2 = Uenig
- 3 = Verken/eller
- 4 = Enig
- 5 = Helt enig

### Q6: Ønskede opplæringstemaer (flervalg A-F, kun pre-kurs)
*Hvilke temaer ønsker du opplæring i?*
- A) Grunnleggende KI-begreper
- B) Praktisk bruk av KI-verktøy i administrative prosesser
- C) Personvern og datasikkerhet ved KI-bruk
- D) Etikk og samfunnsmessige konsekvenser
- E) Hvordan vurdere kvalitet og troverdighet i KI-generert innhold
- F) Forvaltningsaspekter

### Q7: Systemer du jobber i (fritekst)
*Hvilke systemer jobber du i?*

### Q8: Områder hvor AI kan hjelpe (fritekst)
*Er det noen områder i din arbeidshverdag du tror at KI kunne hjulpet deg å gjøre jobben bedre og/eller mer effektivt?*

## Files

### Data Files
- `pre_course_survey.csv` - Pre-course survey responses (100 participants)
- `post_course_survey.csv` - Post-course survey responses (same 100 participants)
- `combined_survey_data.csv` - Combined pre and post data

### Scripts
- `generate_survey_data.py` - Generate synthetic survey data
- `visualize_results.py` - Create visualizations comparing pre/post results

### Output
- `survey_results.png` - Main dashboard with all comparisons
- `q1_understanding_improvement.png` - Detailed view of knowledge improvement
- `q4_perceptions_comparison.png` - Perception changes

## Usage

### 1. Generate Survey Data
```bash
python3 survey-data/generate_survey_data.py
```

This will create:
- Pre-course survey data showing lower AI knowledge and comfort
- Post-course survey data showing improvements after taking the course
- Summary statistics printed to console

### 2. Create Visualizations
```bash
python3 survey-data/visualize_results.py
```

This requires matplotlib, seaborn, pandas, and numpy:
```bash
pip install matplotlib seaborn pandas numpy
```

The script generates:
- Comprehensive dashboard showing all metrics
- Individual comparison plots
- Statistical analysis

## Key Findings (Synthetic Data)

### Expected Improvements
Based on the synthetic data generation:

**Q1 - Understanding of AI concepts:**
- Pre-course average: ~2.2/5
- Post-course average: ~3.8/5
- **Improvement: +1.6 points**

**Q2 - Comfort with AI tools:**
- Pre-course average: ~2.6/5
- Post-course average: ~3.9/5
- **Improvement: +1.3 points**

**Q3 - Frequency of usage:**
- Pre-course average: ~2.1/5
- Post-course average: ~2.7/5
- **Improvement: +0.6 points**

**Q5 - Ethics comfort:**
- Pre-course average: ~2.4/5
- Post-course average: ~3.7/5
- **Improvement: +1.3 points**

**Q4 - Perceptions:**
- "Will make work more efficient" (A): 45% → 75%
- "Lack skills" (B): 55% → 20% ✓ Major reduction
- Privacy concerns remain similar (healthy critical thinking)

**Q8 - Quality of responses:**
- Pre-course: Vague, general ideas
- Post-course: Specific, actionable plans with concrete tools

## Data Characteristics

The synthetic data is designed to reflect realistic learning outcomes:

1. **Knowledge gains**: Significant improvement in understanding basic concepts
2. **Confidence boost**: Increased comfort with using AI tools
3. **Skill gap reduction**: Fewer people feel they lack necessary skills
4. **Practical awareness**: More specific and actionable ideas for AI application
5. **Modest usage increase**: Usage frequency improves but not dramatically (realistic for short-term)
6. **Maintained critical thinking**: Privacy/ethics concerns remain (positive - shows awareness)

## Notes

- This is **synthetic data** generated for demonstration purposes
- Real survey data would show more variation and nuance
- The data is designed to show realistic, achievable learning outcomes
- Participant IDs (P001-P100) are consistent across pre/post surveys for paired analysis
