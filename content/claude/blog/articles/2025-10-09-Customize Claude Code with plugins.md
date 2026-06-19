---
title: Customize Claude Code with plugins
url: https://claude.com/blog/claude-code-plugins
source: blog
published: '2025-10-09'
fetched: 2026-06-13 12:16
---

# Customize Claude Code with plugins

Claude Code now supports plugins: custom collections of slash commands, agents, MCP servers, and hooks that install with a single command.

Claude Code now supports plugins: custom collections of slash commands, agents, MCP servers, and hooks that install with a single command.

- October 9, 2025
- 5min

Slash commands, agents, MCP servers, and hooks are all extension points you can use to customize your experience with Claude Code. As we've rolled them out, we've seen users build increasingly powerful setups that they want to share with teammates and the broader community. We built plugins to make this easier.

Plugins are a lightweight way to package and share any combination of:

- **Slash commands**: Create custom shortcuts for frequently-used operations
- **Subagents**: Install purpose-built agents for specialized development tasks
- **MCP servers**: Connect to tools and data sources through the Model Context Protocol
- **Hooks**: Customize Claude Code's behavior at key points in its workflow

You can install plugins directly within Claude Code using the` /plugin` command, now in public beta. They’re designed to toggle on and off as needed. Enable them when you need specific capabilities and disable them when you don’t to reduce system prompt context and complexity.

Moving forward, plugins will be our standard way to bundle and share Claude Code customizations, and we’ll continue to evolve the format as we add more extension points.

Plugins help you standardize Claude Code environments around a set of shared best practices. Common plugin use cases include:

- **Enforcing standards:**Engineering leaders can maintain consistency across their team by using plugins to ensure specific hooks run for code reviews or testing workflows
- **Supporting users**: Open source maintainers, for example, can provide slash commands that help developers use their packages correctly
- **Sharing workflows:**Developers who build productivity-boosting workflows—like debugging setups, deployment pipelines, or testing harnesses—can easily share them with others
- **Connecting tools:**Teams that need to connect internal tools and data sources through MCP servers can use plugins with the same security and configuration protocols to speed up the process
- **Bundling customizations:**Framework authors or technical leads can package multiple customizations that work together for specific use cases

To make it easier to share these customizations, anyone can build and host plugins and create plugin marketplaces—curated collections where other developers can discover and install plugins.

You can use plugin marketplaces to share plugins with the community, distribute approved plugins across your organization, and build on existing solutions for common development challenges.

To host a marketplace, all you need is a git repository, GitHub repository, or URL with a properly formatted `.claude-plugin/marketplace.json` file. See our documentation for details.

To use plugins from a marketplace, run `/plugin marketplace add user-or-org/repo-name`, then browse and install plugins using the `/plugin` menu.

Plugin marketplaces amplify the best practices our community has already developed, and community members are leading the way. For instance, engineer Dan Ávila's plugin marketplace offers plugins for DevOps automation, documentation generation, project management, and testing suites, while engineer Seth Hobson has curated over 80 specialized sub-agents in his GitHub repository, giving developers instant access via plugins.

You can also check out a few example plugins we've developed for PR reviews, security guidance, Claude Agent SDK development, and even a meta-plugin for creating new plugins.

Plugins are now in public beta for all Claude Code users. Install them with the `/plugin` command and they'll work across your terminal and VS Code.

Check out our documentation to get started, build your own plugins, or publish a marketplace. To see plugins in action, try this multi-agent workflow we use to develop Claude Code:

`/plugin marketplace add anthropics/claude-code`

`/plugin marketplace add anthropics/claude-code``/plugin install feature-dev`Get the developer newsletter
