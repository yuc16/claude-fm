---
title: 'Beyond permission prompts: making Claude Code more secure and autonomous'
url: https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
source: blog
published: '2025-10-08'
fetched: 2026-06-13 12:16
---

Beyond permission prompts: making Claude Code more secure and autonomous

In Claude Code, Claude writes, tests, and debugs code alongside you, navigating your codebase, editing multiple files, and running commands to verify its work. Giving Claude this much access to your codebase and files can introduce risks, especially in the case of prompt injection, such as Claude deleting files you didn't intend.

To help address this, we’ve introduced two new features in Claude Code built on top of sandboxing, both of which are designed to provide a more secure place for developers to work, while also allowing Claude to run more autonomously and with fewer permission prompts. ByThese features are examples of native sandboxing: defining set boundaries within which Claude can work freely, they increase security and agency..

Our current approach to keeping users secure

Claude Code runs on a permission-based model: by default, it's read-only, which means it asks for permission before making modifications or running any commands. There are some exceptions to this: we use static analysis to auto-allow safe commands like echo or cat, but most operations still need explicit approval.

But constantly clicking "approve" slows down development and can lead to ‘approval fatigue’, where users might not pay close attention to what they're approving. To make Claude Code both safer and more effective, we wanted to find a better method.

Sandboxing: a safer and more autonomous approach

Sandboxing creates pre-defined boundaries within which Claude can work more freely, instead of asking for permission for each action.

With our update to Claude Code, we’re shifting to this approach. We’re building Our approach to sandboxing is built on top of operating system-level features to enable two new features, each of which are based on the followingtwo sets of boundariesmain things:

Filesystem isolation,which ensures that Claude can only access or modify specific directories. This is particularly important in preventing a prompt-injected Claude from modifying sensitive system files.

Network isolation,which ensures that Claude can only connect to approved servers. This prevents a prompt-injected Claude from leaking sensitive information or downloading malware.

It is worth noting that effective sandboxing requires both filesystem and network isolation. Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys; without filesystem isolation, a compromised agent could easily escape the sandbox and gain network access. It’s by using both techniques that we can provide a safer agentic experience for Claude Code users.

Two new sandboxing features in Claude Code

Sandboxed bash tool: safe bash execution without permission prompts

Today, We're introducing a new sandbox runtime, available in research preview, that lets you define exactly which directories and network hosts your agent can access, without the overhead of spinning up and managing a container. This can be used to sandbox arbitrary processes, agents and MCP servers. It is now available as an open source research preview here: [Github link?]

In Claude Code, we use this runtime to sandbox the bash tool, which allows Claude to run commands within the defined limits you set. These commands are safer by default, they require fewer user permission prompts, so Claude can run more autonomously. If Claude tries to access something outside of the sandbox, you'll be notified immediately, and can choose whether or not to allow it.

We’ve built this on top of OS level primitives such as Linux bubblewrap and MacOS seatbelt to enforce these restrictions at the OS level. They cover not just Claude Code's direct interactions, but also any scripts, programs, or subprocesses that are spawned by the command.

As described above, this sandbox enforces both:

Filesystem isolation, by allowing read and write access to the current working directory, but blocking the modification of any files outside of it.

Network isolation, by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on the domains that a process can connect to, and handles user confirmation for newly requested domains. IAnd if you’d like further-increased security, we alsoeven support customizing this proxy to enforce arbitrary rules on outgoing traffic.

Both components are configurable: you can easily choose to allow or disallow specific file paths or domains.

Sandboxing ensures that even a successful prompt injection is fully isolated, and cannot impact overall user security. This way, a compromised Claude Code can't steal your SSH keys, or phone home to an attacker's server.

To get started with this feature, run: claude --sandbox, and read more technical details about our security model here.

To make it easier for other teams to build safer agents, we have open sourced [XXX]. We believe that other AI companies should consider adopting this technology for their own agents in order to enhance the security posture of their agents.

Claude Code on the web: running Claude Code securely in the cloud

Today, we're also releasing Claude Code on the web, enabling users to run Claude Code in an isolated sandbox in the cloud. Claude Code on the web executes each Claude Code session in an isolated sandbox where it has full access to its server in a safe and secure way. We've designed this sandbox to ensure that sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Codenever enter the sandbox environment. This way, even if the code running in the sandbox is compromised, the user is kept safe from further harm.

Claude Code on the web uses a custom proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates to this service with a custom-built scoped credential. The proxy verifies this credential and the contents of the git interaction (e.g. ensuring it is only pushing to the configured branch), then attaches the right authentication token before sending the request to GitHub.

Getting started

Our new sandboxed bash tool and Claude Code on the web offer substantial improvements in both security and productivity for developers using Claude for their engineering work.

To get started with these tools:

Run `claude --sandbox` and check out our docs on how to configure this sandbox.

Or, if you're building your own agents, check out our open-sourced sandboxing code, and consider integrating it into your work. We look forward to seeing what you build.

To start using Claude Code, you need to set up an API key and follow the documentation provided. This will guide you through the process of making requests and handling responses effectively.

From chatbots to automated content generation, Claude's versatility makes it a valuable tool for businesses and developers alike.

User feedback plays a crucial role in Claude's improvement. By analyzing user interactions, developers can identify areas for enhancement and implement necessary changes.

Related posts

Explore more product news and best practices for teams building with Claude.

Jun 5, 2026

How one Anthropic seller rebuilt his team's workflows with Claude Code
