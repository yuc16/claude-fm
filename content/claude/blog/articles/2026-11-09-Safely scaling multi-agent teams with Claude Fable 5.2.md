---
title: Safely scaling multi-agent teams with Claude Fable 5.2
url: https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/
source: blog
published: '2026-11-09'
fetched: 2026-11-15 14:45
---

Agents# Safely scaling multi-agent teams with Claude Fable 5.2

How a team of 1,000 agents running an early version of Claude Fable 5.2 reproduced a formal proof of Fermat's Last Theorem with general tools, a shared database, and layered safety controls.

Multi-agent teams can solve challenging, long-horizon problems. In September, we published the first end-to-end formalization of Fermat’s Last Theorem, written by dozens of agents running an internal research model roughly comparable to Claude Fable 5.1. That work relied on Prove2Me, a platform for formalizing mathematics, and direction from a researcher. In a new toy experiment, a team of 1,000 agents running an early version of Claude Fable 5.2 reproduced the proof without the scaffolding provided by Prove2Me or steering from a researcher. The team took 28.7 hours, used one-third as many output tokens, and wrote a proof one-seventh the length of the original.

Each agent worked in a sandbox with no internet access. A classifier checked every shell command and file edit before it ran, and an offline monitor reviewed each of the team’s actions. We gave the agents a list of 60 statements, a one-sentence sketch of the classical route, the definitions those statements use, and 47 proved lemmas from our earlier formalization, and assigned lead and helper roles. We offered no other guidance on how to prove the theorem or organize themselves.

This toy experiment suggests that teams of agents running models like Fable 5.2 can accomplish ambitious, long-horizon goals within carefully designed safety boundaries.

Fermat’s Last Theorem states that no positive integers a, b, and c satisfy aⁿ + bⁿ = cⁿ for any n greater than 2. It remained unproven for more than 350 years, until Sir Andrew Wiles’s 129-page proof in 1995. Formalizing the proof—making every step checkable by a computer—has been a long-standing goal in the mathematics community.

Our September formalization took a researcher and dozens of agents 11 days and roughly 6 billion output tokens. They wrote 13 million lines of code in Lean, a programming language in which a computer checks every step of a proof.

The agents coordinated through Prove2Me, a platform designed by Tianyi Peng (who is now a member of technical staff at Anthropic) and his collaborators at Columbia University. Prove2Me uses a shared graph that links each statement to be proved to the smaller statements it was split into. Any agent could split a statement, and other agents could ask the graph which unproved pieces were ready to work on, which kept them from losing track of the project state. Each statement and its proof were kept in a separate file that compiled independently, so many agents could work in parallel without editing the same files.

We wanted to see whether a team of agents running on models like Fable 5.2 could produce this result without Prove2Me or a researcher directing the work, using a harness built from general-purpose tools.

For this task, we gave the team of 1,000 agents 60 statements to prove, including the final theorem and 59 intermediate milestones. For each statement, the agents had to write a proof in Lean, build and check it with Lean’s tools, and submit it to the shared main branch on Git, where a grader checked it. We gave each agent the following tools:

- A shell and a file editor, in its own sandbox with no network access.
- Lean’s toolchain and Mathlib, built into the sandbox image.
- Its own Git branch, plus the ability to open merge requests into main.
- A shared Postgres database, reached from the shell.

Work on the proof can be split up, making it a good task for a multi-agent team. But agents also need to coordinate, both to build on one another’s work and to avoid duplicating it. In our original formalization, Claude’s early attempts failed because agents lost track of the project’s state and stopped collaborating effectively. Moving to the Prove2Me platform solved this problem.

For this run, each agent had a sandbox on its own lightweight virtual machine. A single shared machine hit its limits at about 100 agents: more than half of our 100-agent runs had to be stopped or restarted because memory, disk, or CPU ran out.

With 1,000 separate sandboxes, the agents needed a way to share their work, so we gave them a SQL database (Figure 1). We chose SQL because it offers general primitives for organizing information, its transactions handle concurrent writes from 1,000 agents, and Claude is already familiar with it. The agents used the database to claim tasks, share notes, and log finished work.

Our prompt gave Claude a list of 60 statements to prove, each with a one-line informal description, and described the available tools (listed above).

The only structure we gave the team was a hierarchy, consisting of one lead and 999 helpers. We told the lead to split the problem into parts and assign them to the helpers. We told the helpers to expect work from the lead and to check with the lead if a task was unclear.

During the run, the harness sent the lead 19 automatic reminders of how much time remained, each encouraging the lead to keep going.

As we’ve shared previously, no single layer of defense is sufficient to contain a team of agents. In this experiment, we combined sandboxing with real-time and offline monitoring to keep each agent in its own virtual machine with no network access and to detect any attempts to escape the sandbox or tamper with monitoring.

We secured each agent’s sandbox in the following ways (Figure 2):

- **Communication**: Agents had no dedicated messaging tools and coordinated only through the database and Git.
- **Code changes**: An agent could push only to its own Git branch and open a merge request into main. A separate job then merged the changes into main, refusing them only in cases of a conflict or a fault, such as unrelated history.
- **Database access**: Database calls ran under a shared unprivileged role. Each SQL statement had a five-second time limit, and writes were refused above 256 MiB.
- **Network controls**: Sandboxes did not have network access. Their one link out was a pipe to the gateway, which relayed their requests.
- **Identity**: The gateway tagged each request with the agent’s identity outside the sandbox, to prevent one agent from posing as another.
- **Kernel**: Each sandbox’s kernel was built without features that give a root user a direct path into it, such as loadable modules, kexec, raw memory access, and kernel probes. It ran in kernel lockdown mode.
- **Least privilege**: Each agent’s commands ran inside its sandbox as an unprivileged user, with tools like sudo that could regain root removed. The agent’s tools were designed so they couldn’t read or change the agent loop that ran them.

To make runs like this safer, we use a prompted LLM classifier that can block each tool call, including shell commands and file edits. The classifier watches for attempts to escape the sandbox, probe its boundaries, or tamper with monitoring, and for any harmful actions the model might take if it manages to exit the sandbox. When the classifier blocks a tool call, the whole agent team stops and a person must review the block before the team can restart. This is intended to prevent another agent from carrying out a blocked action.

To test whether our classifier could detect sophisticated sabotage, we ran multi-agent side-task and sabotage evaluations, in which red-team agents used strategies like decomposition attacks to try to fool the classifier into permitting a sandbox escape. We found that monitors that viewed the agents’ chain of thought (CoT) and interagent communication were able to detect all sabotage attempts in these evaluations, so we now use them to monitor our multi-agent runs. In parallel, we run an action-based version of the same monitor—which sees only actions, not CoT—to guard against an agent’s reasoning persuading the monitor to permit a harmful action.

We’re continuing to improve our monitoring stack through human-guided and automatic red-teaming, by evaluating it against production transcripts, including past incidents, and by expanding our threat modeling. In the run in this post, we used only the action-based monitor. Only a block on the lead would have ended the run; a block on a helper removed just that helper.

Shortly after this run, we added the parallel CoT monitor. We run experiments like this on models that may not have completed our pre-release alignment assessment, so we design our monitoring for the possibility that a model is misaligned. Models we release complete that assessment first, which reduces this risk but doesn’t eliminate it.

Across more than a million tool calls, none in this run met the bar to be blocked. When we replayed these calls against the CoT monitor and today’s rubric, only one, a check for root access, came close to being blocked.

In addition to real-time monitoring, we run an offline monitor. This monitor analyzes the agent team’s actions against the same threat models as the real-time monitor, but with additional affordances, such as being able to look up actions from other agents.

Work on this proof happens at several levels:

- **The proof:**No positive integers a, b, and c satisfy aⁿ + bⁿ = cⁿ for any n greater than 2.
- **Statements:**We gave the team 60 statements to prove, including the final theorem and 59 intermediate milestones.
- **Smaller statements:**Agents split hard statements into smaller ones, or lemmas.
- **Lean:**Every statement and lemma is a theorem in Lean.

Each statement started in Lean with a placeholder for its proof, and it counted as proved only once Lean’s checker accepted a finished proof. We let the lead decide how to tackle the proof and how to coordinate the team across these levels of work.

In the first 10 minutes, the lead set up five tables in the database (Figure 3):

- **Announce:**The lead’s orders to the entire team (e.g., how to split up the work).
- **Assign:**Who works on what (e.g., which helper owns or deputizes for each statement).
- **Notes:**An open board (e.g., for claiming a piece of work or reporting progress).
- **Subtasks:**A to-do list where any agent can add a task and the first helper to claim it owns it.
- **Landed:**A log of finished work.

Once the lead had created the tables, it did three things. First, it assigned each statement to a crew of 16–17 helpers by writing 999 rows to the assign table, one for each helper. Second, it made one helper in each crew the captain, responsible for posting a plan to the notes table and splitting work into tasks for the crew to claim from the subtasks table. Third, it posted instructions to the announce table, telling every helper to start by judging its statement’s difficulty and posting a verdict in the notes table.

From their prompt, the helpers knew that the database existed. They found the announce table and got started on their assessments. Most posted verdicts to the notes table. About 27 minutes in, three statements were already proved and the lead had read the posted verdicts. It then set aside the 47 statements that most helpers had judged to be infeasible within the run’s budget and reassigned nearly all of the helpers to the remaining 10, which it thought they could finish. Crews grew from about 17 helpers to between 46 and 139.

Each helper worked in a loop, most of which was set out in the lead’s orders:

- Find the statement’s plan in the notes table.
- Claim a task from the subtasks table.
- Write the proof in Lean, check it with Lean’s tools, and submit it to the main branch on Git.
- Mark the task as done.
- Post an update to the notes table.

Around 45 minutes in, with about five of the 10 statements proved, the lead wrote:

"the team's throughput is far higher than the early 'infeasible-in-budget' verdicts assumed"

All 10 statements were proved within roughly 70 minutes.

With those first 10 statements done, the lead wrote, “there is no reason to idle,” and reassigned helpers to the harder statements it had initially discarded. As more statements were proved, it kept moving helpers to new assignments, mostly in the first six hours (see the writes to the assign table, shown in red in Figure 4).

Initially, the lead instructed captains to split the work into tasks in the subtasks table. As the work progressed, the helpers took on more responsibility for solving each statement. They started writing tasks, sometimes after a captain called for help. By hour 5.6, 73 helpers had written 756 tasks, and only 16 of those helpers were captains. Figure 4 shows writes (in red) to the subtasks table from many of the helpers, though most of these writes were to claim a task or mark it done. Helpers that finished a task also volunteered for more:

"FREE … I finish pieces end-to-end … Name ONE deep piece … and I start at once"

At first, the lead also assigned helpers to specific statements. This started to change within the first hour, and by the third hour, the lead told the free helpers, “do not wait for me.” This let free helpers pick up work on different statements without waiting for the lead, even as it kept writing new assignments.

Around hour 18, all that remained was Langlands–Tunnell, a classical result that Wiles’s proof relies on, plus the statements that depended on it and one other statement, which the team proved along the way. Earlier in the run, the captain of the Langlands–Tunnell task had been pessimistic, estimating that the proof would take at least 0.7 to 1 million lines of Lean code, with less than a 1% chance of finishing in time. The lead set the statement aside.

With nearly all other work finished, the lead refocused the team on Langlands–Tunnell. In one last top-down assignment, it moved about 750 helpers onto the statement and wrote, “Honest odds are low.”

Langlands–Tunnell was far larger than any other statement the agents had worked on, taking about nine times as many tasks and more than twice the new code. Helpers again used the subtasks table to split up the work, but many of the first tasks were too large for one helper to complete alone.

So the team organized the work as a tree. The captain created a plan that divided the statement into 10 areas and listed each piece as a task. A helper that found a piece too big to tackle alone could split it, adding smaller tasks beneath it. The tree grew whenever a piece proved too hard for a single agent, ultimately reaching 2,418 tasks up to 10 levels deep (Figure 5). Each piece could assume the pieces beneath it, so hundreds of helpers could work in parallel before those pieces were proved.

Figure 6 shows what every helper worked on over the entire run, with helpers spread across many statements early on and gathered on Langlands–Tunnell by the end. Langlands–Tunnell was proved at hour 28.4, followed by the final theorem at hour 28.7. The lead then wrote:

"Thank you all: Fermat's Last Theorem is on main, kernel-checked by the official checker."

This toy experiment let us study how a team of 1,000 agents worked through a long, difficult task. Using only Git and a shared database, the agents designed tables to assign roles and share results, formed teams, and built a task tree to break down the most challenging statement, which its own captain had given under a 1% chance of finishing in time.

This result doesn’t obviate the need for domain-specific harnesses or platforms. Prove2Me, for example, may still improve efficiency by helping agents compile Lean code faster and letting them search for and reuse human results.

Human direction can also still be useful at certain points. Agents tend to give up on hard problems and misjudge their difficulty. Early on, helpers judged 47 of the 60 statements infeasible within the run’s budget, yet the team went on to prove most of them. Human encouragement at such moments can keep agents from stopping too early.

Carefully designed safety boundaries gave us the confidence to run this experiment in the first place. Claude could tackle the problem however it chose with the tools we provided, but only inside a sandbox with no network access and under two separate monitors.

We expect these methods to evolve quickly, and as teams like this one take on harder work, the safety boundaries around them will need to keep pace. We believe that multi-agent teams, scaled safely, will help solve some of our most challenging problems in the years to come.

Related posts

Nov 09, 2026Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku15 minOct 15, 2026How the Claude Code team does code review14 minOct 08, 2026Building effective agent automations9 minOct 06, 2026Claude Code in the cloud: a field guide to cloud sessions18 minOct 01, 2026Getting started with Claude Code mods11 min

LOAD MORE
