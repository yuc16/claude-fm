---
title: The case for targeted regulation
url: https://www.anthropic.com/news/the-case-for-targeted-regulation
source: news
published: '2024-10-31'
fetched: 2026-06-21 15:35
---

# The case for targeted regulation

Increasingly powerful AI systems have the potential to accelerate scientific progress, unlock new medical treatments, and grow the economy. But along with the remarkable new capabilities of these AIs come significant risks. **Governments should urgently take action on AI policy in the next eighteen months. The window for proactive risk prevention is closing fast.**

Judicious, narrowly-targeted regulation can allow us to get the best of both worlds: realizing the benefits of AI while mitigating the risks. Dragging our feet might lead to the worst of both worlds: poorly-designed, knee-jerk regulation that hampers progress while also failing to be effective at preventing risks.

In this post, we suggest some principles for how governments can meaningfully reduce catastrophic risks while supporting innovation in AI’s thriving scientific and commercial sectors.

## Urgency

In the last year, AI systems have grown dramatically better at math, graduate-level reasoning, and computer coding, along with many other capabilities. Inside AI companies, we see continued progress on as-yet undisclosed systems and results. These advances offer many positive applications. But progress in these same broad capabilities also brings with it the potential for destructive applications, either from the misuse of AI in domains such as cybersecurity or biology, or from the accidental or autonomous behavior of the AI system itself.

In the realm of cyber capabilities, models have rapidly advanced on a broad range of coding tasks and cyber offense evaluations. On the SWE-bench software engineering task, models have improved from being able to solve 1.96% of a test set of real-world coding problems (Claude 2, October 2023) to 13.5% (Devin, March 2024) to 49% (Claude 3.5 Sonnet, October 2024). Internally, our Frontier Red Team has found that current models can already assist on a broad range of cyber offense-related tasks, and we expect that the next generation of models—which will be able to plan over long, multi-step tasks—will be even more effective.

On the potential for AI exacerbating CBRN (chemical, biological, radiological, and nuclear) misuses, the UK AI Safety Institute tested a range of models from industry actors (including Anthropic) and concluded that:

...models can be used to obtain expert-level knowledge about biology and chemistry. For several models, replies to science questions were on par with those given by PhD-level experts.

AI systems have progressed dramatically in their understanding of the sciences in the last year. The widely used benchmark GPQA saw scores on its hardest section grow from 38.8% when it was released in November 2023, to 59.4% in June 2024 (Claude 3.5 Sonnet), to 77.3% in September (OpenAI o1; human experts score 81.2%). Our Frontier Red Team has also found continued progress in CBRN capabilities. For now, the uplift of having access to a frontier model relative to existing software and internet tools is still relatively small, however it is growing rapidly. As models advance in capabilities, the potential for misuse is likely to continue on a similar scaling trend.

About a year ago, we warned that frontier models might pose real risks in the cyber and CBRN domains within 2-3 years. Based on the progress described above, we believe we are now substantially closer to such risks. Surgical, careful regulation will soon be needed.

## A year of Anthropic’s Responsible Scaling Policy

Grappling with the catastrophic risks of AI systems is rife with uncertainty. We see the initial glimmers of risks that could become serious in the near future, but we don’t know exactly when the real dangers will arrive. We want to make the critical preparations well in advance.

At Anthropic, we try to deal with this challenge via our Responsible Scaling Policy (RSP): an adaptive framework for identifying, evaluating, and mitigating catastrophic risks. The first principle of the RSP is that it is *proportionate*: the strength of our safety and security measures increase in proportion with defined “capability thresholds” that the AI systems meet. The “if-then” structure requires safety and security measures to be applied, but only when* *models become capable enough to warrant them.

The second key idea is that the RSP should be *iterative*: we regularly measure the capabilities of our models and rethink our security and safety approaches in light of how things have developed.

Anthropic has had a formal RSP in place since September 2023 (and recently released an updated version), and other frontier model labs have, to varying degrees, adopted similar plans.

RSPs serve many useful purposes:

- They increase a developer’s **investment in computer security and in safety evaluations**. Both security and evaluations are typically built after encountering problems, but RSPs publicly commit a developer to develop and resource these areas*ahead of time*. At Anthropic, teams such as Security, Trust & Safety, Interpretability, and the Frontier Red Team have had to ramp up hiring to have a reasonable chance of achieving the safety and security prerequisites set out by our RSP. Properly implemented, RSPs drive organizational structure and priorities. They become a key part of product roadmaps, rather than just being a policy on paper;
- RSPs serve as a forcing function for a developer to **flesh out risks and threat models**. Such models tend to be rather abstract, but an RSP makes them interact directly with the day-to-day business of a company, forcing developers to make them as specific and well-grounded as possible, and to reassess them over time;
- Having an RSP encourages developers to **be transparent about their computer security and misuse mitigation practices**. Our RSP commits us to internally document our findings and recommendations regarding the safeguards we’ve implemented. We’ve also found that our RSP has naturally generated much of the substantive work we’ve needed to meet voluntary commitments such as the White House Voluntary AI Commitments and those made at the Bletchley Park AI Safety Summit.

Our Responsible Scaling Policy isn’t perfect, but as we’ve repeatedly deployed models with it, we’re getting better at making it run smoothly while also testing for risks. **Despite the need for iteration and course-corrections, we are fundamentally convinced that RSPs are a workable policy with which AI companies can successfully comply while remaining competitive in the marketplace.**

RSP-like mechanisms are an efficient, practical way of dealing with the serious risks of AI systems, and should be adopted voluntarily across the industry. However, enforceable regulation is also important, because society will demand reassurance that AI companies are keeping to their promises.

## Responsible Scaling Policies and AI regulation

RSPs are not intended as a substitute for regulation, but as a prototype for it. Based on our experience with RSPs, we believe there are three elements that are key for effective AI regulation:

- **Transparency.**Currently, the public and lawmakers have no way to verify any AI company’s adherence to its RSP (or similar plan), nor the outcome of any tests run as part of it. A simple, sensible step is to- **require companies to have and publish RSP-like policies**, describing at a high level their capability thresholds and the related safeguards that are triggered when a model reaches them. Companies should also be required to- **publish a set of risk evaluations**of each new generation of AI systems, so as to create a public record of the risks of AI systems and best practice for mitigating those risks. Finally, there should be some mechanism to- **verify the accuracy**of these statements.
- **Incentivizing better safety and security practices.**Transparency alone does not guarantee robust policies: companies could simply declare very weak safety and security practices. AI regulation should also- **incentivize companies to develop RSPs that are effective**at preventing catastrophes. There are a number of possible mechanisms for this, with different pros and cons. For instance, regulators could identify the threat models that RSPs must address, under some standard of reasonableness, while leaving the details to companies. Or they could simply specify the standards an RSP must meet. The government can also encourage an RSP “race to the top” by inquiring about and comparing RSPs, learning from the emerging best practices, and holding companies to account if their RSPs are obviously operating beneath the bar set by those practices. Finally, there are a number of possible mechanisms for indirectly incentivizing safe practices. We are uncertain about the exact mechanism, but we feel strongly that any mechanism should be- **flexible**: the technology is developing rapidly, so it is important for regulatory processes to learn from the best practices as they evolve, rather than being static.
- **Simplicity and focus.**Whatever regulations we arrive at should be as surgical as possible. They must- **not impose burdens that are unnecessary**or unrelated to the issues at hand. One of the worst things that could happen to the cause of catastrophic risk prevention is a link forming between regulation that’s needed to prevent risks and burdensome or illogical rules. Any bill or law should also be simple to understand and implement: complexity creates confusion and makes it harder to predict what will happen in practice.

There are many different approaches that could meet these three criteria; we’re not wedded to any one in particular. Instead, we’re pragmatically interested in finding a reasonable proposal that a critical mass of stakeholders can get behind.

## The importance of getting this right - and soon

It is critical over the next year that policymakers, the AI industry, safety advocates, civil society, and lawmakers work together to develop an effective regulatory framework that meets the conditions above and is agreeable to a wide range of stakeholders. In the US, this will ideally happen at the federal level, though urgency may demand it is instead developed by individual states. The same applies to other governments around the world who are simultaneously considering AI regulation.

This regulatory framework won’t be perfect, and we are conscious that effective regulations are very hard to design. But getting this right is essential to realizing AI’s benefits and addressing its risks.

## FAQ:

Below, we address some questions we’ve heard from those who are either skeptical of any AI regulation, or who think it should take a different form. Some of them expand on points we made in the post above.

*Q: Should there be state, federal, or a combination of state and federal regulation in the US?*

A: California has already tried once to legislate on the topic and made some significant progress via SB 1047 (the Safe and Secure Innovation for Frontier Artificial Intelligence Models Act) - though we were positive about it overall, it was imperfect and was unable to garner the support of a critical mass of stakeholders. We think that federal legislation would be the ideal vehicle for regulation of AI catastrophic risks, since it would be uniform across the country and could leverage the federal government’s expertise in risks such as bioterrorism or cybersecurity. It would also strengthen the hand of the federal government in negotiations with other countries. Unfortunately, we are concerned that the federal legislative process will not be fast enough to address risks on the timescale about which we’re concerned. Thus, we believe the right strategy is to push on multiple avenues in parallel, with federal legislation as an ideal first-choice outcome, but state regulation serving as a backstop if necessary. Federal regulation could also serve to pre-empt state regulation.

*Q: What about regulation in other countries?*

Many different countries (or blocs of countries, as in the case of the European Union) are beginning to think carefully about how to regulate AI. We think the principles and approach we’ve outlined here are sufficiently simple and pragmatic that they could be helpful outside the US as well as inside it. We also expect that, as long as such policy approaches have a mechanism for standardization and mutual recognition, mandating certain common safety and security approaches for frontier AI companies could ultimately reduce the overall cost of doing business in diverse global regions.

*Q: Why not regulate AI by use case, rather than trying to regulate general models?*

A: “Regulation by use case” doesn’t make sense for the form and format in which modern AI applications are offered. On the consumer side, AIs such as Claude.ai or ChatGPT are offered to consumers as fully general products, which can write code, summarize documents, or, in principle, be misused for catastrophic risks. Because of this generality, it makes more sense to regulate the fundamental properties of the underlying model, like what safety measures it includes, rather than trying to anticipate and regulate each use case. On the enterprise side—for example, where downstream developers are incorporating model APIs into their own products—distinctions by use case may make more sense. However, it’s still the case that many, if not most, enterprise applications offer some interaction with the model to end-users, in turn meaning that the model can in principle be used for any task. Finally, it is the base model that requires a large amount of money and bottlenecked resources (for example, hundreds of millions of dollars’ worth of GPUs), so in a practical sense it is also the easiest thing to track and regulate.

*Q: This post talks a lot about CBRN misuses and cyber risks. Why not other, nearer-term risks, like deepfakes and child safety?*

This post is not an attempt to address every possible safety problem posed by generative AI systems. Instead, it aims to lay out principles for grappling with *some* types of risks which aren’t well-addressed by regulation today and which show up in computationally-intensive frontier models. We continue to address near term risks through things like our election integrity work and partnering with organizations like Thorn, on their “Safety by Design for Generative AI” initiative on child safety.

*Q: Won’t regulation slow down innovation, and reduce our ability to compete with geopolitical adversaries?*

A: It is critical that the burden of AI regulations is proportionate and tailored to the risks. The RSP framework is designed to do exactly this, by proposing tests that quickly identify models that aren’t capable of posing catastrophic risks and not subjecting them to further delays. Furthermore, even within the RSP framework, we have advocated for high flexibility in designing these tests: the science of AI risk evaluation is nascent, and we don’t want to create unnecessary burdens through inflexible rules. However, it is unrealistic that regulation would impose literally *zero *burden. Our goal should be to achieve a large reduction in catastrophic risk, for a small and manageable cost in compliance burden. One optimistic point is that we think safety requirements could actually *speed up* progress if implemented carefully: it’s been our repeated experience at Anthropic that our safety research efforts have had unexpected spillover benefits to the science of AI in general. Additionally, the security component of an RSP is designed to make it harder for both insider and outsider threats to compromise a company and exfiltrate its IP, which advances both national security and private sector innovation.

*Q: Won’t regulation harm the open source ecosystem?*

A: Our view is that regulation of frontier models should focus on empirically measured risks, not on whether a system is open-or closed-weights. Regulation should thus intrinsically neither favor nor disfavor open-weights models, except to the extent that uniform, empirically rigorous tests show them to present greater or less risk. If there are unique risks associated with open weights models—for instance, their ability to be arbitrarily finetuned onto new datasets—then regulation should be designed to incentivize developers to address those risks, just as with closed-weights models.

## Related content

### Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

Read more### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

Read more
