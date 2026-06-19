---
title: Building AI agents for financial services
url: https://claude.com/blog/building-ai-agents-in-financial-services
source: blog
published: '2025-10-30'
fetched: 2026-06-13 12:16
---

# Building AI agents for financial services

Financial institutions are deploying autonomous AI systems to improve operations while navigating regulatory complexity and risk. Here's how.

Financial institutions are deploying autonomous AI systems to improve operations while navigating regulatory complexity and risk. Here's how.

- October 30, 2025
- 5min

In financial services, AI agents are moving beyond pilot programs to deliver concrete business value.

In banking, wealth management, and insurance, autonomous AI agents are transforming how customers understand spending patterns and find savings opportunities. Among other use cases, these tools spot potential overdraft fees, suggest better savings strategies, and guide financial decisions.

For instance, McKinsey research shows that financial institutions adopting AI agent workflows in fraud detection could generate two hundred to two thousand percent productivity gains, while Norges Bank Investment Management (NBIM) employees save hundreds of cumulative hours per week on analytical and operational tasks using Claude.

For most organizations, the real challenge isn't adopting AI agents. It's building systems that navigate complex regulations, manage real-time risk, and protect customer assets while improving business outcomes.

Agents represent a fundamental shift in enterprise AI, replacing generative AI tools that depend upon constant human input and oversight with autonomous systems that handle long-running, context-heavy tasks with minimal – if any – intervention.

This evolution is especially welcome in financial services, where data often lives in fragmented systems that don't talk to each other, making it harder to see the complete picture of a customer's financial health. Agentic systems can understand financial context, ingest information from multiple unrelated sources, process multiple kinds of data (transaction records, market data, regulatory documents), and apply all of these capabilities to taking meaningful actions within your customer’s existing financial workflows.

What does this look like in practice? Instead of an analyst manually pulling data from five different systems, reviewing it, and then updating a risk assessment, an agent can monitor transaction patterns across those systems, recognize concerning trends, draft updated risk recommendations based on current regulations, and route them to the right analyst for approval. The agent handles the coordination and analysis, while the analyst makes the final decision.

This shift from traditional AI to AI agents is particularly significant for financial services because it tackles the process completion problem. Financial workflows don't just need information, they need actions taken across multiple systems to actually complete transactions and maintain compliance. Agents can bridge those gaps.

AI-powered financial agents are already delivering real-world results in areas such as customer service, fraud detection, and workforce empowerment.

Customer service operations are a natural starting point because this area has already proven successful. Financial institutions implementing AI-powered customer service are seeing measurable improvements:

- Multilingual virtual assistants now handle hundreds of millions of interactions annually, serving millions of users across different language groups.
- Customer service agents automate routine tasks like balance inquiries and card replacements, reducing wait times while delivering 24/7 responses and suggesting relevant products, turning support interactions into opportunities to actually help people manage their finances.

Intuit TurboTax, for example, built an AI financial assistant powered by Claude that generates clear and accurate tax explanations for millions of customers. The agentic implementation was so successful that the AI-powered experiences achieved higher customer ratings compared to non-Claude experiences in the previous tax season.

In fraud detection and cybercrime prevention, AI agents excel at spotting patterns that may slip past human analysts due to sheer volume. When you consider that financial institutions currently catch only about 2% of global financial crime, you can see why this matters.

AI agents monitor millions of transactions in real-time, working around the clock without the fatigue or cognitive limitations that affect human teams. McKinsey found that a single team member can effectively supervise more than 20 AI agents in financial crime-detection workflows.

For Brex, a modern financial platform, Claude powers their AI anomaly detection, reviewing 100% percent of transactions and providing critical aircover for financial professionals by proactively grouping related expenses, flagging policy concerns, and providing explanations with recommended actions.

AI agents deliver tangible benefits right where your teams need them most. When implemented thoughtfully, these tools don't replace your workforce but rather amplify what they can accomplish and let them focus on the high-value work that requires their knowledge and expertise. Here's how financial services organizations like Block and Campfire are doing this:

- Design teams turn ideas into working prototypes without coding barriers
- Operations teams automate case ticket closure
- Accounting teams query financial data through natural language, perform flux analyses, and access audit support

Banks and financial institutions face unique challenges that make AI agent implementation more complex than typical enterprise deployments. When every decision potentially impacts customer finances, regulatory compliance, and institutional risk, the stakes are at a different level altogether.

The combination of complex financial contexts, regulatory requirements, and direct impact on customer outcomes creates an implementation environment where thoroughness trumps speed. These are some of the challenges you can expect to encounter.

Financial institutions typically run on decades-old core banking systems that weren't designed for real-time AI integration. Your loan origination system, trading platforms, and compliance databases often use different protocols, data formats, and security models.

Legacy system integration often shows up in:

- Core banking platform incompatibilities across vendors
- Departmental data silos requiring cross-system orchestration
- Legacy mainframe integration challenges
- Real-time synchronization needs for time-sensitive trading decisions

When tackling these challenges, teams need to make practical decisions about integration approaches. The first consideration involves connectivity: does the AI agent have direct integration capabilities with the necessary systems? If not, teams face two practical options: building custom connectors (typically through APIs or MCP approaches) or implementing middleware systems to bridge these communication gaps.

For early agentic solutions, look to integrate with modern platforms with APIs and standard protocols. If you decide you need to connect to legacy systems, you'll need to develop middleware that can translate between these systems while maintaining transaction integrity and audit trails.

A single transaction might trigger compliance requirements from multiple regulators, including SEC, FDIC, state banking authorities, and international bodies for cross-border payments. AI agents must understand not just what actions to take, but which regulatory frameworks apply to each decision and how to document actions for different audit requirements.

Some regulatory considerations that need to be part of your agent architecture include:

- SOC 2 and PCI DSS compliance for AI data processing workflows
- Evidence-based validation of risk assessment accuracy
- Documentation requirements for AI decision audit trails

Ensure you build observability and traceability into the agentic solutions from day one. You'll want it simply from a troubleshooting perspective, but you'll definitely need it from a regulatory one.

Unlike other industries where decisions can be reviewed later, financial agents often make choices that immediately impact customer accounts, market positions, or regulatory standing. This demands fail-safe architectures where agents can act quickly but always within predefined risk parameters that protect both customers and the institution.

Implementation requires:

- Transparent reasoning that financial professionals can validate and explain to clients
- Clear escalation pathways for complex or ambiguous financial situations
- Override capabilities allowing advisors to reject AI recommendations when client circumstances warrant
- Fail-safe defaults that prioritize customer protection over operational efficiency

Identify which actions will require human-in-the-loop authorization, either from a risk or regulatory perspective. For high-risk actions, consider how the system, agentic or otherwise, can fail in a known safe state.

AI agents are already transforming financial operations for some companies. There are abundant examples of agents currently in production and delivering measurable impact on fraud detection, customer satisfaction, and operational efficiency. So, how do you build and deploy agents that address your specific operational challenges, while making sure they meet regulatory requirements and risk management standards?

The best agent initiatives begin by targeting the things that everyone already agrees need fixing. Clear metrics make all the difference here, because they show whether the solution actually works and help build momentum for wider adoption.

Target opportunities for adding agents within your organization to areas where the stakes are manageable, but the potential impact is meaningful.

Look for processes where human oversight already exists or where consequences of imperfect automation remain minimal: these are perfect for early adoption without introducing excessive organizational risk. Customer service triage, internal knowledge retrieval, and routine data validation are natural entry points where AI agents can immediately reduce workloads while humans remain in the verification loop.

Beyond immediate productivity gains, these initial agent deployments are extremely valuable learning experiences. Each low-risk implementation helps your teams develop practical understanding of agent capabilities, limitation patterns, and integration requirements without the pressure of mission-critical deadlines. Your technical staff learns to fine-tune prompts and monitoring systems in environments where mistakes are learning opportunities rather than costly errors.

Start with agents that handle one straightforward task, like flagging unusual transaction patterns, monitoring compliance deadlines, or automating document classification.

You'll get tangible operational improvements while keeping human judgment firmly in the loop while building the organizational muscle memory needed for more ambitious agent applications. When you eventually tackle higher-risk use cases, you'll have technical capabilities and confidence built through experience rather than theoretical assumptions about how agents might perform in your specific environment.

Success with initial implementations opens the door to enterprise-wide capabilities. The key is moving from point solutions to shared infrastructure that serves multiple departments.

Your organization will get better results when you build foundational AI agent capabilities that serve multiple departments rather than deploying one-off solutions for individual problems.

For example, you might implement a document processing capability that could be used across your organization. The same AI system that automates bank reconciliations and invoice processing can help compliance teams analyze regulatory documents and support various departments with financial data extraction. Each department contributes use cases that strengthen the core capability while benefiting from improvements driven by other teams.

Agents interact with both your workforce and your customers, and each group will respond differently to AI-assisted processes. Trust-building matters as much as technical deployment.

For customers, transparency matters. Make it clear when they're interacting with an AI agent versus a human, explain what the agent can and cannot do, and provide straightforward pathways to human specialists when needed. This clarity builds confidence and encourages broader adoption of AI-assisted services.

Internal adoption follows similar principles. Your organization already has change management processes for new systems. Apply them here. Staff need to understand how agents work, when to trust their recommendations, and how to escalate concerns.

Frame the conversation around enhancement rather than replacement. For example, Block's internal AI agent reached 4,000 active users out of 10,000 employees across 15 different job profiles (sales, design, product, customer success, and operations). Adoption doubled in one month, with user engagement increasing 40-50% weekly as employees found new ways to use it.

The most successful implementations emphasize how AI enhances human capabilities rather than replacing them.

At this stage, your organization has an augmented workforce, refined core capabilities, demonstrated wins, and experienced teams ready for larger challenges. The lessons learned from early implementations provide the foundation for more complex agent deployments.

The observability and human-in-the-loop mechanisms you built for simpler use cases become even more critical as complexity increases. More than ever, your implementation needs:

- **Comprehensive audit trails**that track every agent decision and data source used, enabling review and regulatory compliance
- **Real-time monitoring systems**that detect when agents encounter edge cases or uncertain scenarios requiring human judgment
- **Escalation protocols**that automatically route complex cases to appropriate specialists based on clear criteria
- **Performance metrics**that measure not just technical accuracy but business outcomes and workflow integration success

AI agents represent a significant opportunity to address persistent challenges in financial services. Success requires thoughtful implementation that balances technological capability with industry-specific requirements. This approach delivers quick wins that build confidence while establishing the foundation for more sophisticated initiatives.

The path forward demands partnership between technology and business teams. Financial services leaders who prioritize customer protection through robust testing and escalation pathways, and build modular systems that evolve with advancing AI capabilities, will lead the way.

Learn how organizations like NBIM, Brex, and Verisk build and deply AI agents at scale with Claude in AWS Bedrock.

Learn more about how organizations like Visa, Citi, and NBIM are transforming their industries with Claude for Financial Services.

Get the developer newsletter
