from phi.agent import Agent
from phi.model.groq import Groq
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.googlesearch import GoogleSearch
from phi.playground import Playground, serve_playground_app

import os
from dotenv import load_dotenv

load_dotenv()

compare_agent = Agent(
    name="sheru ",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools= [GoogleSearch() ],
    show_tool_calls=True,
    storage=SqlAgentStorage(table_name="sheru_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
    instructions=["You are a stock market analyst , you will search details about indian stocks and give very factual data, comparing different stocks"] 
)

expert_agent = Agent(
    name= " viru ",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools= [GoogleSearch() ],
    show_tool_calls=True,
    storage=SqlAgentStorage(table_name="viru_agent", db_file="agents.db"),
    add_history_to_messages=True,
    markdown=True,
    instructions=["You are an expert in giving investing advice on indian stocks , take data from compare_agent to give well structured advice"] 
)

agent_team = Agent(
    team=[compare_agent,expert_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Give final conclusion with which stock to buy , put all comparative data in tabulated manner"],
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("zomato vs swiggy stock")