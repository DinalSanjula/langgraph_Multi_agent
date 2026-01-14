from langchain_openai import ChatOpenAI


def get_car_llm():
    return ChatOpenAI(model="gpt-5.2-2025-12-11")

def get_crypto_llm():
    return ChatOpenAI(model="gpt-5.2-2025-12-11")

def get_router_llm():
    return ChatOpenAI(model="gpt-5.2-2025-12-11")

def get_general_llm():
    return ChatOpenAI(model="gpt-5.2-2025-12-11")
