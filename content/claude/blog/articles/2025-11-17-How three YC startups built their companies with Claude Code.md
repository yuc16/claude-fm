---
title: How three YC startups built their companies with Claude Code
url: https://claude.com/blog/building-companies-with-claude-code
source: blog
published: '2025-11-17'
fetched: 2026-06-13 12:15
---

# How three YC startups built their companies with Claude Code

From non-technical founders winning government contracts to solo devs building at scale, here’s how agentic coding is re-writing the startup playbook.

From non-technical founders winning government contracts to solo devs building at scale, here’s how agentic coding is re-writing the startup playbook.

- November 17, 2025
- 5min

Y Combinator, a startup accelerator, has launched over 5,000 companies that have a combined valuation of over $800B since 2005, including household names like Airbnb, Stripe, and DoorDash.

Today, agentic coding tools like Claude Code are fundamentally changing how YC startups build and scale. Founders can now ship products directly from the terminal, compressing development cycles from weeks to hours and enabling even non-technical founders to compete with established players from day one.

We spoke with three YC startups who demonstrate this transformation in action:

- HumanLayer (F24) built their entire platform and pioneered context engineering practices with Claude Code
- Ambral (W25) is scaling AI-powered account management with sophisticated sub-agent powered workflows built with Claude Code and Claude Agents SDK
- Vulcan Technologies (S25) is using Claude Code to tackle regulatory complexity for the government and industry

Let’s dive in.

Dexter Horthy was building autonomous AI agents to manage SQL warehouses when he noticed a fundamental (but understandable) challenge to agentic adoption: companies weren’t comfortable giving AI applications unsupervised access to sensitive operations like dropping database tables.

That realization became HumanLayer's core insight: often the most useful functions in any software are also the most risky, especially for non-deterministic LLM-powered systems.

"Our MVP was an agent that would coordinate with humans in Slack and could do basic cleanup, like dropping any table that hadn't been queried in 90+ days," Horthy explained. "We weren't comfortable with an AI application running raw SQL unsupervised, so we wired in some basic human approval steps."

In August 2024, Horthy built an MVP, demoed it to different startups across SF, and had his first paying customers.

This progress landed HumanLayer in the YC F24 batch, and the team went all in on providing an API and SDK that lets AI agents contact humans for feedback, input, and approvals across Slack, email, SMS, and other channels.

Through Q1 2025, the HumanLayer team conducted extensive customer discovery, talking to dozens of engineering teams building AI agents and realized there was a gap in the agentic development loop they hadn’t accounted for.

"Every team had rolled their own agent architecture," Horthy explained. "We realized we couldn't just build a better API–we needed to help establish the patterns and principles that would let the ecosystem mature."

This led Horthy to document their learnings in "12-Factor Agents: Patterns of reliable LLM applications." Published in April 2025, the guide went viral and synthesized their experience building production agent systems and highlighted best practices for the emergent discipline of context engineering.

With these learnings in hand, the HumanLayer team started exploring alternative product ideas and pivot angles.

When Anthropic launched Claude Code, Horthy and his team were already strong proponents of Claude models for coding. They immediately began using it to build these experiments.

"We just wrote everything with Claude Code," Horthy said. "When the Claude Agent SDK launched with Opus 4 and Sonnet 4, enabling headless agent execution, we knew this was going to be a big deal."

After months of refining their Claude Code workflows internally, Horthy began sharing them with close founder friends.

"The moment that told me we needed to go all in on this was an all-day pairing session with Vaibhav from BoundaryML (YC W23)," Horthy recalled. "Vaibhav was skeptical at first, but after we spent 7 hours shipping what would normally be 1-2 weeks of work, he was sold. I realized this workflow could work for other teams and other codebases."

Today, HumanLayer's product CodeLayer helps teams run multiple Claude agent sessions in parallel using worktrees and remote cloud workers. They've discovered a critical pattern: once an engineer masters Claude Code, their productivity gains are so substantial that the real challenge becomes organizational—scaling these workflows across entire teams.

"Once you have multiple people on your team shipping AI-written code, you have a completely different type of problem," Horthy explained. "It's a communication, collaboration, tooling, and management problem. You have to rewire everything about how your team builds software."

Since the start of Q4 2025, HumanLayer has closed several large pilots across engineering teams of all sizes to deploy these tools and workflows, all built with Claude Code.

Jack Stettner and Sam Brickman founded Ambral to solve a problem familiar to every B2B startup founder and CRO: as companies scale, the founder-level customer intimacy that drives early growth becomes impossible to maintain.

Whether at early companies experiencing hyper growth or at established enterprise companies, account managers routinely juggle 50 to 100 accounts simultaneously. "You can't give an effective account management experience with 1/50th of someone's attention," Stettner explained. Customer context that once fit in a founder's head scatters across systems, logs, Slack messages, meeting transcripts, and product usage data.

Ambral synthesizes signals from customer activity and interactions into AI-powered models of every account. The system pinpoints who needs attention and why, autonomously driving or recommending expansions while catching early signs of dissatisfaction to prevent churn.

"We're trying to provide the experience of every customer having a one-to-one account manager," Stettner said.

As CTO and sole engineer at this young startup, Stettner relies heavily on Claude Code for development and Claude's Agent SDK to power the product itself. The technical architecture reflects sophisticated understanding of how to extract maximum value from different Claude models.

Stettner has adopted a precise workflow that leverages the strengths of different Claude models in conjunction with subagents:

"I use Opus 4.1 to do research and planning. Sonnet 4.5 has been absolutely killer in terms of being able to then go and implement these plans that I create in Markdown," Stettner explained.

His development process follows three discrete phases:

- **Research phase (Opus 4.1)**: Perform deep research on whatever background is needed for a feature implementation. "I think the most important thing is doing research before you plan," Stettner emphasized. "Have Claude do research for you and create a large, long research document." He uses a series of subagents to research multiple areas of the codebase in parallel.
- **Planning phase (Opus 4.1)**: Create a plan with discrete phases on how to implement the feature. "I'll have Opus create a plan with phases, discrete phases on how to actually go about implementing it, and I'll go revise that plan. Maybe I'll chat with Opus about questions about certain details, or I'll manually update this markdown file."
- **Implementation phase (Sonnet 4.5)**: Execute each phase of the plan systematically. "Then I'll use Sonnet 4.5 to go and implement each phase."

This approach prevailed over the other workflows Stettner tried and was influenced by some of the work Horthy is doing at Humanlayer: "I tried every coding tool, and I experimented with basically every model. I just think Anthropic's models are the best at tool use right now, and that translates to code."

The product itself mirrors this multi-agent approach. Stettner built Ambral's core research engine using the Claude Agent SDK with dedicated sub-agents for each data type.

"I spent a lot of time using the Claude Agent SDK to basically build a very robust research engine that can operate across all of this data," Stettner explained. "It's based around Claude sub-agents, and for every type of data we have a dedicated sub-agent which is an expert in understanding that data."

Whether users chat with the system or Ambral builds automations for customers, everything is backed by the Claude Agent SDK and a series of sub-agents retrieving and reasoning across usage data, Slack messages, meeting transcripts, and product interactions.

The architectural inspiration came directly from Stettner's development experience: "I think how well Claude Code subagents were doing and helping me do development is what inspired me to basically want to take those same sub-agents and use it for the research engine in the product itself."

For Tanner Jones, CEO and co-founder of Vulcan, Claude Code's impact extends far beyond productivity—it constitutes the democratization of company building. Founding their startup, the Vulcan team believed there had to be a product that could make government work better for citizens. That vision would have remained impossible without Claude Code because neither founder had an engineering background.

Vulcan tackles a problem that's been accumulating for centuries: regulatory code complexity. Virginia's House of Burgesses, the oldest continuous democratic institution in the world, exemplifies this challenge. Regulatory buildup over 400+ years has created one of the most nuanced and complex codes in the U.S.

When Aleksander Mekhanik and Tanner Jones co-founded Vulcan in April 2025, neither had a traditional engineering background. Mekhanik studied ML and mathematics in college, and Jones' last programming experience was an AP JavaScript class in high school where they wrote code with pen and paper. Yet the duo built a prototype of their first product for Virginia's governor's office by May 1st—and won the contract over established consulting firms.

"The entire prototype was made using Claude," Jones explained. "This was pre-Claude Code. It was literally copy-pasting scripts into the web app, swapping out methods." After building the prototype, they hired their CTO, Christopher Minge, who had experience working at Google on Gemini and Waymo. Then, when Claude Code launched in June, the trio’s velocity multiplied again.

Vulcan's AI-powered regulatory analysis helped reduce the average price of a new home in Virginia by $24,000, saving Virginians over a billion dollars annually by identifying redundant and duplicative regulatory requirements. Virginia’s governor loved Vulcan’s work so much that he signed Executive Order 51, mandating that all state agencies use “agentic AI regulatory review.”

For Jones, Claude Code's impact goes beyond productivity metrics.

"If you understand language and you understand critical thinking, you can use Claude Code well," he said. "I actually think there might be some marginal benefit for people who studied humanities, because the medium by which we're communicating with AI is language. If you have a great command of language and are good at constructing well-organized ordinal lists, nested bullet points and well-thought-out processes, your prompts may execute better."

Jones commends Claude Code as a major component of Vulcan’s success: “In four months, with three founders, only one of whom was properly technical, we secured state and federal government contracts and raised an $11m seed round from some of the top VCs. None of this would have been possible without Anthropic’s unbelievable tools.”

Christopher Minge, Vulcan’s CTO with “properly technical” training, experienced his own shift in how he thinks about engineering.

"It feels a little bit like I have a co-worker at Google who I'm giving all of my ideas and tasks to, and they make mistakes frequently, but my role is delegating to several Claude Code instances and getting good at checking for common mistakes and communicating ideas effectively," Minge explained.

These three startups have developed battle-tested approaches to maximizing Claude Code's impact, including:

"Don't make Claude do research while it's trying to plan, while it's trying to implement," Stettner advised. "Use discrete prompts and make those into discrete steps."

This pattern prevents context contamination and allows each phase to focus on its core objective. Start a new Claude Code session for each major phase, passing only the distilled conclusions forward rather than dragging the entire context history.

Stettner's advice for other founders centers on deliberate context management:

"Context is critical. When I've seen output that was unexpected or low quality, it's generally due to a contradiction that I have in a prompt somewhere," he explained. "Be very deliberate in terms of what information you're putting into a system prompt or when you choose to start a new conversation, because you don't want to cloud your context. If there's any contradictions in your prompt, you're going to receive lower quality output."

"Try to scrutinize the chain of thought and watch what it's doing," Jones suggested. "Have your finger on the trigger to escape and interrupt any bad behavior."

This becomes especially important when running multiple instances. Catching a wrong direction early—within the first few tool calls—saves significantly more time than letting Claude Code complete an entire misguided approach.

These three startups demonstrate a fundamental shift in how companies are built with tools like Claude Code. HumanLayer pivoted and scaled while codifying context engineering practices that are now used across the YC ecosystem. Ambral is tackling customer success at massive scale with a lean founding team. Vulcan won government contracts as non-engineers.

Traditional barriers to building software—technical expertise, team size, development time—are giving way to new competitive advantages: clear thinking, structured problem decomposition, and the ability to effectively collaborate with AI.

**Ready to build with Claude Code?** Get started.

Get the developer newsletter
