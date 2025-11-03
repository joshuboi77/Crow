# Crow MCP Server

Model Context Protocol (MCP) server that exposes Crow CLI commands as tools for use in Cursor and other MCP-compatible IDEs.

## Overview

This MCP server allows you to use Crow directly within Cursor, making Python project formatting setup accessible to AI agents and automation. The server exposes two main tools:

- **crow_setup** - Setup formatting and linting for a Python repository
- **crow_initialize** - Initialize a new Python project with formatting setup

## Installation

### Prerequisites

- Node.js 18+ 
- Crow installed (Homebrew: `brew install crow` or `pip install crow`)
- Crow must be in your PATH

### Setup

1. Install dependencies:
```bash
cd mcp
npm install
```

2. Build the TypeScript code:
```bash
npm run build
```

3. The server will be available at `dist/server.js`

## Cursor Configuration

Add Crow MCP server to your Cursor configuration:

### macOS/Linux

Edit or create `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "crow": {
      "command": "node",
      "args": ["/absolute/path/to/Crow/mcp/dist/server.js"]
    }
  }
}
```

### Windows

Edit or create `%USERPROFILE%\.cursor\mcp.json`:

```json
{
  "mcpServers": {
    "crow": {
      "command": "node",
      "args": ["C:\\full\\path\\to\\Crow\\mcp\\dist\\server.js"]
    }
  }
}
```

## Usage in Cursor

After configuring and restarting Cursor:

1. Open Cursor's tools panel
2. You should see `crow_setup` and `crow_initialize` available
3. Use them in chat or agent mode to automate Python project setup

### Example Agent Workflow

```
1. crow_initialize(name="mytool", description="My awesome tool", python="3.12")
2. crow_setup(projectRoot="./myproject", ruffOnly=true, noVenv=true)
```

## Development

### Running in Development Mode

```bash
npm run dev
```

This uses `tsx` to run TypeScript directly without building.

### Building

```bash
npm run build
```

### Testing Locally

You can test the server manually using the MCP inspector or by connecting from Cursor.

## Tool Reference

### crow_setup

Setup formatting and linting for a Python repository.

**Parameters:**
- `projectRoot` (string, optional) - Project root directory (default: current directory)
- `python` (string, optional) - Python version for CI/tools (default: 3.11)
- `ruffOnly` (boolean, optional) - Skip Black; use Ruff formatter only
- `dryRun` (boolean, optional) - Show what would be done without making changes
- `noFormat` (boolean, optional) - Skip formatting existing code files
- `noInstallHooks` (boolean, optional) - Skip installing pre-commit hooks
- `noVenv` (boolean, optional) - Skip creating .venv; use system tools instead
- `cwd` (string, optional) - Working directory (default: current)

### crow_initialize

Initialize a new Python project with formatting setup.

**Parameters:**
- `name` (string, optional) - Tool name (non-interactive mode)
- `description` (string, optional) - Tool description (non-interactive mode)
- `version` (string, optional) - Initial version (non-interactive mode, default: 0.1.0)
- `projectRoot` (string, optional) - Project root directory (default: current directory)
- `python` (string, optional) - Python version for CI/tools (default: 3.11)
- `ruffOnly` (boolean, optional) - Skip Black; use Ruff formatter only
- `dryRun` (boolean, optional) - Show what would be done without making changes
- `noFormat` (boolean, optional) - Skip formatting existing code files
- `noInstallHooks` (boolean, optional) - Skip installing pre-commit hooks
- `noVenv` (boolean, optional) - Skip creating .venv; use system tools instead
- `cwd` (string, optional) - Working directory (default: current)

## Troubleshooting

### "crow: command not found"

Ensure Crow is installed and in your PATH:
- Homebrew: `brew install crow`
- pip: `pip install crow`
- Check: `which crow`

### MCP Server Not Appearing

1. Check that the path in `mcp.json` is absolute and correct
2. Restart Cursor after changing `mcp.json`
3. Check Cursor's MCP server logs for errors
4. Verify Node.js version: `node --version` (needs 18+)

## License

MIT (same as Crow)

