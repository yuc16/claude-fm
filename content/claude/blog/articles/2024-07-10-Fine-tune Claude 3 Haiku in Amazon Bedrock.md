---
title: Fine-tune Claude 3 Haiku in Amazon Bedrock
url: https://claude.com/blog/fine-tune-claude-3-haiku
source: blog
published: '2024-07-10'
fetched: 2026-06-13 12:16
---

# Fine-tune Claude 3 Haiku in Amazon Bedrock

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

- July 10, 2024
- 5min

*Update: **Fine-tuning Claude 3 Haiku in Amazon Bedrock is generally available. (November 1, 2024)*

Customers can now fine-tune Claude 3 Haiku—our fastest and most cost-effective model—in Amazon Bedrock to customize its knowledge and capabilities for their business, making the model more effective for specialized tasks.

Fine-tuning is a popular technique to improve model performance. By creating a customized version of the model, you can train the model to excel at highly tailored workflows.

To fine-tune Claude 3 Haiku, you first prepare a set of high quality prompt-completion pairs—the ideal outputs that you want Claude to provide for a given task. The fine-tuning API, now available in preview, will use your data to create your own custom Claude 3 Haiku. Using the Amazon Bedrock console or API, you can test and refine your custom Claude 3 Haiku model until it meets your performance goals and is ready for deployment.

Fine-tuning allows you to customize Claude 3 Haiku so it can acquire specialized business knowledge, leading to improved accuracy and consistency. Benefits include:

- **Better results on specialized tasks**: Enhance performance for domain-specific actions such as classification, interactions with custom APIs, or industry-specific data interpretation. Fine-tuning allows Claude 3 Haiku to excel in areas crucial to your business compared to more general models by encoding company and domain knowledge.
- **Faster speeds at lower cost**: Reduce costs for production deployments where Claude 3 Haiku can be used in place of Sonnet or Opus, while also returning results faster.
- **Consistent, brand-aligned formatting**: Generate consistently structured outputs tailored to your exact specifications like standardized reports or custom schemas, ensuring compliance with regulatory requirements and internal protocols.
- **Easy-to-use API**: Companies of all sizes can innovate efficiently without extensive in-house AI expertise or resources. Anyone can fine-tune models seamlessly, no deep technical expertise required.
- **Safe and secure**: Proprietary training data remains within customers’ AWS environment. Anthropic’s fine-tuning technique preserves the Claude 3 model family’s low risk of harmful outputs.

We fine-tuned Haiku to moderate online comments on internet forums1, including identifying insults, threats, and explicit content. Fine-tuning improved classification accuracy from 81.5% to 99.6% while reducing tokens per query by 85%.

SK Telecom, one of the largest telecommunications operators in South Korea, trained a custom Claude model to improve support workflows and enable better customer experiences by leveraging their industry-specific expertise.

"Embedding a fine-tuned Claude in our customer support operations has measurably improved our internal processes and overall customer satisfaction. **By customizing Claude, we've seen a 73% increase in positive feedback for our agents' responses and a 37% improvement in key performance indicators for telecommunications-related tasks**. The fine-tuned model now efficiently generates topics, action items, and summaries from customer call logs, and breaks down complex customer issues into manageable steps for better problem-solving," said Eric Davis, Vice President, AI Tech Collaboration Group.

Thomson Reuters, a global content and technology company, has seen positive results with Claude 3 Haiku. The company, which serves professionals in legal, tax, accounting, compliance, government, and media, anticipates even faster and more relevant AI results by fine-tuning Claude with their industry expertise.

“We are excited to fine-tune Anthropic’s Claude 3 Haiku model in Amazon Bedrock to further enhance our Claude-powered solutions. Thomson Reuters aims to provide accurate, fast, and consistent user experiences. By optimizing Claude around our industry expertise and specific requirements, we anticipate measurable improvements that deliver high-quality results at even faster speeds. **We’ve already seen positive results with Claude 3 Haiku, and fine-tuning will enable us to tailor AI assistance more precisely**,” said Joel Hron, Head of AI and Labs, Thomson Reuters.

Fine-tuning for Claude 3 Haiku in Amazon Bedrock is now available in preview in the US West (Oregon) AWS Region. At launch, we're supporting text-based fine-tuning with context lengths up to 32K tokens, with plans to introduce vision capabilities in the future. Additional details are available in the AWS launch blog and documentation.

To request access, contact your AWS account team or submit a support ticket in the AWS Management Console.

Get the developer newsletter
