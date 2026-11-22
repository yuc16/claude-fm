---
title: How the Claude Code team thinks about verification
url: https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/
source: blog
published: '2026-11-16'
fetched: 2026-11-22 13:52
---

Engineering# How the Claude Code team thinks about verification

How end-to-end, property and differential tests let coding agents verify their work with evidence, and what the Claude Code team does to keep its verifiers honest.

On the Claude Code team, the vast majority of our code (~90%) is written and reviewed by Claude. At this scale, how we equip our agents to verify their work with evidence becomes extremely important.

Verification loops are the building block that lets you delegate more work to Claude. Without them, you can really only run one or two Claudes at a time, because you have to check everything yourself. With them, you can run dozens or hundreds in parallel.

That’s because giving agents a way to verify their output is an effective way to improve quality. In internal testing around structured file generation, having a separate grader check Claude’s work against a rubric improved task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems.

What was once expensive to verify (tests, benchmarks, specs, real end-to-end runs) is now cheap to request from an agent. Like code, agents can quickly generate tests, benchmarks, and specs. And once generated, these tests and benchmarks run as software so they can be run frequently without using many additional tokens.

You can also close the verification loop by using the results to improve the agent’s performance on that task. For example, if an agent repeatedly fails a test that checks logs for user data, you can create a hook or a more explicit rule in your CLAUDE.md to avoid future issues. This (mostly) stops issues from happening again.

So if verification is critical to producing quality code at a high velocity, what types of tests should you use and how should you apply them across your pipeline? This article answers those questions and also shares the process used by the Claude Code team.

No matter which test type you choose, there are a few failure modes to avoid.

If your tests are flaky you’ll train the agent to run them again rather than fixing the failing code. If your tests are slow, the agent will do fewer tests across batches which can make pinpointing issues difficult. Heavier tests are best deployed before you’ve committed the changes.

Now, here are the three types of tests I think are most worth investing in.

If you have to focus on one test type, pick end-to-end. These tests describe real user flows like adding an item to a cart, checking out, and moving to a confirmation page.

The reason E2E tests are so effective is that they are difficult to fool–either the whole feature works or it doesn't. They also have definitive done criteria and can concretely tell you what’s broken.

While unit tests are faster and less flaky, it’s possible to pass them and still break the feature. This is because both the agent and the test don’t understand the full task.

With E2E tests, it is effective to give your agent hands and eyes on the real running system. You can use a skill to boot, drive, and inspect the app with tools like CDP, simulators, or API harnesses.

The feature map can serve as a guide and grading rubric for agents as they typically list features from the user’s point of view with descriptions of paths, keyboard shortcuts, selectors, and expected results.

A lot of tests are based on what you thought might go wrong. Property tests look at the edge cases that people tend to miss, which is where agents often fail.

You start by writing a statement you think can’t fail and then use a test library (fast-check for JS/TS, Hypothesis for Python, proptest for Rust, etc.) to generate thousands of inputs that try to prove otherwise.

There are many properties in virtually every software project like:

- **Round-trip encoding**: “if you encode X then decode it back, you get X.” This works for parsing and serialization as well.
- **Invariants**: Things that must always be true, like “account balance can never become negative.”
- **Idempotency**: Doing an action (migration, normalization, retry) twice has the same effect as doing it once.
- **Equivalence**: Optimized code produces the same result as naive but correct code.

Property libraries are a great way to keep agents honest by using edge cases that aren’t created with the same bias as the agent that created the original code. They are also particularly helpful for rewrites when the spec has drifted from production behavior and is no longer a reliable source for verification.

Differential tests are particularly effective for large-scale migration use cases where functionality is expected to remain the same. For these tests, you run both the old system and the new system with the same inputs and see if you get different results. If you do, there is a bug or breaking change that needs to be fixed.

The key for differential tests is to use randomly generated inputs or a sample of production traffic. You’ll also want to normalize irrelevant factors like whitespace and keep a list of approved changes for situations where the new environment should differ from the old.

We have previously written about how code review works at Anthropic, but this article aims to go deeper on how we verify our work.

Running the app end to end matters more than tests. You wouldn't ship an iOS change without trying it in a simulator, and the same goes for Claude.

Claude can test the whole app the way a human or QA engineer would. Ask it to use the Claude Chrome extension for web changes, an iOS or Android MCP for mobile, computer use for desktop, or to run the service locally for backend work.

To codify how to start the simulator or run your app, create a skill called verify. Put it in a .claude/skills/ folder in your repo, as close to the relevant code as you can, and add as many as you need. Claude knows to use the verify skill before committing changes.

Then invest in making your verify skill fast and reliable. Ask Claude to iterate on it and stress test it. It's your smoke test harness, so you want it rock solid.

When you give Claude a way to smoke test its changes end to end, you get much better results. You'll see it iterate and catch real mistakes faster, the way a human would. This is how we test nearly all changes at Anthropic.

Nobody can read every change, so we use failures as one way to decide what needs a person. Claude runs the checks and tries to fix anything that fails. If a check is still failing after three rounds, Claude stops and brings in a human.

The people who own the code write the checks for it, and refine them until they flag what the owner would flag. When a check pulls in a reviewer, it should say why, so they don't have to work it out from the diff.

We maintain a reliability checklist with 39 items, each with a trigger that can be read from a diff, a check, and the incidents or PRs behind it. One is “--resume loads old transcripts.” When session storage or message types change, we ask whether a new field loads safely, since older transcripts won’t have it.

Claude reads the diff and checks only the items whose trigger matches–usually 3 to 10–so nobody has to memorize past outages.

We don't try to improve reviews by stacking on more reviewers. Adding a second, more expensive, reviewer on top of the primary one is often a worse approach than tuning the primary. Instead, we have a REVIEW.md that says what the reviewer should pay attention to for this code.

We also think review and verification rounds should build on each other. We point each pass at context from earlier rounds and past failures rather than re-checking everything from scratch. It’s cheaper and finds more.

If a change can modify the check that judges it, the check is broken. Code Review reads the REVIEW.md file from the base or default branch, never from the pull request's changes. The Claude Code team ensures the rules that gate changes are on a branch that the change can't modify.

The Claude Code team also reserves reviews for commits. If someone's pushing while the review is happening, then the review result is no longer useful. A passing review on an out-of-date commit means nothing.

The team also runs cheap checks first. If an agent pushes before testing locally, it has spent shared review and CI time when it could have caught the bug itself. On our team, Claude runs the tests, build, and linter before opening a pull request. You can enforce this with a hook that runs the tests when Claude finishes, or a /goal of a passing test suite.

In our own repos, we stamp each commit with how it was verified. The stamp even includes "none" so we can query for commits that weren't verified.

We've also created a commit gate that can block a commit if the session did not contain /code-review or /verify. We've set it up with off, observe, and enforce modes.

Observe mode will log what would have been blocked, so that we can review any false positives and ensure no one is impacted.

Enforce mode will block the commit. Any commit can carry an explanation in its message as to why it didn't get verified. If commits have been blocked twice in the session, the next one will be allowed through so Claude doesn't get stuck – Claude Code isn't perfect.

The Claude Code team also regularly reviews the reviewers. We track how many merged changes were reverted, how many changes a maintainer rejected before merging, and a size-matched subset of changes that have stayed clean.

This can also be done with a formal evaluation. In our code review post, we described how the Code Review team has set up an evaluation based on previous incidents and reverts. They recreate the repo to the state at the time of review for each example, and provide a one-sentence answer key to what the bug was. Only findings that correctly describe the bug in question get points. They use merged and stable changes as a control to prevent over-flagging. Their tuning set is split out from the fixed test set they use to evaluate their system.

They also evaluated the recall rate for raw findings, post-verification, and final review separately. This lets them see if the system is losing bugs it had already found. Any evaluation that treats all these as one end-to-end score won't capture this nuance.

In addition to validity, the other dimension we care about is how important it is to make the change. A good reviewer will catch most things that are technically correct, but people care about whether a given bug is a must-fix, a should-fix, or a nit.

Code Review has this exact idea, and it will tag things as Important, Nit or Pre-existing. The "pre-existing" tag means that the reviewer shouldn't hold the author responsible for something that was already a bug.

Finally, the Claude Code team tunes recall up to the point where the next improvement would be overfitting to the eval rather than actually catching bugs.

In the Claude Code repo, we have two methods of turning missed cases into rules. The first is extracting patterns in human code review comments and PR reverts to identify common issues. These must occur in at least two PRs and be identifiable from a diff to be considered a potential rule. Three agents will try to disprove them, and they will be reviewed and approved by a human in a PR.

The second method is replaying three bug finders against a PR that is associated with a known incident. If at least two find the bug, it's a detectable bug. If the bug is missed on a small diff, this is a gap that is worth turning into a rule in REVIEW.md.

Flaky tests get the same treatment. Claude can't skip them, add sleeps or retry until they pass. If it can't find the root cause, it deletes the test and writes down why.

Rules need cleaning up too. Test suites, verification steps and .md files only grow if you let them, so we tidy them up on a routine.

We’ve found that giving your agent a way to verify its work with a strong feedback loop makes all the difference. Treat your verification layer like you would any other system. Keep it out of reach of the changes they judge, grade them against the bugs that mattered to you, and write down lessons when they miss something so that it doesn’t happen more than once, and prune those lessons so they stay worth running.

Do that and your job shifts from reading every diff to defining what “done” looks like and reviewing the evidence, which is what lets you run many Claudes at once.

Related posts

Nov 17, 2026Using a "chaos loop" to harden the Claude Docs launch: 60 server errors across billions of requests9 minNov 09, 2026Safely scaling multi-agent teams with Claude Fable 5.212 minNov 09, 2026Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku15 minOct 15, 2026How the Claude Code team does code review14 minOct 08, 2026Building effective agent automations9 min

LOAD MORE
