from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from config import get_car_llm


@tool
def  load_webpages(car_model: str):
    """
    load car listings from multiple websites and return taw scraped text

    """
    urls = [
         f"https://ikman.lk/en/ads?query={car_model}"
     ]

    loader = WebBaseLoader(urls)
    docs = loader.load()

    return "\n".join([doc.page_content for doc in docs])

@tool
def analyze_car_ads ( raw_ads:str, car_model:str):
    """ gives an analysis on car deals using raw_ads of a car model"""

    car_llm = get_car_llm()
    response_prompt = ChatPromptTemplate.from_template(
        """
        You are an automotive assistant helping  users find the best car deals.
        here are raw car ads for the car model- {car_model}.

        {raw_ads}

        Highlight key insights, suggest buyer types, and provide a 2-3 sentence summary.
        also provide best average price to buy.

        """
    )

    resp_chain =  response_prompt | car_llm
    resp = resp_chain.invoke({"raw_ads": raw_ads, "car_model": car_model})

    return resp





