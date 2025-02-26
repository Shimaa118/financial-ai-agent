from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

load_dotenv()

agent= Agent(
    model= Groq(id='deepseek-r1-distill-llama-70b'),
    description= "you are a simple GROQ agent that can provide information on stocks, cryptocurrencies, and other financial instruments. be friendly",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),],
    show_tool_calls=True,
    markdown=True,
    instructions= ["use tables to display data"]

)

agent.print_response("summarize and compare analyst recommendation and fundamentals for AAPL and MSFT . compare using tables")
