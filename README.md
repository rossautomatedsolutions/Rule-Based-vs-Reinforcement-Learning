# Rule-Based vs Reinforcement Learning: Which Strategy Performs Best on AAPL?

What happens when we put traditional rule-based trading head-to-head with machine learning?

we run a backtest comparison of **simple SMA strategies** vs **Reinforcement Learning (RL)-driven bots** using 2 years of daily AAPL stock data from Yahoo Finance.

---

## Strategies Compared

| Model # | Strategy Type       | Description                                   |
|---------|---------------------|-----------------------------------------------|
| **Model 0** | Rule-Based        | Buy when price > 10-day SMA, sell otherwise     |
| **Model 1** | RL                | SMA + Volume as state inputs                  |
| **Model 2** | RL                | SMA + Day of Week                             |
| **Model 3** | RL                | SMA + Volume + Day of Week                    |
| **Model 4** | RL                | SMA only (learns via Q-table)                 |
| **Model 5** | Rule-Based        | Buy if 3-day return < -3% (Mean Reversion)    |
| **Model 6** | RL                | Learns from 1d return, 3d return, volatility, RSI |

---

## Summary Results (Trading 1 Share Per Trade)

| Model | Total Return (%) | Sharpe | Max Drawdown (%) | Avg Daily Return (%) | # Trades |
|-------|------------------|--------|------------------|-----------------------|----------|
| Model0 (Rule SMA)             | **28.33**        | **0.2105** | -15.11           | 0.7455                | 76       |
| Model1 (RL)                   | -3.90            | -0.0122    | -47.93           | -0.0118               | 43       |
| Model2 (RL)                   | 11.80            | -0.0099    | -37.98           | -0.0069               | 36       |
| Model3 (RL)                   | 22.62            | 0.0128     | -31.66           | 0.0108                | 39       |
| Model4 (RL)                   | 7.91             | 0.0610     | -29.45           | 0.0657                | 16       |
| Model5 (Rule Mean Reversion) | -0.24            | -0.0045    | -20.21           | -0.0111               | 44       |
| Model6 (RL Mean Reversion)   | 5.22             | 0.0608     | **-2.28**        | 0.0107                | 16       |

---

## Key Takeaways

- **Model0 (SMA Rule)** still performs best in total return and Sharpe — simple and effective.
- **Model6 (RL Mean Reversion)** stands out with **lowest drawdown** and a consistent return profile.
- Not all RL models outperform rules. Some, like **Model1**, can overfit or perform erratically without good feature selection.
- Adding **Volume and Day of Week** improves certain RL models (Model3), but not always reliably.


---

## Final Thoughts

Reinforcement Learning has **potential**, but isn't guaranteed to outperform basic strategies — especially without tuning. However, with the right features and evaluation metrics (Sharpe, drawdown), it can lead to **more consistent and risk-aware bots**.

This comparison helps us better understand where traditional logic shines and where RL can provide an edge.
