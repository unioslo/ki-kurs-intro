"""
Generate synthetic survey data for AI course evaluation.
Pre-course and post-course measurements for 100 participants.
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of participants
N = 100

# Generate participant IDs
participant_ids = [f"P{i:03d}" for i in range(1, N+1)]

# Question 1: Understanding of AI concepts (1-5)
# Pre-course: Lower scores, Post-course: Significant improvement
pre_q1 = np.random.choice([1, 2, 3, 4, 5], N, p=[0.15, 0.40, 0.30, 0.12, 0.03])
post_q1 = np.clip(pre_q1 + np.random.choice([1, 2, 3], N, p=[0.2, 0.5, 0.3]), 1, 5)

# Question 2: Comfort with AI tools (1-5)
# Pre-course: Lower scores, Post-course: Good improvement
pre_q2 = np.random.choice([1, 2, 3, 4, 5], N, p=[0.10, 0.35, 0.35, 0.15, 0.05])
post_q2 = np.clip(pre_q2 + np.random.choice([1, 2, 3], N, p=[0.3, 0.5, 0.2]), 1, 5)

# Question 3: Frequency of AI tool usage (1-5)
# Pre-course: Low usage, Post-course: Moderate increase
pre_q3 = np.random.choice([1, 2, 3, 4, 5], N, p=[0.30, 0.35, 0.20, 0.10, 0.05])
post_q3 = np.clip(pre_q3 + np.random.choice([0, 1, 2], N, p=[0.4, 0.4, 0.2]), 1, 5)

# Question 4: Perceptions of AI (multi-select A-F)
def generate_q4_responses(is_post_course=False):
    responses = []
    for _ in range(N):
        if is_post_course:
            # Post-course: More see efficiency, fewer feel they lack skills
            choices = []
            if random.random() < 0.75:  # A - Will make work more efficient
                choices.append('A')
            if random.random() < 0.20:  # B - Relevant but lack skills (decreased)
                choices.append('B')
            if random.random() < 0.35:  # C - Privacy/ethics concerns
                choices.append('C')
            if random.random() < 0.25:  # D - Lack tools (some improvement)
                choices.append('D')
            if random.random() < 0.05:  # E - Not relevant
                choices.append('E')
        else:
            # Pre-course: More uncertainty and skill gaps
            choices = []
            if random.random() < 0.45:  # A - Will make work more efficient
                choices.append('A')
            if random.random() < 0.55:  # B - Relevant but lack skills
                choices.append('B')
            if random.random() < 0.40:  # C - Privacy/ethics concerns
                choices.append('C')
            if random.random() < 0.35:  # D - Lack tools
                choices.append('D')
            if random.random() < 0.15:  # E - Not relevant
                choices.append('E')

        # Ensure at least one choice, max 3
        if not choices:
            choices = [random.choice(['A', 'B', 'C'])]
        responses.append(','.join(sorted(choices[:3])))
    return responses

pre_q4 = generate_q4_responses(is_post_course=False)
post_q4 = generate_q4_responses(is_post_course=True)

# Question 5: Comfort with ethics/privacy (1-5)
# Pre-course: Lower, Post-course: Significant improvement
pre_q5 = np.random.choice([1, 2, 3, 4, 5], N, p=[0.18, 0.35, 0.30, 0.13, 0.04])
post_q5 = np.clip(pre_q5 + np.random.choice([1, 2, 3], N, p=[0.25, 0.50, 0.25]), 1, 5)

# Question 6: Desired training topics (multi-select A-F)
# Only in pre-course survey
def generate_q6_responses():
    responses = []
    for _ in range(N):
        choices = []
        if random.random() < 0.70:  # A - Basic AI concepts
            choices.append('A')
        if random.random() < 0.65:  # B - Practical use
            choices.append('B')
        if random.random() < 0.55:  # C - Privacy and security
            choices.append('C')
        if random.random() < 0.45:  # D - Ethics
            choices.append('D')
        if random.random() < 0.60:  # E - Quality assessment
            choices.append('E')
        if random.random() < 0.30:  # F - Governance aspects
            choices.append('F')

        if not choices:
            choices = ['A', 'B']
        responses.append(','.join(sorted(choices)))
    return responses

pre_q6 = generate_q6_responses()

# Question 7: Systems they work in
systems_list = [
    "SAP", "Workday", "Sharepoint", "Canvas",
    "Outlook", "Teams", "Salesforce", "ServiceNow",
    "Oracle", "Cristin", "FS (Felles Studentsystem)",
    "Power BI", "Excel", "BOTT (Bestilling og tidtaking)",
    "Agresso/Unit4", "Cerebrum", "Ephorte",
    "Planleggingsverktøy", "CRM-system", "HR-system"
]

def generate_systems():
    responses = []
    for _ in range(N):
        num_systems = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.30, 0.30, 0.20, 0.05])[0]
        selected = random.sample(systems_list, num_systems)
        responses.append(', '.join(selected))
    return responses

systems = generate_systems()

# Question 8: Areas where AI could help (open text)
pre_q8_responses = [
    "Automatisering av repeterende oppgaver",
    "Saksbehandling - raskere prosessering",
    "Rapportskriving og dokumentasjon",
    "E-postbehandling og svar på vanlige spørsmål",
    "Møtereferat og oppsummeringer",
    "Ikke sikker",
    "Dataanalyse og rapportering",
    "Planlegging og koordinering av aktiviteter",
    "Tekstforbedring og korrektur",
    "Søk i dokumenter og regelverk",
    "Oversettelse av tekster",
    "Kvalitetssikring av data",
    "Forbedring av intern kommunikasjon",
    "Studenthenvendelser - chatbot",
    "Budsjettanalyse og prognoser",
    "Personalhåndtering og rekruttering",
    "Kursplanlegging",
    "Timeplanlegging",
    "Arkivering og kategorisering",
    "Opplæring og kunnskapsdeling",
]

post_q8_responses = [
    "Bruke ChatGPT til å skrive utkast til e-poster og møtereferater",
    "Automatisk kategorisering av innkommende henvendelser med språkmodeller",
    "Oppsummere lange dokumenter og rapporter med KI-verktøy",
    "Lage FAQ-bot for repeterende spørsmål fra studenter",
    "Dataanalyse med KI for å identifisere mønstre i studentdata",
    "Kvalitetssikring av tekster ved hjelp av generativ KI",
    "Generere utkast til prosedyrer og veiledninger",
    "Oversette dokumenter mellom norsk og engelsk med KI-støtte",
    "Chatbot for førstelinje support til ansatte",
    "Automatisk tagging og kategorisering av dokumenter i arkivet",
    "Prediktiv analyse for ressursplanlegging",
    "KI-assistert tekstforbedring i Outlook",
    "Generere rapportutkast fra strukturerte data",
    "Prompt-basert søk i interne kunnskapsbaser",
    "AI-støttet prosjektplanlegging",
    "Automatisering av datainnsamling og rapportering",
    "KI til å forberede møtedokumenter basert på tidligere møter",
    "Generativ KI for å lage maler og standardtekster",
    "Sentiment-analyse av tilbakemeldinger",
    "KI-basert prioritering av arbeidsoppgaver",
]

# Randomly assign responses
pre_q8 = [random.choice(pre_q8_responses) for _ in range(N)]
post_q8 = [random.choice(post_q8_responses) for _ in range(N)]

# Create DataFrames
pre_survey = pd.DataFrame({
    'participant_id': participant_ids,
    'survey_type': 'pre',
    'q1_understanding_ai': pre_q1,
    'q2_comfort_ai_tools': pre_q2,
    'q3_frequency_usage': pre_q3,
    'q4_perceptions': pre_q4,
    'q5_ethics_comfort': pre_q5,
    'q6_training_topics': pre_q6,
    'q7_systems': systems,
    'q8_ai_help_areas': pre_q8
})

post_survey = pd.DataFrame({
    'participant_id': participant_ids,
    'survey_type': 'post',
    'q1_understanding_ai': post_q1,
    'q2_comfort_ai_tools': post_q2,
    'q3_frequency_usage': post_q3,
    'q4_perceptions': post_q4,
    'q5_ethics_comfort': post_q5,
    'q6_training_topics': ['N/A'] * N,  # Not asked in post-survey
    'q7_systems': systems,  # Same systems
    'q8_ai_help_areas': post_q8
})

# Combine and save
all_data = pd.concat([pre_survey, post_survey], ignore_index=True)

# Save to CSV
pre_survey.to_csv('survey-data/pre_course_survey.csv', index=False, encoding='utf-8')
post_survey.to_csv('survey-data/post_course_survey.csv', index=False, encoding='utf-8')
all_data.to_csv('survey-data/combined_survey_data.csv', index=False, encoding='utf-8')

print("✓ Survey data generated successfully!")
print(f"  - Pre-course survey: {len(pre_survey)} responses")
print(f"  - Post-course survey: {len(post_survey)} responses")
print(f"  - Combined data: {len(all_data)} responses")
print("\nFiles created:")
print("  - survey-data/pre_course_survey.csv")
print("  - survey-data/post_course_survey.csv")
print("  - survey-data/combined_survey_data.csv")

# Print summary statistics
print("\n=== SUMMARY STATISTICS ===")
print("\nQ1 - Understanding of AI (1-5):")
print(f"  Pre-course:  Mean={pre_q1.mean():.2f}, Median={np.median(pre_q1):.0f}")
print(f"  Post-course: Mean={post_q1.mean():.2f}, Median={np.median(post_q1):.0f}")
print(f"  Improvement: +{(post_q1.mean() - pre_q1.mean()):.2f}")

print("\nQ2 - Comfort with AI tools (1-5):")
print(f"  Pre-course:  Mean={pre_q2.mean():.2f}, Median={np.median(pre_q2):.0f}")
print(f"  Post-course: Mean={post_q2.mean():.2f}, Median={np.median(post_q2):.0f}")
print(f"  Improvement: +{(post_q2.mean() - pre_q2.mean()):.2f}")

print("\nQ3 - Frequency of usage (1-5):")
print(f"  Pre-course:  Mean={pre_q3.mean():.2f}, Median={np.median(pre_q3):.0f}")
print(f"  Post-course: Mean={post_q3.mean():.2f}, Median={np.median(post_q3):.0f}")
print(f"  Improvement: +{(post_q3.mean() - pre_q3.mean()):.2f}")

print("\nQ5 - Ethics comfort (1-5):")
print(f"  Pre-course:  Mean={pre_q5.mean():.2f}, Median={np.median(pre_q5):.0f}")
print(f"  Post-course: Mean={post_q5.mean():.2f}, Median={np.median(post_q5):.0f}")
print(f"  Improvement: +{(post_q5.mean() - pre_q5.mean()):.2f}")
