---
title: Build plugins for Claude with the directory submission portal | Claude by Anthropic
url: https://claude.com/blog/build-plugins-for-claude
source: blog
published: '2026-09-25'
fetched: 2026-09-27 13:34
---

# Build plugins for Claude

*You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.*

*You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.*

- September 25, 2026
- 5min

Every day, millions of people connect Claude to their apps, work tools, and data. Today, we're making it easier for developers to reach them.

Plugins package MCP connectors, Agent Skills, or both, and are the main way to build third-party extensions for Claude. Build a plugin, submit it through the new directory submission portal, and once approved, it's listed in the Claude directory.

The directory submission portal is open to developers on paid Claude plans. There are two ways to submit and get your plugin published in the Claude directory:

- **Single MCP connector:**point to your remote MCP server.
- **Plugin bundle:**combine MCP servers and skills, host them on GitHub, and submit the repo. In Claude Code, plugins can also include LSPs, commands, hooks, and agents.

Whichever path you choose, the portal will guide you from submission to launch. You can:

- **Auto-validate your plugin.**Each submission is checked and safety-scanned as soon as you submit, so you catch issues early.
- **Review status and feedback.**See where your plugin is in the review process, results from the safety scan, and recommended changes.
- **Publish when you’re ready.**Once approved, you decide when to publish your plugin in Claude.

Once your plugin is live, usage analytics show installs by product surface and version, so you can prioritize fixes and features for your users. On the discovery side, you’ll see how often your listing is viewed and which searches lead people to it, so you can refine it to reach new users.

Claude supports the latest MCP spec, commonly referred to as MCP 2.0, which includes a stateless core. You can improve the experience of using your plugin with two MCP extensions: MCP Apps, for interactive UI inside chat, and Enterprise Managed Auth, for zero-touch OAuth for enterprise users. Support for more MCP features and extensions is coming soon.

Plugins are the main way for third-party developers to create extensions for Claude. Over the coming weeks, one discovery experience will roll out across Claude and Claude Code.

Skills and MCP connectors stay as building blocks, and the Claude directory will continue to list them. In the future, developers will be able to turn their connector listing into a plugin. If you have an existing skill, connector, or plugin on the Claude directory, you do not need to make any changes.

To get started with building plugins, read our docs for how to build a plugin and submit your plugin here.

Get the developer newsletter
