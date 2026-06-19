---
title: 'Claude Managed Agents: get to production 10x faster'
url: https://claude.com/blog/claude-managed-agents
source: blog
published: '2026-04-08'
fetched: 2026-06-13 12:12
---

- April 8, 2026
- 5min

Today, we're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Until now, building agents meant spending development cycles on secure infrastructure, state management, permissioning, and reworking your agent loops for every model upgrade. Managed Agents pairs an agent harness tuned for performance with production infrastructure to go from prototype to launch in days rather than months.

Whether you're building single-task runners or complex multi-agent pipelines, you can focus on the user experience, not the operational overhead.

Managed Agents is available today in public beta on the Claude Platform.

**Build and deploy agents 10x faster**

Shipping a production agent requires sandboxed code execution, checkpointing, credential management, scoped permissions, and end-to-end tracing. That's months of infrastructure work before you ship anything users see.

Managed Agents handles the complexity. You define your agent's tasks, tools, and guardrails and we run it on our infrastructure. A built-in orchestration harness decides when to call tools, how to manage context, and how to recover from errors.

Managed Agents includes:

- **Production-grade agents**with secure sandboxing, authentication, and tool execution handled for you.
- **Long-running sessions**that operate autonomously for hours, with progress and outputs that persist even through disconnections.
- **Multi-agent coordination**so agents can spin up and direct other agents to parallelize complex work (available in- *research preview*, request access here).- ****
- **Trusted governance,**giving agents access to real systems with scoped permissions, identity management, and execution tracing built in.

**Designed to make the most of Claude**

Claude models are built for agentic work. Managed Agents is purpose-built for Claude, enabling you to get better agent outcomes with less effort.

With Managed Agents, you define outcomes and success criteria, and Claude self-evaluates and iterates until it gets there (available in *research preview*, request access here). It also supports traditional prompt-and-response workflows when you want tighter control.

In internal testing around structured file generation, Managed Agents improved outcome task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems.

Session tracing, integration analytics, and troubleshooting guidance are built directly into the Claude Console, so you can inspect every tool call, decision, and failure mode.

**What teams are building**

Teams are already shipping 10x faster with Managed Agents across a range of production use cases. Coding agents that read a codebase, plan a fix, and open a PR. Productivity agents that join a project, pick up tasks, and deliver work alongside the rest of the team. Finance and legal agents that process documents and extract what matters. In each case, shipping in days meant providing value to users faster.

- **Notion**lets teams delegate work to Claude directly inside their workspace (available now in private alpha inside Notion Custom Agents). Engineers use it to ship code, while knowledge workers use it to produce websites and presentations. Dozens of tasks can run in parallel while the whole team collaborates on the output.
- **Rakuten**shipped enterprise agents across product, sales, marketing and finance that plug into Slack and Teams, letting employees assign tasks and get back deliverables like spreadsheets, slides, and apps. Each specialist agent was deployed within a week.
- **Asana**- **Vibecode**helps their customers go from prompt to deployed app using Managed Agents as the default integration, powering a new generation of AI-native apps. Users can now spin up that same infrastructure at least 10x quicker than before.- ****
- **Sentry**paired Seer, their debugging agent, with a Claude-powered agent that writes the patch and opens the PR, so developers go from a flagged bug to a reviewable fix in one flow. The integration shipped in weeks instead of months on Managed Agents.

## Getting started

Managed Agents is priced on consumption. Standard Claude Platform token rates apply, plus $0.08 per session-hour for active runtime. See the docs for full pricing details.

Managed Agents is available now on the Claude Platform. Read our docs to learn more, head to the Claude Console, or use our new CLI to deploy your first agent.

Developers can also use the latest version of Claude Code and built-in claude-api Skill to build with Managed Agents. Just ask “start onboarding for managed agents in Claude API” to get started.

## Transform how your organization operates with Claude

Get the developer newsletter
