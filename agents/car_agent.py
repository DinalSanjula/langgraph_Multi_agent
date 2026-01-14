from langchain.agents import create_agent

from config import get_car_llm
from langchain.agents.structured_output import ToolStrategy
from langchain_core.messages import HumanMessage

from car_models import CarDealsResponse
from langgraph_multi_agent.models.router_models import AgentState
from langgraph_multi_agent.tools import car_tools


def car_agent_node(state: AgentState):

    car_models = state["extracted_entities"].cars

    if not car_models:
        return {
            **state, #** mean expanding to list update final response ( Value Unpacking)
            "final_response" : {"error" : " No car model specified in the question "}
        }

    agent = create_agent(
        model=get_car_llm(),
        tools=car_tools,
        response_format=ToolStrategy(CarDealsResponse)
    )

    result = agent.invoke({
    "messages": [
        HumanMessage(content=f"fetch and analyze car listings for {car_models}")
    ]
    })

    final_message = result.get("structured_output", {})

    return {**state, "final_response" : final_message}



