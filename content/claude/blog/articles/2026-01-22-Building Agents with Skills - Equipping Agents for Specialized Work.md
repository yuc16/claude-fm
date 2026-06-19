---
title: 'Building Agents with Skills: Equipping Agents for Specialized Work'
url: https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
source: blog
published: '2026-01-22'
fetched: 2026-06-13 12:15
---

# Building agents with Skills: Equipping agents for specialized work

Skills package domain expertise in files agents can access and apply—turning general-purpose agents into knowledgeable specialists for real work.

Skills package domain expertise in files agents can access and apply—turning general-purpose agents into knowledgeable specialists for real work.

- January 22, 2026
- 5min

A lot has changed in the past year. MCP became the standard for agent connectivity with rapid adoption from industry leaders and the developer community. Claude Code launched as a general-purpose coding agent. And we launched the Claude Agent SDK, which now provides a production-ready agent out of the box.

But as we've built and deployed these agents, we keep running into the same gap: agents have intelligence and capabilities, but not always the expertise to effectively tackle real work. This led us to create Agent Skills. Skills are organized collections of files that package domain expertise - workflows, best practices, scripts - in a format agents can access and apply. They turn a capable generalist into a knowledgeable specialist.

In this post, we'll explain why we stopped building specialized agents and started building skills instead, and how this shift is changing how we think about extending agent capabilities.

We used to think agents in different domains would look very different. A coding agent, a research agent, one for finance, one for marketing—each seemed to need its own tools and scaffolding. The industry initially embraced this model of domain-specific agents. But as models improved in intelligence and agent capabilities progressed, we converged on a different approach.

We came to see code less as just a use case and more as an interface for agents to do almost any digital work. Claude Code is a coding agent, but also a general-purpose agent that happens to work through code.

Consider working with Claude Code to generate a financial report. It can call APIs for research, store data in the filesystem, analyze it with Python, and synthesize insights. All of that happens through code. The scaffolding becomes as simple as bash and a filesystem.

But general capability isn't the same as expertise. When we started using Claude Code for real work, a gap emerged.

Who would you want filing your taxes: a math genius figuring it out from first principles, or an experienced tax professional who's filed thousands of returns? Most people would choose the tax professional. Not because they're smarter, but because they have the right expertise.

Agents today are like that math genius: brilliant at reasoning through novel situations, but often lacking the accumulated expertise of a seasoned professional. They can do amazing things with proper guidance. However, they're often missing important context, can't easily absorb your organization's expertise, and don't automatically learn from repeated tasks.

Skills bridge this gap by packaging domain expertise in a format that agents can progressively access and apply.

Skills package domain expertise and procedural knowledge for agents.

```
anthropic_brand/
├── SKILL.md
├── docs.md
├── slide-decks.md
└── apply_template.py
```
The simplicity of skills is deliberate. Files are a universal primitive that works with what you already have. You can version them with Git, store them in Google Drive, and share them with your team. This simplicity also means skill creation isn't limited to engineers. Product managers, analysts, and domain experts are already building skills to codify their workflows.

Skills can contain extensive information. To protect the context window and make skills composable, they use progressive disclosure: at runtime, only the metadata (name and description from the YAML frontmatter) is shown to the model.

```
---
name: Anthropic Brand Style Guidelines
description: Anthropic's official brand colors and typography…
---
```
If Claude determines a skill is needed, it reads the full SKILL.md file. For additional detail, skills can include a references/ directory with supporting documentation loaded only on demand.

This three-tier approach means you can equip an agent with hundreds of skills without overwhelming its context window—metadata uses ~50 tokens, full SKILL.md files ~500 tokens, and reference files 2,000+ tokens and only when specifically needed.

Traditional tools have problems: some have poorly written instructions, the model can't always modify or extend them, and they often bloat the context window. Code, on the other hand, is self-documenting, modifiable, and doesn't need to be in context at all times.

Here's a real example: we kept seeing Claude write the same script to apply Anthropic styling to slides. So we asked Claude to save it as a tool for itself:

```
# anthropic/brand_styling/apply_template.py
import sys
from pptx import Presentation
if len(sys.argv) != 2:
    print("USAGE: apply_template.py <pptx>")
    sys.exit(1)
prs = Presentation(sys.argv[1])
for slide in prs.slides:
    ...
```
The corresponding documentation in slide-decks.md simply references this script:

```
## Anthropic Slide Decks
- Intro/outro slides
  - background color: `#141413`
  - foreground color: oat
- Section slides:
  - background color: `#da7857`
  - foreground color: `#141413`
Use the `./apply_template.py` script to update a pptx file in-place.
```
The skills ecosystem has emerged quickly, and so far we've seen three major types of skills being built:

These provide core capabilities everyone needs: working with documents, spreadsheets, presentations, etc. They encode best practices for document generation and manipulation. You can see what this looks like in practice by exploring the foundational skills in our public repository.

As skills standardize how agents interact with specialized capabilities, companies are building skills to make their services agent-accessible. K-Dense, Browserbase, Notion, and many others are creating skills that integrate their services directly, extending Claude's capabilities in specific domains while maintaining the simplicity of the skills format.

Organizations build proprietary skills encoding their internal processes and domain expertise. Skills help capture the specific workflows, compliance requirements, and institutional knowledge that make an agent useful for enterprise work.

As skills adoption grows, several patterns are emerging that point to where this paradigm may be heading. These trends shape how we think about skill design and the tooling we're building to support skill developers.

Early skills were simple documentation references. Now we're seeing sophisticated multi-step workflows that coordinate data retrieval, complex calculations, and formatted output across multiple tools.

- **Simple**: "Status report writer" (~100 lines) - Templates and formatting
- **Intermediate**: "Financial model builder" (~800 lines) - Data retrieval, Excel modeling with Python
- **Complex**: "RNA sequencing pipeline" (2,500+ lines) - Coordinates HISAT2, StringTie, DESeq2 analysis

Skills and MCP servers work together naturally. A competitive analysis skill might coordinate web search, internal databases via MCP, Slack message history, and Notion pages to synthesize a comprehensive report.

Skill creation is expanding beyond engineers to product managers, analysts, and domain experts across disciplines. They can create and test their first skill in under 30 minutes using the skill-creator tool, which guides them through the process interactively. We're working to make skill creation even more accessible, with improved tooling and templates that let anyone capture and share expertise.

Putting it all together, the emerging agent architecture looks like a combination of:

- **Agent loop**: The core reasoning system that decides what to do next
- **Agent runtime**: Execution environment (code, filesystem)
- **MCP servers**: Connections to external tools and data sources
- **Skills library**: Domain expertise and procedural knowledge

Each layer has a clear purpose: the loop reasons, the runtime executes, MCP connects, and skills guide. This separation makes the system comprehensible and allows each piece to evolve independently.

Consider what happens when you add a single skill to this architecture. The frontend design skill transforms Claude's frontend capabilities instantly. It provides specialized guidance on typography, color theory, and animation, activating only when building web interfaces. Progressive disclosure means it loads only when relevant. Adding new capabilities is straightforward.

This emerging pattern of general agents equipped with MCP servers and skills is already helping us deploy Claude to new verticals.

Just after launching skills, we enhanced Claude for the financial services sector with skills that make Claude more useful for finance professionals:

- **DCF model builder**: Constructs discounted cash flow models with proper WACC calculations and sensitivity analysis
- **Comparable company analysis**: Generates comps tables with relevant multiples and benchmarking
- **Earnings analysis**: Processes quarterly results and creates investment update reports
- **Initiation coverage**: Builds comprehensive research reports with financial models
- **Due diligence**: Structures M&A analysis with standardized frameworks
- **Pitch materials**: Creates client presentations following industry standards

We've also enhanced our healthcare and life sciences offerings with skills that make Claude more useful for researchers, clinicians, and healthcare developers:

- **Bioinformatics bundles**: Skills for scVI-tools and Nextflow deployments, essential for managing genomic pipelines and single-cell RNA sequencing
- **Clinical trial protocol generation**: Accelerates protocol development for clinical research
- **Scientific problem selection**: Helps researchers identify and frame impactful research questions
- **FHIR development**: Helps developers write more accurate code for health data interoperability, connecting healthcare systems faster with fewer errors
- **Prior authorization review**: Cuts administrative burden and accelerates patient access to needed care by cross-referencing coverage requirements, clinical guidelines, and patient records

To enable this vision, we're publishing Agent Skills as an open standard. Like MCP, we believe skills should be portable across tools and platforms. The same skill should work whether you're using Claude or other AI platforms. We've been collaborating with members of the ecosystem on the standard, and we're excited to see early adoption.

When someone starts using an AI agent for the first time, it should already know what you and your team care about because skills capture and transfer that expertise. As this ecosystem grows, a skill built by someone else in the community can make your agent more useful, reliable, and capable - regardless of which AI platform they're using.

We're converging on an architecture for general agents, and skills provide a paradigm for shipping and sharing new capabilities. The real value emerges from the collective knowledge base we build together: capturing expertise, transferring it across teams, and making every agent more capable than the last.

**Resources:**

- Don’t Build Agents, Build Skills Instead (YouTube Video)
- Skills documentation
- GitHub repository
- Skills cookbook
- Using skills in Claude
- Skills API quickstart
- Skills best practices documentation

Barry Zhang, Mahesh Murag, Keith Lazuka, Ryan Whitehead

Get the developer newsletter
