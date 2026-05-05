library(ggplot2)
library(tidyr)

# Data
data <- data.frame(
  Year = c(2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022),
  Hybrid_AI = c(2.1, 11.5, 26.7, 23.5, 47.6, 61.9, 80.6, 96.2),
  SP500 = c(1.4, 13.4, 35.2, 30.8, 62.3, 82.7, 108.4, 90.3),
  Portfolio_60_40 = c(0.9, 9.2, 23.1, 18.9, 41.2, 52.9, 67.4, 69.4),
  Rule_Only = c(1.2, 9.0, 22.1, 17.9, 38.1, 47.9, 62.3, 51.3)
)

# Reshape for ggplot
data_long <- pivot_longer(data, cols = -Year, names_to = "Strategy", values_to = "Cumulative_Return")

# Plot
ggplot(data_long, aes(x = Year, y = Cumulative_Return, color = Strategy, shape = Strategy)) +
  geom_line(size = 1.2) +
  geom_point(size = 3) +
  scale_color_manual(values = c("Hybrid_AI" = "#4caf50", "SP500" = "#2196f3", 
                                "Portfolio_60_40" = "#ff9800", "Rule_Only" = "#f44336")) +
  scale_shape_manual(values = c("Hybrid_AI" = 16, "SP500" = 17, 
                                "Portfolio_60_40" = 15, "Rule_Only" = 18)) +
  labs(title = "Figure 4.15: Backtest Performance Comparison (2015–2022)",
       x = "Year", y = "Cumulative Return (%)") +
  theme_minimal() +
  theme(legend.position = "bottom") +
  geom_hline(yintercept = 0, linetype = "solid", color = "black") +
  geom_vline(xintercept = 2020, linetype = "dashed", color = "gray", alpha = 0.7)

ggsave("figure-4.15-backtest-performance.png", width = 10, height = 6, dpi = 300)