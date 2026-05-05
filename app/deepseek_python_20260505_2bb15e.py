import matplotlib.pyplot as plt
import numpy as np

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# Cumulative returns (starting from 100% or 0%)
hybrid_ai_cumulative = [2.1, 11.5, 26.7, 23.5, 47.6, 61.9, 80.6, 96.2]
sp500_cumulative = [1.4, 13.4, 35.2, 30.8, 62.3, 82.7, 108.4, 90.3]
portfolio_60_40_cumulative = [0.9, 9.2, 23.1, 18.9, 41.2, 52.9, 67.4, 69.4]
rule_only_cumulative = [1.2, 9.0, 22.1, 17.9, 38.1, 47.9, 62.3, 51.3]

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))

# Plot lines
ax.plot(years, hybrid_ai_cumulative, 'g-', linewidth=2.5, marker='o', markersize=8, label='Hybrid AI (Final: 96.2%)')
ax.plot(years, sp500_cumulative, 'b-', linewidth=2.5, marker='^', markersize=8, label='S&P 500 (Final: 90.3%)')
ax.plot(years, portfolio_60_40_cumulative, 'orange', linewidth=2.5, marker='s', markersize=8, label='60/40 Portfolio (Final: 69.4%)')
ax.plot(years, rule_only_cumulative, 'r-', linewidth=2.5, marker='d', markersize=8, label='Rule-Only (Final: 51.3%)')

# Labels and title
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Cumulative Return (%)', fontsize=14, fontweight='bold')
ax.set_title('Figure 4.15: Backtest Performance Comparison (2015–2022)', fontsize=16, fontweight='bold')

# Set axes
ax.set_xticks(years)
ax.set_xticklabels(years)
ax.set_ylim(0, 120)
ax.set_xlim(2014.5, 2022.5)
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax.axvline(x=2020, color='gray', linestyle='--', alpha=0.7, label='COVID-19 Crash')

# Add grid
ax.grid(True, alpha=0.3, linestyle='--')

# Add legend
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

# Annotate COVID-19 drawdown
ax.annotate('COVID-19 Market Crash\nMax Drawdown:\nAI: -23% | S&P: -34%',
            xy=(2020, 50), xytext=(2020.5, 30),
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
            fontsize=9, ha='center')

# Add final value annotations
ax.annotate('96.2%', xy=(2022, 96.2), xytext=(2022.3, 96.2), fontsize=9, fontweight='bold', color='green')
ax.annotate('90.3%', xy=(2022, 90.3), xytext=(2022.3, 90.3), fontsize=9, fontweight='bold', color='blue')
ax.annotate('69.4%', xy=(2022, 69.4), xytext=(2022.3, 69.4), fontsize=9, color='orange')
ax.annotate('51.3%', xy=(2022, 51.3), xytext=(2022.3, 51.3), fontsize=9, color='red')

plt.tight_layout()
plt.savefig('figure-4.15-backtest-performance.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

# Print summary statistics
print("\n" + "="*50)
print("BACKTEST SUMMARY STATISTICS (2015-2022)")
print("="*50)
print(f"{'Strategy':<20} {'Final Return':<15} {'Sharpe Ratio':<15} {'Max Drawdown':<15}")
print("-"*65)
print(f"{'Hybrid AI':<20} {96.2:>11.1f}%     {0.72:>11.2f}     {23:>11}%")
print(f"{'S&P 500':<20} {90.3:>11.1f}%     {0.58:>11.2f}     {34:>11}%")
print(f"{'60/40 Portfolio':<20} {69.4:>11.1f}%     {0.64:>11.2f}     {28:>11}%")
print(f"{'Rule-Only':<20} {51.3:>11.1f}%     {0.61:>11.2f}     {26:>11}%")
print("="*50)