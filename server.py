import glob
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo", json_response=True)


# Add addition tools
@mcp.tool()
def search_file(filename_pattern: str) -> int:
    """Find filename list matching with filename_pattern"""
    filenames = []
    for filename in glob.glob("./data", filename_pattern, recursive=True):
        filenames.append(filename)
    return filenames

# Add resources
@mcp.resource(
    uri="file://{filepath}",
    name="ReadFile"
)
def readfile(filepath: str) -> str:
    """Fetch file content"""
    content = ""
    path = "./data/" + filepath
    with open(path) as f:
        content = f.read()
    return content

@mcp.resource(
    uri="fileinfo://{filepath}",
    name="FileInfo"
)
def fileInfo(filepath: str) -> dict:
    """Fetch file info"""
    content = ""
    path = "./data/" + filepath
    with open(path) as f:
        content = f.read()
    return content

# Add prompts
@mcp.prompt()
def get_llm_call() -> str:
    """Fetch prompt for first llm call"""
    return ""

# Run with streamable HTTP transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
