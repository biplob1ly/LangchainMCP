import asyncio
from models import load_llm

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            # Make sure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        }
    }
)


async def main():
    llm = load_llm()
    tools = await client.get_tools()
    agent = create_agent(model=llm, tools=tools)
    math_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    # print(math_response)
    print('-' * 30)
    for msg in math_response['messages']:
        msg.pretty_print()
    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    # print(weather_response)
    print('-' * 30)
    for msg in weather_response['messages']:
        msg.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())