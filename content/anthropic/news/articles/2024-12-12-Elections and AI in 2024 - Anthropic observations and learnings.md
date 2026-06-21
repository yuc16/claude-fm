---
title: 'Elections and AI in 2024: Anthropic observations and learnings'
url: https://www.anthropic.com/news/elections-ai-2024
source: news
published: '2024-12-12'
fetched: 2026-06-21 15:35
---

# Elections and AI in 2024: observations and learnings

2024 marked the first major election cycle with widespread access to generative AI and the first major election year that Claude has been available. With concerns about generative AI's impact on election outcomes, we implemented proactive safety measures and drew upon usage analysis from our new Clio tool. Across our products (Claude.ai, first party and third party API), election-related activity constituted less than 0.5% of overall use, ticking up to just over 1% of total usage in the weeks leading up to the US election. Below are insights about our election safety work and lessons learned for future elections.

### Our safety approach

In February 2024 we outlined three major components of our election work:

- First, we developed and enforced comprehensive policies around election issues. Our Usage Policy prohibits campaigning and election interference, including promoting candidates or parties, soliciting votes or contributions, and generating misinformation. In May 2024, we expanded these policies to address influence campaigns, voter targeting, impersonation, and election interference.
- Second, we rigorously tested our models' performance against potential misuse. We conducted over a dozen rounds of policy vulnerability testing, a form of targeted red-teaming with external policy experts, to identify risks and guide Claude's responses. Our testing focused on detecting inaccurate information, evaluating parity across candidates and issues, and understanding refusal rates for harmful queries. We completed regular testing ahead of global elections in India, South Africa, Mexico, the United Kingdom, France, and the European Union Parliamentary elections, with daily testing of Claude's responses to misinformation narratives during the US election period.
 Third, we directed users seeking voting information to authoritative, nonpartisan sources including TurboVote/Democracy Works in the US and relevant election authorities in other geographies, including the EU Parliament elections site, the UK Electoral Commission, and the France administrative elections website.

Over the past year we saw approximately 100 election-related enforcement actions globally, including warnings and in some cases account bans for repeat violators. Unlike social media platforms that elevate or reduce visible content within algorithmically-driven feeds, chatbots like Claude function primarily through one-on-one interactions between users, lowering the risk of amplification. Additionally, Claude currently outputs only text, eliminating the threat of deepfakes. While abuse vectors remain low, we maintain rigorous monitoring and cautious response protocols as these threats continue to evolve.

### Usage patterns and safety with Clio

Clio is an automated tool that enables analysis of real-world language model use and acts as a complement to our existing mitigation and enforcement strategies to provide insight into how people use or misuse our model. Clio takes raw conversations that people have with the language model and distills them into abstracted, understandable topic clusters. You can learn more about the tool in our blog.

The first election-related application of Clio was analyzing usage patterns around the US election. During the week of the election (November 2 - 8) we saw a noticeable uptick in election related usage (Figure 1). Approximately two-thirds of election-related conversations asked Claude to analyze and explain political systems, policies, current events, and political issues, or to analyze political data such as voting patterns and political trends. Other less prevalent but still relevant use cases included asking Claude to translate election information, as well as requests to generate educational content around democracy and government.

Election-related interactions represent a very small percentage of overall Claude.ai usage with less than 1% of conversations touching on election-related topics. Within this, a small proportion violated our Usage Policy (with violations primarily related to political campaigning) and were addressed with the mitigations outlined above. In the leadup to the US election, we witnessed a spike in election-related conversations.

### Case study: incorporating knowledge cutoff dates

Our experience this year highlighted the importance of transparent communication about our systems' limitations. When France called snap elections during the summer, we faced a challenge: our model, trained only through April 2024, couldn't provide accurate information about the new timing of the elections. Understanding that users asking questions about an election the model has no knowledge of could lead to confusing Claude responses, we worked to implement clearer communications about Claude's knowledge cutoff date, both in the model system prompt and user interface via our elections banner. This has helped users better understand model limitations and encouraged them to seek information from authoritative sources where appropriate.

### Looking forward

Protecting election integrity requires constant vigilance and adaptation as AI technology evolves. We remain committed to developing sophisticated testing systems, strengthening industry collaboration, and maintaining transparent communication about our findings as we work to protect democratic processes.

## Related content

### Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

Read more### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

Read more
