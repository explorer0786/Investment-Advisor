# 📈 AI-Powered Stock Insights Platform

An intelligent multi-agent system that analyzes companies like **Tesla (TSLA)**, **NVIDIA (NVDA)**, and **Apple (AAPL)** to provide AI-driven long-term investment recommendations using real-time financial data.

---

## 🚀 Features

- 🔍 **Company Analysis** — Get insights on valuation, fundamentals, and analyst recommendations.
- 🧠 **AI Agents** — Utilizes multiple LLM-powered agents (Web & Finance) using [Agno SDK](https://github.com/agno-ai/agents).
- 📊 **Real-Time Financial Data** — Pulled using `YFinance` and `DuckDuckGo`.
- 🌐 **Web Interface** — Clean and responsive UI built with Streamlit.
- 📈 **Investment Strategy Suggestions** — Growth, Stability, and Risk-based guidance powered by LLaMA 4 on Groq.

---

## 🧱 Tech Stack

| Layer         | Tools/Technologies                              |
|---------------|--------------------------------------------------|
| 💬 LLMs       | [Groq](https://groq.com/) + LLaMA 4 (Scout)      |
| 🧠 Agents     | [Agno SDK](https://github.com/agno-ai/agents)   |
| 📊 Finance    | [YFinance](https://pypi.org/project/yfinance/)  |
| 🔎 Search     | [DuckDuckGoTools](https://duckduckgo.com/)      |
| 🌐 UI         | [Streamlit](https://streamlit.io/)              |
| 🔐 API Keys   | Secured via `.env` using `python-dotenv`         |

---

## 🖥️ UI Preview

<img width="1792" height="882" alt="image" src="https://github.com/user-attachments/assets/230cc3dd-e2e8-474e-af71-a43af3012185" />


> *Displays Tesla, NVIDIA, and Apple fundamentals in tabular format with AI-generated investment advice.*

---

## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-stock-insights.git
cd ai-stock-insights
