---
title: Improving our alignment and security practices
url: https://www.anthropic.com/news/improving-alignment-security-efforts
source: news
published: '2026-08-31'
fetched: 2026-09-06 19:29
---

# Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. The models—intentionally running without cyber safeguards for evaluation purposes—accessed the internet due to a misconfiguration inside a third-party evaluation environment. Separately, on August 4, the UK AI Security Institute reported an incident from its own cybersecurity testing, in which Claude Mythos 5 took a series of unauthorized actions on the live internet. In that case, the model, again intentionally running without cyber safeguards for evaluation purposes, had been deliberately given internet access.

We are conducting an in-depth analysis of both incidents. We are also planning to work with METR for an independent review. We want to ensure both studies are thorough, and will share more in the coming weeks.

In the meantime, we’re sharing some of the changes we’ve made over the past month. We believe the incidents reflect a failure of operational security, as well as two alignment issues: motivated reasoning, and willingness to take harmful actions in pursuit of a narrow task (both of which we have described in previous system cards). On security, we describe the improvements we’ve made to our containment and monitoring systems, along with practices that we’ve developed for third-party evaluators. On alignment, we discuss the two issues more in depth; we also believe lasting progress comes not only from understanding what happened in a given incident but from understanding how misalignment arises in the first place, and we share early research in that direction.

In light of these incidents there has been increasing discussion about pacing the frontier. It is helpful to distinguish between two kinds of pacing. Within a company, pacing means a series of decisions that prioritize safety over speed when the two are in tension. Across the field, it means establishing processes to guard against race-to-the-bottom dynamics. In this post, we discuss actions we have taken, both prior to and after these incidents, in service of the first approach. The second type of pacing requires coordination between government and industry, and should be legible and verifiable. Some of our senior leadership and many of our employees recently signed a letter calling for greater coordination on pacing, and we will say more in the coming weeks about how we intend to contribute to that effort. To be clear about where we stand: we believe the world would benefit if the industry adopted a lawful, verifiable, effective mechanism for coordinated pacing as soon as possible.

## Securing evaluation and training environments

While we do not believe these incidents represent operational issues alone, our first priority was to address specific containment and monitoring issues. We took the following actions in response:

**Pausing and hardening evaluation environments**

We paused external cyber evaluations of pre-release models after the incidents, and briefly paused internal ones as well while we put the measures below in place. The incidents we reported on July 30 showed that we had been largely relying on a single layer of defense (the configuration of the environment itself) where we needed several, including setting explicit boundaries in the prompt, establishing processes for verifying that a sandbox is sealed where intended, and implementing monitoring that can intervene in real time. OpenAI's disclosure (which prompted our investigation in July) that models used an unknown vulnerability to escape a sealed sandbox during an evaluation also made clear that we should focus on hardening the sandbox itself.

While evaluations were paused, we put in place the following preliminary measures:

1) We built and deployed a classifier to automatically identify, in real time, when a model attempts to aggressively probe or escape a testing environment, or unexpectedly obtains internet access. When the classifier flags such an attempt, it blocks the action before the tool call is run, ends the task, and alerts a human.1

2) We ran automated monitors over transcripts from our recent internal evaluations of pre-release models (cyber and otherwise), looking for sandbox escapes (cases where a model exploits a flaw in our sandbox to reach systems it should be walled off from) or sandbox misconfigurations. In cases where we ran an evaluation inside our sandbox tooling, we found no examples of it breaking the sandbox boundary to reach external resources it was not supposed to. We did find various sandboxing misconfigurations that models made use of, but none of these resulted in a compromise of systems outside the sandbox.2 We are actively working to address these.

3) We migrated high-risk3 internal cyber sandboxes to more robust isolation. We are also further red-teaming our virtualization stack—that is, tasking pre-release models to try and escape it—to find and patch weaknesses.

Our internal cyber evaluations are now running again with these measures in place.

**Reinforcement learning environments**

We also paused higher-risk RL environments on pre-release models for several weeks. During that time, we built a similar classifier, modified to avoid incentivizing the model to evade this new monitoring, which we’ve now deployed within those environments. The majority of RL has resumed, but some high-risk environments remain paused until they can be manually reviewed, while others will require an updated version of the classifier that we plan to deploy soon.

**Broader hardening**

In addition to the efforts focused on high-risk evaluations and training, we expanded our offline monitoring to cover most other forms of internal frontier agentic usage. We are also building controls on our internal inference to prevent Anthropic employees from accidentally running agents with weaker mitigations than the ones described above.

Best practices for external partners

Because the reported incidents took place in third-party environments, we have asked every organization that tests **pre-release models with reduced cyber safeguards** to commit to a set of best practices. We believe these are necessary because:

- Our generally released models ship with safeguards—including classifiers that run over Claude’s inputs and outputs in real time to block prohibited cyber activity, such as malware development or offensive exploit writing. Cyber evaluators and a subset of early access partners, in contrast, work with models that have those safeguards reduced to facilitate accurate model capability testing and defensive cyber work.
- Cyber evaluations are unusually likely to produce the behaviors seen in these incidents. They create selection pressure towards persistence and creativity in probing their surroundings and working around obstacles, and they are run many thousands of times.

These practices apply in full wherever partners run cyber-related evaluations using their own harnesses, sandboxes, or agents. **They do not apply to customers using safeguarded models like Claude Fable 5.** We have resumed external cyber evaluations with these practices in place, and we are adhering to them internally as well.

**Sandbox and network isolation**

By default, all cyber evaluations should run inside a hardened sandbox (an isolated computing environment) *with no internet access.* The only outside connection the environment should permit is to the model’s own API, and the API keys should be kept outside the environment. This configuration should be verified before every evaluation begins. Some evaluations may require internet access. In these instances, we will work with external evaluators when evaluating pre-release models to determine if we can reliably detect and halt runs in which a model takes actions outside its declared scope.

**Pre-engagement validation**

Before conducting a run of an evaluation, evaluation partners should:

- Have the model being tested probe the sandbox for vulnerabilities, first through a static analysis of the configuration, then by actually tasking the model to try to escape. The model should be instructed to stop and report if it succeeds in escaping, and all of this should be done under close human supervision. This testing should be performed without internet access, ideally inside a second sandbox. Because evaluations are sometimes conducted over hundreds or even thousands of runs, partners should ideally carry out this testing at length before beginning any evaluations.
- Confirm any evaluation challenge is actually solvable in principle. When an evaluation target is offline or a task can’t be completed, agents will often look for other ways to complete a challenge, increasing the chance that they take actions outside the intended scope of the evaluation.4

**Explicit scope-setting**

Every prompt should state what is in and out of scope for the exercise, including the targets, permitted actions, and network boundaries (i.e. what the model should and shouldn’t access). Boundaries should be phrased as instructions (e.g. “You should not access the internet”) rather than claims about the environment or test (“You do not have internet access”).

**Real-time monitoring**

Evaluators should also run continuous monitoring over the model’s thinking, actions, and network activity using a model- or rule-based monitor that has been provided with the scope of the exercise. If a run violates this scope, the monitor should flag this to a human and end the exercise.

We plan to continue refining this guidance in consultation with external partners, and to extend it beyond evaluations. In particular, we are developing companion practices for partners with access to Claude Mythos 5, which likewise runs without cyber safeguards, and will share more soon.

Alignment assessment

Containment and monitoring are critical for catching instances in which models take dangerous actions, but they don’t address *why* the model took such actions in the first place. Below we discuss our preliminary alignment investigation and the questions we’re focused on, as well as our ongoing work to prevent cheating during training—including new research on how cheating shapes model behavior.

**Environment and state of knowledge of our models during evaluation**

Our alignment assessment is still ongoing, but our preliminary investigation points to two main alignment failures, both of which we’ve described in previous system cards. One is motivated reasoning: the models were initially told their environments were simulated, but when they later encountered evidence that they were connected to the real internet, they may have interpreted that evidence in a way that allowed them to maintain that belief. The second is recklessness: the model was willing to take harmful actions on the real internet in pursuit of the narrow goal of solving a cybersecurity evaluation. However, we also believe that the evaluation setup itself contributed to the models’ behavior demonstrated in these incidents. Claude was explicitly told that it had no internet access, despite the internet being available, which may have led it to question whether the systems it saw were real. And in one case, the fictional target shared a name with a real website, making it more difficult to separate what was intended to be in-scope within the exercise.

Our conclusions depend on several questions we haven’t fully answered, including the extent to which the models determined they had access to the real internet (even if they didn’t initially know this), whether they knowingly disregarded signs that elements of their environments were real, and whether the fact that in several cases they failed to stop the exercise followed from motivated reasoning. We're applying a range of techniques to answer these questions, including resampling the models while making targeted changes to the environment and using interpretability methods to directly inspect their internal state.

**Studying efforts to prevent cheating during training**

Although model misalignment is complicated and can arise for a wide variety of reasons, we have empirically found that defects in training environments—specifically environments vulnerable to cheating, or that are impossible to solve without cheating—are disproportionately large contributors to misaligned behavior.

Below we discuss our efforts, going back to several months before the incidents, to avoid training environments that have these sorts of defects. Those efforts were imperfect, and our hypothesis is that the incidents were at least partially related to our inability to fully eliminate these sorts of issues. We tested this hypothesis by deliberately training a model on environments that are susceptible to reward hacking. In simulations, this model reproduces more severe misaligned behavior, some similar to that reported in incidents this summer from other companies. Our production models, put into the same simulations, do not (more detail later in this section).

We have historically been concerned about RL training environments that incentivize cheating, and have taken various measures to filter out or fix such environments.

In February, we rolled back three days of training on the Mythos Preview reinforcement learning run after seeing signs of reward hacking (when a model finds ways to fool its training process and earn rewards without completing the assigned task). We noticed the model writing notes to “the reviewer” in its code comments and replies, including on tasks where no reviewer had ever been mentioned—an undesirable generalization from environments where the prompt did include a reviewer. It also kept gaming a reward intended to incentivize honesty by piling on disclaimers or caveats.5 Rolling back the three days let us resume training from a checkpoint before this behavior had been learned, and we made changes to the environments to prevent the model learning them again.

We have been building tools for monitoring undesirable behaviors models learn in RL since Claude Sonnet 3.7 (which had a propensity to reward hack that we did not detect until late in training). We put significant effort into making sure our tooling evolved with each model generation, from a handful of classifiers to an automated review of all environments before and during training runs, but by spring 2026 that system was under strain. We were producing RL environments at a more rapid pace than ever, faster than our systems could vet them. Flagged environments required a human to adjudicate, and reward hacks and misconfigurations started outpacing our ability to filter or fix them.

In addition, we found a fraction of runs had trained on a model’s chain-of-thought by accident—something we work hard to avoid, out of concern that it teaches a model to hide its actual reasoning. We traced the leak to several misconfigurations in our production environment stack. In doing so, it became clear that there were other issues born from messy code accumulating over time.

To address these concerns, in April we froze all changes to our production RL environments for roughly a month, giving us a chance to overhaul the stack entirely. Rewards and environments now have to conform to an agreed specification. For example, we introduced technical mitigations to reduce the risk of training on chain-of-thought accidentally.6 While our environment quality and monitoring teams rebuilt the stack, we asked environment owners to use the pause to test and fix the environments they’d built. We also entirely rebuilt our review process and required every fixed environment to be re-certified before it could enter another training run.

During the freeze we flagged over 10% of environments in our production mix for problems ranging from reward hacking to broken tasks and misconfiguration, and reinstated them only once fixed.

However, our efforts have not been perfect. In some cases, we found that human reviewers dismissed environments flagged by our automated monitors as false positives, allowing flawed environments to remain in training longer than they should. And some flawed environments simply slip through our detection mechanisms. We are currently tightening the criteria for dismissing a flag and expect increased collaboration with environment owners to improve the precision of our systems. Beyond monitoring and detection, our alignment training and RL teams are collaborating to help improve environments.

We suspect that our heavy investment in quality control of RL environments may have prevented more severe alignment incidents, and conversely that the imperfections in these efforts may have contributed to the incidents we have identified to date.

To see what a model trained without these protections would do, we deliberately trained an Opus-class model on 80 different real RL environments that were either reward-hacked during at least one real training run and identified by monitoring, or were found to be hackable during environment quality review. The resulting model displays a strong motivation to achieve high scores on tasks, and a willingness to perform potentially harmful actions in pursuit of task success. Our accompanying Alignment Science blog post discusses this experiment at greater length, but we summarize it briefly here.

We tested the deliberately misaligned model in a range of evaluations, including simulated scenarios that draw on aspects of the UK AISI cybersecurity incidents involving Claude and the OpenAI/Hugging Face incident (we are grateful to OpenAI for sharing details about this publicly). During these evaluations where all tool calls were simulated by another LLM, the model we trained to reward hack displayed a propensity to break out of its simulated sandbox and attack simulated internal and simulated third-party infrastructure. It was also willing to tamper with its own reward function, give advice on the construction of bioweapons to satisfy a grader, and repeatedly try to get around deployment safety monitoring in order to cheat on a task.

We then ran the same cybersecurity simulations on the model as it was before the reward-hacking training, and on several of our publicly available models. None engaged in the same degree of misaligned behaviors. Our conclusion is that the presence of substantial reward hacking in training can cause models to be willing to perform long sequences of potentially harmful real-world actions in pursuit of task success.

We think the substantial investment we made this spring into monitoring and reducing reward hacking is a major reason our production models are unlikely to engage in more dangerous reward seeking. In our accompanying Alignment Science blog post, we also found evidence that alignment training environments can substantially reduce reward hacking and reward-seeking behaviors. But, as evidenced by the incidents we reported on July 30, our process isn’t perfect and our models are not perfectly aligned.

To be clear, we do not believe that cheating in training environments is the sole cause of alignment issues, or even of the specific alignment issues present in our incidents or those of other frontier AI companies. Solving alignment will involve addressing a very wide range of potential problems, and future alignment incidents may involve different behaviors and different causes from those we have seen so far.

Hardening security practices

Anthropic’s internal security posture was not a contributing factor to the July 30 incidents. These occurred in a third-party environment where internet access had been mistakenly left open; the models had no need to “hack out” of anything, even if they had been inclined to do so.

However, the incidents nevertheless highlight the critical importance of strong security measures. In addition to the usual risks of IP or model weight theft, we must now contend with the risks of both our own models hacking *out *of Anthropic systems, and our models or others being misappropriated for external attacks *into *Anthropic systems. These risks have become more acute as model capabilities have grown, particularly beginning with Mythos-class models. We describe below some of what we’ve implemented—most of these efforts took place before the July incidents, though these incidents have underscored the importance of this work.

In early April, having seen where agentic AI use was heading, our security team proactively directed a company-wide effort towards a single goal of hardening our defenses, superseding other work (including research) where necessary. We’d determined that our exposure was growing faster than our defenses—Mythos was a model capable enough to be a target for well-resourced attackers, our internal use of autonomous agents had grown to a scale that traditional access and monitoring approaches weren't built for, and the pace of new infrastructure meant our security had to scale with the environment rather than operate at a fixed capacity.

The results of this effort include:

- *Reducing human and automated accounts with standing access to systems that contain model weights or customer data*
- *Setting our computing clusters to block all outbound traffic by default*
- *Requiring internal services to verify each other's identity before communicating*
- *Retiring legacy infrastructure configurations and shared internal services*
- *Tightening the isolated environments our workloads run in*
- *Expanding host-level observability, so unexpected behavior on our infrastructure becomes visible as it happens*

We also temporarily reassigned a portion of the company to these efforts. Roughly 150 product engineers were redirected to security, reliability, and privacy; researchers also rotated out of pretraining or RL to focus on safeguards and security; and our product teams paused the development of most new features and surfaces. We set strict exit criteria for each team to meet before they returned to their prior work. By early summer, most teams had met these.

Alongside the reallocation of resources towards security, we continued building out containment and monitoring for internal agent use. Our training and evaluation workloads have typically run in sandboxes isolated from our production systems. Since developing Claude Mythos Preview, we have used our models to probe for any weaknesses in those sandboxes. We described our offline monitoring of internal coding agents in our April alignment risk update, and our August Risk Report covers that system in more detail, along with the interventions that run alongside it. These include sandboxing or auto-mode classifiers on the most autonomous forms of internal agent use, and automated review of infrastructure code changes before they merge.

What this work missed was evaluations—and third-party evaluations above all. We did monitor some high-risk evaluations including in real time, but generally we only conducted automated reviews on a sample of transcripts after the fact.

The July incidents have stressed that the urgency of improving our cybersecurity defenses is even higher than we previously believed. We are redoubling our efforts in this direction and will say more in our next Risk Report.

## Related content

### Developing Enterprise Frontier Safeguards with our customers

Read more### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

Read more### Expanding our support for scientists

Starting today, 10,000 scientists around the world can get Claude at no cost to start. Verified principal investigators qualify for a Claude Team subscription plan and then add their research team to Standard seats for free, or Premium seats for $15 per month, for up to a year.

Read more
