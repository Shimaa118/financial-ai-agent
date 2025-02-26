import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

# Initialize the agent
agent = Agent(
    model=Groq(id='deepseek-r1-distill-llama-70b'),
    description="you are a simple GROQ agent that provides stock and crypto info.",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data"]
)

# Streamlit UI
st.title("Financial AI Assistant")
user_query = st.text_input("Ask something about stocks or crypto:", "")

if st.button("Get Answer"):
    if user_query:
        response = agent.respond(user_query)
        st.markdown(response)
