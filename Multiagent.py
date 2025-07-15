from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = "API_KEY"  # Replace with your actual Groq API key

web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],    
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)
# --- Streamlit UI ---
st.set_page_config(page_title="Investment Insights", layout="wide")
st.title("📈 Investment Advisor - Powered by LangGraph Agents")

st.markdown("📊 Analyze Top Tech Stocks for Smart Long-Term Investing")

# Input box
query = st.text_input("Enter your investment query:", "Analyze companies like Tesla, NVDA, Apple and suggest which to buy for long term")

# Submit
if st.button("Analyze"):
    with st.spinner("Analyzing... Please wait."):
        response = agent_team.run(query)
        st.markdown("---")
        st.markdown("### 🧠 AI Recommendation")
        st.markdown(response.content, unsafe_allow_html=True)