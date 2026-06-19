---
title: Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp
url: https://claude.com/blog/claude-api-skill
source: blog
published: '2026-04-29'
fetched: 2026-06-13 12:15
---

- April 29, 2026
- 5min

Today, CodeRabbit, JetBrains, Resolve AI, and Warp are bundling the claude-api skill, giving developers production-ready Claude API code wherever they build. First introduced in Claude Code in March, the skill is now in more of the tools developers already use.

## Building with the Claude API skill

The `claude-api `skill captures the details that make Claude API code work well, like which agent pattern fits a given job, what parameters change between model generations, and when to apply prompt caching. The result is fewer errors, better caching, cleaner agent patterns, and smoother model migrations.

It stays current as our SDKs change. When a new model is released or the API gains a feature, Claude already knows.

Anywhere the skill is available, ask Claude to:

- **"Improve my cache hit rate."**The skill applies prompt caching rules many developers miss.
- **"Add context compaction to my agent."**It walks you through the compaction primitives and agent patterns in our docs.
- **"Upgrade me to the latest Claude model."**Claude reviews your code and walks you through updating model names, prompts, and effort settings for a new model like Opus 4.7. In Claude Code, you can also run this directly with- `/claude-api migrate.`- ****
- **"Build a deep research agent for my industry."**Claude walks you through configuring Claude Managed Agents, so long-running research is a few prompts, not a custom project. In Claude Code, you can also run this directly with- `/claude-api managed-agents-onboard`.

## For Claude-powered coding agents

Any coding agent can bundle the `claude-api `skill to give their users expertise around the Claude API. If you are building a tool where developers write Claude API code, the skill is open source at anthropics/skills. Our bundling guide walks through the setup in about 20 lines of CI, and the skill stays current automatically.

## Getting started

The skill is already in Claude Code, CodeRabbit, JetBrains, Junie, Resolve AI, and Warp. To learn more, see the claude-api skill docs.

## Transform how your organization operates with Claude

Get the developer newsletter
