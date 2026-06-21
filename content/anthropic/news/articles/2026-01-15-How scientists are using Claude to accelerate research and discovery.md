---
title: How scientists are using Claude to accelerate research and discovery
url: https://www.anthropic.com/news/accelerating-scientific-research
source: news
published: '2026-01-15'
fetched: 2026-06-21 15:29
---

# How scientists are using Claude to accelerate research and discovery

Last October we launched Claude for Life Sciences—a suite of connectors and skills that made Claude a better scientific collaborator. Since then, we've invested heavily in making Claude the most capable model for scientific work, with Opus 4.5 showing significant improvements in figure interpretation, computational biology, and protein understanding benchmarks. These advances, informed by our partnerships with researchers in academia and industry, reflect our commitment to understanding exactly how scientists are using AI to accelerate progress.

We’ve also been working closely with scientists through our AI for Science program, which provides free API credits to leading researchers working on high-impact scientific projects around the world.

These researchers have developed custom systems that use Claude in ways that go far beyond tasks like literature reviews or coding assistance. In the labs we spoke to, Claude is a collaborator that works across all stages of the research process: making it easier and more cost-effective to understand which experiments to run, using a variety of tools to help compress projects that normally take months into hours, and finding patterns in massive datasets that humans might overlook. In many cases it’s eliminating bottlenecks, handling tasks that require deep knowledge and have previously been impossible to scale; in some it’s enabling entirely different research approaches than researchers have traditionally been able to take.

In other words, Claude is beginning to reshape how these scientists work—and point them towards novel scientific insights and discoveries.

## Biomni: a general-purpose biomedical agent with access to hundreds of tools and databases

One bottleneck in biological research is the fragmentation of tools: there are hundreds of databases, software packages, and protocols available, and researchers spend substantial time selecting from and mastering various platforms. That’s time that, in a perfect world, would be spent on running experiments, interpreting data, or pursuing new projects.

Biomni, an agentic AI platform from Stanford University, collects hundreds of tools, packages, and data-sets into a single system through which a Claude-powered agent can navigate. Researchers give it requests in plain English; Biomni automatically selects the appropriate resources. It can form hypotheses, design experimental protocols, and perform analyses across more than 25 biological subfields.

Consider the example of a genome-wide association study (GWAS), a search for genetic variants linked to some trait or disease. Perfect pitch, for instance, has a strong genetic basis. Researchers would take a very large group of people—some who are able to produce a musical note without any reference tone, and others you would never invite to karaoke—and scan their genomes for genetic variants that show up more often in one group than another.

The genome scanning is (relatively) simple. It’s the process of analyzing and making sense of the data that’s time-consuming: genomic data comes in messy formats and needs extensive cleaning; researchers must control for confounding and deal with missing data; once they identify any “hits,” they need to figure out what they actually mean—what gene is nearby (since GWAS only points to locations in a genome), what cell types it’s expressed in, what biological pathway it might affect, and so on. Each step might involve different tools, different file formats, and a lot of manual decision-making. It’s a tedious process. A single GWAS can take months. But in an early trial of Biomni, it took 20 minutes.

This might sound too good to be true—can we be sure of the accuracy of this kind of AI analysis? The Biomni team has validated the system through several case studies in different fields. In one, Biomni designed a molecular cloning experiment; in a blind evaluation, the protocol and design matched that of a postdoc with more than five years of experience. In another, Biomni analyzed the data from over 450 wearable data files from 30 different people (a mix of continuous glucose monitoring, temperature, and physical activity) in just 35 minutes—a task estimated to take a human expert three weeks. In a third, Biomni analyzed gene activity data from over 336,000 individual cells taken from human embryonic tissue. The system confirmed regulatory relationships scientists already knew about, but also identified new transcription factors—proteins that control when genes turn on and off—that researchers hadn’t previously connected to human embryonic development.

Biomni isn’t a perfect system, which is why it includes guardrails to detect if Claude has gone off-track. Nor can it yet do everything out of the box. However, where it comes up short, experts can encode their methodology as a skill—teaching the agent how an expert might approach a problem, rather than letting it improvise. For example, when working with the Undiagnosed Diseases Network on rare disease diagnosis, the team found that Claude's default approach differed substantially from what a clinician would do. So they interviewed an expert, documented their diagnostic process step by step, and taught it to Claude. With that new, previously-tacit knowledge, the agent performed well.

Biomni represents one approach: a general-purpose system that brings hundreds of tools under one roof. But other labs are building more specialized systems—targeting specific bottlenecks in their own research workflows.

## Cheeseman Lab: automating the interpretation of large-scale gene knockout experiments

When scientists want to understand what a gene does, one approach is to remove it from the cell or organism in question and see what breaks. The gene-editing tool CRISPR, which emerged around 2012, made this easy to do precisely at scale. But the utility of CRISPR was still limited: labs could generate far more data than they had the bandwidth to analyze.

This is exactly the challenge faced by Iain Cheeseman’s lab at the Whitehead Institute and Department of Biology at MIT. Using CRISPR, they knock out thousands of different genes across tens of millions of human cells, then photograph each cell to see what changed. The patterns in those images reveal that genes that do similar jobs tend to produce similar-looking damage when removed. Software can detect these patterns and group genes together automatically—Cheeseman's lab built a pipeline to do exactly this called Brieflow (yes, brie the cheese).

But interpreting what these gene groupings mean—why the genes cluster together, what they might have in common, whether it’s a known biological relationship or something new—still requires a human expert to comb through the scientific literature, gene by gene. It’s slow. A single screen can produce hundreds of clusters, and most never get investigated simply because labs don’t have the time, bandwidth, or in-depth knowledge about the diverse things that cells do.

For years, Cheeseman did all the interpretation himself. He estimates he can recall the function of about 5,000 genes off the top of his head, but it still takes hundreds of hours to analyze this data effectively. To accelerate this process, PhD student Matteo Di Bernardo sought to build a system that would automate Cheeseman’s approach. Working closely with Cheeseman to understand exactly how he approaches interpretation—what data sources he consults, what patterns he looks for, what makes a finding interesting—they built a Claude-powered system called MozzareLLM (you might be seeing a theme developing here).

It takes a cluster of genes and does what an expert like Cheeseman would do: identifies what biological process they might share, flags which genes are well-understood versus poorly studied, and highlights which ones might be worth following up on. Not only does this substantially accelerate their work, but it is also helping them make important additional biological discoveries. Cheeseman finds Claude consistently catches things he missed. “Every time I go through I’m like, I didn’t notice that one! And in each case, these are discoveries that we can understand and verify,” he says.

What helps make MozzareLLM so useful is that it isn’t a one-trick pony: it can incorporate diverse information and reason like a scientist. Most notably, it provides confidence levels in its findings, which Cheeseman emphasizes is crucial. It helps him decide whether or not to invest more resources in following up on its conclusions.

In building MozzareLLM, Di Bernardo tested multiple AI models. Claude outperformed the alternatives—in one case correctly identifying an RNA modification pathway that other models dismissed as random noise.

Cheeseman and Di Bernardo envision making these Claude-annotated datasets public—letting experts in other fields follow up on clusters his lab doesn't have time to pursue. A mitochondrial biologist, for instance, could dive into mitochondrial clusters that Cheeseman's team has flagged but never investigated. As other labs adopt MozzareLLM for their own CRISPR experiments, it could accelerate the interpretation and validation of genes whose functions have remained uncharacterized for years.

## Lundberg Lab: testing AI-led hypothesis generation for which genes to study

The Cheeseman lab uses optical pooled screening—a technique that lets them knock out thousands of genes in a single experiment. Their bottleneck is interpretation. But not every cell type works with pooled approaches. Some labs, such as the Lundberg Lab at Stanford, run smaller, focused screens, and their bottleneck comes earlier: deciding which genes to target in the first place.

Because a single focused screen can cost upwards of $20,000 and costs increase with size, labs typically target a few hundred genes they think are *most likely* to be involved in a given condition. The conventional process involves a team of grad students and postdocs sitting around a Google spreadsheet, adding candidate genes one by one with a sentence of justification, or maybe a link to a paper. It's an educated guessing game, informed by literature reviews, expertise, and intuition, but constrained by human bandwidth. It’s also fallible, based as it is on what other scientists already figured out and written down, and what the humans in the room happen to recall.

The Lundberg Lab is using Claude to flip that approach. Instead of asking “what guesses can we make based on what researchers have already studied?”, their system asks “what *should* be studied, based on molecular properties?”

The team built a map of every known molecule in the cell—proteins, RNA, DNA—and how they relate to each other. They mapped out which proteins bind together, which genes code for which products, and which molecules are structurally similar. They can then give Claude a target—for instance which genes might govern a particular cellular structure or process—and Claude navigates that map to identify candidate genes based on their biological properties and relationships.

The Lundberg lab is currently running an experiment to study how well this approach works. To do so, they needed to identify a topic where very little research had been done (if they’d looked at something well-studied, Claude might already know about the established findings). They chose primary cilia: antenna-like appendages on cells that we still know little about but which are implicated in a variety of developmental and neurological disorders. Next, they’ll run a whole genome screen to see which genes actually affect cilia formation, and establish the ground-truth.

The test is to compare human experts to Claude. The humans will use the spreadsheet approach to make their guesses. Claude will generate its own using the molecular relationship map. If Claude catches (hypothetically) 150 out of 200, and the humans catch 80 out of 200, that's proof the approach works better. Even if they're about equal in discovering the genes, it’s still likely Claude works much faster, and could make the whole research process more efficient.

If the approach works, the team envisions it becoming a standard first step in focused perturbation screening. Instead of gambling on intuition or using brute-force approaches that have become prevalent in contemporary research, labs could make informed bets about which genes to target—getting better results without needing the infrastructure for whole-genome screening.

### Looking forward

None of these systems are perfect. But they point to the ways that in just a few short years scientists have begun to incorporate AI as a research partner capable of far more than basic tasks—indeed, increasingly able to speed up, and in some cases even replace, many different aspects of the research process.

In speaking with these labs, a common theme emerged: the usefulness of the tools they’ve built continues to grow in concert with AI capabilities. Each model release brings noticeable improvements. Where just two years ago earlier models were limited to writing code or summarizing papers, more powerful agents have begun, if slowly, to replicate the very work those papers describe.

As tools advance and AI models continue to grow more intelligent, we’re continuing to watch and learn from how scientific discovery develops along with them.

*For more detail on the expanded Claude for Life Sciences capabilities, see here, and our tutorials here. We’re also continuing to accept applications to our AI for Science program. Applications will be reviewed by our team, including subject matter experts in relevant fields.*

## Related content

### Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem

Read more### Statement on the US government directive to suspend access to Fable 5 and Mythos 5

The US government has issued an export control directive to suspend all access to Fable 5 and Mythos 5.

Read more
