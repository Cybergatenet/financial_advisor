import matplotlib.pyplot as plt
import numpy as np

# Data
scenarios = ['Retirement\nPlanning', 'College\nSavings', 'Debt\nManagement', 'Tax\nPlanning', 'Estate\nPlanning']
ai_scores = [4.3, 4.5, 4.2, 4.4, 4.7]
human_scores = [4.7, 4.9, 4.5, 4.8, 4.9]
ai_std = [0.4, 0.3, 0.5, 0.4, 0.3]
human_std = [0.3, 0.2, 0.4, 0.3, 0.2]

x = np.arange(len(scenarios))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, ai_scores, width, label='AI Advisor', color='#64b5f6', yerr=ai_std, capsize=5, error_kw={'linewidth': 1.5})
bars2 = ax.bar(x + width/2, human_scores, width, label='Human Advisor', color='#1565c0', yerr=human_std, capsize=5, error_kw={'linewidth': 1.5})

# Labels and title
ax.set_ylabel('Average Rating (1-5)', fontsize=12, fontweight='bold')
ax.set_xlabel('Financial Scenarios', fontsize=12, fontweight='bold')
ax.set_title('Figure 5.1: Comparison of AI vs. Human Advisor Recommendations\n(3 CFPs per scenario, error bars = ±1 SD)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.set_ylim(0, 5.5)
ax.legend(loc='upper left', fontsize=11)
ax.axhline(y=4.0, color='gray', linestyle='--', alpha=0.5, label='Good threshold')

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width()/2, height), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('figure-5.1-ai-vs-human.png', dpi=300, bbox_inches='tight')
plt.show()