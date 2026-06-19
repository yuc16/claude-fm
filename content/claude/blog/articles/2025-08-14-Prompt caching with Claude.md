---
title: Prompt caching with Claude
url: https://claude.com/blog/prompt-caching
source: blog
published: '2025-08-14'
fetched: 2026-06-13 12:16
---

# Prompt caching with Claude

Claude caches frequently used context between API calls, reducing costs and latency for long prompts.

Claude caches frequently used context between API calls, reducing costs and latency for long prompts.

- August 14, 2025
- 5min

*Update**: Prompt caching is Generally Available on the Anthropic API. Prompt caching is also available in preview in Amazon Bedrock and on Google Cloud’s Vertex AI. (December 17, 2024)*Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API. With prompt caching, customers can provide Claude with more background knowledge and example outputs—all while reducing costs by up to 90% and latency by up to 85% for long prompts. Prompt caching is available today in public beta for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.

Prompt caching can be effective in situations where you want to send a large amount of prompt context once and then refer to that information repeatedly in subsequent requests, including:

- **Conversational agents:**Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents.
- **Coding assistants:**Improve autocomplete and codebase Q&A by keeping a summarized version of the codebase in the prompt.
- **Large document processing:**Incorporate complete long-form material including images in your prompt without increasing response latency.
- **Detailed instruction sets:**Share extensive lists of instructions, procedures, and examples to fine-tune Claude's responses. Developers often include a few examples in their prompt, but with prompt caching you can get even better performance by including dozens of diverse examples of high quality outputs.
- **Agentic search and tool use:**Enhance performance for scenarios involving multiple rounds of tool calls and iterative changes, where each step typically requires a new API call.
- **Talk to books, papers, documentation, podcast transcripts, and other long-form content:**Bring any knowledge base alive by embedding the entire document(s) into the prompt, and letting users ask it questions.

Early customers have seen substantial speed and cost improvements with prompt caching for a variety of use cases—from including a full knowledge base to 100-shot examples to including each turn of a conversation in their prompt.

Cached prompts are priced based on the number of input tokens you cache and how frequently you use that content. Writing to the cache costs 25% more than our base input token price for any given model, while using cached content is significantly cheaper, costing only 10% of the base input token price.

Notion is adding prompt caching to Claude-powered features for its AI assistant, Notion AI. With reduced costs and increased speed, Notion is able to optimize internal operations and create a more elevated and responsive user experience for their customers.

We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality.

— Simon Last, Co-founder at Notion

To start using the prompt caching public beta on the Anthropic API, explore our documentation and pricing page.

Get the developer newsletter
