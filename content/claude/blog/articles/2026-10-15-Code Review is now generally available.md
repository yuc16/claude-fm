---
title: Code Review is now generally available
url: https://claude.com/resources/articles/code-review-is-now-generally-available
source: blog
published: '2026-10-15'
fetched: 2026-10-18 15:34
---

# Code Review is now generally available

Catch more bugs before they reach production.

Code Review is out of research preview and available to Claude Team and Enterprise organizations.

Eligible Claude Enterprise organizations can claim at least $10,000 in Code Review credits by January 15, 2027. Credits expire 30 days after you claim them. Terms apply.

### What's new in Code Review

Coding agents keep increasing the pace at which teams write code, and the review bottleneck hasn't eased. For general availability, we made Code Review faster, better at finding the bugs that matter, and easier to tune to each of your repositories.

Since we released the research preview, Code Review has gotten sharper, catching more of the bugs that would otherwise reach production. We also run Code Review on pull requests at Anthropic, which shows us where reviews slow our own engineers down. Teams using Code Review during the preview told us the rest: it was catching real issues before a human reviewer looked at the PR, but they wanted reviews that were quieter, sized to each change, and faster. Here’s what we shipped:

- **Speed:**Most reviews now finish about 3x faster (~20 minutes down to 6-10 minutes) compared to during preview.
- **Quality:**Find more of the bugs that matter, with clear, concise findings that state the problem, what triggers it, and the fix in a few sentences.
- **Flexibility:**Admins choose Quick, Standard (default), or Deep for each repository, so routine codebases get a quick pass and the most critical ones get a deep review. Every level delivers high-quality reviews.

### Get started

Code Review is now generally available for Team and Enterprise plans.

- **For admins**: Enable Code Review in your Claude Code settings, install the GitHub App, and select repositories you’d like to run reviews on.
- **For developers**: Once enabled, reviews run automatically on new PRs. No configuration needed.

Explore the docs for more information.
