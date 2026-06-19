---
title: Introducing Citations on the Anthropic API
url: https://claude.com/blog/introducing-citations-api
source: blog
published: '2025-06-23'
fetched: 2026-06-13 12:16
---

# Introducing Citations on the Anthropic API

Claude can now cite specific passages from your documents, delivering verifiable responses with built-in source tracking.

Claude can now cite specific passages from your documents, delivering verifiable responses with built-in source tracking.

- June 23, 2025
- 5min

*Update: **Now available in Amazon Bedrock. (June 30, 2025)*

Today, we're launching Citations, a new API feature that lets Claude ground its answers in source documents. Claude can now provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs.

Citations is generally available on the Anthropic API and Google Cloud’s Vertex AI.

All Claude models are trained to be trustworthy and steerable by design. Citations builds upon this foundation, addressing a specific need in AI applications: verifying the sources behind AI-generated responses.

Previously, developers relied on complex prompts that instruct Claude to include source information, often resulting in inconsistent performance and significant time investment in prompt engineering and testing. With Citations, users can now add source documents to the context window, and when querying the model, Claude automatically cites claims in its output that are inferred from those sources.

**Our internal evaluations show that Claude's built-in citation capabilities outperform most custom implementations, increasing recall accuracy by up to 15%. 1**

With Citations, developers can create AI solutions that offer enhanced accountability across use cases like:

- Document summarization: Generate concise summaries of long documents, like case files, with each key point linked back to its original source.
- Complex Q&A: Provide detailed answers to user queries across a large corpus of documents, like financial statements, with each response element traced back to specific sections of relevant texts.
- Customer support: Create support systems that can answer complex queries by referencing multiple product manuals, FAQs, and support tickets, always citing the exact source of information.

When Citations is enabled, the API processes user-provided source documents (PDF documents and plain text files) by chunking them into sentences. These chunked sentences, along with user-provided context, are then passed to the model with the user's query. Alternatively, users can provide their own chunks for the source documents.

Claude analyzes the query and generates a response that includes precise citations based on the provided chunks and context for any claims derived from the source material. Cited text will reference source documents to minimize hallucinations.

This approach offers superior flexibility and ease of use, as it doesn't require file storage and seamlessly integrates with the Messages API.

Citations uses our standard token-based pricing model. While it may use additional input tokens to process documents, users will not pay for output tokens that return the quoted text itself.

Thomson Reuters uses Claude to power their AI platform, CoCounsel, helping legal and tax professionals synthesize expert knowledge and deliver comprehensive advice to clients.

“For CoCounsel to be trustworthy and immediately useful for practicing attorneys, it needs to cite its work. We first built this ourselves, but it was really hard to build and maintain. That's why we were excited to test out Anthropic’s Citations functionality. It makes citing and linking to primary sources much easier to build, maintain, and deploy to our users. This capability not only helps minimize hallucination risk but also strengthens trust in AI-generated content. The Citations feature will enable us to build an even more accurate and thorough AI assistant for lawyers,” said Jake Heller, Head of Product, CoCounsel, Thomson Reuters.

Endex uses Claude to power an Autonomous Agent for financial firms.

"With Anthropic's Citations, we reduced source hallucinations and formatting issues from 10% to 0% and saw a 20% increase in references per response. This removed the need for elaborate prompt engineering around references and improved our accuracy when conducting complex, multi-stage financial research,” said Tarun Amasa, CEO, Endex.

Citations is now available for the new Claude 3.5 Sonnet and Claude 3.5 Haiku. To start using Citations, explore our documentation.

Get the developer newsletter
