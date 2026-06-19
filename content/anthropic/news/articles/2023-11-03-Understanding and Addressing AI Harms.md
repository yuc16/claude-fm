---
title: Understanding and Addressing AI Harms
url: https://www.anthropic.com/news/our-approach-to-understanding-and-addressing-ai-harms
source: news
published: '2023-11-03'
fetched: 2026-06-13 05:04
---

# Our approach to understanding and addressing AI harms

As AI capabilities rapidly advance, understanding and addressing the full spectrum of potential impacts becomes increasingly important. Today, we're sharing insights into our evolving approach to assessing and mitigating various harms that could result from our systems, ranging from catastrophic scenarios like biological threats to critical concerns like child safety, disinformation and fraud.

Why is this approach important? As models continue to evolve, we need more comprehensive ways to think about and manage their potential impacts. We believe that considering different types of harms in a structured way helps us better understand the challenges ahead and informs our thinking about responsible AI development.

Our approach complements our Responsible Scaling Policy (RSP), which focuses specifically on catastrophic risks. Identifying and addressing the full range of potential impacts requires a broader perspective. That's why we've built out a more comprehensive framework to assess harm that we can then proportionately manage and mitigate.

***Important note**: This approach is still evolving. We're sharing our current thinking while acknowledging it will continue to develop as we learn more. We welcome collaboration from across the AI ecosystem as we work to make these systems benefit humanity.

**Breaking down our approach:**

We've developed an approach that helps our teams communicate clearly, make well-reasoned decisions, and develop targeted solutions for both known and emergent harms. This approach is designed to be both principled and adaptable to keep up with the evolving AI landscape. We examine potential AI impacts across multiple baseline dimensions, with room to grow and expand over time:

- **Physical impacts:**Effects on bodily health and well-being
- **Psychological impacts:**Effects on mental health and cognitive functioning
- **Economic impacts:**Financial consequences and property considerations
- **Societal impacts:**Effects on communities, institutions, and shared systems
- **Individual autonomy impacts:**Effects on personal decision-making and freedoms

For each dimension, we consider factors like likelihood, scale, affected populations, duration, causality, technology contribution, and mitigation feasibility. This helps us understand the real-world significance of different potential impacts.

Depending on harm type and severity, we address and manage risks through a variety of policies and practices including developing and maintaining a comprehensive Usage Policy, conducting evaluations (including red teaming and adversarial testing) before and after launch, sophisticated detection techniques to spot misuse and abuse, and robust enforcement ranging from prompt modifications to account blocking. This perspective helps us balance multiple considerations: addressing harms with proportionate safeguards while maintaining the helpfulness and functionality of our systems in everyday use cases. We’re excited to share more about this work in the near future.

**Some examples of how we’ve used our framework to inform our understanding of harm**

When exploring new capabilities or features, we examine how they might introduce additional considerations across different harm dimensions. For example:**Computer Use: **As our models develop the ability to interact with computer interfaces, we consider factors like the types of software AI systems might interact with and the contexts in which these interactions occur, which helps us identify where additional safeguards might be beneficial. For computer use, we specifically examine a multitude of risks including those related to financial software and banking platforms where unauthorized automation could potentially facilitate fraud or manipulation, and communication tools where AI systems could be used for targeted influence operations or phishing campaigns. This analysis helps us develop approaches that maintain the utility of these capabilities while incorporating appropriate monitoring and enforcement to prevent misuse. For example, our initial work on computer use functionality led us to design more stringent enforcement thresholds and employ novel approaches to enforcement such as hierarchical summarization that allows us to detect harms while maintaining our privacy standards.

**Model Response Boundaries: **When considering how models should respond to different types of user requests, we've found value in examining tradeoffs between helpfulness and appropriate limitations. Models that are trained to be more helpful and responsive to user requests may also lean towards harmful behaviors (e.g., sharing information that violates our AUP or could be used in dangerous ways). Conversely, models that over-index on harmlessness can tend towards not sharing any information with users, even when requests are harmless. By thinking about both individual and societal impacts, we can better understand where to focus our safety evaluations and training. For example, with Claude 3.7 Sonnet, we evaluated different types of requests along this spectrum and improved how our model handles ambiguous prompts by encouraging safe, helpful responses rather than simply refusing to engage. This resulted in a 45% reduction in unnecessary refusals while maintaining strong safeguards against truly harmful content. This approach helps us make more nuanced decisions about model behavior, particularly in scenarios where certain vulnerable populations—such as children, marginalized communities, or individuals in crisis—might be at heightened risk.

**Looking ahead**

There's still a lot to do. Our approach to understanding and addressing harms is just one input into our overall safety strategy, but we think it represents a useful step toward more systematic thinking about AI impacts.

As AI systems become more capable, we expect new challenges will emerge that we haven't yet anticipated. We're committed to evolving our approach alongside these developments, including adapting our frameworks, refining our assessment methods, and learning from both successes and failures along the way.

We know we can't do this work alone. We invite researchers, policy experts, and industry partners to collaborate with us as we continue exploring these important questions. You can connect with us on these issues via usersafety@anthropic.com.

## Related content

### Results from the first Anthropic Public Record

Read more### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

Read more### DXC will integrate Claude into the systems banks, airlines, and other regulated industries rely on

We’re announcing a multi-year global alliance with DXC Technology, one of the world’s largest IT services companies.

Read more
