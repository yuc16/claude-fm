---
title: 'Code w/ Claude London 2026: Rethinking how we build'
url: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
source: blog
published: '2026-05-26'
fetched: 2026-06-13 12:15
---

# Code w/ Claude London 2026: Rethinking how we build

Couldn't make it to London? Keynotes and breakout sessions are now live.

Couldn't make it to London? Keynotes and breakout sessions are now live.

- May 26, 2026
- 5min

This week in London, we brought Code w/ Claude to Europe. The event brought together builders, developers, and founders for two days of keynotes, breakout sessions, and workshops with the teams building Claude.

Boris Cherny, Head of Claude Code, kicked off the keynote by describing the first time he felt the “magic” of coding. In secondary school, he wrote TI-83 programs that solved his math homework and tests, and taught himself HTML to make his eBay listings for Pokémon cards sell better. He learned by tinkering, and when something ran, it was exciting.

Somewhere along the way, he suggested, programming got complicated. Compilers, typecheckers, build systems, and each layer pushed the distance between "I have an idea" and "it runs" a little further out. With agents, that distance is collapsing again: you describe a problem, and the program shows up. It's the calculator feeling, except the calculator can write a distributed system.

From workshops highlighting how to go beyond the basics with Claude Code to optimizing thinking budgets and effort levels across our models, we demonstrated how Anthropic and customers like Spotify, Base44, and Legora are already recapturing this experience.

Announced at the conference, Claude Managed Agents can now operate in a sandbox you control and connect to your private Model Context Protocol (MCP) servers. Now both the environment where an agent executes tools and the services it reaches run within the established boundaries of your enterprise. These two new capabilities are available on the Claude Platform:

- **Self-hosted sandboxes**(public beta). Tool execution moves to an environment you configure—your own infrastructure or a managed provider like Cloudflare, Daytona, Modal, or Vercel—while the agent loop that handles orchestration, context management, and error recovery stays on Anthropic's infrastructure. Your network policies, audit logging, and security tooling apply, files and repositories don't leave your perimeter, and you control compute sizing and the runtime image for compute-heavy work.
- **MCP tunnels**(research preview)- *.*Your agents reach MCP servers inside your private network without exposing them to the public internet. A lightweight gateway you deploy makes a single outbound connection: no inbound firewall rules, no public endpoints, and traffic encrypted end to end. MCP tunnels are supported in Managed Agents and the Messages API, and are managed from the Claude Console by organization admins.

Teams including Amplitude, Clay, and Rogo are already building on Managed Agents with self-hosted sandboxes. To get started, explore the docs, follow our cookbooks, or request access to MCP tunnels.

If you missed the livestream, check our keynote and breakout session recordings.

Code w/ Claude heads to Tokyo next (June 5–6). All Day 1 keynotes and breakout sessions will be streamed live.

*Stay tuned for technical tutorials, guides, and customer stories inspired by our talks.*

Get the developer newsletter
