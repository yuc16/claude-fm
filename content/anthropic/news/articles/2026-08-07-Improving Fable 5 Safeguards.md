---
title: Improving Fable 5 Safeguards
url: https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards
source: news
published: '2026-08-07'
fetched: 2026-08-09 12:54
---

# Improving Fable 5's biology safeguards

We’re making updates to Claude Fable 5’s biology safeguards in a way that substantially reduces false positives. Fable 5 users will now experience many fewer “fallbacks”—where the system switches to a less capable model after they make a biology-related query. In our testing, this update reduced *biology-related* fallbacks by about 85% across our product surfaces.1

Fable 5 will thus be able to assist with a wider range of biology tasks.

In practice, users should see far fewer fallbacks on everyday health and educational questions—for example, interpreting lab results, understanding symptoms, and learning about biology in an educational context. Healthcare professionals will be able to receive more support from Fable 5 on clinical tasks.

We believe the greatest opportunity for AI to positively affect the world is in biology and medicine, and we're investing significantly in building a responsible way to give biologists frontier access. Today, Fable still falls back to Opus 5 for requests we consider dual-use—including virology, toxicology, and molecular design—so it isn't yet usable for professional biology research and drug development. We're committed to closing that gap through trusted access pathways for frontier biology capabilities.

### Why we built strong biology safeguards

Our objective is to get Fable 5’s frontier capabilities into the hands of as many of our users as possible, as quickly as possible. However, to do so, we need to manage the increasing risks that come with models this capable. One such risk is in the field of biology: Fable 5 can now outperform experts on some highly complex biological tasks and provide operational support on others. That means that it can provide genuine assistance to a researcher developing a new medical treatment (which is the reason we’re so keen to widen access to the model via both classifier improvements and trusted access programs). But in the wrong hands, those same capabilities could be used by a malicious actor, for example in developing a biological weapon. Our capability assessments show that Fable 5 could provide significant *uplift* to such an actor—that is, it could provide them with capabilities they could not find anywhere else.

It’s often difficult to tell apart beneficial and harmful uses of AI in biology. For example, in some cases researching a treatment for a disease requires scientists to produce the dangerous compounds that *cause* that disease in the first place. This is most obvious for live vaccines, which require scientists to grow the same pathogen they’re aiming to prevent. It’s also the case for some medicines. To develop the drug captopril, which treats hypertension, scientists isolated toxic components of snake venom that crash blood pressure in humans. As new biological capabilities develop on the frontier of AI, we need to be cautious to ensure that the new risks they pose do not materialize ahead of their potential scientific benefits.

Sophisticated actors who wish to use our models to do harm know how to exploit this ambiguity to obscure their intent, making dangerous tasks look like ordinary research pursuits. The US Intelligence Community’s 2026 Annual Threat Assessment makes clear that such actors exist, and that advances in biotechnology including synthetic biology and genomic editing *“could lead to novel biological threats.”* It notes that several state actors likely maintain active offensive biological and chemical weapons programs—programs that could be accelerated by access to the raw capabilities of frontier AI models.

Because of our concerns about these “dual-use” capabilities (those that could be used for beneficial or harmful purposes, and where the line between them is not always easy to draw), we intentionally launched Fable 5 with almost all biology queries blocked. This enabled us to make the model available for users in other domains. We knew this would be frustrating for legitimate biology users: it would result in a high number of false positives in the near term, where users asking biology-related questions would have their requests blocked and sent to a less capable model. Nevertheless, we chose to make this tradeoff because the cost of Fable being misused in a dual-use domain like biology could potentially be catastrophic.

### How our biology safeguards work

One of the core ways we protect against misuse in biology is via safety *classifiers:* smaller, automated AI systems that detect when Fable 5 is asked to perform a safeguarded biology task, or produce a harmful output (we've previously written about our similar classifiers in the domain of cybersecurity).

In the case of Fable 5, when a classifier fires, the model re-routes the user’s request to Opus 5, a capable model that does not have the same level of biological capability as Fable 5 and which cannot provide as much assistance to a malicious user. This is the fallback that users see when their requests are blocked.

Developing precise, robust classifiers is not a straightforward task. For a classifier to work rapidly and consistently, it has to learn the difference between what we consider “in scope” and “out of scope” for the topics and queries we consider to be potentially harmful. It takes time and iteration to tune the classifiers, avoiding both false positives (where classifiers fire on out-of-scope content) and false negatives (where in-scope content is missed). We also require our classifiers to be robust to attempts to bypass them (known as jailbreaks), which requires even further research and testing.

Starting with a very broad biology classifier meant that we could give our users access to Fable 5 while we continued our research aimed at refining it. The alternative—holding back the model until much more safeguards progress was made—would have delayed the model’s general access, and its potential benefits to our users, by weeks or months.

Over the past several weeks, we've carefully rewritten the classifier’s constitution (which consists of a collection of rules to help the model discern between safeguarded and allowed content), taking care to carve out benign uses in detail. We solicited feedback on the changes from a diverse range of experts (both internal and external to Anthropic). We then developed updated training data for the classifier based on that constitution, and retrained it, and verified the new classifier would still generally trigger for harmful and dual-use research biology content but would now enable a wider range of benign and beneficial uses.

As is illustrated in the diagram below, these updates meant that—compared to at the time of Fable 5’s launch—the classifier will trigger for many fewer benign biology-related requests.

## Conclusions

There’s still much more to be done to refine our safeguards. There will inevitably remain false positives—requests that fall within the classifier’s safety margin where the request is very low-risk but where the classifier still fires. As we noted above, Fable will continue to block dual-use professional biology and drug development queries because of potential dual-use risk. We are fully committed to developing a safe, scalable path for researchers to use our most capable models via trusted access pathways.

We hope you’ll continue to share your feedback with us so we can improve our safeguards even further.

#### Footnotes

1 As a result, we expect the total number of fallbacks—for biology–related or any other reasons—will also be reduced: by roughly 67% on Claude.ai, 55% on Cowork, 17% on Claude Code, and 7% on the Claude Platform.

## Related content

### Mariano-Florentino (Tino) Cuéllar to join Anthropic as Chief Global Affairs Officer

Mariano-Florentino (Tino) Cuéllar will join Anthropic as its first Chief Global Affairs Officer.

Read more
