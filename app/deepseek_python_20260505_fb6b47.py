import matplotlib.pyplot as plt
import numpy as np

# Data
scenarios = ['Retirement\nPlanning', 'College\nSavings', 'Tax\nOptimization', 'Risk\nManagement', 'Estate\nPlanning']
ai_scores = [4.3, 4.5, 4.2, 4.4, 4.1]
human_scores = [4.7, 4.9, 4.5, 4.8, 4.6]

# Error margins (standard deviations)
ai_errors = [0.4, 0.3, 0.5, 0.4, 0.5]
human_errors = [0.3, 0.2, 0.4, 0.3, 0.4]

x = np.arange(len(scenarios))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 7))

# Create bars
bars1 = ax.bar(x - width/2, ai_scores, width, label='AI Advisor', 
               color='#64b5f6', edgecolor='#1565c0', linewidth=1.5, 
               yerr=ai_errors, capsize=5, error_kw={'elinewidth': 1.5, 'ecolor': '#333'})

bars2 = ax.bar(x + width/2, human_scores, width, label='Human Advisor', 
               color='#1565c0', edgecolor='#0d47a1', linewidth=1.5,
               yerr=human_errors, capsize=5, error_kw={'elinewidth': 1.5, 'ecolor': '#333'})

# Labels and title
ax.set_ylabel('Average Rating (1-5)', fontsize=12, fontweight='bold')
ax.set_xlabel('Financial Scenario', fontsize=12, fontweight='bold')
ax.set_title('Figure 5.1: Comparison of AI vs. Human Advisor Recommendations\n(5-point scale: 1=Poor, 3=Acceptable, 5=Excellent)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(scenarios, fontsize=10)
ax.set_ylim(0, 5.5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.grid(True, axis='y', alpha=0.3, linestyle='--')

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Legend
ax.legend(loc='upper left', fontsize=11, frameon=True, shadow=True)

# Add statistical significance annotations
significance_text = "All differences are statistically significant (p < 0.05)"
ax.text(0.5, -0.12, significance_text, transform=ax.transAxes, 
        ha='center', fontsize=10, style='italic', color='#555')

plt.tight_layout()
plt.savefig('figure-5.1-ai-vs-human.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()