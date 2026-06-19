---
title: 'Towards Monosemanticity: Decomposing Language Models With Dictionary Learning'
url: https://www.anthropic.com/research/towards-monosemanticity-decomposing-language-models-with-dictionary-learning
source: research
published: '2023-10-05'
fetched: 2026-06-16 20:46
---

# Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

## Abstract

In our latest paper, *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*, we outline evidence that there are better units of analysis than individual neurons, and we have built machinery that lets us find these units in small transformer models. These units, called features, correspond to patterns (linear combinations) of neuron activations. This provides a path to breaking down complex neural networks into parts we can understand, and builds on previous efforts to interpret high-dimensional systems in neuroscience, machine learning, and statistics. In a transformer language model, we decompose a layer with 512 neurons into more than 4000 features which separately represent things like DNA sequences, legal language, HTTP requests, Hebrew text, nutrition statements, and much, much more. Most of these model properties are invisible when looking at the activations of individual neurons in isolation.
