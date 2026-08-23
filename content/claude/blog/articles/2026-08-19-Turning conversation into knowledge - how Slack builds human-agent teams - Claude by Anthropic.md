---
title: 'Turning conversation into knowledge: how Slack builds human-agent teams |
  Claude by Anthropic'
url: https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams
source: blog
published: '2026-08-19'
fetched: 2026-08-23 16:16
---

# Turning conversation into knowledge: how Slack builds human-agent teams

*A conversation with Jaime DeLanghe, Chief Product Officer at Slack.*

*A conversation with Jaime DeLanghe, Chief Product Officer at Slack.*

- August 19, 2026
- 5min

*This is the second post in our series on building human-agent teams. The **first** shared what we've learned building teams with multiplayer AI at Anthropic. In this article, we share best practices from a company that was thinking about human-agent teams long before AI arrived.*

Jaime Delanghe joined Slack in 2017 to work on search and machine learning, with a mission to turn workplace conversation into institutional knowledge. Now the company’s Chief Product Officer, she has believed from the start that to achieve this goal, people need to work in the open, keeping conversations, decisions, and work in progress in channels anyone at the company can read and search. In her recent essay *The Work is the Conversation*, she makes the same case for agents: The conversation around the work is the context that agents need to be useful and finally help us achieve this decades-old goal of turning scattered knowledge into productivity.

To learn what this looks like in practice at Slack, we talked with Jaime about her best practices for building effective human-agent teams and spreading these new ways of working.

For years, the promise that workplace conversation—the "exhaust" of people working together—would compound into organizational knowledge never materialized.

"I have so many research papers from the early days at Slack that showed that, actually, no, conversation doesn't turn into knowledge," Jaime says. "You wish it did, but really it's just a lot of stuff that just hangs out there and people still have to repeat themselves."

Making sense of all that exhaust simply wasn't humanly possible. Now it's an agent's job.

- **Default to public channels**:- **Ask agents for the reasoning, not just the record**: Instead of searching for what was decided, ask an agent to reconstruct- *why*it was decided, and how the context has shifted since.
- **Widen the surface area**: Tools like Slack and Claude are stitching meetings, emails, calendars, and document repositories together—the more of that context you connect, the less your team repeats itself.

The core rhythm of a human-agent team is a cycle of handoffs. Powered by Claude in Slack, agents handle the production work—drafting, summarizing, monitoring, preparing—and pass the results to a person. The person reviews, decides, and redirects, then hands the work back for agents to carry out the next step.

To see all this in practice, look no further than how Jaime starts her week.

"It’s Monday morning, and I’ve just had my daily briefing that an agent has built for me,” Jaime says.

Also waiting for her review is a recap of the previous week's product workshops with flagged escalations, a report on AI developments across the web, briefings for the day's meetings, and a stale bio she'd handed to an agent to rewrite. At the end of each loop, humans review and make decisions based on the agent’s actions.

- **Start the day with agent-built briefings.**Recaps, escalations, meeting prep, and web roundups are great tasks for agents to drive, with human review.
- **Anchor the work in a shared channel.**Share all work in a shared channel so that humans and agents can triage it together, with humans leading the charge on prioritization.
- **Make lightweight signals actionable.**In Jaime's channel, an emoji reaction adds an item to the list and an agent picks up the task.

Working with a fleet of specialized Claude agents can feel disorienting if your mental model is a one-on-one chatbot. Jaime's approach is social rather than technical: "I like to think that agents are kind of like coworkers."

In the same way that human teammates have roles and responsibilities, agents should also have clear goals and focus areas. "If the value of the agent feels mandated rather than very clearly felt and understood by the people using it, it's really hard to remember what the thing is for,” she says.

**How to put this into practice:**

- **Route routine, transactional tasks to a general agent.**Rather than asking people to remember a specialized tool, train an agent to tackle a repetitive task, like filing a help desk ticket or pulling last week's metrics into a status update.
- **Let value be felt, not mandated.**If people can't articulate what an agent is for, it may be time to retire it.

Slack has recommended public-by-default channels since its earliest days: "You're building a shared understanding, a shared context for all of the work that's going to come next,” Jaime says.

She suggests keeping channels public unless there is a specific reason to gate context and knowledge. The most information agents have to pull from and inform their work, the more effective team mates they’ll be.

Open context compounds—new people onboard into history instead of an empty inbox, and no one repeats themselves. Now agents benefit too, and that context and working memory flows back to humans.

**How to put this into practice:**

- **Keep business-as-usual work in the open.**Make- **Remember your agents read what your team reads.**A private channel is a blind spot for every agent that reports on it.
- **Let psychological safety drive the line.**Once genuinely sensitive material is walled off, the main reason work retreats into DMs isn't secrecy—it's discomfort with being seen mid-process. People should feel confident doing everyday work in the open, rough drafts and half-formed questions included, trusting their coworkers to meet it in good faith. And that openness compounds: "you gain trust by giving trust."

The fastest way to learn a new way of working is to watch a teammate do it. Jaime has seen this at Salesforce, where employees share skills, debugging tips, and workflow tricks in a company-wide channel called *How I Slackbot*, which by her count has thousands of members. In that channel, which is public by default, a trick from a sales process can end up reshaping an engineering process.

Inside Slack, a push to get product managers using Claude "was the most self-organized thing you could possibly imagine." One PM got the developer experience lead to help him get set up, then he wrote up a canvas showing what he did and how he did it. Other PMs copied the format. Teams organized workshops and built their own git repos.

**How to put this into practice:**

- **Stand up a company-wide show-and-tell channel.**Give employees one public place to share skills, debugging tips, and workflow tricks, so a trick from one function can reshape another.
- **Encourage write-ups others can copy.**A short "what I did and how" doc turns one person's setup into a team template or skill.

Since her early days at Slack, Jaime has grappled with the question of how to measure productivity. "Do we want people to send more messages?” she says. “Maybe not. Sending messages might not actually mean that they're getting more out of Slack. More messages can mean people can't find what they need, or can't say what they mean the first time."

Now, the question of measuring the value of AI looks quite similar—and with something that complex, simple metrics don’t do the job. Token usage tells you the lights are on, but while that’s important to know, it’s not sufficient.

**How to put this into practice:**

- **Treat usage metrics as a pulse check, not proof of value.**Activity tells you adoption is happening, not that it's working.
- **Be ready to use your own judgment.**There's no clean way to prove that how people use these tools leads to better business results. As Jaime puts it, connecting the two still takes "a lot of leaps of faith," and no dashboard or usage stat will prove it for you.

Jaime's biggest piece of advice for organizations trying to implement human-agent teams is to reimagine every workflow: "We're going to have to figure out how to change the ways that we're working, not just do more of the same kind of work faster. And that is going to be a team sport."

Her biggest advice for building an effective human-agent team? Start soon, but start small. Bring a group of people into a shared channel with Claude, give them the same set of resources, and let them work. If Slack's experience is any guide, what they build will spread on its own.

Get the developer newsletter
