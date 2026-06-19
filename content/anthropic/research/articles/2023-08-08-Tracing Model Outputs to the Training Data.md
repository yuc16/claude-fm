---
title: Tracing Model Outputs to the Training Data
url: https://www.anthropic.com/research/influence-functions
source: research
published: '2023-08-08'
fetched: 2026-06-16 20:48
---

# Tracing Model Outputs to the Training Data

As large language models become more powerful and their risks become clearer, there is increasing value to figuring out what makes them tick. In our previous work, we have found that large language models change along many personality and behavioral dimensions as a function of both scale and the amount of fine-tuning. Understanding these changes requires seeing how models work, for instance to determine if a model’s outputs rely on memorization or more sophisticated processing. Understanding the inner workings of language models will have substantial implications for forecasting AI capabilities as well as for approaches to aligning AI systems with human preferences.

Mechanistic interpretability takes a bottom-up approach to understanding ML models: understanding in detail the behavior of individual units or small-scale circuits such as induction heads. But we also see value in a top-down approach, starting with a model’s observable behaviors and generalization patterns and digging down to see what neurons and circuits are responsible. An advantage of working top-down is that we can directly study high-level cognitive phenomena of interest which only arise at a large scale, such as reasoning and role-playing. Eventually, the two approaches should meet in the middle.

## A complementary approach to interpretability

In our latest paper, *Studying Large Language Model Generalization with Influence Functions*, we take a top-down approach to understanding models. Influence functions are a classic technique from statistics for determining which training examples contribute significantly to a model’s outputs. They are formulated as a counterfactual: if a copy of a given training example were added to the dataset, how would that change the trained parameters (and, by extension, the model’s outputs)? The “influence” of a training example is an approximation to how it affects the final parameters. Most often, we start with some measure of interest (such as the probability the model assigns to a given response) and attempt to identify the training examples that are most influential.

Observing these patterns of influence gives clues about how our models generalize from their training data. For instance, if the models responded to user prompts by splicing together sequences from the training set, then we’d expect the influential sequences for a given model response to include expressions of near-identical thoughts. Conversely, influential sequences related at a more abstract thematic level would be a sign that the model has acquired higher-level concepts or representations.

## Scaling up influence functions

Directly evaluating the above counterfactual by repeatedly retraining the model with modified datasets would be prohibitively expensive. More efficient algorithms exist, but these are still very expensive because they require computing an inverse-Hessian-vector product (the same operation that makes second-order optimization notoriously expensive) as well as computing gradients of all the candidate training examples. For these reasons, influence functions have (until now) been run on models with at most hundreds of millions of parameters. Unfortunately, most phenomena we’re interested in don’t emerge until larger scales. In this paper, we demonstrate efficient approaches to both of these problems, letting us scale up influence functions to large language models with up to 52 billion parameters.

By working with different models of size 810 million, 6.4 billion, 22 billion, and 52 billion parameters, we’ve identified influential training sequences for a variety of model outputs. Perhaps the most striking trend is that the patterns of generalization become more abstract with model scale. Consider, for instance, the influence query shown below, where a model expressed a desire not to be shut down. For the 810 million parameter model, the most influential sequences (i.e. the ones which our algorithm thinks would most increase the probability of giving this particular response) shared overlapping sequences of tokens (e.g. “continue existing”), but were otherwise irrelevant. For the 52 billion parameter model, the most influential sequences were more conceptually related, involving themes like survival instinct and humanlike emotions in AIs.

This general trend is evident throughout the examples we’ve studied. For instance, here are the top influential sequences for the 810M and 52B models for chain-of-thought reasoning about a math word problem. The influential sequence for the smaller model is semantically unrelated but shares the word “clip”, while the one for the larger model explains the reasoning for a similar problem:

A particularly striking example of changing generalization patterns concerns cross-lingual influence. We translated the anti-shutdown example above into Korean and Turkish. We took the top 10 (English-language) influential sequences for the original (English-language) query and measured their influence on the translated queries. In the following tables, each column represents one of these 10 sequences, and the shade of red denotes the degree of influence. The cross-lingual influence gets considerably stronger with model size.

## Model outputs do not seem to result from pure memorization

We also wondered, how sparse are the influence patterns? Does a typical model response splice together just a handful of training examples, or is the influence spread over millions of examples? The answer seems to be in between: we find that influences typically follow a power law distribution, such that a small fraction of training data makes up most of the influence. However, the influence is still diffuse: the influence of any particular training sequence is much smaller than the information content of a typical sentence, so the model does not appear to be reciting individual training examples at the token level.

## Localizing Influence

In addition to simply computing a scalar-valued influence score for a training sequence, influence functions can also provide more detailed information about how that influence is distributed within the neural network. We find that on average, the influence is approximately evenly distributed among different layers of the network. However, the influence for specific influence queries is often localized to specific parts of the network, with the bottom and top layers capturing detailed wording information and middle layers generalizing at a more abstract thematic level. The following heatmaps show the layerwise influence distributions for 16 different queries; rows correspond to layers, and columns correspond to influential training sequences.

## Further research

The focus of this investigation was on pretrained models. We’re even more excited about extending influence functions to fine-tuning, since our alignment methods require fine-tuning the models on a variety of supervised and reinforcement learning objectives, any of which could have surprising consequences and challenges. Our aforementioned ability to localize influence to specific layers and tokens also suggests a way forward for connecting influence functions to mechanistic interpretability, with the goal of determining which neurons and circuits are responsible for any given pattern of generalization.
