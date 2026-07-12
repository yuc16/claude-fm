---
title: Choosing a Claude model and effort level in Claude Code | Claude by Anthropic
url: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
source: blog
published: '2026-07-07'
fetched: 2026-07-12 16:09
---

- July 7, 2026
- 5min

**Key takeaways**:

- Claude model selection chooses the set of fixed weights, or the overall capability range of the model. While models can be provided context or steered, the model’s overall knowledge base and capabilities are set.
- Effort means more than "thinking time.” It controls how much work Claude does on your request overall including the number of files read, tools used, and how many steps it takes before it checks back in with you.
- Choose smaller models for more routine tasks and larger models for more complex or ambiguous tasks. Start with default effort levels for each model and tune as a general preference based on the type of work you do rather than task-by-task.
- If Claude has all the pertinent context, clearly tried, and still got it wrong, that's a signal to pick a more capable model. If Claude got it wrong by skipping a file, not running the tests, or bailing on a refactor partway through, pick a higher effort level.

**Claude Code effort level and model selection**

Claude Code gives you two settings that appear to "make the answer better": the model setting and the effort level. You may expect that larger models like Claude Fable 5 provide a smarter output than Claude Sonnet, and a higher effort level means Claude thinks longer before it answers.

The first assumption is accurate. Our largest models are more capable, according to industry-standard benchmarks.

But effort means more than just "thinking time." Effort level controls how much work Claude does on your request overall. This does include how long the model thinks, but also:

- How many files it reads;
- How much it verifies; and
- How far it pushes through a multi-step task before checking in with you.

At a higher effort, Claude will take more of those actions (for example, read files, run tests, and double-check) before it comes back to you. At lower effort, it would rather ask you for more context than spend tokens figuring something out on its own.

**How model selection works**

When you press enter, Claude Code assembles your message together with the system prompt, tool definitions, your CLAUDE.md, the conversation history, and any files in context. All of this is sent as one request to the API.

The model never sees that as plain text, though. The first thing that happens on the server is **tokenization**; the text is split into pieces, and each piece is mapped to an integer from a fixed vocabulary the model was trained with. const might map to 1978, await might map to 4293. From here on, your prompt is an array of integers.

The model's job is to take that array and predict which token comes next. It does this by computing a *probability* for every token in its vocabulary and picking from the top. After const x = await, a well-trained model puts high probability on fetch (very likely) and near-zero on banana (not likely at all).

What turns your input tokens into those probabilities is the **weights** (also called *parameters*). These are billions of numbers organized into large matrices. To predict one token, the model runs your input through those matrices, a long chain of matrix multiplications, and reads the probabilities at the end. The weights are where everything the model "knows" lives.

**The weights of each model are set during training, and by the time you're sending requests they're read-only.** Nothing in your prompt, your CLAUDE.md, or your context changes them. (If you've run into the word inference, that's all it means: using the model after training is done, with the weights fixed.)

Everything Claude knows about TypeScript, popular frameworks, idiomatic Go, or any other general programming knowledge, was encoded into those weights at training time.

Your prompt and context can still *steer* the prediction (putting your real code in front of Claude is *steering*, and it works really well), but they don't add anything to the weights themselves.

If a library didn't exist when the model was trained, it isn't in the weights. You can put the docs in context and Claude will use them, but that's *steering*, not *teaching*. Claude’s response will only be influenced for that request; the underlying model hasn’t retained the information.

So when Claude confidently calls an API that doesn't exist (a hallucination), that's the weights producing a token sequence that *looks* plausible from training patterns, not a failed lookup.

So what does changing the model actually do? It swaps **which set of frozen weights** handles your request.

The model doesn't generate a whole answer at once. It predicts one token, appends it to the sequence, and runs the whole computation again to get the next one. A 200-token response is 200 separate passes through the weights. This loop is where most of your wait time and your output cost come from.

So the **model setting** decides *which weights* handle your request, and it also decides what each output token costs.

What it doesn't decide is how many tokens get generated. That number can vary a lot for the same prompt, depending on how much work Claude decides to do.

This is what **effort** **level** controls: *how much work* Claude decides to do for each turn.

**How Claude Code effort level works**

When Claude Code is working on a task, the tokens it generates fall into a few categories:

- **Thinking**: the reasoning you see streaming before and between actions.
- **Tool calls**: structured blocks naming a tool like Read or Edit and its arguments, which Claude Code then parses and executes.
- **Text to you**: the plan, progress updates, the summary at the end.

These are all ordinary output tokens from the same loop, billed at the same rate. For example, thinking tokens are generated exactly like the other output tokens and stay in context for the rest of that turn.

When Claude moves on to writing code, its earlier reasoning is part of the input just like a file it’s read.

How does effort change any of this? The effort level is sent to the model as part of the request, right alongside your prompt. The model was trained to understand how to behave at each effort level and that learned behavior is baked into the frozen weights.

When your request arrives, effort level is one more input the model responds to, the same way it responds to your prompt text. This sets Claude’s behavior for how thorough and certain it needs to be before it considers the task done.

**This is considered on every turn **and** **results in more tokens to produce higher confidence answers.

At higher effort levels, Claude often starts with creating a plan and the level of effort influences the depth and breadth of that plan. However, the plan is not frozen in place. As Claude receives results from its actions, it updates the progress that has been made and how certain it is of the accumulated result.

So when step 1 of a three-hypothesis debugging plan finds the bug, "investigate hypotheses 2 and 3" may no longer be necessary actions. Claude will typically say this explicitly, "the first check found it, so the remaining checks aren't needed" and skip ahead. You see this happen in Claude Code when task lists get revised mid-run.

Claude will be more predisposed to double-checking additional hypotheses or verifying correctness at higher effort levels, but it generally won’t artificially inflate usage for simple tasks at higher effort levels. In fact, our team pays close attention to “overthinking” during model training as it degrades effectiveness.

**Picking an effort level **

Our guidance is that** for most tasks you should use the model’s default effort level**. The default is the level where Claude will scale its token usage according to what most people would want to spend on a task.

Think of effort as a manual override to scale how hard and long Claude works. Choose it deliberately when you have a strong preference for thoroughness or speed based on your domain or the type of work you do. Consider this more as a general preference than a task-by-task decision.

Some practical insight that may help guide you following the launch of Claude Opus 4.8: in our testing we found when you use the default effort setting for Opus 4.8, it will produce better results for about the same number of tokens when compared to using the default effort setting of Opus 4.7 for the same task.

**What to change when Claude gets it wrong**

When Claude gets something wrong, your first instinct shouldn’t be to adjust a knob, but to examine the context you have provided. Is your prompt too vague? Is Claude connected to the right tools? Equipped with the right skills?

If you're increasing effort on a task that *shouldn't* need it, the fix is often upstream, in your context, your CLAUDE.md, or how the task is scoped.

But assuming you have provided clear context and Claude still gets something wrong, the question to ask yourself is: did it not *try* hard enough, or did it not *know* enough?

**Model: The problem was too hard**

Pick a larger model when the problem is genuinely hard. For example, problems like subtle bugs, unfamiliar domains, or architecture decisions. A larger model is helpful for situations where the smaller model is confidently wrong no matter how much context you give it.

Larger models are also better at handling ambiguity, whereas specific instructions directing execution are a better recipe for success on the smaller models.

Pick a smaller model when the work is routine. For example, edits you can describe precisely, mechanical changes, or questions about code that's already in context. There's no reason to pay for capability the task doesn't need.

If Claude has all the pertinent context and clearly tried and still got it wrong, that's a signal to pick a larger model. If you're on the larger model and the work has been routine for a while, dropping down will increase speed and typically reduce cost without impacting the quality of the output.

**Effort: Claude didn’t try hard enough**

Pick a higher effort level if Claude got it wrong by skipping a file, not running the tests, or not double-checking its work. This is most relevant if you selected an effort level below the model’s default.

**Effort, model, and token consumption**

So how do model selection, effort, and token consumption all interact? It depends on the task.

On routine work at the same effort level, both models generally will get it right. The larger model consumes more tokens with extra verification steps at a higher per-token price. That's why dropping to the smaller model for routine stretches saves real money at no quality cost.

On harder, multi-step work, the equation is different. The smaller model has to grind toward the limit of its ability, burning iterations, while the larger model reaches the same quality bar in fewer steps.

You're paying more per token for the larger model, but on tasks that genuinely stretch the smaller one, the total cost per task can come out lower. Also, more importantly, the larger model can accomplish tasks the smaller one cannot even at the highest effort settings.

This is most pronounced with Fable. On long, multi-step work it pulls furthest ahead. In our testing, it finished jobs Opus and Sonnet can't reach at any effort level. It also costs the most per token, which is the other reason to save it for the work that needs it.

The key point in the graphs above is that effort level picks how far Claude **is willing to travel **along the curve, but again, that doesn’t mean Claude **will need to travel** that far to complete the task.

Another nuance to this: effort shapes token consumption but doesn't limit it. The only hard cap in the system is max_tokens, which truncates a response mid-stream when hit. It’s a blunt instrument, mostly relevant to API developers. Softer controls, like task budgets or asking Claude to keep it brief in your prompt, are more helpful tools. They serve as guidance the model is trained to follow-it will look to conclude its tasks if it gets near the limit–rather than a wall it runs into.

**Start with the defaults, then reach for the dials**

Most of the time, you shouldn't be thinking about either setting. When a result misses the mark, ask, “did Claude not know enough or did it not try hard enough?” and adjust as needed.

*This article was written by Lydia Hallie, member of technical staff on the Claude Code team. *

## Transform how your organization operates with Claude

Get the developer newsletter
