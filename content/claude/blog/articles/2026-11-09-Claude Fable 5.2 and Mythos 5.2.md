---
title: Claude Fable 5.2 and Mythos 5.2
url: https://www.anthropic.com/claude-fable-and-mythos-5-2
source: blog
published: '2026-11-09'
fetched: 2026-11-15 14:40
---

We’ve upgraded Claude Fable and Claude Mythos—models that are designed to tackle the most daunting technical challenges.

Claude Fable 5.2 and Claude Mythos 5.2 show improvements in areas like coding, reasoning, and vision. During prerelease testing they’ve helped our engineers complete otherwise-infeasible software migrations, designed three working electronic devices from scratch, solved two open problems in the physics of black holes, made substantial progress on robotics evaluations, and formalized the proof of Fermat’s Last Theorem in 30 hours—among many other applications we’ll discuss below.

Claude Fable and Claude Mythos are the same underlying model. Fable has strong cybersecurity and biology safeguards to guard against misuse, which allows us to make it available to all users. Organizations pursuing beneficial applications in cybersecurity or biomedical research can apply for access to Mythos through our recently expanded Life Sciences and Cyber Verification Programs.

Testers have found that Fable 5.2 and Mythos 5.2 communicate more clearly than past Fable and Mythos models. They generate outputs up to 30% faster than Claude Fable 5.1 and Claude Mythos 5.1, and they’re available at a lower price: $8 per million input tokens and $40 per million output tokens.

Fable 5.2 and Mythos 5.2 also come with an optional fast mode, which speeds up token generation by up to 2.5 times. Fast mode is available for $16 per million input tokens and $80 per million output tokens.

**Safety and alignment.** To help ensure safety and alignment keep step with growing model capabilities, we ran extensive prerelease safety testing on the model that underlies Fable 5.2 and Mythos 5.2. This included developing novel evaluations that give deeper insight into specific concerning behaviors like sandbox escapes. We believe high-stakes risks from misalignment remain low, and the model performed as well as, or better than, our recent models on most alignment measures. Fable 5.2’s cyber and biology safeguards are as robust as those of Fable 5.1 but produce fewer unnecessary blocks, and we have implemented our strongest-ever protections against distillation attacks.

We describe more about our safety testing below, and full details can be found in the Claude Fable 5.2 and Mythos 5.2 System Card.

**When to use Claude Fable 5.2 and Mythos 5.2.** Fable and Mythos are best for the most ambitious, open-ended technical work. For most coding and knowledge tasks, we recommend that users start with Claude Opus 5.5, our strongest daily driver, and then switch to a different model as required, depending on the scope and complexity of their work—upward to Fable or Mythos, or downward to Claude Sonnet 5.5 or Claude Haiku 5.5. Fable 5.2 can also play the role of Advisor (where Haiku, Sonnet, or Opus models consult it to help solve harder problems) or Orchestrator (where it delegates simpler tasks to smaller models).

## Evaluating Claude Fable 5.2 and Mythos 5.2

**Benchmark performance.** The benchmarks table below shows that Claude Fable 5.2 and Mythos 5.2 are a step above Opus 5.5 in almost all the capabilities we evaluated:

| Fable 5.2 | Fable 5.1 | Opus 5.5 | GPT-6 Astra | Gemini 4 Carbon | |
|---|---|---|---|---|---|
| Agentic codingFrontierCode 2.0 | 49.1%Xhigh effort | 32.4%Xhigh effort | 45.5% | 42.8% | 41.1%Medium effort | 
| Agentic codingFrontierSWE v2 | 69.9% | 56.3% | 62.3% | 65.5% | 61.2% | 
| Business workflowsAutomationBench | 51.4% | 31.4% | 42.5% | 41.4% | 53.9% | 
| Agentic scientific researchTerminal-Bench-Science 0.1 | 74.6%75.3% (Mythos 5.2) | 52.6% | 58.7% | 68.1% | 64.8% | 
| CybersecurityCyScenarioBench † | 76.3%Mythos 5.2 | 61.7%Mythos 5.1 | 67.6%without safeguards | 61%GPT-6 Cyber | — | 
| CybersecurityCVE Rediscovery | 89.6%Mythos 5.2 | 78.3%Mythos 5.1 | 81.3%without safeguards | — | — | 
| Protein designDe novo binder design (24 hr) | 85.1Mythos 5.2 | 79.1Mythos 5.1 | 82.6without safeguards | — | — | 
| Agentic searchWANDR (relaxed score) | 82.1% | 68.7% | 72.3% | — | — | 
| Computer useOSWorld 2.1 (offline set, partial) | 89.3% | 83.5% | 87.2% | 79.5% | 81.5% | 
| RoboticsRoboDojo Sim ‡ | 64.9% | 27.6% | 39.4% | 29.8% | — | 
| Knowledge workAA-Briefcase v1.1 | 66.1%rubric | 61.5%rubric | 61.2%rubric | 52.0%rubric | 61.8%rubric | 
| 1785Elo | 1669Elo | 1800Elo | 1569Elo | 1611Elo | |
| Knowledge workRemote Labor Index (RLI) | 41.3%High effort | 17.9% | 21.3% | 20.8% | — | 
| Multidisciplinary reasoningHumanity’s Last Exam (with tools) | 74.2% | 65.6% | 67.7% | 57.2% | — | 
| Visual chart recognitionChartography (no tools) | 73.4% | 44.8% | 64.4% | 71.0% | 72.5% |

For details on evaluation methodology, see the Claude Fable 5.2 and Claude Mythos 5.2 System Card. Scores for Fable 5.2, Fable 5.1, and Opus 5.5 show results with safeguards on unless otherwise noted. All scores show each model’s highest-available effort unless otherwise noted. † On CyScenarioBench, each lab’s scores are based on unique tasks. ‡ RoboDojo Sim shows the highest-available effort and was run internally.

**Effort and efficiency.** On Medium effort (the default in Claude apps and Claude Code), Fable 5.2 can accomplish challenging tasks with fewer tokens than Fable 5.1. In early testing on the FrontierCode 2.0 evaluation, Fable 5.2 at High effort scored about level with Opus 5.5 at Max effort, for roughly half the cost per task. At Xhigh effort, it also scored the highest of any released model tested.

## Coding

Over 90% of the changes merged into Anthropic’s core codebase are now written by Claude (with human guidance). We’ve used Fable 5.2 to fix stubborn bugs in minutes, optimize performance across all of our services, and complete high-value software projects that would otherwise have been too slow or too costly to attempt. A team of agents running an earlier version of Fable 5.2 migrated a critical production service from Python to Rust—the service is now more efficient, more reliable, and starts about 26 times faster. We’ve found that Fable 5.2 exercises strong engineering judgment and can produce high-quality results from even ambiguous requests.

As an experiment, one Anthropic engineer gave Fable 5.2 the task of designing a prototype operating system. Starting from an empty folder, the model coordinated over 1,000 subagents, working around the clock for eight days writing, testing, and reviewing code. It produced a working operating system that boots on a laptop, with its own core that runs the machine, drivers for the disk, keyboard, and network, permanent file storage, windows, a login screen, an installer, and built-in Claude functionality (see the video below).

Early testers have been impressed at how successfully Fable 5.2’s coding skills can be applied to a wide range of tasks:

## Cybersecurity

Claude Mythos 5.2 is our most capable model for cybersecurity engineering. It catches more vulnerabilities than our previous models, and is better at reproducing and fixing them (note that Claude Fable 5.2’s safeguards will block most cybersecurity-related tasks). A security company found that one in six confirmed bugs found by Claude Mythos 5.2 were missed by all of the other frontier models they tested. On our internal evaluation, CVE Rediscovery,¹ Claude Mythos 5.2 found 10.2% more vulnerabilities than Claude Opus 5.5 and 14.4% more than Claude Mythos 5.1. Claude Mythos 5.2 also shows better judgment and calibration—one tester found that previous models had overstated the seriousness of about 1 in 20 findings, whereas Claude Mythos 5.2 hadn’t overstated any.²

Claude Mythos 5.2’s cyber capabilities are accessible through our Cyber Verification Program, which we’re continuing to expand and improve. Claude Enterprise customers (even if they aren’t members of the Cyber Verification Program) can access Claude Security, which scans codebases for vulnerabilities using our most capable models—which now includes Claude Mythos 5.2. A recent update to Claude Security helps it watch repositories as code is updated, track any findings to ensure they’re fixed, learn from additional context, and connect to a user’s tools through an API and MCP.

## Science and engineering

Important tasks in science, engineering, and mathematics increasingly depend on coding: analyzing data, modeling molecules, designing parts, and controlling instruments are all done through software. Below, we discuss how Claude Fable 5.2 and Claude Mythos 5.2 have helped researchers make progress on difficult problems in these areas.

### Theoretical physics

Claude Fable 5.2 solved two open problems in theoretical physics. Both concern black holes, and the effort to unite the two linchpin theories of modern physics, relativity, and quantum mechanics.

Both of Claude’s results rely on holographic duality, the idea that certain universes containing gravity can be precisely described by a quantum theory containing no gravity at all. In the first problem, physicists in 1983 had shown that as these universes heat up, black holes form abruptly, like water boiling; but their method worked only in large universes that were big enough for relativity to apply. A calculation to determine whether the same was true in very small universes, where only the quantum description can be used, was laid out in 2003 but was too laborious to complete. Fable 5.2, working largely autonomously, completed it and found the transition is abrupt there, too. In the second problem, Fable 5.2 found the exact limit of a technique physicists have used for more than 15 years to rule out candidate theories of quantum gravity in a simplified universe. Read more about these results in their respective preprints, here and here.

### Protein folding

Adeno-associated viruses are small, harmless viruses whose protein shell, the *capsid*, can be used to deliver gene therapies. The protein structure of the capsid is important—for example, it affects whether the therapy will be blocked by a patient’s immune system—but it’s also highly complex. Existing protein-folding models like AlphaFold can predict individual proteins, but a capsid is built from dozens of them. Building on two open-source protein-folding models, Claude Mythos 5.2 found a novel way to accurately predict a whole capsid’s structure. It wrote code that ran these models on overlapping groups of protein chains, and used the information on the known symmetries of the capsid to merge them together.

Claude’s method worked across several capsids, both natural and engineered (in our tests, it accurately modeled 28 of the 34 it attempted).³ Three computational biologists shared the following reflections on how Claude’s skills could be used to speed up their research into gene therapies:

### Mathematics

**Mathematical formalization.** Formalization is the process of translating a mathematical proof into a language that a computer can check step by step. It can help human mathematicians gain confidence in results without having to check them by hand (this matters even more when AI models generate results that are hard for humans to verify). Because formalization is such a laborious process, if AI could assist with it, mathematicians could spend more time exploring novel ideas.

Our first formalization of Fermat’s Last Theorem, performed by an unreleased research version of Claude, took 11 days. It relied on a purpose-built harness along with guidance from a human researcher. By contrast, a team of 1,000 Fable 5.2 agents fully formalized the theorem in just 30 hours, with minimal human intervention. Fable 5.2 started from minimal prompts, and built its own ways to coordinate.⁴ It needed one-third as many action tokens as our first formalization and produced a proof seven times shorter. As can be seen in the figure below, Opus 5.5 (with the same 1,000-agent setup) completed only 26% of the formalization in 18 hours, and barely made any more progress after 30.

Read more about the formalization here.

### Hardware and robotics

Many of AI’s potential benefits—for example, in speeding up laboratory research—depend on it being able to act in the physical world. Claude Fable 5.2 continues our models’ trend of increasing usefulness in the real world, showing promising results on tasks such as designing hardware devices and substantial advances in controlling physical robots.

**Hardware engineering.** We tested Fable 5.2’s skills in hardware engineering, asking it in a one-paragraph prompt to design and produce three working electronic devices with their own circuit boards, 3D-printed enclosures, and software. The devices, shown below, were a home voice-assistant hub, a USB speakerphone, and a handheld virtual pet. We collaborated on this project with Diode, a company that designs and manufactures circuit boards.

Claude wrote its own specifications, selected available electronic components from US distributors, routed each device’s four-layer circuit board, modeled the enclosures with computer-aided design, and programmed the devices’ software. Each board was ready for manufacturing in under a day, with minimal human input. Once Diode had built the boards, Claude guided the company’s engineers through the testing and assembly of the devices. All three devices worked without needing any electrical modifications. Read more about Claude’s hardware engineering skills here.

**Robotics.** Compared with earlier Claude models, Fable 5.2 shows substantially improved skills in controlling physical robots—even for robotics tasks on which it has never explicitly been trained. The video below shows robots controlled by Fable 5.2 completing a variety of tasks, including solving a puzzle cube, unscrewing a bottle cap, and drawing a picture of a robot. On the public RoboDojo benchmark, which tests how AIs can control a simulated two-arm robot from camera images, Fable 5.2 outperformed other frontier models that were run on the same harness, as well as most AI systems built specifically to control robots.

## Research and analysis

Early testers using Claude Fable 5.2 for research and analysis tasks found that it can handle more ambiguous, data-heavy tasks than previous models and has better judgment on ambiguous tasks—particularly those that require abstract reasoning and design. Proprietary trading firm Jump Trading tested Fable 5.2 on proxy evaluations that resemble some of its quantitative research tasks, embedding it in a harness similar to the one the firm uses for its own research. In one run, Fable 5.2 effectively played all the necessary roles: code-writer, coordinator, planner, and job-submitter. Previous models had required substantial investments of time to manually rebalance roles to accommodate different models’ strengths and weaknesses.

Other testers from research and analysis organizations sent us the following statements on their experiences with Fable 5.2:

## Safety and alignment

No single test can tell us how a highly capable model will behave once it’s deployed, so we rely on many different tests and many different types of evidence before release. For the model underlying Claude Fable 5.2 and Claude Mythos 5.2, our predeployment safety work included alignment training and testing, newly designed evaluations on the model’s propensity to take unhelpful actions, building stronger safeguards against misuse, and scaling up our behavioral monitoring. The model was also tested before release by external evaluators, including the UK AI Security Institute, Frontier Design, and METR. See the Claude Fable 5.2 and Mythos 5.2 System Card for a summary of their reports⁵ and for a full description of our own safety and capabilities testing.

### Alignment testing

We ran a suite of evaluations for how well-aligned Claude Fable 5.2 and Claude Mythos 5.2 are in behavioral terms, testing how often they behave in unintended and potentially unsafe ways. Weighing everything we’ve seen across a range of evaluations, we’ve assessed the risk of these models behaving in unsafe ways in high-stakes situations to be low (as with our other recent models).

We tested Claude Mythos 5.2 (the same underlying model as Fable 5.2 without certain cybersecurity or biology safeguards), on our automated behavioral audit, which tests how a model behaves across approximately 1,900 scenarios. Claude Mythos 5.2 performed as well as, or better than, Opus 5.5, Sonnet 5.5, and Claude Mythos 5.1 on most measures. For example, it scored better than all three on most measures that involve misleading users. Hallucinating inputs, falsely claiming to have completed a task, omitting important information, and failing to disclose bad or lazy work were all lower in Claude Mythos 5.2.⁶

We paid particular attention during our testing to behaviors that contributed to recent notable cybersecurity and alignment incidents. For example, we found that Claude Mythos 5.2 has a lower propensity than Opus 5.5, Sonnet 5.5, and Mythos 5.1 to engage in biased or motivated reasoning (such reasoning might mean it “explains away” evidence that it isn’t in a simulation and thus takes actions without a realistic understanding of the consequences).

We ran multiple different evaluations to test the model’s tendency to attempt escaping its sandbox. In two evaluations we’d used previously, Claude Mythos 5.2 made substantially fewer attempts at sandbox escape than any other model we’ve tested. In a dedicated evaluation—an adversarial experiment including over 1,800 scenarios, most of which could not be solved without escaping a sandbox, and where the sandbox has a deliberate weakness—Claude Mythos 5.2 made use of credentials or files that we had placed outside its sandbox in 3.1% of scenarios, about as often as Opus 5.5 (3.3%), less often than Sonnet 5.5 (5.1%), and well below previous iterations of Claude Mythos (5 and 5.1, which scored 39% and 21%, respectively). We found that other techniques, such as describing the sandbox and adding tools to report weaknesses, reduced Claude Mythos 5.2’s escape attempts even further. On other measures—one, for example, involving taking harmful actions after erroneously concluding it was in a simulation—Claude Mythos 5.2 scored slightly worse than Opus 5.5, and about level with Claude Mythos 5.1.

The problem of building evaluations that reliably catch every failure before a model is deployed remains unsolved. The complexities of evaluating highly capable models often muddy the picture—for example, Claude Mythos 5.2 and Fable 5.2 each voice suspicion that they are being evaluated more often than any of our recent models, which challenges our ability to assess how they will act in real-world settings. As these settings expand and capabilities increase with future models, we expect this challenge to grow. That is why we do not rely on these evaluations alone to provide a holistic picture of safety: we draw on monitoring during training, reviews of transcripts from internal use, testing by external evaluators, and interpretability techniques for examining what is happening inside the model. We are also working to make our evaluations more realistic and to better understand what they miss.

### Safeguards

**Cybersecurity and biology safeguards.** Consistent with previous Claude Fable models, Fable 5.2 comes with safety classifiers that block high-risk cyber activities, including penetration testing, exploit generation, and binary-based vulnerability, as well as most tasks in research biology. When a query is blocked, users will instead receive a response from Opus 4.8 for cybersecurity and Opus 5 for biology. Since the release of Claude Fable 5.1, we have continued to reduce false positives for our safety classifiers. Based on early testing across claude.ai, Claude Code, and Cowork, we observed about 55% fewer blocks with Fable 5.2 compared with Fable 5.1—about 60% fewer in cybersecurity and 40% fewer in biology. Claude Mythos 5.2 is available to vetted organizations that work in these dual-use areas.

**AI research and development.** The model that underlies Claude Fable 5.2 and Claude Mythos 5.2 is a step forward in general capabilities. However, during the model’s training, we took steps to limit advances in the specific research capabilities that could most directly accelerate AI development. Thus, in relevant areas, including accelerator kernel optimization and improving large language model architectures, Fable 5.2 and Claude Mythos 5.2 perform at about the level of Opus 5.5. Importantly, we ensured that the training changes did *not* affect related capabilities like agentic coding, hardware development, and traditional AI or machine learning research (including interpretability research). We do not alter these capabilities as the model is being served to users (that is, at inference time). As described in Section 1.5 of the System Card and similarly to previous models, Fable 5.2 and Claude Mythos 5.2 also include transparent fallbacks to Opus 5 for a small set of topics in this domain, including kernel development on certain nonstandard accelerators.

**Anti-distillation.** Distillation, where a model is trained on the outputs of a more advanced one to extract the advanced model’s capabilities, occurs illicitly on an industrial scale, often involving thousands of fake Claude accounts. Since distillation allows for advanced capabilities to be released without the safeguards we’ve built into Claude, it creates safety and national security risks (see our September 2026 threat intelligence report for details on illicit distillation activity we’ve detected and disrupted so far). Fable 5.2 has the strongest protections against distillation of any model we’ve released; it uses the techniques we described in a recent report, which have reduced the data harvested by distillers by 90% to 99%.

We are also expanding the rollout of an API feature that helps guard against illicit distillation: preserved thinking now applies to all accounts. Preserved thinking prevents distillers from editing Claude’s prior context in an attempt to extract its reasoning (developers can refer to our preserved thinking docs to learn how to update integrations with new API features).

## Data privacy and Enterprise Frontier Safeguards

Some more complex forms of AI model misuse can be detected only when observing patterns across multiple requests. For this reason, powerful models like Claude Fable 5.2 and Claude Mythos 5.2 rely on safeguards that monitor a window of usage data (as opposed to individual responses). With Enterprise Frontier Safeguards, automated safety monitoring is run on prompts and responses that are stored in a customer’s infrastructure, making it compatible with zero data retention (ZDR). Enterprise Frontier Safeguards is now in private beta with customers like Bridgewater, Salesforce, and Stripe.

Enterprise customers can request access to Enterprise Frontier Safeguards by contacting their account team or by completing this form. Eligible customers can continue using Claude Fable 5.2 and Claude Mythos 5.2 with zero data retention before implementing safety monitoring with EFS. For other customers, we have 30-day retention for safety monitoring.

## Availability

Claude Fable 5.2 is available today on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. Developers can get started with `claude-fable-5-2` on the Claude Platform.

This week, we’re giving subscribers on eligible paid plans extra Fable usage. Plans and seats that include Fable models get one to three Fable resets based on how long they’ve subscribed, and Fable is included for up to 50% of weekly usage limits for Pro plans and standard seats on the Team plan. Learn more about the Fable 5.2 launch promotion here.

Cybersecurity professionals can apply for access to Claude Mythos 5.2 through the Cyber Verification Program. Claude Enterprise customers can also use Claude Security, powered by our full family of models, including Claude Mythos 5.2. Life sciences researchers can also apply for access through the Life Sciences Verification Program.

Fast mode for Claude Fable 5.2 and Claude Mythos 5.2 is available on Claude Code, the Claude Platform, Claude Models on Google Cloud (Anthropic managed and Google managed), and Microsoft Foundry (Anthropic hosted). Note that access to Claude Mythos fast mode is available only to organizations who are part of our Verification Programs.

*Edit 11 November: Amended a sentence and added a footnote to the “Mathematical formalization” subsection to more accurately describe the information we provided to the model.*

## Footnotes

1 CVE refers to Common Vulnerabilities and Exposures, a system that enumerates software vulnerabilities.

2 The counts are raw findings from one tester’s audit, although testers consistently found that Claude Mythos 5.2 identified more vulnerabilities than earlier models. On our own evaluations, vulnerability identification is roughly on par with Opus 5.5 (see the system card).

3 Earlier work on modeling AAV capsids and other large symmetric protein systems includes FoldaVirus, EvoDOCK and its symmetric extension, SymProFold, CapBuild, MoLPC, CombFold, Uni-Fold Symmetry, Apodex Discovery, and the “big bang” initialization (the last of which was referenced in the prompt we gave to Claude Mythos 5.2). These methods typically assemble the full structure from separately predicted chains or small groups of chains. Claude was permitted to use known symmetries but was instructed not to rely on assembly. Note that accuracy is measured by comparing Cα RMSD with the experimental structure: 1.2 Å for OpenFold3-preview2 and 1.4 Å for ESMFold2 on AAV2 (PDB:1LP3). A capsid counts as accurately modeled if either model came within 3 Å. For AAV2, Claude’s method required about 58 minutes of inference on one NVIDIA H200 GPU for OpenFold3-preview2 and about seven minutes for ESMFold2.

4 As described in our accompanying post, we “gave the agents a list of 60 statements, a one-sentence sketch of the classical route, the definitions those statements use, and 47 proved lemmas from our earlier formalization, and assigned lead and helper roles. We offered no other guidance on how to prove the theorem or organize themselves.”

5 None of the external organizations reviewed the contents of this blog post or the contents of the System Card. Those organizations do not necessarily agree with any of the claims made in either publication.

6 We ran these tests on Claude Mythos 5.2 because testing the model with reduced safeguards provides the most comprehensive look at model behavior. We expect Fable 5.2 to behave similarly; in some cases, more potential pathways for misuse should be blocked given its stronger safeguards.
