# MCP Server FAQ

## Q: What is an MCP server used for?
A: It exposes tools and resources to AI clients using a standard protocol and typed contracts.

## Q: How should tools be exposed?
A: Expose only necessary tools with strict input schemas and explicit permission boundaries.

## Q: How is MCP secured?
A: Use authenticated clients, scoped authorization, request validation, and full audit logging.

## Q: Should MCP tools be read-only?
A: Start with read-only tools and require human approval for destructive or external actions.

## Q: How do we monitor MCP usage?
A: Track tool usage metrics, failures, denial counts, and suspicious request patterns.
