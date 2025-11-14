import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
load_dotenv()

def load_llm():
    # print("Hello from langchainmcp!")
    # LLM Initialization


    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )
    return llm