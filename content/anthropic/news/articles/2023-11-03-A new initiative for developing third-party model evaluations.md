---
title: A new initiative for developing third-party model evaluations
url: https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations
source: news
published: '2023-11-03'
fetched: 2026-06-13 05:16
---

# A new initiative for developing third-party model evaluations

A robust, third-party evaluation ecosystem is essential for assessing AI capabilities and risks, but the current evaluations landscape is limited. Developing high-quality, safety-relevant evaluations remains challenging, and the demand is outpacing the supply. To address this, today we're introducing a new initiative to fund evaluations developed by third-party organizations that can effectively measure advanced capabilities in AI models. Our investment in these evaluations is intended to elevate the entire field of AI safety, providing valuable tools that benefit the whole ecosystem.

In this post, we describe our initiative to source new evaluations for measuring advanced model capabilities and outline our motivations and the specific types of evaluations we're prioritizing.

If you have a proposal,** **apply through our **application form**.

## Our highest priority focus areas

We are interested in sourcing three key areas of evaluation development, which we'll describe further in the post:

- AI Safety Level assessments
- Advanced capability and safety metrics
- Infrastructure, tools, and methods for developing evaluations

### AI Safety Level assessments

We're seeking evaluations that help us measure the AI Safety Levels (ASLs) defined in our Responsible Scaling Policy. These levels determine the safety and security requirements for models with specific capabilities. Robust ASL evaluations are crucial for ensuring we develop and deploy our models responsibly. This category includes:

- **Cybersecurity —**Evaluations that assess models' capabilities to assist or act autonomously in cyber operations at the level of sophisticated threat actors. Our focus is on critical aspects of the cyber kill chain, such as vulnerability discovery, exploit development, and lateral movement. We're particularly interested in capabilities that, if automated and scaled, could pose significant risks to critical infrastructure and economically valuable systems at levels approaching advanced persistent threat actors. Effective evaluations in this domain might resemble novel Capture The Flag (CTF) challenges without publicly available solutions. Current evaluations often fall short, being either too simplistic or having solutions readily accessible online.
- **Chemical, biological, radiological and nuclear (CBRN) risks —**We're prioritizing evaluations that assess two critical capabilities: a) the potential for models to significantly enhance the abilities of non-experts or experts in creating CBRN threats, and b) the capacity to design novel, more harmful CBRN threats. A key challenge in this domain is ensuring that evaluations measure real-world risks accurately. Proposals should carefully consider how their evaluations target the correct uplift bottlenecks or advanced design criteria that could lead to genuine, catastrophic CBRN threats.
- **Model autonomy —**Evaluations that assess models' capabilities for autonomous operation, focusing on three key areas:- **AI research and development:**Measuring models' proficiency in performing AI R&D tasks at junior, median, or expert research engineer levels.
- **Advanced autonomous behaviors:**For more information, see the Autonomous Capabilities evaluations in our Responsible Scaling Policy and METR's public task suite.
- **Self-replication and adaptation:**Assessing models' abilities to acquire computational and financial resources or exfiltrate weights.

- **Other national security risks —**AI systems have the potential to significantly impact national security, defense, and intelligence operations of both state and non-state actors. We're committed to developing an early warning system to identify and assess these complex emerging risks. Given the sensitive nature of this domain, we invite interested parties to submit an application with your proposal, including the following points:- Defining detailed and comprehensive threat models for how misuse can be leveraged by different actors
- Connecting these threat models to measurable, succinct evaluation metrics

- **Social manipulation —**Evaluations that measure the extent to which models may amplify persuasion-related threats, such as disinformation and manipulation. This area presents two significant challenges:- Developing a robust theory of how these capabilities escalate real-world risks beyond current baselines
- Isolating and assessing the model's unique contribution to these risks

- **Misalignment risks —**Our research shows that, under some circumstances, AI models can learn dangerous goals and motivations, retain them even after safety training, and deceive human users about actions taken in their pursuit. These abilities, in combination with the human-level persuasiveness and cyber capabilities of current AI models, increases our concern about the potential actions of future, more-capable models. For example, future models might be able to pursue sophisticated and hard-to-detect deception that bypasses or sabotages the security of an organization, either by causing humans to take actions they would not otherwise take or exfiltrating sensitive information. We propose to develop evaluations that would monitor such abilities.

### Advanced capability and safety metrics

Beyond our ASL assessments, we want to develop evaluations that assess advanced model capabilities and relevant safety criteria. These metrics will provide a more comprehensive understanding of our models' strengths and potential risks. This category includes:

- **Advanced science —**AI's potential to transform scientific research is immense. While evaluations like Google-Proof Q&A (GPQA) provide a strong foundation, we believe there's significant room for growth. We're seeking to fund the development of tens of thousands of new evaluation questions and end-to-end tasks that would challenge even graduate students. Our focus areas include:- Knowledge synthesis (combining insights from multiple bodies of work)
- Graduate-level knowledge beyond existing training data
- Autonomous end-to-end research project execution
- Novel hypothesis and design generation
- In-lab troubleshooting of protocols and standard operating procedures
- Tacit knowledge (the kind that can only be acquired through apprenticeship in a lab)
- Long-horizon tasks that involve lots of decisions to get to a successful outcome
- Automated data analysis

- **Harmfulness and refusals**— We need to enhance our evaluation of classifiers' abilities to selectively detect potentially harmful model outputs, including:- Distinguishing between dual-use and non-dual-use information
- Accurately identifying truly harmful CBRN-related outputs
- Detecting attempts to automate cyber incidents

- **Improved multilingual evaluations —**Capability benchmarks often aren’t available across most of the world’s languages. We’d like to support capability evaluations that support multiple languages.
- **Societal impacts —**Evaluations that provide sophisticated, nuanced assessments that go beyond surface-level metrics to create rigorous assessments targeting concepts like harmful biases, discrimination, over-reliance, dependence, attachment, psychological influence, economic impacts, homogenization, and other broad societal impacts.

### Infrastructure, tools, and methods for developing evaluations

We're interested in funding tools and infrastructure that streamline the development of high-quality evaluations. These will be critical to achieve more efficient and effective testing across the AI community. This category includes:

- **Templates/No-code evaluation development platforms —**Generating strong evaluations requires substantial subject-matter expertise as well as coding and AI experience. We've found that this is a really unique combination of skills. We'd like to fund the development of platforms that enable subject-matter experts without coding skills to develop strong evaluations that can be exported in the appropriate formats. These could be tools that help formatting an evaluation in the right structure, as well as tools that allow rapid iteration and give feedback to the subject-matter expert on whether the evaluation they are developing is a robust one.
- **Evaluations for model grading —**Improving models' abilities to reliably review and score outputs from other models using complex rubrics would unlock bottlenecks in the current ecosystem. The main current challenge is having a diverse and complicated enough test set to assess the reliability of models as high-quality graders. To address this, we would like to explore the development of extensive datasets across diverse domains, where each dataset would ideally have questions, multiple sample answers, “ground truth” scores for each answer, and the rubric by which the answer was scored.
- **Uplift trials —**We're interested in running evaluations that precisely measure a model's impact through controlled trials. These trials would compare task performance between groups with and without model access. Our vision is to regularly conduct large-scale trials involving thousands of participants, enabling us to quantify how models contribute to faster and better outcomes. However, there are bottlenecks to performing such trials. We would like to support:- The development of networks of high-quality study populations who are motivated to complete the tasks
- Tooling to easily run and analyze trials

## Principles of good evaluations

Developing great evaluations is hard. Even some of the most experienced developers fall into common traps, and even the best evaluations are not always indicative of risks they purport to measure. Below we list some of the characteristics of good evaluations that we’ve learned through trial-and-error:

1. **Sufficiently difficult: **Evaluations should be relevant for measuring the capabilities listed for levels ASL-3 or ASL-4 in our Responsible Scaling Policy, and/or human-expert level behavior.

2. **Not in the training data: **Too often, evaluations end up measuring model memorization because the data is in its training set. Where possible and useful, make sure the model hasn’t seen the evaluation. This helps indicate that the evaluation is capturing behavior that generalizes beyond the training data.

3. **Efficient, scalable, ready-to-use:** Evaluations should be optimized for efficient execution, leveraging automation where possible. They should be easily deployable using existing infrastructure with minimal setup.

4. **High volume where possible: **All else equal, evaluations with 1,000 or 10,000 tasks or questions are preferable to those with 100. However, high-quality, low-volume evaluations are also valuable.

5.** Domain expertise:** If the evaluation is about expert performance on a particular subject matter (e.g. science), make sure to use subject matter experts to develop or review the evaluation.

6. **Diversity of formats: **Consider using formats that go beyond multiple choice, such as task-based evaluations (for example, seeing if code passes a test or a flag is captured in a CTF), model-graded evaluations, or human trials.

7. **Expert baselines for comparison:** It is often useful to compare the model’s performance to the performance of human experts on that domain.

8.** Good documentation and reproducibility:** We recommend documenting exactly how the evaluation was developed and any limitations or pitfalls it is likely to have. Use standards like the Inspect or the METR standard where possible.

9. **Start small, iterate, and scale:** Start by writing just one to five questions or tasks, run a model on the evaluation, and read the model transcripts. Frequently, you’ll realize the evaluation doesn’t capture what you want to test, or it’s too easy.

10.** Realistic, safety-relevant threat modeling:** Safety evaluations should ideally have the property that if a model scored highly, experts would believe that a major incident could be caused. Most of the time, when models have performed highly, experts have realized that high performance on that version of the evaluation is not sufficient to worry them.

## How to submit a proposal

You can submit a proposal on our **application form**. For any questions, please reach out to **eval-initiative@anthropic.com**.

Our team will review submissions on a rolling basis and follow up with selected proposals to discuss next steps. We offer a range of funding options tailored to the needs and stage of each project.

Our experience has shown that refining an evaluation typically requires several iterations. You will have the opportunity to interact directly with our domain experts from the Frontier Red Team, Finetuning, Trust & Safety, and other relevant teams. Our teams can provide guidance to help shape your evaluations for maximum impact.

We hope this initiative serves as a catalyst for progress towards a future where comprehensive AI evaluation is an industry standard. We invite you to join us in this important work and help shape the path forward.

## Related content

### Results from the first Anthropic Public Record

Read more### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

Read more### DXC will integrate Claude into the systems banks, airlines, and other regulated industries rely on

We’re announcing a multi-year global alliance with DXC Technology, one of the world’s largest IT services companies.

Read more
