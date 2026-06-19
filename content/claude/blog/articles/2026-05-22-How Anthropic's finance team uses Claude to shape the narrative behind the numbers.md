---
title: How Anthropic's finance team uses Claude to shape the narrative behind the
  numbers
url: https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers
source: blog
published: '2026-05-22'
fetched: 2026-06-13 12:15
---

How Anthropic's finance team uses Claude to shape the narrative behind the numbers

Alice Fong, on the corporate finance and strategy team at Anthropic, shares how she uses Claude to maintain a single coherent financial narrative for the CFO and board, and free up 10 to 20 hours a week for higher-impact work.

In finance, your job is to shape the story behind the numbers: explaining why a key metric shifted, setting expectations based on market trends, and connecting financial results to product strategy. But it's easy to spend most of your time just making sure the numbers are right—re-reading a deck for the fourth time after the figures refresh again—instead of thinking about what those figures mean.

For example, I'm responsible for running the analysis and pulling the metrics that go into the quarterly board deck our team prepares for the CFO. Normally, by the time a deck ships, I’ve had to revise it several times. The numbers keep getting refreshed up to the morning the deck goes out, and with every refresh the commentary has to be checked against the latest numbers. On top of that, the deck is collaborative, with partners updating their own slides simultaneously. Every update means the entire narrative has to be re-baselined: does the commentary on slide 4 still reconcile with the figure on slide 17, did someone introduce a metric without defining it? I’d have to keep re-reading the entire deck to make sure the story is still consistent.

Claude does all of this for me now: it holds the integrity layer underneath the work, so my time goes to the narrative on top. It is also part of my monthly review process and my model audits, giving me time back that I can now spend collaborating with my team, or on creative thinking and the parts of finance that require judgment.

A bird’s-eye view of a fast-moving business

I joined Anthropic's corporate finance and strategy team in March 2025. Corporate finance sits at the center of the finance organization: the other finance teams partner directly with the business—go-to-market finance with sales, for example—and everything they learn flows back to us. Our job is to prepare the narrative that the CFO and the board need to see: how revenue performed, what's happening to margins, how cash is being deployed, and what it means for the rest of the year.

That narrative has to stay coherent while the business changes underneath it. At Anthropic, that means product launches, model launches, pricing changes, and shifts in how we segment our sales motion, among other factors, often all in the same week. Corporate finance has to absorb the full rate of change of the company and still hand the board a story that holds together.

How I use Claude across my workflows

I use Claude Cowork and Claude for Excel in parallel: Claude Cowork helps me with writing and synthesizing information in a document or deck, and I use Claude for Excel to edit with Claude directly in the financial model.

Working on the board deck I mentioned earlier, I hand the file to Claude Cowork and ask it to validate that every number and claim reconciles to a single source of truth. I also ask it to read the narrative the way a board member would, flagging where it contradicts itself or assumes context the reader doesn't have. Claude catches things I'd otherwise miss, and it does it every time the numbers move, not just once.

Another example is our monthly financial review, a Google Doc with a tab for each month, structured as a variance analysis against forecast. When I'm ready to write up a month, I drop the relevant financial table from our model into the doc, link the supporting context, and ask Claude Cowork to write the first pass in the voice we already use: revenue was A versus B, off by C%, driven by D. I edit from there. Consistency of voice month over month matters as much as the numbers and Claude accomplishes that when I reference the prior month’s document.

As Claude and our product surfaces improve, so too does my way of working with them. Claude for Excel, for example, has gone from being unable to follow references across tabs to being able to trace a balance sheet that won't balance through multiple tabs to find the root cause. When I open a model I haven't seen before, I ask Claude to summarize the key drivers and flag structural issues before I invest time in it.

Across all of these workflows—narrative integrity on board materials, model diagnostics in Sheets and Excel, and first-pass commentary in Claude Cowork—I've reclaimed hours that now go straight into the work that actually requires judgment: framing, scenario questions, and the forward-looking analyses.

Workflow

Cadence

Tool

What Claude does

Board deck

Quarterly

Claude Cowork

Reconciles numbers across slides and checks narrative consistency

Monthly financial review

Monthly

Claude Cowork

Drafts first-pass commentary in the established voice

Financial model work

As needed

Claude for Excel

Traces references across tabs and diagnoses model issues

Cross-team context

Continuous

Google Workspace and Slack connectors

Pulls decisions and reasoning from docs, email, and Slack

Context makes it all work

Claude Cowork works because it sees the same context I do: documents and local files, email, and Slack, to name a few sources of team knowledge. When I come across a doc that matters, I commit it to project memory. When a decision gets made in a long cross-functional thread, I have Claude pull out the conclusion and the reasoning so it's on hand the next time the topic surfaces in a board cycle.

I also keep separate projects for separate audiences: one for the monthly review, one for the board deck. The tone and conventions differ, so the memory does too, and Claude generates the content accordingly.

Claude Cowork across the finance org

Across the financial organization, my colleagues use many of the skills that are now packaged into Claude Cowork plugins for financial services. Here are a few examples of how the CFO organization uses Claude Cowork today:

Finance & strategy: Interactive forecasting and cohort dashboards built from a prompt by analysts themselves: no SQL or engineering involvement needed. A daily revenue and metrics digest lands in leadership’s slack at 7 am.

Accounting: GL-to-subledger and bank reconciliations, with breaks classified and reviewer commentary drafted as a first pass. Flux runs on all three financial statements. Anyone on the team can ask Claude a question in Slack and get a sourced answer.

Corporate development and IR: Screening reports for three to four acquisition targets a day, built from notes and public data, then rolled up into memos in minutes. The team spends their time on judgment and making the call, not on the first draft.

Tax & treasury: Transfer pricing, R&D credit, and nexus questions answered with primary-source citations. Indirect-tax and cash reconciliations run on the same skill pattern as accounting.

Advice for finance teams on getting started with Claude

When I joined Anthropic a year ago, AI tools were mostly LLMs: great at text, not so great with numbers. What pulled me in was watching Claude for Excel improve. I can literally track the difference as models get better.

If you're on the fence, start simple: ask Claude to read a doc and summarize it, then keep pushing the boundaries. It's most valuable on workflows that recur, including board cycles and monthly reviews, where consistency compounds and project memory gets richer every pass. You don't need an elaborate stack; I run almost entirely on Claude Cowork projects, Claude for Excel, and Google Suite Connector.

And if you don't know which Claude surface to use, just ask Claude. With Claude in the loop, I can keep up with the pace of change underneath the work. I get to the insights faster, with fewer surprises or bottlenecks, and I can spend more time on the framing and forward-looking analysis.
