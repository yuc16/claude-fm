---
title: Which Claude model should you build with?
url: https://claude.dev/blog/which-claude-model-should-you-build-with/
source: blog
published: '2026-11-09'
fetched: 2026-11-15 14:53
---

Playbooks# Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku

Which Claude model to pick, what they cost, and how to use them together.

The current Claude lineup has four generally available models: Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5 and Claude Fable 5.2. Claude Mythos 5.2 is our most capable model for cybersecurity and life sciences research, available through our verification programs.

If you build on the Claude Platform or work in Claude Code, you may be wondering which model to use for your common tasks. This article will help answer that question and how to think about the trade-offs.

The quick answer is that you should start most work on Opus 5.5 at its default effort level, `medium`.

There's a reason it's the default model in Claude Code. It costs half as much per input and output token as Fable 5.2, and it's the model we recommend starting with for most coding and knowledge work.

From there:

- Move down to Sonnet 5.5 for well-scoped everyday work, like a bug fix or a feature built against a spec. Just because you have a clear spec doesn't mean you should use Sonnet, though. A migration or a performance optimization can have clear specs and still be difficult enough to warrant Opus 5.5, or Fable 5.2 for a major one.
- Move further down to Haiku 5.5 for the simplest high-volume work, such as classification, routing, and extraction. Haiku 5.5 is also good to use with subagents that work on a larger model's side tasks.
- Move up to Claude Fable 5.2 for the hardest technical projects in coding, finance and the sciences. Also move up when Opus 5.5 at `high`still falls short, or for long unattended runs.

Before you move models, try adjusting your effort level. It's a finer dial for both cost and capability. Past `high`, one more effort level can cost as much as a bigger model, so compare both on your own work. If you're past `high`, test the next model up at a lower effort instead. Conversely, one level down can get you the result you need at a lower rate.

Higher effort helps when the model needs to think longer, call more tools, or check its own work more. Just keep in mind that it also adds latency. Additionally, moving to a higher effort level won't give a model knowledge or skill it doesn't have. For that, you still need to move up a model.

| Task | Starting model | Starting effort | Why | 
|---|---|---|---|
| Everyday engineering and debugging. Multi-PR feature work | Opus 5.5 | `medium`(default), then`high` | Balance of cost and capability for everyday tasks. | 
| Classification, routing, tagging, and high volume extraction | Haiku 5.5 | `medium`(default) | Lowest cost and latency in the model family. | 
| Subagents that search files, read logs, or summarize | Haiku 5.5 or Sonnet 5.5 | The model's default | Wrong answers are cheap to spot, and the main model has the judgment calls anyway. | 
| Chat and interactive sessions | Sonnet 5.5 (or Haiku 5.5 for simple chat at volume) | `low`or`medium` | Sonnet 5.5 is fast, especially on `low`or`medium`effort. | 
| Well-scoped coding, like bug fixes, feature iteration, and spec driven work | Sonnet 5.5 | `medium`, then`high`for harder tasks | It handles scoped tasks well at half the Opus 5.5 token price. | 
| Everyday documents, slides, and spreadsheets | Sonnet 5.5 | `high`(default;`medium`in Claude Code) | It iterates fast and has a strong eye for design. For a complex financial model, or a document built from a large pile of source material, start on Opus 5.5. | 
| Agent tasks you run repeatedly such as investigation, review, or drafting | Sonnet 5.5 | `medium` | Well-defined, repeated tasks rarely need a bigger model. | 
| Computer use and vision-heavy workflows | Opus 5.5 | `medium` | These runs are long agentic loops over many screenshots and images, the kind of long-running agentic work Opus 5.5 is built for. | 
| Major refactors and migrations, architecture planning, and leading many subagents | Fable 5.2 | `medium`, then`high`(the API default is`high`) | It's Anthropic's most capable generally available model for technical fields. | 
| Deep research, and scientific or quantitative analysis | Fable 5.2 | `medium`, then`high`(the API default is`high`) | It's built for the hardest technical projects in coding, finance and the sciences. | 
| You aren't sure yet | Opus 5.5 | `medium`(default) | Claude Code uses it by default on Pro, Max, Ultra, Team, Enterprise and the Anthropic API, and the platform docs recommend it as the starting point. |

| Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.2 | |
|---|---|---|---|---|
| Built for | High-volume, cost-sensitive tasks | Fast, capable help with well-scoped tasks | Our daily driver for complex coding and knowledge work | The most ambitious, open-ended technical work | 
| Relative latency | Fastest | Fast | Moderate | Moderate | 
| Input / output, per million tokens | $0.10 / $0.50 for prompts up to 100K tokens, $0.50 / $2.50 over 100K | $2 / $10 | $4 / $20 | $8 / $40 | 
| Cache reads, per million tokens | $0.01 up to 100K, $0.05 over 100K | $0.10 | $0.20 | $0.20 | 
| Context window | 1M tokens | 1M tokens | 1M tokens | 1M tokens | 
| Max output | 128K tokens | 128K tokens | 128K tokens | 128K tokens | 
| Thinking on the API | Adaptive, on by default, and you can turn it off | Adaptive, on by default; `between_tools`skips upfront thinking | Adaptive, always on | Adaptive, always on | 
| Default effort on the API(Claude Code can differ;`/effort status`shows yours) | `medium` | `high`(`medium`in Claude Code) | `medium` | `high`(`medium`in Claude Code) | 
| Fast mode | No | No | Yes | Yes |

Prices are Claude API list prices. For benchmark results, see the Fable 5.2 page.

When you choose between models, you're making a trade-off. When you pick a larger model, for example, you are choosing capability over latency. These are the main trade-offs to think through.

Generally, bigger models cost more per token and are more capable, but the cost vs capability trade-off isn't universally true at the task level.

A higher price per token doesn't always mean a higher cost per task, or a better result. As we showed in Spending your effort, on Anthropic's runs of Terminal-Bench 3.0, the previous Fable, 5.1, at `max` scored 58.0%, while Opus 5.5 at `high` scored 58.9% with half the tokens.

On the hardest work, the price gap can close. On FrontierCode 2.0, Fable 5.2 at `high` scored about level with Opus 5.5 at `max` (45.3% vs. 45.5%) for roughly half the cost per task. So before you raise Opus 5.5 past `high` on a hard task, test Fable 5.2. For everyday work, Opus 5.5 at `medium` is still the place to start. For benchmark results, see the launch post.

However, the Claude Platform's cost and intelligence measurements also show the limits of a small model. These generally do well on high-volume work with checkable outputs and are less suited to long agentic loops.

When you compare two models, price the hardest tasks in your set as well as the typical ones, because the hardest tasks carry most of the spend. On one 20-problem search benchmark, two problems carried 43% of the spend.

A faster setup finishes sooner and can miss more. Think through how long a person can wait before you pick your model and effort level. For replies a person waits on, start Sonnet 5.5 at `low` or `medium`.

Often next generation models are faster than their predecessors. Fable 5.2 generates output up to 30% faster than Fable 5.1. Sonnet 5.5 runs 30% faster than Sonnet 5.

Effort level and latency are roughly correlated. Determine if the accuracy you gain is worth the extra latency. For example, on SWE-bench Pro, Opus 5.5 at `medium` scored about 2.5 points lower for about 70% of the cost as the `high` effort setting. At `low` it scored about 8 points lower for about a third of the cost. At `xhigh` it scored about 1.4 points higher for 2.5 times the cost of `high`.

Often providing a means of self-verification is more cost effective and adds less latency than changing effort levels. When a model isn't good enough for a task, take these steps in order:

- Check that the model can verify its own work, with a test, a build or a script that calls the endpoint.
- Raise effort one level.
- Move to the next model up, starting at a lower effort level than you used on the smaller one.

If you can check outcomes automatically, run everything at a low level and re-run only the failures at a high one. On the same SWE-bench Pro subset, Opus 5.5 at `low` with failures re-run at `high` passed about 97% of tasks for about $0.17 each, against 95.3% for $0.29 with every task at `high`.

If you need a faster reply from the same model, you can pay for speed instead of giving up capability. On the Claude API, Opus 5.5 and Fable 5.2 both offer fast mode, with higher output speed at premium pricing.

Every model in the current generation has a 1M-token context window. Large context can help the model complete the task but it costs you on every turn, because each turn resends it. That being said, on long runs most of your input bills as cache reads.

Opus 5.5 charges $0.20 per million tokens for a cache read, and Sonnet 5.5 charges $0.10. Fable 5.2 charges the same $0.20, so on a long, cache-heavy run the gap between Fable and Opus comes down to uncached input and output, where Fable costs twice as much per token.

In What a task costs on Opus 5.5, a turn's cache read costs about $0.03 at 150K tokens of context. At 20K it costs about $0.004.

One takeaway from this is that a lean main context matters more the bigger the main model is. Keep the expensive model's context for the decisions, and let cheaper subagents do the verbose reading.

Haiku 5.5 is the only model where the token price varies by prompt length. A prompt of up to 100K tokens bills at the lower tier, and a prompt over 100K bills at five times that rate. The long-prompt tier still costs a quarter of Sonnet 5.5's per-token price. So Haiku 5.5 pays off most on short prompts, where it costs a twentieth of Sonnet 5.5's input price.

When every call needs a long prompt, compare Haiku 5.5 with Sonnet 5.5 on cost per finished task, not list price.

The prompt cache belongs to the model that wrote it. Your first turn on a new model pays the cache-write price on the whole conversation. To make that turn smaller, run `/compact` first in Claude Code, or start a fresh session with a short written plan. On the API, open the new model's conversation with a summary of the work so far instead of the full history.

Each thinking block records the model that produced it, and each model reads only some other models' blocks. On the Claude API and Claude Models on Google Cloud (Google managed), Opus 5.5 reads Sonnet 5.5's and Haiku 5.5's thinking blocks. Sonnet 5.5 reads Haiku 5.5's. Fable 5.2 reads Opus 5.5's, Sonnet 5.5's and Haiku 5.5's. On the Claude API, Fable 5.1 reads Opus 5.5's.

A move down a tier loses the earlier reasoning, because a model never reads the blocks of a model above it. Other moves can lose it too. When the new model can't read the earlier model's thinking blocks, the API drops them and the request still succeeds. The new model then works without that reasoning.

Preserved thinking lists every case. A move from Fable 5.2 to any other generally available model drops its reasoning.

A subagent runs in its own context window and hands back a summary. You pay for its tokens at the rates of the model it runs on. In Claude Code, set `model: haiku` or `model: sonnet` in a subagent's definition. The `CLAUDE_CODE_SUBAGENT_MODEL` environment variable sets the default for subagents that don't specify a model.

Save this as `.claude/agents/log-reader.md`:

CODEMarkdown

--- name: log-reader description: Reads test output and logs, and reports each failing case. Use after a test run. tools: Read, Grep, Glob, Bash model: haiku --- Read the logs you're given. For each failure, report the file, the test name and the first error line. Don't edit any files.

Keep small models on work where a mistake is cheap to spot, like finding files, running tests and reading logs. Keep code edits and judgment calls on the main model. When a small model misreads a search result, the main model opens the wrong file and spends tokens on it.

In current versions of Claude Code, the built-in Explore subagent runs on your session's model instead of always running on Haiku. On the Claude API, that model is capped at Opus. To keep exploration cheap, define your own subagent named `Explore` with `model: haiku`. You can pin the model the `haiku` alias uses with `ANTHROPIC_DEFAULT_HAIKU_MODEL`.

On the Anthropic API, the `haiku` alias now resolves to Haiku 5.5, which needs Claude Code v2.1.293 or later. On Amazon Bedrock, Google Cloud, Microsoft Foundry and Claude Platform on AWS, it still resolves to Haiku 4.5. Claude Code's model configuration docs have the details.

Claude Code also has the `opusplan` alias, which plans with Opus in plan mode and then carries out the plan with Sonnet. That puts your code edits on Sonnet. The advice above does the reverse. It keeps code edits on the main model and gives smaller models only work where a mistake is cheap to spot. Measure `opusplan` on your own tasks before you make it your default.

The advisor tool (beta) pairs a faster, cheaper executor model with a stronger advisor model. The executor runs the task and can ask the advisor for guidance partway through. Most of the tokens bill at the executor's rate. The advisor helps only when it adds capability the executor lacks and the executor asks for advice, which it does less often at low effort.

Where it might pay off: agentic work where most turns are routine. The platform's cost guide is cautious: of the four pairings in its advisor table, none clearly beat its executor alone, and an advisor can help only when the executor consults it. Measure your executor's consult rate first. Check which advisors your executor accepts. A Sonnet 5.5 executor accepts Fable 5.2, Opus 5.5, Opus 5 and Sonnet 5.5, for example, and a Fable 5.2 executor accepts only Fable 5.2 or Mythos 5.2.

Where it adds little: one of those pairings was an Opus 5.5 executor at `high` with a Fable 5.1 advisor on an internal coding benchmark. It scored 90.1% at $2.92 per attempt. That's 1.7 points over Opus 5.5 alone at `high` for about 2.1 times the money. A gain that size is at the edge of run-to-run noise, and about what raising effort would have bought.

Subagents, above, handle side tasks while one main model keeps the thread. This pattern is for work bigger than one context window. A top-tier model leads, splits the task, hands the pieces to many cheaper workers in parallel, and merges what comes back. On an internal defect-search benchmark over about 22 million tokens of source code, an Opus 5.5 lead over Sonnet 5.5 workers, up to 25 at a time, cost about a third less than Opus 5.5 alone at its default effort. It scored about the same.

On the Claude Platform, multiagent orchestration in Claude Managed Agents gives you a coordinator agent and a roster of workers. Skip it for one chain of dependent steps or for work that fits in one context window. There, the planning and merging cost more than they save. When to fold subagents into your main agent loop covers when one agent loop beats a team of subagents.

Model choice is mostly a question of capability and cost, but you can't always change the model name and nothing else. Every current model supports tool use and image input, but there are differences to test before you move a request from one model to another.

- **Fable 5.2 extends preserved thinking to every API account.**The API rejects a request with a 400 error when anything before a Fable 5.2 thinking block has changed, including the system prompt, the tools or an earlier message, unless you opt in to dropping the affected thinking. If you build requests through Claude Code, the Claude Agent SDK or Claude Managed Agents, you don't need to change anything. If your own code edits history, keep it append-only, and test before you switch.
- **Thinking.**Opus 5.5 and Fable 5.2 always think, and a request that turns thinking off returns an error. Sonnet 5.5 thinks by default, and- `between_tools`limits thinking to the gaps between tool calls. Haiku 5.5 thinks by default, and you can turn thinking off at- `high`effort or below. On all of them, read content blocks by- `type`, because a response can begin with a thinking block.
- **Forced tool use.**A- `tool_choice`of- `any`or- `tool`returns a 400 error on Sonnet 5.5, Opus 5.5 and Fable 5.2. Send- `auto`, mark the tool- `strict: true`, and say in the prompt when to use it.
- **Computer use.**Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2 support computer use only through the- `computer_toolset_20260801`toolset on the Claude API and Claude Models on Google Cloud (Google managed).
- **Haiku 4.5 to Haiku 5.5.**Replace- `budget_tokens`with an effort level, and drop non-default- `temperature`,- `top_p`and- `top_k`values, which return a 400 error. End- `messages`with a user turn, because a final assistant turn for the model to continue also returns a 400 error.
- **Safety fallbacks.**Opus 5.5, Sonnet 5.5 and Fable 5.2 run safety classifiers that most often flag cybersecurity and biology content. In Claude Code, a flagged request can re-run on an older model, and a notice in the transcript tells you which. Fable 5.2 keeps the fallback models that Fable 5.1 uses. Flagged cybersecurity requests fall back to Opus 4.8, and flagged biology requests to Opus 5.

If one system runs several models, build every request for the strictest of them: keep history append-only, send `tool_choice: auto` with strict tools, read content blocks by `type`, and write prompts and tool descriptions precisely enough for the most literal model. Then a step can move up or down a tier without a code change. When the routing rule is simple, such as one model for each step type, let code pick the model rather than asking a model to.

Published results, like the SWE-bench Pro and Terminal-Bench numbers above, get you a starting model. Then test the candidates on your own tasks before you commit.

- Pull a sample of real tasks. Write an outcome check for each one, such as a passing test, a closed ticket or a correct row count.
- Run each candidate model at two or three effort levels, each in its own session so that the runs don't share a cache. Record the cost of each completed task from the `usage`field of each response.
- Plot score against spend. Keep a multi-model setup only if it beats every single-model point on that chart.
- Run the winner in shadow on a slice of real traffic before you cut over.

For a quick check in Claude Code, run one task from your backlog on two models with `/model` and compare what `/usage` reports.

- Building with Claude Sonnet 5.5 covers when to choose Sonnet over Opus, pricing, migration and tuning.
- Getting the most out of Opus 5.5 in Claude and Claude Code covers prompting Opus 5.5 and steering long runs.
- What a task costs on Opus 5.5 prices effort, model choice and subagents.
- On the Claude blog, choosing the best Claude model for your use case and picking a model and effort level in Claude Code go deeper.
- In the docs, see Choosing a model, Optimizing for cost and intelligence, Effort, Claude Code model configuration and subagents.

Related posts

Nov 09, 2026Safely scaling multi-agent teams with Claude Fable 5.212 minOct 15, 2026How the Claude Code team does code review14 minOct 08, 2026Building effective agent automations9 minOct 06, 2026Claude Code in the cloud: a field guide to cloud sessions18 minOct 01, 2026Getting started with Claude Code mods11 min

LOAD MORE
