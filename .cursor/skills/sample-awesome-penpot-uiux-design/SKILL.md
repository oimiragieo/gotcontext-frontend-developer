---
name: sample-awesome-penpot-uiux-design
description: Adapter pointer to canonical skills/sample-awesome-penpot-uiux-design for Cursor
---

# sample-awesome-penpot-uiux-design (Cursor adapter)

Canonical skill: [`../../../skills/sample-awesome-penpot-uiux-design/SKILL.md`](../../../skills/sample-awesome-penpot-uiux-design/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: sample-awesome-penpot-uiux-design
description: 'Comprehensive guide for creating professional UI/UX designs in Penpot using MCP tools. Use this skill when: (1) Creating new UI/UX designs for web, mobile, or desktop applications, (2) Building design systems with components and tokens, (3) Designing dashboards, forms, navigation, or landing pages, (4) Applying accessibility standards and best practices, (5) Following platform guidelines (iOS, Android, Material Design), (6) Reviewing or improving existing Penpot designs for usability. Triggers: "design a UI", "create interface", "build layout", "design dashboard", "create form", "design landing page", "make it accessible", "design system", "component library".'
---

# Penpot UI/UX Design Guide

Create professional, user-centered designs in Penpot using the `penpot/penpot-mcp` MCP server and proven UI/UX principles.

## Available MCP Tools

| Tool | Purpose |
| ---- | ------- |
| `mcp__penpot__execute_code` | Run JavaScript in Penpot plugin context to create/modify designs |
| `mcp__penpot__export_shape` | Export shapes as PNG/SVG for visual inspection |
| `mcp__penpot__import_image` | Import images (icons, photos, logos) into designs |
| `mcp__penpot__penpot_api_info` | Retrieve Penpot API documentation |

## MCP Server Setup

The Penpot MCP tools require the `penpot/penpot-mcp` server running locally. For detailed installation and troubleshooting, see [setup-troubleshooting.md](references/setup-troubleshooting.md).

### Before Setup: Check If Already Running

**Always check if the MCP server is already available before attempting setup:**

1. **Try calling a tool first**: Attempt `mcp__penpot__penpot_api_info` - if it succeeds, the server is running and connected. No setup needed.

2. **If the tool fails**, ask the user:
   > "The Penpot MCP server doesn't appear to be connected. Is the server already installed and running? If so, I can help troubleshoot. If not, I can guide you through the setup."
```
