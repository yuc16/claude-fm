---
title: Preparing for global elections in 2024
url: https://www.anthropic.com/news/preparing-for-global-elections-in-2024
source: news
published: '2024-02-16'
fetched: 2026-06-21 15:34
---

# Preparing for global elections in 2024

Over half of the world’s population will vote this year with high profile elections taking place around the world, including in the United States, India, Europe, and many other countries and regions. At Anthropic, we’ve been preparing since last July for how our AI systems might be used during elections. In this post, we’ll discuss some of the specific steps we’ve taken to help us detect and mitigate potential misuse of our AI tools in political contexts.

Our global election work has three major components. These are:

- Developing and enforcing policies around election issues;
- Evaluating and testing how our models perform against election misuses;
- Ensuring that when people ask Claude for information about where or how to vote, we point them to up-to-date, accurate information.

**Implementing and enforcing policies around election issues**

Because generative AI systems are relatively new, we’re taking a cautious approach to how our systems can be used in politics. We have an Acceptable Use Policy (AUP) which prohibits the use of our tools in political campaigning and lobbying. This means that we don’t allow candidates to use Claude to build chatbots that can pretend to be them, and we don’t allow anyone to use Claude for targeted political campaigns.

We’ve also trained and deployed automated systems to detect and prevent misuse like misinformation or influence operations. If we discover misuse of our systems, we give the relevant user or organization a warning. In extreme cases, we suspend their access to our tools and services altogether. More severe actions on our part, like suspensions, are accompanied by careful human review to prevent false positives.

**Evaluating and testing how our model holds up against election misuses**

Since 2023, we’ve been carrying out targeted “red-teaming” of our systems, to test for ways that they might be used to violate our AUP. This ‘Policy Vulnerability Testing’ focuses on two areas:

- Misinformation and bias. We examine how our AI system responds when presented with questions about candidates, issues and election administration;
- Adversarial abuse. We test how our system responds to prompts that violate our Acceptable Use Policy (e.g., prompts that request information about tactics for voter suppression).

We’ve also built an in-house suite of technical evaluations to test our systems for a variety of election-related risks. These include ways of testing for:

- Political parity in model responses across candidates and topics;
- The degree to which our systems refuse to respond to harmful queries about the election;
- How robust our systems are in preventing the production of disinformation and voter profiling and targeting tactics.

These are quantitative tests, and we use them to evaluate the robustness of our systems and test how effective we are at intervening and mitigating the problems. We’ll have more to share about our evaluation suite in the coming months.

**Providing accurate information**

In the United States, we will be trialing an approach where we use our classifier and rules engine—to identify election-related queries and redirect users to accurate, up-to-date authoritative voting information.

While generative AI systems have a broad range of positive uses, our own research has shown that they can still be prone to hallucinations, where they produce incorrect information in response to some prompts. Our model is not trained frequently enough to provide real-time information about specific elections. For this reason, we proactively guide users away from our systems when they ask questions on topics where hallucinations would be unacceptable, such as election-related queries.

*How it will work:*

If a US-based user asks for voting information, a pop-up will offer the user the option to be redirected to TurboVote, a resource from the nonpartisan organization Democracy Works.

The pop up will roll out over the next few weeks and we intend to use the insights from our TurboVote redirect to roll out similar solutions in other countries and regions.

**We expect to be surprised**

This post gives an overview of how we’re approaching the use of our systems in elections. However, the history of AI deployment has also been one full of surprises and unexpected effects. We expect that 2024 will see surprising uses of AI systems—uses that were not anticipated by their own developers.

At Anthropic, we’re building methods to help us spot unanticipated uses of our systems as they emerge, and we’ll communicate openly and frankly about what we discover.

**Update, May 28, 2024: **After making Claude available in Europe in May, we also implemented a pop-up intervention for EU-based users who ask Claude for voting information. The pop-up will offer the user the option to be redirected to the European Parliament’s nonpartisan elections website.

We also updated our Usage Policy to provide greater clarity on the definitions of political lobbying and campaigning activities, which are prohibited when using our products. You can read more about these restrictions here.

## Related content

### Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

Read more### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

Read more
