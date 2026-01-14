from langchain.agents import create_agent

from langgraph_multi_agent.config import get_car_llm
from langgraph_multi_agent.models.router_models import AgentState


def car_agent_node(state: AgentState):

    car_models = state["extracted_entities"].cars

    if not car_models:
        return {
            **state, #** mean expanding to list update final response ( Value Unpacking)
            "final_response" : {"error" : " No car model specified in the question "}
        }

    agent = create_agent(
        model=get_car_llm(),
        tools=car_tools
    )
