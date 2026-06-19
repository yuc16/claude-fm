---
title: Code Review for Claude Code
url: https://claude.com/blog/code-review
source: blog
published: '2026-03-09'
fetched: 2026-06-13 12:15
---

# Bringing Code Review to Claude Code

Claude Code now has a thorough, agent team-based review system, modeled on the one we run at Anthropic. Available in research preview.

Claude Code now has a thorough, agent team-based review system, modeled on the one we run at Anthropic. Available in research preview.

- March 9, 2026
- 5min

Today we're introducing Code Review, which dispatches a team of agents on every PR to catch the bugs that skims miss, built for depth, not speed. It's the system we run on nearly every PR at Anthropic. Now in research preview for Team and Enterprise.

Code output per Anthropic engineer has grown 200% in the last year. Code review has become a bottleneck, and we hear the same from customers every week. They tell us developers are stretched thin, and many PRs get skims rather than deep reads.

We needed a reviewer we could trust on every PR. Code Review is the result: deep, multi-agent reviews that catch bugs human reviewers often miss themselves. It's a more thorough (and more expensive) option than our existing Claude Code GitHub Action, which remains open source and available.

We run Code Review on nearly every PR at Anthropic. Before, 16% of PRs got substantive review comments. Now 54% do. It won't approve PRs — that's still a human call — but it closes the gap so reviewers can actually cover what's shipping.

When a PR is opened, Code Review dispatches a team of agents. The agents look for bugs in parallel, verify bugs to filter out false positives, and rank bugs by severity. The result lands on the PR as a single high-signal overview comment, plus in-line comments for specific bugs.

Reviews scale with the PR. Large or complex changes get more agents and a deeper read; trivial ones get a lightweight pass. Based on our testing, the average review takes around 20 minutes.

We've been running Code Review internally for months: on large PRs (over 1,000 lines changed), 84% get findings, averaging 7.5 issues. On small PRs under 50 lines, that drops to 31%, averaging 0.5 issues. Engineers largely agree with what it surfaces: less than 1% of findings are marked incorrect.

In one case, a one-line change to a production service looked routine and was the kind of diff that normally gets a quick approval. But Code Review flagged it as critical. The change would have broken authentication for the service, a failure mode that’s easy to read past in the diff but obvious once pointed out. It was fixed before merge, and the engineer shared afterwards that they wouldn't have caught it on their own.

Early access customers have seen similar patterns. On a ZFS encryption refactor in TrueNAS's open-source middleware, Code Review surfaced a pre-existing bug in adjacent code: a type mismatch that was silently wiping the encryption key cache on every sync. It was a latent issue in code the PR happened to touch, the kind of thing a human reviewer scanning the changeset wouldn't immediately go looking for.

Code Review optimizes for depth and is more expensive than lighter-weight solutions like the Claude Code GitHub Action. Reviews are billed on token usage and generally average $15–25, scaling with PR size and complexity.

Admins have many ways to control spend and usage:

- **Monthly organization caps**: Define total monthly spend across all reviews
- **Repository-level control**: Enable reviews only on the repositories you choose
- **Analytics dashboard**: Track PRs reviewed, acceptance rate, and total review costs

Code Review is available now as a research preview in beta for Team and Enterprise plans.

- **For admins**: Enable Code Review in your Claude Code settings, install the GitHub App, and select repositories you’d like to run reviews on.
- **For developers**: Once enabled, reviews run automatically on new PRs. No configuration needed.

Explore the docs for more information.

Get the developer newsletter
