---
title: 'New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels'
url: https://claude.com/blog/claude-managed-agents-updates
source: blog
published: '2026-05-19'
fetched: 2026-06-13 12:12
---

- May 19, 2026
- 5min

Starting today, Claude Managed Agents can operate in a sandbox you control and connect to your private Model Context Protocol (MCP) servers. Both the sandbox where an agent executes tools and the services it reaches run within the established boundaries of your enterprise, under your security and runtime controls.

The sandbox runs on your own infrastructure, or with managed providers like Cloudflare, Daytona, Modal, or Vercel to handle the compute and isolation for you.

On the Claude Platform, self-hosted sandboxes is available in public beta and MCP tunnels in research preview (request access).

**Keep agent execution within your perimeter**

With self-hosted sandboxes, you keep sensitive files, packages, and services in your own infrastructure or with a managed sandbox provider. The agent loop that handles orchestration, context management, and error recovery stays on Anthropic’s infrastructure, while tool execution moves to your own configured environment.

Inside your perimeter, network policies, audit logging, and security tooling are already in place, and files and repositories don't leave. You also control the compute: resource sizing and the runtime image are set on your side, so agents running compute-heavy work such as long builds or image generation get the CPU, memory, and capacity the task needs.

**Choose your sandbox client**

Bring any sandbox client you want, or start with one of our supported providers:

- **Cloudflare**runs sandboxes at scale using microVMs and lighter weight isolates. Outbound network requests are in your control with zero-trust secrets injection, customizable proxies to audit, reroute, or modify egress, and the ability to connect to internal services over Cloudflare's network.- **Amplitude**is building Design Agent, an internal tool for on-brand production UI and marketing design, on Managed Agents and Cloudflare for tighter observability and control.
- **Daytona**sandboxes are full composable computers, long-running and stateful. The same primitive runs a quick burst or an agent that works for hours. The sandbox stays accessible while a session runs over SSH or an authenticated preview URL, or can be paused and restored with full state preserved.- **Clay’s**- **Modal**is a cloud platform built for AI workloads, where sandboxes share the same foundation as Modal's functions, storage, and networking primitives, giving you everything you need to build production AI systems. Modal's custom container runtime delivers sub-second startup on any image, scales to hundreds of thousands of concurrent sandboxes, and gives you CPU and GPU resources on demand.
- **Vercel**- **Rogo**, an AI platform for institutional finance, is building an analyst agent on Managed Agents and Vercel Sandbox to handle their proprietary data securely.

**Connect to services within your private network**

With MCP tunnels, your agents reach MCP servers inside your private network without exposing them to the public internet. Internal databases, private APIs, knowledge bases, and ticketing systems become tools your agents can call. A lightweight gateway you deploy makes a single outbound connection, no inbound firewall rules, no public endpoints, and traffic encrypted end to end.

MCP tunnels is supported in Managed Agents and the Messages API. MCP tunnels is managed from workspace settings within the Claude Console by organization admins.

**Getting started**

Both self-hosted sandboxes and MCP tunnels work within the same core primitives supported by Managed Agents. Self-hosted sandboxes is available in public beta and MCP tunnels in research preview. To get started with MCP tunnels, request access.

Explore our docs to learn more, follow our cookbooks to set up your sandbox provider, or deploy your first agent in the Claude Console.

## Transform how your organization operates with Claude

Get the developer newsletter
