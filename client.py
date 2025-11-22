import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
            # List available resources
            resources = await session.list_resources()
            print(f"Available resources: {[resource.name for resource in resources.resources]}")
            # List available prompts
            prompts = await session.list_prompts()
            print(f"Available prompts: {[prompt.name for prompt in prompts.prompts]}")

            # Call Tool
            tool_res = await session.call_tool("search_file", {"filename_pattern": "file*"})
            filenames = tool_res.structuredContent["result"]
            print(filenames)

if __name__ == "__main__":
    asyncio.run(main())
