---
title: Built-in memory for Claude Managed Agents
url: https://claude.com/blog/claude-managed-agents-memory
source: blog
published: '2026-04-23'
fetched: 2026-06-13 12:12
---

- April 23, 2026
- 5min

Memory on Claude Managed Agents is available today in public beta. Your agents can now learn from every session, using an intelligence-optimized memory layer that balances performance with flexibility. Because memories are stored as files, developers can export them, manage them via the API, and keep full control over what agents retain.

## Agents that learn across sessions

Managed Agents pairs production infrastructure with a harness tuned for performance. Memory extends that: it’s optimized against internal benchmarks for long-running agents that improve across sessions and share what they've learned with each other.

We've found that agents are most effective with memory when it builds on the tools they already use. Memory on Managed Agents mounts directly onto a filesystem, so Claude can rely on the same bash and code execution capabilities that make it effective at agentic tasks. With filesystem-based memory, our latest models save more comprehensive, well-organized memories and are more discerning about what to remember for a given task.

## Portable memories for production-grade agents

Memory is built for enterprise deployments, with scoped permissions, audit logs, and full programmatic control. Stores can be shared across multiple agents with different access scopes. For example, an org-wide store might be read-only, while per-user stores allow reads and writes. Multiple agents can work concurrently against the same store without overwriting each other.

Memories are files that can be exported and independently managed via the API, giving developers full control. All changes are tracked with a detailed audit log, so you can tell which agent and session a memory came from. You can roll back to an earlier version or redact content from history. Updates also surface in the Claude Console as session events, so developers can trace what an agent learned and where it came from.

**What teams are building**

Teams have been using memory to close feedback loops, speed up verification, and replace custom retrieval infrastructure:

- **Netflix**agents carry context across sessions, including insights that took multiple turns to uncover and corrections from a human mid-conversation, instead of manually updating prompts and skills.
- **Rakuten's**task-based long-running agents use memory to learn from every session and avoid repeating past mistakes, cutting first-pass errors by 97%, all within workspace-scoped, observable boundaries.
- **Wisedocs**built their document verification pipeline on Managed Agents, using cross-session memory to spot and remember recurring document issues, speeding up verification by 30%.- ****
- **Ando**is building their workplace messaging platform on Managed Agents, capturing how each organization interacts instead of building memory infrastructure themselves.

## Getting started

Memory on Managed Agents is now available in public beta on the Claude Platform. Visit the Claude Console or use our new CLI to deploy your first agent with memory. Explore the documentation to learn more.

## Transform how your organization operates with Claude

Get the developer newsletter
