# Installing the Invi Labs iPhone MCP server

This is a hosted remote MCP server. Nothing needs to be cloned, built or installed.

## Requirements

- An Invi Labs account with at least one phone: a stock iPhone with the Invi Dongle, a jailbroken iPhone with Invi Link, or a rented phone (https://invilabs.io).
- An API key: in https://panel.invilabs.io open Resources -> AI agents (MCP) and create a key with the Control permission. Ask the user for it; never invent one.

## Configuration

Add this server to the MCP settings file (Cline: `cline_mcp_settings.json`). Replace `YOUR_API_KEY` with the user's key:

```json
{
  "mcpServers": {
    "invilabs": {
      "type": "streamableHttp",
      "url": "https://api.invilabs.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_API_KEY" },
      "timeout": 300
    }
  }
}
```

Clients that support OAuth sign-in can use the URL alone and sign in when asked.

## Check it works

Call the `devices` tool. It returns the phones on the account with their codes (for example `SE001`). Then call `phone_screenshot` with that code as `phone_id`.

## Optional limits

Append query parameters to the URL: `?phone=SE001` (only that phone), `read_only=1` (tools that change nothing), `exclude_tools=jb_*` (hide jailbroken-only tools).
