---
title: How Brex improves code quality and productivity with Claude Code
url: https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
source: blog
published: '2025-10-30'
fetched: 2026-06-13 12:16
---

# How Brex improves code quality and productivity with Claude Code

Learn how Claude Code breaks down barriers between technical and non-technical teams by making programming easier and more accessible.

94%

Learn how Claude Code breaks down barriers between technical and non-technical teams by making programming easier and more accessible.

- October 30, 2025
- 5min

When Andy Reed joined Brex as a content designer two years ago, he never imagined he'd be writing code and building Figma plugins.

"I don't know how I would have gotten even half my work done in the past month without Claude Code," Reed said.

But that's exactly what happened when Reed embraced Claude Code, Anthropic’s agentic coding solution—and his story is just one example of how the intelligent finance platform is transforming the way their company works.

To learn more, we spoke with three Brex team members about how they’re using Claude Code:

- Hércules Gimenes, Software Engineering Lead on the Product AI team
- Sumeet Marwaha, Head of Data & Analytics
- Andy Reed, Senior Content Designer

What emerged from these conversations wasn't just a story about productivity gains, though teams report 3-4x improvements on specific tasks. It's about fundamentally reimagining how the company works together to streamline workflows, inspire creative problem solving, and drive collaboration at scale.

For Hércules Gimenes and the Product AI team, Claude Code represented something more profound than a new tool.

"Claude Code offers a mindset shift," he explained. "Instead of being in the driver's seat, you're the reviewer of the changes that Claude introduces. You're guiding the vision and direction."

This shift has redefined what "writing code" means at Brex—a reflection of the company’s AI-first principles in action. Rather than spending time on implementation details, engineers now focus on architecture and problem-solving. The result? Better code, not just faster code.

"I don't think I save time using Claude Code," Gimenes said. "I refine the problem itself much more. You can try three approaches for the same problem during the same amount of time, and after the third approach, you have a much clearer understanding and a much cleaner interface."

While the Product AI team was discovering new ways to iterate on code quality, Reed was experiencing his own revelation.

As a content designer, he found in Claude Code something unexpected: independence.

Previously, updating a simple string meant filing a ticket and waiting for an engineer. Now, Reed makes PRs directly, but the real transformation came when he tackled a project that had been on the backlog indefinitely: integrating comprehensive content guidelines into every component of Brex's design system.

"It would have taken me probably weeks if not months doing it manually," Reed explained. Using Claude Code, he completed the project in a few days, systematically adding content-specific guidelines pulled from internal style guides, accessibility standards and external best practices.

The impact rippled across teams. Engineers and designers now have content guidelines embedded directly in their tools, eliminating the need for constant cross-referencing and reducing errors before they happen. It’s a small but powerful example of intelligent finance at work: systems running in the background, allowing people to focus on higher-value, creative work.

Meanwhile, Sumeet Marwaha's Data & Analytics team was solving a different but equally important challenge: making data accessible to everyone at Brex, not just SQL experts.

The team built Brex Explorer, a text-to-SQL interface powered by Claude Code and MCP servers. Now, a sales manager can ask in plain text: "How many customers exist with over $10 million in their Brex account in Jacksonville, Florida and were onboarded in the last year?" The system translates the query, runs it and summarizes the results.

The real multiplier effect came from their AI data engineering agent. Tasks that previously required specialized knowledge, like adding data tables with all the necessary file edits and test configurations, can now be completed by any engineer.

"It's like a 4x speed increase across maybe 2x more people that are contributing," Marwaha noted. Claude Code has seen 50% adoption across the org, with Marwaha hoping to reach 100% adoption by month's end.

As teams across Brex adopted Claude Code, surprising use cases emerged. During a company hackathon, Gimenes used Claude Code's headless mode to build a sophisticated submission agent in just a few hours, something that would typically take days of development.

Reed discovered he could now build tools he never imagined creating, like a Figma plugin that automatically reviews designs against Brex's standards. "It feels like I have the world's best intern," he said.

But perhaps the most significant unexpected benefit has been Claude Code's role as an organizational knowledge repository. With Brex's complex monorepo structure using Kotlin and Bazel, understanding how different systems connect has always been challenging. Now, Claude Code serves as an "oracle" that can answer questions about codebase functionality instantly.

"Traditionally, a design meeting would involve talking about how something should work, but nobody really understands how the sausage was made," Reed explained. "Now I've got the oracle sitting on my other monitor."

As Claude Code adoption spread across Brex, teams developed best practices that have become standard:

- **Structured Context Management**: Each major directory in the monorepo now has its own CLAUDE.md file containing domain-specific context. New engineers can understand Mastercard integration details or banking regulations without relying on tribal knowledge.
- **Automated Documentation**: The Product AI team implemented CI/CD checks that verify when code changes might outdate documentation, prompting updates. "Having up-to-date documentation is something you can trust—it's so powerful," Gimenes emphasized.
- **Context-Aware Commands**: Teams created custom commands that automatically load relevant context. The /submit-pr command, for instance, fetches git status, recent changes, and related PR information before executing.
- **Start with Discovery**: "Being able to find what you need is not really stored in some staff engineer's brain anymore," Marwaha observed. "It's in the codebase, accessible to everyone."

Teams at Brex are already planning next-generation applications:

- The Data team is preparing to tackle previously untouchable projects, like analyzing trillions of credit card transaction itemization data points, work that was too tedious to justify before Claude Code made it feasible. They're also developing role-specific agents, including one to power RevOps tasks.
- The Product AI team envisions more sophisticated context management, where documentation updates itself automatically and context remains decentralized yet accessible.

From content designers building technical tools to data analysts democratizing access, Claude Code has become what Gimenes calls an “everything tool” — useful for integrating Brex’s domain knowledge with external best practices.

It also highlights a powerful duality: the intelligent finance Brex delivers to customers, helping them spend smarter and move faster, is the same philosophy that shapes how Brex teams work internally, empowering every employee to build with speed and confidence, regardless of their technical background.

Learn how financial organizations like Brex drive productivity with Claude Code.

Get the developer newsletter
