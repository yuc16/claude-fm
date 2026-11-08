---
title: Progress on provable inference for large language models
url: https://www.anthropic.com/research/provable-inference
source: research
published: '2026-11-02'
fetched: 2026-11-08 19:50
---

*Roy Rinberg (Anthropic), Alex Allain (Anthropic); Alessandro Chiesa (EPFL, StarkWare), Miranda Christ (MIT, RESI), Rahul Dalal (Anthropic STEM Fellows Program, Succinct), Giacomo Fenzi (EPFL), Ben Mayer (Anthropic Fellows Program, MIT), Guy Weissenberg (EPFL)*

## Executive summary

When you talk to a friend in person, you have many ways to know it is really them: you can see them, hear them, shake their hand. When you talk to an AI model, you have almost none. A user querying a model today cannot check that the responses came from the specific model that a developer claims is responding, as opposed to one secretly substituted in by a routing service for cost reasons, or even by an attacker who has tampered with the token stream. Judging from the model’s output alone is unreliable, even if it produces high-quality responses. Cryptographic proofs of inference solve this problem: they let a model provider commit to a model and then prove that each response was produced by that model. Such proofs could enable applications ranging from consumer products to internal security, and could contribute to a toolkit for verifying compliance with AI pacing requirements.

Specifically, we have made progress on a powerful type of cryptographic proof known as a “zkSNARK”, which is uniquely fit for **provable inference** (owing to its strong hiding and efficiency properties). In this post, we share some of that progress, primarily through a system we call FlashProve. A brief technical summary is as follows:

- Claude has produced improvements on zkSNARKs for inference, building a system that is substantially faster than prior open-source systems. - For a large model (Llama 4 Maverick, 400B-parameter mixture of experts), a single H100 GPU generates proofs at around 110 tokens/second, with a proof size of ~19 MB per 1,024-token request, when in 4-bit quantized weights, using integer arithmetic in prefill. This is ~70-95x the GPU time of running the model itself on vLLM, a common open-source library.
- Prior open-source systems are orders of magnitude slower, as we discuss in section 6. Claude found novel ways to apply state-of-the-art tools in the cryptography and security literature, while relying on well-established design principles for cryptographic proof systems. The commitment to the model, and subsequent inference proofs, hide the weights of the model; hiding the architecture of the model is not a goal of this system.

- Claude is good at optimization, but often makes decisions that are hard to evaluate, especially in large complex systems. We counter this by providing top-level auditable statements in Lean (a formal verification language) for the claimed security guarantees.

Today we are releasing five artifacts:

- The current blog post, which outlines our system and its potential applications;
- A technical report explaining the details of our system;
- A (Claude-written) protocol specification document;
- Executable code that includes: a prover and two verifiers, a fast verifier in C++, and a provably correct verifier in Lean; and
- Lean proofs for the top level mathematical statements, along with an interactive visualizer of the Lean theorems to aid with auditing.

We release our code, Lean proofs, and documentation under the Apache 2.0 license.1 This research post is meant to share intermediate progress, and not a completed research agenda. We are sharing this explicitly with the goal that others look at what we have done, take it, and improve it.

## Introduction

When a user sends a request to an AI model, today they have no way of knowing for certain that the model they selected is the one that generated the response. For everyday uses, in which users mostly care about the output and not necessarily which specific model produced it, this is a less pressing concern. But there are several cases where such assurance would be useful. For example, independent evaluators who test AI models before and after release need to know that the model they are evaluating is the model being served. Clients who use a model through a third-party routing service want assurance that the tokens came from the model they paid for. And if a cyberattacker modifies the token stream while pretending to be a given model, a user has no way to detect it from the output alone.

However, enabling verification of model responses is challenging. Most frontier models’ weights are kept private, and even if the user had access to the weights, checking that a given response was produced by a model with those weights would involve running the model, which requires computational resources far beyond what a typical user (or even evaluator) can afford.

The goal of *provable inference* (PI) is to enable a user with limited computational resources and without any information about the weights to verify that a response came from the requested model. PI is motivated both by a desire to increase customer trust in AI providers, and—because it can be used to provide assurances to independent evaluators and allows providers to demonstrate that they are meeting certain commitments and legal obligations—it also has implications for pacing the frontier of AI development and for AI regulation.

One way to implement PI is via a cryptographic object called a *zero-knowledge succinct argument: *the model provider sends, along with the claimed response, a short *proof *(say, a few megabytes) that the user can *quickly* verify (ideally, in seconds on a CPU). If the claimed response deviates from the specified model, the user’s check will fail. Importantly, cryptographic techniques ensure that the proof reveals *nothing* about the model’s weights.

Today, we release FlashProve: an **open-source performant prototype for provable inference**. For a 400B-parameter mixture-of-experts model (Llama 4 Maverick, 4-bit quantization), we show that a single H100 GPU generates proofs at over 100 tokens/second, with proof size of ~19 MB per 1,024-token request (~70-95 times the GPU time that vLLM, a common open-source library, takes to process prompts of the same length).

The release comes with executable code, Lean formalization, and a technical description of the protocol. Our aim is twofold: (i) accelerating and facilitating the development of provable inference; and (ii) demonstrating that zero-knowledge succinct arguments are practical for provable inference.

We believe that this progress has meaningful implications for security, in **pacing AI development**, in **providing AI customers with integrity guarantees**, in **facilitating tooling for auditors and regulators**, and more.

## Trust challenges in AI proliferation

The development of artificial intelligence and its growing role in our digital infrastructure and economy raises trust challenges that AI providers must answer. Addressing these and other challenges is facilitated by relying on tools for *provable inference (PI).*

Tools for PI include hardware approaches, software approaches, or a combination of both. Here, we focus on a software-only approach: a cryptographic tool known as a “zkSNARK” (*zero-knowledge succinct argument of knowledge*). Informally, a zkSNARK is a system allowing a *prover *to convince a *verifier*, by way of a short “certificate”, that a given computation was executed correctly; crucially, the certificate is *zero-knowledge* in that it reveals no information beyond what is implied by the computation’s correctness and is *succinct* in that it’s exponentially faster to verify compared to the proved computation.

Below we outline several challenges and how zkSNARKs help in addressing them.

### Challenge 1: pacing

Some proposals to regulate and pace AI development rely on monitoring hardware and how it is used. For example, a provider might be required to devote its hardware to inference rather than to training a powerful new model. The provider might try to cheat by serving cheaper models or using compute in an unexpected way, freeing up resources for training. How can a regulator reliably ensure that the hardware is used for inference?

*How zkSNARKs can help: *The regulator can ask the provider for certificates covering the inference requests served in a given period. The certificates must show that the requests were generated by the claimed model. A malicious provider cannot satisfy this request unless its hardware was genuinely serving the right model. Using a zkSNARK, the regulator can check that the provider claims are valid without needing the elaborate hardware setup that the provider may have, and at the same time the provider has the guarantee that the regulator does not learn proprietary model information.2 We note that although this verifies that the hardware is serving inference, it does not establish that the hardware is not, e.g., training on the side.

### Challenge 2: tamper detection

As AI models grow more valuable, the servers that run them become prime targets. An attacker or rogue agent may compromise an inference server to exfiltrate the weights, serve users malicious responses (such as delivering malware to the user’s computer), and more, all while hiding among genuine responses. The adversary need not be external. As models become capable of improving and deploying themselves, a more advanced model could run in place of the one that was authorized and present itself as the weaker model, so as to avoid the classifiers and monitoring that would apply to it. In both cases the question is the same: how can a company be sure of *which weights* are actually running on its servers? In our Frontier Safety Roadmap, Anthropic set a public goal to produce a prototype for verifying inference traffic: “*We will develop a prototype by September 30, 2026 of provable inference, a technique for reliably, provably ‘signing’ AI model outputs in a way that makes them attributable to a specific set of model weights.*” As stated in our RSP updates, we met that goal through a separate but related project, which signs our inference traffic and recomputes inference on a trusted server; the work in this blog post pursues the same objective by a different method.3

*How zkSNARKs can help:* The provider can require a valid zkSNARK from the server on every response. A proof is bound to a specific commitment to the weights, so it certifies not just that *some* model produced the response but that the *committed* model did. An attacker who compromises a server, or a model that substitutes itself for another, must then produce valid proofs for the expected weights to avoid detection, which they cannot do. The user may receive the proofs as well, since they leak no internal information (by zero knowledge) and are cheap to check (by succinctness); this limits what an attacker can accomplish through the inference API.

### Challenge 3: text provenance

One may want to prove that considerable effort went into understanding/analyzing something. For example, a developer might claim that their software library was scanned for vulnerabilities by a frontier cybersecurity model, or a company might claim that its business plan was given the go-ahead by an appropriate model. How can a user verify these claims? The user might not have the resources to run the model itself (or they might not have the clearance to do so). Even publishing the chat logs gives no absolute guarantees; a developer might in theory fake them, generating them not with a frontier model but instead with a cheaper one or a degraded version. In general, how can users verify that they are being served by their chosen model?

*How zkSNARKs can help:* The provider can append, along with each response, a zkSNARK proving that the output was produced by the claimed model on the given input. Succinctness lets the user check this certificate quickly, without specialized hardware, and zero-knowledge assures the provider that the user learns nothing about the proprietary weights. This complements existing mechanisms for verifying which model produced a response.

For example, in a world where exploits are being found regularly, prior to releasing new code a model provider could provide the code-developer a Proof-of-Failure that the model-provider spent at least X tokens on a specific model, and did not achieve a specific result (for example, this specific model did not find any bugs in a specific patch, after trying for at least 1M tokens).

### Challenge 4: model approval

Regulation might require providers to serve only models approved as safe, rather than models deemed a cybersecurity or safety risk. A provider might have an incentive to circumvent this, since risky models might outperform competitors or be cheaper to serve. How can a regulator ensure that only approved models are served?

*How zkSNARKs can help:* The regulator can require the provider to attach a zkSNARK to its responses, enforcing the use of approved models. The proof binds each request to the used model, so it will not verify if the provider is using an unapproved model. The regulator can check this in a lightweight way thanks to succinctness without requiring to re-execute each request.

*A note on PI from trusted hardware.* Prior work often focuses on *trusted execution environments* to achieve PI. These are hardware-based solutions that provide privacy and attestation that rely on the manufacturer producing tamper-resistant hardware. In this research, our focus is on software-only cryptographic solutions whose security and privacy relies on the hardness of computational problems. Even in the face of compromised environments (hardware, operating system and more) an adversary cannot produce a invalid proof without breaking a computationally infeasible problem. Trusted hardware and cryptography are complementary approaches with different guarantees and tradeoffs. Both will play a role in addressing the above trust challenges.

## Our system: FlashProve

FlashProve is a system for provable inference of large Mixture-of-Experts (MoE) language models. More details are in our technical report; here we outline the system.

FlashProve involves two parties: the model provider (the *prover*) and a user (the *verifier*). It is split into two phases:

- In the **offline phase**, the prover publishes a*commitment*to the model weights, which is a short fingerprint to pin down*one*exact choice of weights while the weights themselves remain hidden. The later inference claims will be checked against that commitment, i.e., the weight model committed to in this phase.
- In the **online phase**, upon requests from the verifier (i.e., prompts and the corresponding output tokens), the prover produces a proof file proving the following statement:

*The committed model produces these output tokens when evaluated.*

Anyone who holds the commitment, the prompt, and the reply can check it, without the weights and with limited compute power, and be convinced that the committed weights, run on this prompt, produce exactly these tokens.

### Guarantees

A proof file satisfies the following “completeness” and “soundness” properties:

- **A proof file is accepted if it is honest (completeness).**An honest prover's proof is accepted by the verifier.
- **A proof file cannot be forged (soundness).**It is effectively impossible (i.e., tantamount to breaking widely believed cryptographic assumptions) to produce a valid proof of a false statement, so the verifier does not have to trust the prover.

Completeness and soundness alone can be achieved by a computationally powerful verifier that knows the model weights (evaluate the model on the prompt and check whether the result matches the response). The next two properties are what makes the system non-trivial.

- **A proof file reveals nothing beyond the statement (zero-knowledge).**The verifier learns- *nothing*about the weights, the intermediate values of the computation, or which experts ran at every layer. The model architecture (excluding the weights) is not hidden.
- **A proof file is small and cheap to check (succinctness).**The attested computation is a run of a 400B-parameter (about 232 GB for a quantized version) model on an H100 GPU, while the verifier receives a proof file of about 19 MB that takes seconds to check on a 24-core CPU. An auditor, or a user with far less hardware than the provider, can check proof files without access to elaborate infrastructure.

### Evaluation

We measured an implementation of the protocol on Llama 4 Maverick (a 400B-parameter mixture of experts, with ~17B parameters used per token), using the publicly available 4-bit weights. Each verifier request is a window of 1,024 tokens, and each proof checks one token. The prover runs on a server with a single H100 and 24 CPU cores, and the verifier on a CPU.

- **Prover.**The prover runs on a server with a single H100 and 24 CPU cores. The- *offline phase*runs once per model and takes about 39 minutes. (For technical reasons we discuss in the technical report, the resulting commitment is good for about 16 million requests, after which the provider has to commit again.) The- *online phase*, on a batch of 24 requests, takes the prover about 223 seconds, which is 110 tokens per second, and each proof is 18.78 MB.
- **Verifier.**The verifier runs on the client's CPU. It needs no GPU and only has access to a commitment to the weights. The client downloads the commitment, ~6.5 MB in all, and then one proof per request. Checking a proof takes 17 seconds on 24 threads (and 21 seconds on a single thread), including the offline phase's checks.

Comparison with plain inference: We ran vLLM, a widely used inference engine, with the FP8 release of the same model on eight H100s, and found that, per GPU, proving a batch of 24 requests takes about 72 times longer than vLLM takes to process the same 24 requests at once (66 to 77 across runs), and about 94 times longer when vLLM runs at the highest load we tried.

**Inside the system.** The underlying mechanism behind FlashProve is a zkSNARK of the kind deployed in peer-to-peer systems (e.g., L2 networks such as Starknet or Mantle for blockchains like Ethereum). Our zkSNARK is built according to a well-established recipe: an underlying information-theoretic object called an *interactive oracle proof* (IOP) is compiled* *into a cryptographic proof by relying on hash functions (and offers even post-quantum security). Our IOP is assembled from state-of-the-art building blocks using tools such as *code proximity tests with linear constraints* and *lookup arguments*, which are based on techniques from coding theory and complexity theory. Combining these pieces into a bespoke IOP for inference is a delicate task; more details about the construction can be found in the technical report.

### Engineering the system

FlashProve benefits from architectural decisions that we took, and which are discussed in detail in the technical report. Here we highlight a few:

- The prover's work is proportional to the experts that actually ran. In a MoE model a token uses ~17B of the 400B parameters, and the prover's work per token is proportional to those ~17B instead of all parameters (the proof still hides which experts were chosen).
- Requests are proved in batches, after the fact. The prover reads finished text in one parallel pass (as in prefill), and it opens the commitment to the weights once per batch instead of once per request.
- The system is designed to fit on a single GPU. The model weights at each layer are split to segments and are proven one segment of layers at a time. The weights are kept in ordinary memory and streamed in, so a single 80 GB GPU, with ~290 GB of host memory beside it, suffices.

### Post-hoc versus in-line

When integrating proving mechanisms into inference servers there is a choice: in-line proving (i.e. proving alongside the inference) versus post-hoc proving (i.e. proving after-the-fact, for a subset of tokens). Our system follows the latter. In-line solutions are expected to be ultra-fast and may sacrifice security for efficiency, whereas post-hoc solutions are allowed to be slower and may not suffer such a tradeoff. On the other hand, post-hoc proving has limitations: added complexity of recomputation, the delay in getting guarantees about your traffic, and inherent “non-determinism”. We elaborate on the motivation and implications of post-hoc proving in the technical report.

## Trustworthiness from formal verification

Cryptographic code is notoriously brittle and error-prone. How can users trust the code we’re releasing today?

The answer is **formal verification**: we use the Lean proof assistant to specify the protocol and the desired security properties. We prove these properties in a form that is machine-checkable and guaranteed to be correct (up to compiler errors). We target three top-level properties:

- **Completeness**: if the statement is correct, the resulting proof is accepted by the verifier.
- **Soundness**: any fake proof is rejected by the verifier (except with negligible probability).
- **Zero knowledge**: the proof reveals no information about the weights of the model, beyond what the verifier can infer from the response itself.- 4

These properties are stated in the so-called random oracle model, an information-theoretic way to analyze cryptographic protocols that rely on hash functions.

Formal verification leaves two important trust gaps. First, the formal statements must be audited to ensure that they match their intent. This has to be done manually (though it is dramatically less onerous than auditing proofs); we provide an interactive visualizer to assist with this.

Second, the executable code must be audited to ensure it matches the formally-defined protocol for which the security properties are proven. How to best assist with this depends on the property, because soundness depends solely on the verifier, zero-knowledge depends solely on the prover, and completeness depends on their interaction.

- For soundness, we only need the verifier code to be correct (the entire value of having “proofs” is that you can fully distrust the prover if you trust the verifier). We provide an executable Lean verifier, alongside the C++ verifier. The Lean verifier runs more slowly, but Lean proves that it accepts only what the verifier in our soundness theorem accepts. Nevertheless, the C++ verifier is the one to use day to day: it carries no formal guarantee, and it agrees with the Lean verifier on every proof in our tests.
- For completeness, the threat model does not assume adversarial attacks (the prover and verifier are honest). Therefore, a Lean verifier lets us gain confidence through standard software testing that the honest prover produces accepting proofs: run the prover on a correct statement, and then the Lean verifier on the resulting proof.
- For zero knowledge, we only need the prover to be correct. However, unlike the verifier, the prover is an expensive procedure, and it would be impractical to run a Lean prover. We do not provide facilitations here: we expect that any prover that wants to hide the weights of a model they are serving has access to enough resources for careful agentic and/or human security audits to ensure equivalence to the Lean prover.

## Prior work

Achieving provable inference is the objective of a line of work colloquially termed “zkML”. Early works, such as SafetyNets (2017) verified a two-conv-layer MNIST CNN and a small fully connected speech model, zkCNN (2021) reached VGG-16 (15M parameters) at 88.3 s per proof, and Kang et al. (2022) proved MobileNet v2 on full-resolution ImageNet.

Transformer proofs followed: ZKML’s GPT-2 took about 159 s per token for 117M parameters (≈0.006 tok/s), and Modulus Labs’ 1.5B-parameter GPT-2 XL needed over 90 hours. EZKL (2023) proved a 1M-parameter GPT-style transformer in about 966 s per token (≈0.001 tok/s). Performance progressively improved: zkLLM (2024) proved LLaMA-2-13B on a 2,048-token input in about 15 minutes on GPU, which is ≈0.001 tok/s per new token, or ~2.5 tok/s in the batch. In 2025, zkGPT reduced GPT-2 to 21.8 s (≈0.05 tok/s), zkPyTorch proved Llama-3 8B at ~150 s per token on one CPU core (≈0.007 tok/s), and ZKTorch proved GPT-J (6B) in about 20 minutes (≈0.001 tok/s). VerInf proved Llama 4 Maverick (the same 400B-parameter MoE model we prove) at ≈0.02 tok/s. DeepProve, a current peer-reviewed state of the art, certifies an entire generated sequence with a single forward pass. It reaches about 2.9 tok/s for GPT-2 and 1.4 tok/s for Gemma 3 on one machine, and 31 tok/s distributed. SASH's prover (2026) reached ≈1.25 tok/s on Llama 3.1 8B on a single H100.

Recently commercial efforts have reached impressive numbers, with Attestable proving Gemma 4 31B at 53–77 tok/s on a single H100; at the time of writing, Attestable has not released a corresponding open source library.

The above numbers speak to the precipitous progress of provable inference in the past years. They should update our priors on what it is possible to prove in zero-knowledge.

- In 2024, zkLLM proved a 13B model at about 2.5 tokens/second on one A100. The only earlier proof of Llama 4 Maverick that we know of, VerInf, reports 14.3 hours for 1,000 tokens on a DGX Spark, with a 93.6 GB proof which took almost a day to verify.
- FlashProve proves the same model at 110 tokens/second on a single H100, with 19 MB proofs that can be verified in seconds. Attestable independently reports 53–77 tokens/second for a dense 31B model.

We believe that the progress should transfer to more models and architectures, yielding a flexible and powerful tool with overhead over native computation of roughly 2 orders of magnitude (about 70 to 95 times in our measurements), much less than previously expected.

## Limitations

This release is a research prototype, and has the following technical limitations:

- **No formal guarantees on fast executable code.**We provide a Lean implementation of the protocol (including an executable “slow” Lean verifier), along with security properties proved in Lean. The paper and the fast executable code are derived from the Lean protocol, but we do not guarantee that all three (Lean, paper, code) match each other.
- **The proof is about an integer model under greedy decoding.**We prove an exact integer version of the published weights, and a proof asserts that each checked token is that model’s greedy choice. A reply from a floating-point implementation, or sampled decoding, could depart at some position and no longer exactly match the computation proved. The integer version is generally expected and empirically tested to be within some small error rate of true floating-point inference generically (even taking into account non-determinism of floating-point computations), though this does not cover adversarially designed prompts.
- **Architecture hiding.**Our system assumes the served model uses a Mixture-of-Experts (MoE) architecture, in which each transformer layer’s feed-forward block is replaced by multiple expert sub-networks and a- *router*that activates only a small subset of experts for each token and our system uses the MoE structure for efficiency gains. Other architectures, such as the dense models, are also widely used and its description may contain intellectual-property the model provider would like to keep secret. Indeed, one could also imagine a system that further hides the architecture of the model: the prover commits to both the weights and the architecture (i.e., the “executable code” for inference) via a hiding commitment and the verifier’s claim is about checking the execution of that committed executable on the commitment model.
- **Side channel attacks.**The current guarantee of the protocol is that the proof itself reveals nothing about the weights of the committed model. However, “side channel attacks”, such as measuring the time it takes to produce a proof, could potentially reveal information about the weights. We consider this out of scope for this release.
- **Longer contexts.**The system currently proves inference over contexts of up to 1,024 tokens. This is quite short in comparison to the contexts accumulated in chat settings. Ideally, this context length could be increased to full context windows for frontier models (which regularly have context windows of 100s of thousands to millions of tokens).
