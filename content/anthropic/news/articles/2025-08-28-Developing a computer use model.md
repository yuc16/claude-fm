---
title: Developing a computer use model
url: https://www.anthropic.com/news/developing-computer-use
source: news
published: '2025-08-28'
fetched: 2026-06-13 05:02
---

# Developing a computer use model

- Consumer Terms and Privacy Policy - Aug 28, 2025

Claude can now use computers. The latest version of Claude 3.5 Sonnet can, when run through the appropriate software setup, follow a user’s commands to move a cursor around their computer’s screen, click on relevant locations, and input information via a virtual keyboard, emulating the way people interact with their own computer.

We think this skill—which is currently in public beta—represents a significant breakthrough in AI progress. Below, we share some insights from the research that went into developing computer use models—and into making them safer.

## Why computer use?

Why is this new capability important? A vast amount of modern work happens via computers. Enabling AIs to interact directly with computer software in the same way people do will unlock a huge range of applications that simply aren’t possible for the current generation of AI assistants.

Over the last few years, many important milestones have been reached in the development of powerful AI—for example, the ability to perform complex logical reasoning and the ability to see and understand images. The next frontier is computer use: AI models that don’t have to interact via bespoke tools, but that instead are empowered to use essentially any piece of software as instructed.

## The research process

Our previous work on tool use and multimodality provided the groundwork for these new computer use skills. Operating computers involves the ability to see and interpret images—in this case, images of a computer screen. It also requires reasoning about how and when to carry out specific operations in response to what’s on the screen. Combining these abilities, we trained Claude to interpret what’s happening on a screen and then use the software tools available to carry out tasks.

When a developer tasks Claude with using a piece of computer software and gives it the necessary access, Claude looks at screenshots of what’s visible to the user, then counts how many pixels vertically or horizontally it needs to move a cursor in order to click in the correct place. Training Claude to count pixels accurately was critical. Without this skill, the model finds it difficult to give mouse commands—similar to how models often struggle with simple-seeming questions like “how many A’s in the word ‘banana’?”.

We were surprised by how rapidly Claude generalized from the computer-use training we gave it on just a few pieces of simple software, such as a calculator and a text editor (for safety reasons we did not allow the model to access the internet during training). In combination with Claude’s other skills, this training granted it the remarkable ability to turn a user’s written prompt into a sequence of logical steps and then take actions on the computer. We observed that the model would even self-correct and retry tasks when it encountered obstacles.

Although the subsequent advances came quickly once we made the initial breakthrough, it took a great deal of trial and error to get there. Some of our researchers noted that developing computer use was close to the “idealized” process of AI research they’d pictured when they first started in the field: constant iteration and repeated visits back to the drawing board until there was progress.

The research paid off. At present, Claude is state-of-the-art for models that use computers in the same way as a person does—that is, from looking at the screen and taking actions in response. On one evaluation created to test developers’ attempts to have models use computers, OSWorld, Claude currently gets 14.9%. That’s nowhere near human-level skill (which is generally 70-75%), but it’s far higher than the 7.7% obtained by the next-best AI model in the same category.

## Making computer use safe

Every advance in AI brings with it new safety challenges. Computer use is mainly a way of lowering the barrier to AI systems applying their existing cognitive skills, rather than fundamentally increasing those skills, so our chief concerns with computer use focus on present-day harms rather than future ones. We confirmed this by assessing whether computer use increases the risk of frontier threats as outlined in our Responsible Scaling Policy. We found that the updated Claude 3.5 Sonnet, including its new computer use skill, remains at AI Safety Level 2—that is, it doesn’t require a higher standard of safety and security measures than those we currently have in place.

When future models require AI Safety Level 3 or 4 safeguards because they present catastrophic risks, computer use might exacerbate those risks. We judge that it’s likely better to introduce computer use now, while models still only need AI Safety Level 2 safeguards. This means we can begin grappling with any safety issues before the stakes are too high, rather than adding computer use capabilities for the first time into a model with much more serious risks.

In this spirit, our Trust & Safety teams have conducted extensive analysis of our new computer-use models to identify potential vulnerabilities. One concern they've identified is “prompt injection”—a type of cyberattack where malicious instructions are fed to an AI model, causing it to either override its prior directions or perform unintended actions that deviate from the user's original intent. Since Claude can interpret screenshots from computers connected to the internet, it’s possible that it may be exposed to content that includes prompt injection attacks.

Those using the computer-use version of Claude in our public beta should take the relevant precautions to minimize these kinds of risks. As a resource for developers, we have provided further guidance in our reference implementation.

As with any AI capability, there’s also the potential for users to intentionally misuse Claude’s computer skills. Our teams have developed classifiers and other methods to flag and mitigate these kinds of abuses. Given the upcoming U.S. elections, we’re on high alert for attempted misuses that could be perceived as undermining public trust in electoral processes. While computer use is not sufficiently advanced or capable of operating at a scale that would present heightened risks relative to existing capabilities, we've put in place measures to monitor when Claude is asked to engage in election-related activity, as well as systems for nudging Claude away from activities like generating and posting content on social media, registering web domains, or interacting with government websites. We will continuously evaluate and iterate on these safety measures to balance Claude's capabilities with responsible use during the public beta.

## The future of computer use

Computer use is a completely different approach to AI development. Up until now, LLM developers have *made tools fit the model*, producing custom environments where AIs use specially-designed tools to complete various tasks. Now, we can *make the model fit the tools*—Claude can fit into the computer environments we all use every day. Our goal is for Claude to take pre-existing pieces of computer software and simply use them as a person would.

There’s still a lot to do. Even though it’s the current state of the art, Claude’s computer use remains slow and often error-prone. There are many actions that people routinely do with computers (dragging, zooming, and so on) that Claude can’t yet attempt. The “flipbook” nature of Claude’s view of the screen—taking screenshots and piecing them together, rather than observing a more granular video stream—means that it can miss short-lived actions or notifications.

Even while we were recording demonstrations of computer use for today’s launch, we encountered some amusing errors. In one, Claude accidentally clicked to stop a long-running screen recording, causing all footage to be lost. In another, Claude suddenly took a break from our coding demo and began to peruse photos of Yellowstone National Park.

We expect that computer use will rapidly improve to become faster, more reliable, and more useful for the tasks our users want to complete. It’ll also become much easier to implement for those with less software-development experience. At every stage, our researchers will be working closely with our safety teams to ensure that Claude’s new capabilities are accompanied by the appropriate safety measures.

We invite developers who try computer use in our public beta to contact us with their feedback using this form, so that our researchers can continue to improve the usefulness and safety of this new capability.

## Related content

### Results from the first Anthropic Public Record

Read more### TCS and Anthropic partner to bring Claude to regulated industries

We’re announcing a partnership with Tata Consultancy Services (TCS). TCS will provide Claude to 50,000 of its own employees across 56 countries; build Claude-powered products for clients in financial services, healthcare, the public sector, and other regulated industries; and join the Claude Partner Network.

Read more### DXC will integrate Claude into the systems banks, airlines, and other regulated industries rely on

We’re announcing a multi-year global alliance with DXC Technology, one of the world’s largest IT services companies.

Read more
