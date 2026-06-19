---
title: Privileged Bases in the Transformer Residual Stream
url: https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream
source: research
published: '2023-03-16'
fetched: 2026-06-16 20:48
---

## Abstract

Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.

We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.
