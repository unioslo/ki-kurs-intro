"""
Create visualizations showing pre-course vs post-course improvements.
Simple version using only matplotlib (no seaborn dependency).
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Set style
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 10

# Load data
pre_df = pd.read_csv('survey-data/pre_course_survey.csv')
post_df = pd.read_csv('survey-data/post_course_survey.csv')

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(4, 3, hspace=0.3, wspace=0.3)

# Color scheme
color_pre = '#ff6b6b'
color_post = '#4ecdc4'

# === Plot 1: Q1 - Understanding of AI ===
ax1 = fig.add_subplot(gs[0, 0])
q1_pre = pre_df['q1_understanding_ai'].value_counts().sort_index()
q1_post = post_df['q1_understanding_ai'].value_counts().sort_index()

x = np.arange(1, 6)
width = 0.35

ax1.bar(x - width/2, [q1_pre.get(i, 0) for i in range(1, 6)], width,
        label='Pre-kurs', color=color_pre, alpha=0.8)
ax1.bar(x + width/2, [q1_post.get(i, 0) for i in range(1, 6)], width,
        label='Post-kurs', color=color_post, alpha=0.8)

ax1.set_xlabel('Nivå (1=Ingen kunnskap, 5=Svært godt)')
ax1.set_ylabel('Antall respondenter')
ax1.set_title('Q1: Forståelse av AI-begreper', fontweight='bold')
ax1.set_xticks(x)
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Add mean annotation
ax1.text(0.02, 0.98, f'Pre: {pre_df["q1_understanding_ai"].mean():.2f}\nPost: {post_df["q1_understanding_ai"].mean():.2f}',
         transform=ax1.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# === Plot 2: Q2 - Comfort with AI tools ===
ax2 = fig.add_subplot(gs[0, 1])
q2_pre = pre_df['q2_comfort_ai_tools'].value_counts().sort_index()
q2_post = post_df['q2_comfort_ai_tools'].value_counts().sort_index()

ax2.bar(x - width/2, [q2_pre.get(i, 0) for i in range(1, 6)], width,
        label='Pre-kurs', color=color_pre, alpha=0.8)
ax2.bar(x + width/2, [q2_post.get(i, 0) for i in range(1, 6)], width,
        label='Post-kurs', color=color_post, alpha=0.8)

ax2.set_xlabel('Nivå (1=Ikke komfortabel, 5=Meget komfortabel)')
ax2.set_ylabel('Antall respondenter')
ax2.set_title('Q2: Komfort med AI-verktøy', fontweight='bold')
ax2.set_xticks(x)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

ax2.text(0.02, 0.98, f'Pre: {pre_df["q2_comfort_ai_tools"].mean():.2f}\nPost: {post_df["q2_comfort_ai_tools"].mean():.2f}',
         transform=ax2.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# === Plot 3: Q3 - Frequency of usage ===
ax3 = fig.add_subplot(gs[0, 2])
q3_pre = pre_df['q3_frequency_usage'].value_counts().sort_index()
q3_post = post_df['q3_frequency_usage'].value_counts().sort_index()

ax3.bar(x - width/2, [q3_pre.get(i, 0) for i in range(1, 6)], width,
        label='Pre-kurs', color=color_pre, alpha=0.8)
ax3.bar(x + width/2, [q3_post.get(i, 0) for i in range(1, 6)], width,
        label='Post-kurs', color=color_post, alpha=0.8)

ax3.set_xlabel('Frekvens (1=Aldri, 5=Daglig)')
ax3.set_ylabel('Antall respondenter')
ax3.set_title('Q3: Hyppighet av AI-bruk', fontweight='bold')
ax3.set_xticks(x)
ax3.legend()
ax3.grid(axis='y', alpha=0.3)

ax3.text(0.02, 0.98, f'Pre: {pre_df["q3_frequency_usage"].mean():.2f}\nPost: {post_df["q3_frequency_usage"].mean():.2f}',
         transform=ax3.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# === Plot 4: Q5 - Ethics comfort ===
ax4 = fig.add_subplot(gs[1, 0])
q5_pre = pre_df['q5_ethics_comfort'].value_counts().sort_index()
q5_post = post_df['q5_ethics_comfort'].value_counts().sort_index()

ax4.bar(x - width/2, [q5_pre.get(i, 0) for i in range(1, 6)], width,
        label='Pre-kurs', color=color_pre, alpha=0.8)
ax4.bar(x + width/2, [q5_post.get(i, 0) for i in range(1, 6)], width,
        label='Post-kurs', color=color_post, alpha=0.8)

ax4.set_xlabel('Enighet (1=Helt uenig, 5=Helt enig)')
ax4.set_ylabel('Antall respondenter')
ax4.set_title('Q5: Komfort med etikk/personvern', fontweight='bold')
ax4.set_xticks(x)
ax4.legend()
ax4.grid(axis='y', alpha=0.3)

ax4.text(0.02, 0.98, f'Pre: {pre_df["q5_ethics_comfort"].mean():.2f}\nPost: {post_df["q5_ethics_comfort"].mean():.2f}',
         transform=ax4.transAxes, fontsize=9, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# === Plot 5: Q4 Perceptions - Pre-course ===
ax5 = fig.add_subplot(gs[1, 1])

# Count perception options
def count_perceptions(series):
    all_options = []
    for responses in series:
        all_options.extend(responses.split(','))
    return Counter(all_options)

pre_perceptions = count_perceptions(pre_df['q4_perceptions'])
labels = ['A: Mer\neffektivt', 'B: Mangler\nferdigheter', 'C: Personvern\nbekymring',
          'D: Mangler\nverktøy', 'E: Ikke\nrelevant']
values_pre = [pre_perceptions.get(letter, 0) for letter in ['A', 'B', 'C', 'D', 'E']]

ax5.barh(labels, values_pre, color=color_pre, alpha=0.8)
ax5.set_xlabel('Antall respondenter')
ax5.set_title('Q4: Oppfatning av AI (Pre-kurs)', fontweight='bold')
ax5.grid(axis='x', alpha=0.3)

# === Plot 6: Q4 Perceptions - Post-course ===
ax6 = fig.add_subplot(gs[1, 2])

post_perceptions = count_perceptions(post_df['q4_perceptions'])
values_post = [post_perceptions.get(letter, 0) for letter in ['A', 'B', 'C', 'D', 'E']]

ax6.barh(labels, values_post, color=color_post, alpha=0.8)
ax6.set_xlabel('Antall respondenter')
ax6.set_title('Q4: Oppfatning av AI (Post-kurs)', fontweight='bold')
ax6.grid(axis='x', alpha=0.3)

# === Plot 7: Mean improvements comparison ===
ax7 = fig.add_subplot(gs[2, :])

questions = ['Q1:\nForståelse', 'Q2:\nKomfort', 'Q3:\nHyppighet', 'Q5:\nEtikk']
pre_means = [
    pre_df['q1_understanding_ai'].mean(),
    pre_df['q2_comfort_ai_tools'].mean(),
    pre_df['q3_frequency_usage'].mean(),
    pre_df['q5_ethics_comfort'].mean()
]
post_means = [
    post_df['q1_understanding_ai'].mean(),
    post_df['q2_comfort_ai_tools'].mean(),
    post_df['q3_frequency_usage'].mean(),
    post_df['q5_ethics_comfort'].mean()
]
improvements = [post - pre for post, pre in zip(post_means, pre_means)]

x_pos = np.arange(len(questions))
width = 0.35

bars1 = ax7.bar(x_pos - width/2, pre_means, width, label='Pre-kurs',
                color=color_pre, alpha=0.8)
bars2 = ax7.bar(x_pos + width/2, post_means, width, label='Post-kurs',
                color=color_post, alpha=0.8)

# Add improvement labels
for i, (pre, post, imp) in enumerate(zip(pre_means, post_means, improvements)):
    ax7.text(i, max(pre, post) + 0.15, f'+{imp:.2f}', ha='center',
             fontweight='bold', fontsize=10, color='green')

ax7.set_ylabel('Gjennomsnittlig score (1-5)')
ax7.set_title('Sammenligning av gjennomsnittlig forbedring', fontweight='bold', fontsize=14)
ax7.set_xticks(x_pos)
ax7.set_xticklabels(questions)
ax7.legend()
ax7.set_ylim(0, 5.5)
ax7.axhline(y=3, color='gray', linestyle='--', alpha=0.3)
ax7.grid(axis='y', alpha=0.3)

# === Plot 8: Distribution of improvements per participant ===
ax8 = fig.add_subplot(gs[3, 0:2])

# Calculate individual improvements
individual_improvements = []
for i in range(len(pre_df)):
    avg_pre = (pre_df.iloc[i]['q1_understanding_ai'] +
               pre_df.iloc[i]['q2_comfort_ai_tools'] +
               pre_df.iloc[i]['q5_ethics_comfort']) / 3
    avg_post = (post_df.iloc[i]['q1_understanding_ai'] +
                post_df.iloc[i]['q2_comfort_ai_tools'] +
                post_df.iloc[i]['q5_ethics_comfort']) / 3
    individual_improvements.append(avg_post - avg_pre)

ax8.hist(individual_improvements, bins=15, color='#51cf66', alpha=0.7, edgecolor='black')
ax8.axvline(x=np.mean(individual_improvements), color='red', linestyle='--',
            linewidth=2, label=f'Gjennomsnitt: +{np.mean(individual_improvements):.2f}')
ax8.set_xlabel('Forbedring i gjennomsnittlig score')
ax8.set_ylabel('Antall deltakere')
ax8.set_title('Fordeling av individuelle forbedringer', fontweight='bold')
ax8.legend()
ax8.grid(axis='y', alpha=0.3)

# === Plot 9: Training topics requested (Q6) ===
ax9 = fig.add_subplot(gs[3, 2])

training_topics = count_perceptions(pre_df['q6_training_topics'])
topic_labels = ['A: Grunnleg.\nbegreper', 'B: Praktisk\nbruk', 'C: Personvern',
                'D: Etikk', 'E: Kvalitets-\nvurdering', 'F: Forvaltning']
topic_values = [training_topics.get(letter, 0) for letter in ['A', 'B', 'C', 'D', 'E', 'F']]

ax9.barh(topic_labels, topic_values, color='#7950f2', alpha=0.8)
ax9.set_xlabel('Antall respondenter')
ax9.set_title('Q6: Ønskede opplæringstemaer', fontweight='bold')
ax9.grid(axis='x', alpha=0.3)

# Add main title
fig.suptitle('Evaluering av Grunnkurs i generativ KI - Før og etter analyse (N=100)',
             fontsize=16, fontweight='bold', y=0.995)

# Save figure
plt.savefig('survey-data/survey_results.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved: survey-data/survey_results.png")

# === Create individual plot for Understanding improvement ===

fig1, ax = plt.subplots(figsize=(10, 6))
x = np.arange(1, 6)
width = 0.35
q1_pre = pre_df['q1_understanding_ai'].value_counts().sort_index()
q1_post = post_df['q1_understanding_ai'].value_counts().sort_index()

ax.bar(x - width/2, [q1_pre.get(i, 0) for i in range(1, 6)], width,
       label='Pre-kurs', color=color_pre, alpha=0.8)
ax.bar(x + width/2, [q1_post.get(i, 0) for i in range(1, 6)], width,
       label='Post-kurs', color=color_post, alpha=0.8)

ax.set_xlabel('Nivå (1=Ingen kunnskap, 5=Svært godt)', fontsize=12)
ax.set_ylabel('Antall respondenter', fontsize=12)
ax.set_title('Forståelse av AI-begreper - Før og etter kurs', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)

# Add statistics box
textstr = f'Pre-kurs gjennomsnitt: {pre_df["q1_understanding_ai"].mean():.2f}\n'
textstr += f'Post-kurs gjennomsnitt: {post_df["q1_understanding_ai"].mean():.2f}\n'
textstr += f'Forbedring: +{(post_df["q1_understanding_ai"].mean() - pre_df["q1_understanding_ai"].mean()):.2f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('survey-data/q1_understanding_improvement.png', dpi=300, bbox_inches='tight')
print("✓ Individual plot saved: survey-data/q1_understanding_improvement.png")
plt.close()

print("\n✓ All visualizations created successfully!")
print("\nGenerated files:")
print("  - survey-data/survey_results.png (main dashboard)")
print("  - survey-data/q1_understanding_improvement.png")
