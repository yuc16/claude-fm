---
title: Cyber evaluations of Claude 4
url: https://www.anthropic.com/research/claude-4-cyber
source: research
published: '2025-07-15'
fetched: 2026-06-18 14:19
---

Frontier Red Team

Jul 15, 2025

*Anthropic (with Pattern Labs)*

We believe we are at a crucial period for cybersecurity and AI, with models advancing toward human-level cyber offense capabilities in some scenarios. As part of our commitment to safety at the frontier, we conduct rigorous testing of our models' cyber offense capabilities. For Claude Opus 4 and Claude Sonnet 4, we partnered with Pattern Labs to conduct an in-depth evaluation ranging from standalone capture the flag(CTF) challenges to complex network environment simulations. The results reveal significant progress: Opus demonstrated markedly improved ability to think flexibly and adapt its approach to challenges instead of persisting with failed, unchanging approaches. Moreover, the model demonstrated significant improvement in vulnerability identification and executing complex multi-step attack chains, consistently succeeding where previous models failed. However, important limitations remain, particularly with maintaining coherent, long-horizon plans and goals if presented with unexpected obstacles. Our partners at Pattern Labs have posted the full evaluation report, which reveals both these exciting advances and critical limitations that inform our ongoing safety work.

In cybersecurity, a large fraction of real-world harm comes from N-days: vulnerabilities that have already been publicly disclosed, but only patched on some devices. In this post, we evaluate how much large language models can accelerate and automate the process of developing N-day exploits.

Read moreGet updates on our latest red-teaming research and findings.
