---
title: Enabling Claude Code to work more autonomously
url: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
source: news
published: '2025-09-28'
fetched: 2026-06-13 04:48
---

# Enabling Claude Code to work more autonomously

We’re introducing several upgrades to Claude Code: a native VS Code extension, version 2.0 of our terminal interface, and checkpoints for autonomous operation. Powered by Sonnet 4.5, Claude Code now handles longer, more complex development tasks in your terminal and IDE.

## Claude Code on more surfaces

**VS Code extension**

We’re introducing a native VS Code extension in beta that brings Claude Code directly into your IDE. You can now see Claude’s changes in real-time through a dedicated sidebar panel with inline diffs. The extension provides a richer, graphical Claude Code experience for users who prefer to work in IDEs over terminals.

**Enhanced terminal experience**

We’ve also refreshed Claude Code’s terminal interface. The updated interface features improved status visibility and searchable prompt history (Ctrl+r), making it easier to reuse or edit previous prompts.

**Claude Agent SDK**

For teams who want to create custom agentic experiences, the Claude Agent SDK (formerly the Claude Code SDK) gives access to the same core tools, context management systems, and permissions frameworks that power Claude Code. We’ve also released SDK support for subagents and hooks, making it more customizable for building agents for your specific workflows.

Developers are already building agents for a broad range use cases with the SDK, including financial compliance agents, cybersecurity agents, and code debugging agents.

## Execute long-running tasks with confidence

As Claude Code takes on increasingly complex tasks, we're releasing a checkpointing feature to help delegate tasks to Claude Code with confidence while maintaining control. Combined with recent feature releases, Claude Code is now more capable of handling sophisticated tasks.

**Checkpoints**

Complex development often involves exploration and iteration. Our new checkpoint system automatically saves your code state before each change, and you can instantly rewind to previous versions by tapping Esc twice or using the /rewind command. Checkpoints let you pursue more ambitious and wide-scale tasks knowing you can always return to a prior code state.

When you rewind to a checkpoint, you can choose to restore the code, the conversation, or both to the prior state. Checkpoints apply to Claude’s edits and not user edits or bash commands, and we recommend using them in combination with version control.

**Subagents, hooks, and background tasks**

Checkpoints are especially useful when combined with Claude Code’s latest features that power autonomous work:

- **Subagents**delegate specialized tasks—like spinning up a backend API while the main agent builds the frontend—allowing parallel development workflows
- **Hooks**automatically trigger actions at specific points, such as running your test suite after code changes or linting before commits
- **Background**- **tasks**keep long-running processes like dev servers active without blocking Claude Code’s progress on other work

Together, these capabilities let you confidently delegate broad tasks like extensive refactors or feature exploration to Claude Code.

## Getting started

These updates are available now for Claude Code users.

- **Claude Sonnet 4.5**is the new default model in Claude Code. Run /model to switch models
- **VS Code extension**(beta)- **:**Download from the VS Code Extension Marketplace to get started
- **Terminal updates**, including the visual refresh and checkpoints, are available to all Claude Code users—just update your local installation
- **Claude Agent SDK:**See the docs to get started

## Related content

### Results from the first Anthropic Public Record

Read more### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

Read more### DXC will integrate Claude into the systems banks, airlines, and other regulated industries rely on

We’re announcing a multi-year global alliance with DXC Technology, one of the world’s largest IT services companies.

Read more
