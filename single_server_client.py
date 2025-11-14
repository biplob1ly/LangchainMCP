import asyncio
from models import load_llm
# Create server parameters for stdio connection
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["math_server.py"],
)

async def main():
    llm = load_llm()
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Get tools
            tools = await load_mcp_tools(session)

            # Create and run the agent
            agent = create_agent(model=llm, tools=tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            for msg in agent_response['messages']:
                msg.pretty_print()


if __name__ == "__main__":
    asyncio.run(main())