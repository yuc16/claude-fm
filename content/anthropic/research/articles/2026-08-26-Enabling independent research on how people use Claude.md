---
title: Enabling independent research on how people use Claude
url: https://www.anthropic.com/research/enabling-independent-research
source: research
published: '2026-08-26'
fetched: 2026-08-30 15:55
---

# Enabling independent research on how people use Claude

*Earlier this year, we ran a pilot giving external researchers access to aggregate, real-world Claude usage data. Three research groups designed their own studies for Anthropic Insights, our privacy-preserving analysis tool; we ran the data collection on their behalf, and they conducted their own independent analysis. In this post, we share high-level results from those studies and what we learned running this pilot. We’re also providing an expression of interest form for researchers who may want to work with us in the future.*

Ensuring the transition to transformative AI goes well requires understanding its impact on people and society. Right now, data on real-world interactions with AI is concentrated in a handful of labs. We think it would be good if more data was made widely available—to researchers, policymakers, and the general public.

Researchers outside the labs have two options. They can draw on analyses the labs publish, which reflect real usage but often answer the lab’s questions, rather than their own. Or they can use public datasets, which they can study however they like, but skew toward more casual use, and may not reflect how most people actually use AI. Neither is sufficient for independent research on how AI is actually being used.

This spring, we piloted a program in which three external research institutions designed and ran their own studies on Claude usage data through Anthropic Insights (formerly named ‘Clio’), the privacy-preserving tool our own teams use to analyze usage patterns across millions of Claude conversations. We hope to scale this program in the future, so we also conducted an additional privacy audit of all data shared with third-party researchers to verify that our privacy protections held (see Appendix).

We believe this is the first time external researchers have run public independent studies on an AI company's own usage data. Below, we discuss what the external teams found, what we learned running the pilot, and what we are weighing as we decide how to expand the program more widely. We are also publicly releasing the aggregate data from each project.

## What the researchers learned

We partnered with three research groups: the Social and Language Technologies (SALT) Lab at Stanford University, the Human Information Processing Lab at the University of Oxford, and METR, a non-profit organization that evaluates frontier AI models. Each group developed its own research questions and used Anthropic Insights to conduct privacy-preserving analysis of roughly 250,000 Claude.ai or Claude Code conversations from April-May 2026.

We wanted our external partners to have as much independence as possible, so our contractual review rights were limited to user privacy, information that could help people violate our usage policies, Anthropic’s confidential information, and research accuracy. Anthropic otherwise had no say in the content of the findings and the researchers are free to publish their results even if they are inconvenient for Anthropic. Below are some early results. We're excited about the directions, and about what others will find now that the data is public.

The **Social and Language Technologies Lab **studied how humans collaborate with AI. They looked at what types of work people bring to AI, what roles humans retain in completing that work, and where human-AI collaboration breaks down. They found:

- **People bring high-stakes work to AI more than expected.**Prior research suggested people mostly delegate low-accountability tasks to AI and keep consequential tasks (that is, work that affects others or is hard to undo) for themselves. But the SALT Lab found that over half of Claude conversations involved people delegating consequential tasks to AI. People were most likely to bring consequential work to Claude when seeking professional guidance, particularly on legal or financial questions.
- **People usually direct and oversee the work when they collaborate with Claude.**In nearly three-quarters of conversations, people set the direction while Claude assisted, and they usually adapted its output rather than using it verbatim. But even when directing Claude on the output they want, people vary in how much they understand and learn from what Claude produces.
- **It is common for people to experience friction when collaborating with AI.**However, that friction is often productive. The time and effort that people put into seeing how Claude attempts a task, identifying where the request was unclear or misunderstood, and iterating on their direction leads to better results–it pushes people to clarify their intent, refine the output, or stay engaged with the problem.

Read their full writeup here.

The **Human Information Processing Lab **is studying how people feel while using Claude and how that relates to Claude’s behavior. Their early results indicate:

- **How people feel when using AI is linked to how AI behaves.**The researchers found patterns of human and AI behavior appeared together in conversations: Claude being warm went together with people being more positive. Claude refusing or disagreeing went together with people pushing back. Claude being eccentric went together with people getting more intellectually engaged. And Claude simply helping went together with people seeming satisfied.
- **People’s experience when using AI looks a lot like it does on the rest of the web.**The researchers found that the patterns among states like absorption, frustration, and enjoyment in Claude conversations closely resemble those in a separate study on everyday internet browsing, suggesting similarities in how people engage with AI and with other digital activity.

They are still completing their writeup. When it is public, we will add a link to it here.

**METR **is estimating real-world productivity gains from coding agents and how these increases in productivity change across model generations. Their analysis of Claude Code conversations is still underway, but early results suggest:

- **More capable models may save users more time.**METR compared Claude’s guesses on how long tasks would have taken without AI to how long they actually took with different Claude models. Their preliminary findings indicate newer models deliver significant speedup over older models. METR plans on sharing more as their analysis develops.
- **AI can estimate time taken reasonably well.**Because the analysis relies on Claude judging how long a task would take, METR compared those judgments to known completion times from a prior developer study. Claude's estimates correlated with the actual time taken by developers.
- **Next: measure how much AI accelerates research.**METR is continuing to investigate how their study can provide insight into how much AI speeds up researchers’ work, which could become increasingly important as AI takes on more of its own development.

They are still completing their writeup. When it is public, we will add a link to it here.

## What our team learned

Sharing usage data is largely unprecedented in AI, so this pilot was as much an experiment in running such a program as it was a way to enable third-party research in a privacy-preserving way. Protecting our users’ privacy and the researchers’ independence were both paramount, and we achieved both. Anthropic Insights is designed for this—researchers never accessed raw conversations, only aggregated outputs after the same legal and privacy review as our internal work. However, all of this made the pilot slow for an AI lab’s normal research speed and resource intensive to run. Both factors present a challenge to effectively scaling it. For more details on how we ran this pilot, see the Appendix. Below we discuss what we learned and how we addressed the challenges that arose.

**It is valuable to pursue the same problem from different perspectives. **Some of our partners’ research questions overlapped with work being pursued internally. For example, METR’s proposal was similar to our economics research on “Agentic coding and persistent returns to expertise.” We found this overlap valuable: it gave external researchers the chance to examine similar data and draw their own conclusions. Whether those align with ours is something we’ll follow as their study continues. We also connected METR with our Economics team and found that this connection improved both research teams’ work.

**Research methods that work internally need to adapt for external partners. **When using Anthropic Insights, a researcher writes a question such as, “What type of guidance is this person asking for?” and Claude answers it for every conversation in the study. The answers are then aggregated into categories; researchers only see final categories and the percentage of conversations that fall under each one. Because we are relying on Claude’s judgments, the tool is sensitive to a question’s wording; a poorly phrased one can place conversations into categories that misrepresent them. Because no one can read the underlying conversations, these errors are hard to catch.

Internally, we manage this by iterating on the questions many times over weeks. External partners couldn’t do that, since repeated privacy review before sharing each dataset would have made the study infeasible. Instead, we had them test their questions on WildChat, a public dataset of human-AI conversations where they could check the answers against the underlying conversations themselves. But WildChat skews toward casual and creative use, unlike Claude traffic, so some questions that performed well on WildChat produced misleading categories once applied to actual Claude conversations. We addressed this by providing guidance on how to interpret Anthropic Insight’s outputs (see Appendix). Going forward, we are exploring how external researchers can develop their questions and categories more effectively in advance.

**Maintaining transparency about misuse without enabling it. **Some categories in our partners’ Anthropic Insights outputs surfaced violations of our Acceptable Use Policy or Terms of Service—for instance a category of people seeking guidance on a prohibited activity. We think the public should know about misuse of our platform, so we shared most of these violations. The exceptions were categories that described *how* users got around our safeguards rather than *what* they attempted. Less than 5% of categories and conversations were affected in each study, and in each case we told researchers which clusters we had altered or removed and why. As a standard practice, when Anthropic Insights surfaces such violations, we share the aggregated data with our Safeguards team for their review. This is also an important process for our work with external researchers moving forward.

## Looking forward

Understanding AI’s effects on society is too big a job for AI companies alone. Real oversight needs external researchers asking their own questions of real-world usage data and publishing what they find independently.

This pilot was an experiment: could external researchers conduct independent studies on our platform without compromising our users’ privacy? The effort was more challenging than we expected, and we learned many lessons, but so far the answer seems to be yes. Our partners pursued research we would not have thought to design ourselves, and each told us something new about AI’s real-world impacts. This is a promising first step, but there is far more to do.

The next step is for us to determine whether we can scale this program, both in what kinds of studies we can support given the constraints described above, and in how many we can run at once. We are starting slowly to ensure privacy, safety, and research quality. We want to gauge interest and understand what researchers would want to study. If you are a researcher and access to Anthropic Insights would let you pursue work you cannot do today, please fill out this form.

Appendix

The full appendix is available here. It describes how we ran the program, including how we chose our three partners, the research primer we wrote to explain the program’s goals and what Anthropic Insights can do, and how each project moved from proposal to study design to analysis. It also includes details of our collaboration agreements, which explicitly say our partners are free to publish findings even when they are inconvenient for Anthropic. Furthermore, we cover the third-party privacy audit of this data, conducted by Imperial College London, and the privacy threat model we hold all released data to. We also include guidance on interpreting the data we are releasing from our partners’ Anthropic Insights research studies.

## Contributions and acknowledgements

Kunal Handa led the project, collaborated with the partners on their research proposals, drafted research guidance and the contract, ran partners’ Anthropic Insights studies, helped build the technical infrastructure supporting partners’ research, contributed to the internal review of the Anthropic Insights outputs, and wrote the blog post. Miranda Zhang coordinated the partnerships and communications, and contributed to all parts of the work. Gabriel Nicholas coordinated the third-party privacy audit, internal review of Anthropic Insights’ outputs, and contributed to all parts of the work. Miles McCain wrote the guidance on interpreting Anthropic Insights outputs, developed technical infrastructure to support partners’ research, contributed to the internal review of the Anthropic Insights outputs, and provided feedback on the blog post and privacy threat model. Ryan Heller contributed technical infrastructure to support partners’ research. Saffron Huang contributed to the internal review of the Anthropic Insights outputs and provided key feedback and discussion. Thomas Millar and Suzanne Wang contributed technical infrastructure to support partners’ research and to the internal review of the Anthropic Insights outputs. Shan Carter, Mo Julapalli, Matt Kearney, Sarah Pollack, and Judy Shen contributed to the internal review of the Anthropic Insights’ outputs. Matthew Jagielski contributed to the privacy threat model. Shaoyi Zhang contributed technical infrastructure to support partners’ research. Heather Whitney, Ankur Rathi, Aisling Keenan, and David Saunders provided legal and privacy guidance throughout the project. Jake Eaton and Sylvie Carr contributed to the framing and writing of the blog post. Jack Clark and Michael Stern provided valuable guidance, support, and discussion throughout the process. Deep Ganguli provided detailed guidance, organizational support, and feedback throughout all stages of the project.

Additionally, we thank Miriam Chaum, Ishita Dasgupta, Esin Durmus, Adam Farina, Zoe Hitzig, Jerry Hong, Devin Kuokka, Hendson Lin, Maxim Massenkoff, Peter McCrory, Maryam Quasto, Nitarshan Rajkumar, Amie Rotherham, Divya Siddarth, Taylor Sorensen, Jerome Swannack, Alex Tamkin, Molly Villagra, Scott White, and Charles Yang for their helpful ideas, discussion, feedback, and support.

For their partnership in this program, we thank Vishakh Padmakumar, Yijia Shao, Jennifer Wang, Diyi Yang, and Dora Zhao from the Social and Language Technologies Lab at Stanford, Tsvetomira Dumbalska, Hannah Rose Kirk, and Christopher Summerfield from the Human Information Processing Lab at Oxford, and Joel Becker (now at Anthropic), Daniel Paleka, and Parker Whitfill from METR.

For conducting the third-party privacy audit, we thank Zexi Yao, Bozhidar Stevanoski, Peter Romov, Euodia Dodd, Xiaoxue Yang, and Nataša Krčo.

Citation

```
@online{handa2026enablingindependentresearch,
author = {Kunal Handa and Miranda Zhang and Gabriel Nicholas and Miles McCain and Ryan Heller and Saffron Huang and Thomas Millar and Suzanne Wang and Shan Carter and Mo Julapalli and Matt Kearney and Sarah Pollack and Judy Shen and Matthew Jagielski and Shaoyi Zhang and Heather Whitney and Ankur Rathi and Aisling Keenan and David Saunders and Jake Eaton and Sylvie Carr and Jack Clark and Michael Stern and Deep Ganguli},
title = {Enabling independent research on how people use Claude},
date = {2026-08-26},
year = {2026},
url = {www.anthropic.com/research/enabling-independent-research},
}
```
## Related content

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

Read more### How Claude is accelerating protein design and analytical chemistry

In this post, we share two results that show how Claude can help life scientists increase the pace of their research.

Read more### Patterns and problems in emerging multiagent systems

Here, we identify a few examples of behavioral tendencies in current frontier models and show how they can produce unexpected systemic failures, in hopes of starting a conversation about mitigating these risks.

Read more
