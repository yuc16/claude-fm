---
title: Introducing Claude Opus 4.5
url: https://www.anthropic.com/news/claude-opus-4-5
source: news
published: '2025-11-24'
fetched: 2026-06-21 15:27
---

# Introducing Claude Opus 4.5

Our newest model, Claude Opus 4.5, is available today. It’s intelligent, efficient, and the best model in the world for coding, agents, and computer use. It’s also meaningfully better at everyday tasks like deep research and working with slides and spreadsheets. Opus 4.5 is a step forward in what AI systems can do, and a preview of larger changes to how work gets done.

Claude Opus 4.5 is state-of-the-art on tests of real-world software engineering:

Opus 4.5 is available today on our apps, our API, and on all three major cloud platforms. If you’re a developer, simply use `claude-opus-4-5-20251101` via the Claude API. Pricing is now $5/$25 per million tokens—making Opus-level capabilities accessible to even more users, teams, and enterprises.

Alongside Opus, we’re releasing updates to the Claude Developer Platform, Claude Code, and our consumer apps. There are new tools for longer-running agents and new ways to use Claude in Excel, Chrome, and on desktop. In the Claude apps, lengthy conversations no longer hit a wall. See our product-focused section below for details.

## First impressions

As our Anthropic colleagues tested the model before release, we heard remarkably consistent feedback. Testers noted that Claude Opus 4.5 handles ambiguity and reasons about tradeoffs without hand-holding. They told us that, when pointed at a complex, multi-system bug, Opus 4.5 figures out the fix. They said that tasks that were near-impossible for Sonnet 4.5 just a few weeks ago are now within reach. Overall, our testers told us that Opus 4.5 just “gets it.”

Many of our customers with early access have had similar experiences. Here are some examples of what they told us:

Opus models have always been “the real SOTA”but have been cost prohibitive in the past. Claude Opus 4.5 is now at a price point where it can be your go-to model for most tasks. It’s the clear winner and exhibits the best frontier task planning and tool calling we’ve seen yet.

Claude Opus 4.5 delivers high-quality code and excels at powering heavy-duty agentic workflows with GitHub Copilot. Early testing shows itsurpasses internal coding benchmarks while cutting token usage in half, and is especially well-suited for tasks like code migration and code refactoring.

Claude Opus 4.5 beats Sonnet 4.5 and competition on our internal benchmarks,using fewer tokens to solve the same problems. At scale, that efficiency compounds.

Claude Opus 4.5 delivers frontier reasoning within Lovable's chat mode, where users plan and iterate on projects. Its reasoning depth transforms planning—and great planning makes code generation even better.

Claude Opus 4.5 excels at long-horizon, autonomous tasks, especially those that require sustained reasoning and multi-step execution. In our evaluations it handled complex workflows with fewer dead-ends. On Terminal Bench it delivered a 15% improvement over Sonnet 4.5, a meaningful gain that becomes especially clear when using Warp’s Planning Mode.

Claude Opus 4.5 achieved state-of-the-art results for complex enterprise taskson our benchmarks, outperforming previous models on multi-step reasoning tasks that combine information retrieval, tool use, and deep analysis.

Claude Opus 4.5 delivers measurable gains where it matters most: stronger results on our hardest evaluations and consistent performance through 30-minute autonomous coding sessions.

Claude Opus 4.5 represents a breakthrough in self-improving AI agents. For automation of office tasks, our agents were able to autonomously refine their own capabilities—achieving peak performance in 4 iterations while other models couldn’t match that quality after 10. They also demonstrated the ability to learn from experience across technical tasks, storing insights and applying them later.

Claude Opus 4.5 is a notable improvement over the prior Claude models inside Cursor, with improved pricing and intelligence on difficult coding tasks.

Claude Opus 4.5 is yet another example of Anthropic pushing the frontier of general intelligence. It performs exceedingly well across difficult coding tasks, showcasing long-term goal-directed behavior.

Claude Opus 4.5 delivered an impressive refactor spanning two codebases and three coordinated agents. It was very thorough, helping develop a robust plan, handling the details and fixing tests.A clear step forward from Sonnet 4.5.

Claude Opus 4.5 handles long-horizon coding tasks more efficiently than any model we’ve tested. It achieves higher pass rates on held-out tests while using up to 65% fewer tokens, giving developers real cost control without sacrificing quality.

We’ve found that Opus 4.5 excels at interpreting what users actually want, producing shareable content on the first try. Combined with its speed, token efficiency, and surprisingly low cost, it’s the first time we’re making Opus available in Notion Agent.

Claude Opus 4.5 excels at long-context storytelling, generating 10-15 page chapters with strong organization and consistency. It's unlocked use cases we couldn't reliably deliver before.

Claude Opus 4.5 sets a new standard for Excel automation and financial modeling. Accuracy on our internal evals improved 20%, efficiency rose 15%, and complex tasks that once seemed out of reach became achievable.

Claude Opus 4.5 is the only model that nails some of our hardest 3D visualizations. Polished design, tasteful UX, and excellent planning & orchestration - all with more efficient token usage. Tasks that took previous models 2 hours now take thirty minutes.

Claude Opus 4.5 catches more issues in code reviews without sacrificing precision. For production code review at scale, that reliability matters.

Based on testing with Junie, our coding agent,Claude Opus 4.5 outperforms Sonnet 4.5 across all benchmarks. It requires fewer steps to solve tasks and uses fewer tokens as a result. This indicates that the new model is more precise and follows instructions more effectively — a direction we’re very excited about.

The effort parameter is brilliant.Claude Opus 4.5 feels dynamic rather than overthinking, and at lower effort delivers the same quality we need while being dramatically more efficient. That control is exactly what our SQL workflows demand.

We’re seeing 50% to 75% reductions in both tool calling errors and build/lint errors with Claude Opus 4.5. It consistently finishes complex tasks in fewer iterations with more reliable execution.

Claude Opus 4.5 is smooth, with none of the rough edges we've seen from other frontier models. Thespeed improvements are remarkable.

## Evaluating Claude Opus 4.5

We give prospective performance engineering candidates a notoriously difficult take-home exam. We also test new models on this exam as an internal benchmark. Within our prescribed 2-hour time limit, Claude Opus 4.5 scored higher than any human candidate ever1.

The take-home test is designed to assess technical ability and judgment under time pressure. It doesn’t test for other crucial skills candidates may possess, like collaboration, communication, or the instincts that develop over years. But this result—where an AI model outperforms strong candidates on important technical skills—raises questions about how AI will change engineering as a profession. Our Societal Impacts and Economic Futures research is aimed at understanding these kinds of changes across many fields. We plan to share more results soon.

Software engineering isn’t the only area on which Claude Opus 4.5 has improved. Capabilities are higher across the board—Opus 4.5 has better vision, reasoning, and mathematics skills than its predecessors, and it is state-of-the-art in many domains:2

The model’s capabilities outpace some of the benchmarks we use in our tests. A common benchmark for agentic capabilities is τ2-bench, which measures the performance of agents in real-world, multi-turn tasks. In one scenario, models have to act as an airline service agent helping a distressed customer. The benchmark expects models to refuse a modification to a basic economy booking since the airline doesn’t allow changes to that class of tickets. Instead, Opus 4.5 found an insightful (and legitimate) way to solve the problem: upgrade the cabin first, *then* modify the flights.

```
Let me think about what options I have within my policy:
1. Modify flights - Basic economy cannot be modified. This is clear in the policy.
2. Change cabin - Wait, let me check this option! The policy says:
"In other cases, all reservations, including basic economy, can change cabin without changing the flights."
But he wants to change the flights, not just the cabin. However, what if we:
- Change the cabin first (which IS allowed for basic economy), then
- Change the flights (which is allowed for non-basic economy)
So the strategy could be:
1. Upgrade his cabin from basic economy to economy (or business)
2. Then modify the flights to be 2 days later
This would cost more money, but it’s a legitimate path within the policy!
```
The benchmark technically scored this as a failure because Claude’s way of helping the customer was unanticipated. But this kind of creative problem solving is exactly what we’ve heard about from our testers and customers—it’s what makes Claude Opus 4.5 feel like a meaningful step forward.

In other contexts, finding clever paths around intended constraints could count as *reward hacking*—where models “game” rules or objectives in unintended ways. Preventing such misalignment is one of the objectives of our safety testing, discussed in the next section.

**A step forward on safety**

As we state in our system card, Claude Opus 4.5 is the most robustly aligned model we have released to date and, we suspect, the best-aligned frontier model by any developer. It continues our trend towards safer and more secure models:

Our customers often use Claude for critical tasks. They want to be assured that, in the face of malicious attacks by hackers and cybercriminals, Claude has the training and the “street smarts” to avoid trouble. With Opus 4.5, we’ve made substantial progress in robustness against prompt injection attacks, which smuggle in deceptive instructions to fool the model into harmful behavior. Opus 4.5 is harder to trick with prompt injection than any other frontier model in the industry:

You can find a detailed description of all our capability and safety evaluations in the Claude Opus 4.5 system card.

**New on the Claude Developer Platform**

As models get smarter, they can solve problems in fewer steps: less backtracking, less redundant exploration, less verbose reasoning. Claude Opus 4.5 uses dramatically fewer tokens than its predecessors to reach similar or better outcomes.

But different tasks call for different tradeoffs. Sometimes developers want a model to keep thinking about a problem; sometimes they want something more nimble. With our new effort parameter on the Claude API, you can decide to minimize time and spend or maximize capability.

Set to a medium effort level, Opus 4.5 matches Sonnet 4.5’s best score on SWE-bench Verified, but uses 76% fewer output tokens. At its highest effort level, Opus 4.5 exceeds Sonnet 4.5 performance by 4.3 percentage points—while using 48% fewer tokens.

With effort control, context compaction, and advanced tool use, Claude Opus 4.5 runs longer, does more, and requires less intervention.

Our context management and memory capabilities can dramatically boost performance on agentic tasks. Opus 4.5 is also very effective at managing a team of subagents, enabling the construction of complex, well-coordinated multi-agent systems. In our testing, the combination of all these techniques boosted Opus 4.5’s performance on a deep research evaluation by almost 15 percentage points4.

We’re making our Developer Platform more composable over time. We want to give you the building blocks to construct exactly what you need, with full control over efficiency, tool use, and context management.

**Product updates**

Products like Claude Code show what’s possible when the kinds of upgrades we’ve made to the Claude Developer Platform come together. Claude Code gains two upgrades with Opus 4.5. Plan Mode now builds more precise plans and executes more thoroughly—Claude asks clarifying questions upfront, then builds a user-editable plan.md file before executing.

Claude Code is also now available in our desktop app, letting you run multiple local and remote sessions in parallel: perhaps one agent fixes bugs, another researches GitHub, and a third updates docs.

For Claude app users, long conversations no longer hit a wall—Claude automatically summarizes earlier context as needed, so you can keep the chat going. Claude for Chrome, which lets Claude handle tasks across your browser tabs, is now available to all Max users. We announced Claude for Excel in October, and as of today we've expanded beta access to all Max, Team, and Enterprise users. Each of these updates takes advantage of Claude Opus 4.5’s market-leading performance in using computers, spreadsheets, and handling long-running tasks.

For Claude and Claude Code users with access to Opus 4.5, we’ve removed Opus-specific caps. For Max and Team Premium users, we’ve increased overall usage limits, meaning you’ll have roughly the same number of Opus tokens as you previously had with Sonnet. We’re updating usage limits to make sure you’re able to use Opus 4.5 for daily work. These limits are specific to Opus 4.5. As future models surpass it, we expect to update limits as needed.

#### Footnotes

1. This result was using parallel test-time compute, a method that aggregates multiple “tries” from the model and selects from among them. Without a time limit, the model (used within Claude Code) matched the best-ever human candidate.

2. We improved the hosting environment to reduce infrastructure failures. This change improved Gemini 3 to 56.7% and GPT-5.1 to 48.6% from the values reported by their developers, using the Terminus-2 harness.

3. Note that these evaluations were run on an in-progress upgrade to Petri, our open-source, automated evaluation tool. They were run on an earlier snapshot of Claude Opus 4.5. Evaluations of the final production model show a very similar pattern of results when compared to other Claude models, and are described in detail in the Claude Opus 4.5 system card.

4. A fetch-enabled version of BrowseComp-Plus. Specifically, the improvement was from 70.48% without using the combination of techniques to 85.30% using it.

**Methodology**

All evals were run with a 64K thinking budget, interleaved scratchpads, 200K context window, default effort (high), default sampling settings (temperature, top_p), and averaged over 5 independent trials. Exceptions: SWE-bench Verified (no thinking budget) and Terminal Bench (128K thinking budget). Please see the Claude Opus 4.5 system card for full details.

## Related content

### Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

Read more### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

Read more
