# Rule-Based vs Reinforcement Learning: Backtesting Trading Strategies on Stocks

This repository contains the full source code, notebooks, and dashboard for a 3-part blog and video series comparing **rule-based trading strategies** to **Reinforcement Learning (RL)** models using historical stock data.

We start with a single stock (AAPL), scale up to all **S&P 500 tickers**, and build an interactive dashboard for exploring model performance across sectors.

---

## Project Overview

### Part I: Single Stock Comparison (AAPL)
- File: `Part I - Single Stock.ipynb`
- Backtests 7 trading models (Rule-based and RL) on AAPL using 2 years of daily price data.
- Evaluates models using **Sharpe ratio**, **Max Drawdown**, **Avg Return**, **# of Trades**, and more.
- Highlights how feature selection impacts RL performance.

### Part II: Increasing Analysis — Which Models Perform Best Across the Entire S&P 500?
- File: `Part II - S&P 500 Analysis.ipynb`
- Scales the backtesting engine to all tickers in the **S&P 500**, grouped by sector.
- Compares model performance across tickers and sectors.
- Generates summary tables, leaderboards, and sector-by-sector breakdowns.
- Outputs a cleaned DataFrame of all model results for dashboard use.

### 🔹 Part III: Streamlit Dashboard
- File: `streamlit_app.py`
- Interactive web app for filtering and exploring:
  - Model performance by sector, ticker, or strategy type
  - Metrics: Return %, Sharpe Ratio, Drawdown, Trade Count, Profit Factor, etc.
- Easy local or cloud deployment via **Streamlit Cloud** or **Hugging Face Spaces**

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

