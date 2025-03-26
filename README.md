# Rule-Based vs Reinforcement Learning: Backtesting Trading Strategies on Stocks

This repository contains the full source code, notebooks, and dashboard for a 3-part blog and video series comparing **rule-based trading strategies** to **Reinforcement Learning (RL)** models using historical stock data.

We start with a single stock (AAPL), scale up to all **S&P 500 tickers**, and build an interactive dashboard for exploring model performance across sectors.

---

## Project Overview

### Part I: Single Stock Comparison (AAPL)
- File: `Part I - Single Stock.ipynb`
- Backtests 5 trading models on AAPL using 2 years of daily data.
- Compares a simple rule-based SMA strategy against four RL models.
- Evaluates Total Return, Sharpe Ratio, Drawdown, Avg Daily Reward, and Trade Count.
- Provides a gentle introduction to Q-Learning.
- Demonstrates how model features influence RL outcomes.

Note: This notebook represents the foundation of the full analysis. It was later expanded upon in Part II.

### Part II: Increasing Analysis — Which Models Perform Best Across the Entire S&P 500?
- File: `Part II - S&P 500 Analysis.ipynb`
- Builds directly on Part I with additional models and metrics.
- Adds:
  - Model 5: Rule-based Mean Reversion
  - Model 6: RL using returns, volatility, and RSI
- Extends analysis from AAPL to all tickers in the S&P 500.
- Summarizes results by ticker and sector.
- Generates leaderboards of most consistent models by sector.
- Outputs a clean dataset of all results for dashboard visualization.

### Part III: Streamlit Dashboard
- File: `streamlit_app.py`
- Interactive dashboard to explore results from Part II.
- Filter by Model, Sector, Ticker, and Performance Metrics.
- View aggregated tables or detailed model-by-model comparisons.
- Helps identify which models work best in different industries or market conditions.

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

