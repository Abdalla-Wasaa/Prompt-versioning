"""Check the logistics MCP through a bounded stdio handshake."""
import asyncio
import sys
from pathlib import Path

EXPECTED_TOOLS = {'check_stock', 'list_low_stock'}
EXPECTED_VERSION = '1.1.0'
SERVER = Path(__file__).resolve().parents[1] / 'logistics_mcp_versioned.py'


def validate_health(tools, contents):
    missing = EXPECTED_TOOLS - tools
    if missing:
        raise ValueError(f'missing tools: {sorted(missing)}')
    version = ''.join(getattr(part, 'text', '') for part in contents).strip()
    if version != EXPECTED_VERSION:
        raise ValueError(f'expected version {EXPECTED_VERSION}, got {version!r}')
    return version


async def handshake() -> int:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client

    async with asyncio.timeout(30):
        params = StdioServerParameters(command=sys.executable, args=[str(SERVER)])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = {t.name for t in (await session.list_tools()).tools}
                resource = await session.read_resource('version://current')
                version = validate_health(tools, resource.contents)
                print('MCP HEALTH OK:', 'tools', sorted(tools), 'version', version)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(asyncio.run(handshake()))
    except Exception as exc:
        print('MCP HEALTH FAILED:', repr(exc))
        raise SystemExit(1)
