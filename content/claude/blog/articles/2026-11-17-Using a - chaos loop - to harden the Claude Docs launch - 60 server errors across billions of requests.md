---
title: 'Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across
  billions of requests'
url: https://claude.dev/blog/chaos-loop-claude-docs-launch/
source: blog
published: '2026-11-17'
fetched: 2026-11-22 13:46
---

Engineering# Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across billions of requests

Claude Docs is a doc editor that you, your teammates, and Claude all work in together. The interesting part is that a Claude session anywhere, from chat to Claude Code, can open the same doc and read, write, and comment in it live, right next to you. We released Docs on September 16, 2026. This post is about the service that runs underneath it.

Three weeks before Claude Docs opened to the public, it was running as a proof of concept on a single node, used by a few thousand people inside Anthropic. We were racing toward an ambitious launch date, and our own estimate said we'd see millions of docs within the first few days.

We launched on September 16. By September 22, people had created over 4.6 million docs. Across 2 billion requests we saw only 60 server errors, and we never had to roll back. The whole Docs service ran on about 50 memory-optimized pods.

Two decisions got us there:

- **A chaos loop at launch scale.**We set up a test harness on our staging environment where Claude ran constantly for two weeks to try and break the service. It load tested every part of our infrastructure and fixed whatever fell over.
- **Improving legibility to Claude.**Claude could only close the loop effectively on fixes if our system produced accurate telemetry every iteration. We made a call early to avoid any runtime that uses memory or CPU in ways our code can't easily control (e.g. runtimes with garbage collection). When a telemetry signal looked concerning, Claude could easily trace it to a bug or a specific design decision.

But honestly, this only worked because our frontier models have gotten much better recently (I used an internal research model roughly comparable to Claude Fable 5.2). In our experience, they can now stick with one goal through a run like this for weeks, which is what helped us hit launch scale in a tight timeline.

A few thousand internal users on one machine told us nothing about whether the service would survive launch, and we obviously didn't have launch traffic to test with.

We wanted real evidence to decide how fast we could roll out. So on September 4, about two weeks before launch, I had Claude drive a staging cluster that mirrored production at over a million synthetic docs a day and break core components on purpose. And then... I just left it running (I've included the full cost at the end of this article).

My setup was pretty simple. The loop was a session in Claude Code that I left running: pick a scenario, run the harness, read the telemetry, propose a fix, ship it to staging, repeat. That session acted as a coordinator and handed most of the work to sub-agents. In the busiest week, that usually meant about 11 sub-agents running at a time, and 30 at the peak. The coordinator also talked to our internal variant of Claude Tag (beta) via the Slack MCP to learn from other infrastructure teams at Anthropic who had scaled similar services. Their agents checked our scaling approach for pitfalls they’d already hit.

The fun part was picking scenarios I thought were paranoid:

- 10M new docs created in a single day
- 22,000 live connections reconnecting at once
- One hot doc with hundreds of viewers, a server killed while it was still loading a doc, and the database stalling

Each iteration looked the same. Our testing harness selected a feature like document creation and pushed creation to saturation. Claude then read telemetry using the Datadog MCP and came back with a short menu of options and a recommendation.

If the recommendation was easy to undo, Claude wrote and deployed the change to staging and reran the test. We had telemetry on every operation the service ran. Every database query, for example, reported its name and how many rows it scanned versus how many it returned, so Claude could spot a bad query and rewrite it.

Before the loop started, I told Claude which decisions needed my approval; basically anything hard to undo, like changing the database schema or key layout, or changing how a doc is stored and materialized.

When Claude ran into one of those, it stopped and asked me, usually with a recommendation that I ended up approving. Schema changes were the classic case where I wanted to be consulted: there are usually a few reasonable answers, and changing directions is often painful.

And during the whole testing process, Claude had to conform to two invariants:

- Docs had to open almost instantly (even ones with a long history)
- Once the server acknowledged an edit, tests had to show the edit was still there

My colleague Felix Rieseberg recently wrote a tutorial on being more ambitious with models. His main idea is to raise the "altitude" you prompt Claude at: ask for the *outcome* you want, not the individual task.

So instead of asking Claude to fix individual crashes, you ask it to make your app crash-free. (Our own apps aren't all the way there yet, but this is how we're making real progress.) To work at that altitude, though, you have to set up your code so Claude can pull crash reports on its own and run a harness that reproduces each crash and checks the fix.

For us, the outcome was a service that could handle launch. To get there, we did two things to make the service as legible to Claude as we could:

- **A diagnostic loop.**Claude read the telemetry on every iteration and added whatever it thought was missing.
- **Legible technology choices.**We picked a runtime and dependencies so any number Claude measured traced back to code we wrote.

Every iteration, Claude read the telemetry and added whatever it thought was missing. Writing telemetry by hand is tedious, so in practice most telemetry would go in after something broke. Now Claude just writes it as it goes.

Memory is the best example.

Early in the harness run, one large doc was using about 3 GB on its pod (not a fun number to see). Claude’s first stab at fixing it was to shrink one of our caches so our server would evict docs sooner. The next harness run showed the memory was actually in a *separate* cache inside one of our dependencies, so Claude dropped the change.

From there Claude kept narrowing it down with finer-grained memory profiling. Eventually it found that every keystroke was copying the doc into several different data structures, adding a few MB each time. Claude switched those structures to copy-on-write, so they now share one reference instead of each holding its own copy.

After about three days of iterating, that doc topped out around 180 MB, and our estimate of what we’d need for launch dropped from more than 500 memory-optimized pods to about 50.

We were picky about the service’s runtime and dependencies. We wanted any number Claude measured to trace back to code we wrote.

This is because our models hill climb best with a clean signal. We expected a garbage collector to add noise, because memory and latency shift on the collector’s schedule.

Two choices helped the most.

- **We wrote the service in Rust**. With no garbage collector, all of a doc’s memory sits in structures we defined, so when it grew, Claude could point to the one responsible, change it, and see whether memory came down on the next iteration. We have great Go tooling at Anthropic too, and we didn’t bake off the two languages, so this is our experience with Rust. What I did appreciate, coming from past work in Go, was how little I had to think about memory sticking around after my code was done with it.
- **We also kept dependencies to a minimum**. Every library brings data structures we didn’t write and can’t easily account for. For the few we really needed, we vendored the code so we could read and measure it ourselves.

Rust is hard for people to write, and a few years ago that would have weighed heavily on the choice. Claude writes it and most other languages fine, so that matters a lot less now.

The service held at launch scale. The first million docs showed up in about 30 hours, and we were past 4.6 million by September 22. We rolled prod 629 times in September and never once rolled back.

Launch week felt weirdly familiar. Claude is great at imagining ways a service can fail and had planned for most of them well before launch. Seven of the ten scenarios we’d rehearsed on staging actually happened in prod. By then the harness had already put staging through most of it, and Claude had shipped the fixes behind runtime flags. When part of the infra ran into pressure, we usually just flipped a flag.

A few months ago this probably wouldn’t have worked. Older models were fine at reading telemetry through an MCP server, but ten or twenty iterations into a long loop, they’d start forgetting what we were optimizing for, and I’d end up restating the goal. Other Anthropic employees have called this goal drift.

Our newer frontier models are built for long-running work. Claude held all of our invariants across many compactions, and I never had to repeat them.

We're not the only ones doing this, either. Vercel made Turborepo up to 96% faster with a supervised agent loop a lot like ours.

At Claude Fable 5.2's API list price (as of November 2026), I used roughly $125,000 of inference from the end of August to launch day. A couple of years ago, work on this scale I'd guess would have taken a team of engineers about six months.

Most of that went to reading telemetry, writing proposals, generating fixes, and reviewing code.

A couple of things about the cost:

- **Our launch was particularly massive.**A good chunk of the money went into infrastructure that only makes sense at that scale, and that infrastructure took more inference to reason about. Claude had to think a lot harder about how a growing set of services fit together and all the ways they could fail.
- **I also burned a lot of tokens figuring out the process.**The loop ran nonstop while I was experimenting with the setup. Knowing what I know now, I think we could have spent about half as much.

This works for much smaller services too, and it should cost a lot less.

To get a rough number, I priced out a classic small team stack: a couple of reasonably sized Kubernetes nodes and a Postgres instance. Then I went through the changes I landed between the end of August and launch day and removed the work that setup wouldn’t need:

- Fitting in with our other internal services
- Client and product work that was intermixed with the scale work
- Running across many pods
- Fine-grained rate limiting

About a third of the changes were left.

Scaling our spend down to that third and taking out the mistakes I made while I was still figuring out the setup, I’d put a two week push like this one at $3,000 to $10,000 at the same list price (I haven’t actually run this, so it’s only a rough sense).

The steps below assume one engineer with Claude Code, a staging environment, and an observability provider. The coordinator and sub-agents helped speed up the process, but if you find they’re burning too many tokens per hour, going back to a single agent should also work quite well. If you want to try it:

- Give Claude access to your telemetry. Most observability providers have an MCP server that Claude can use.
- Have Claude write a load script that throws ten times your real traffic at the staging copy of the service and breaks things on purpose. Killing an instance, stalling the database, and deploying in the middle of a spike are good places to start. Then let Claude keep fixing whatever falls over.
- When you’re picking your stack, lean toward whatever Claude can measure most easily. For us that was Rust and as few dependencies as possible.
- Before you start, write down your most important technical invariants and give them to Claude.
- For anything that’s hard to undo, have Claude stop and give you a few options with a clear recommendation.

*Huge thanks to the Docs team, who landed thousands of editor fixes in the same three weeks, and to the platform and storage teams who built everything this sits on.*

**Further reading.** How we made claude.ai 3x faster in two weeks (claude.dev) · A harness for every task: dynamic workflows in Claude Code (claude.dev), on goal drift.

Related posts

Nov 16, 2026How the Claude Code team thinks about verification10 minNov 09, 2026Safely scaling multi-agent teams with Claude Fable 5.212 minNov 09, 2026Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku15 minOct 15, 2026How the Claude Code team does code review14 minOct 08, 2026Building effective agent automations9 min

LOAD MORE
