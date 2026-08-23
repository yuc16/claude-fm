---
title: Build production agents with computer use, the Skills API, and the Files API
  | Claude by Anthropic
url: https://claude.com/blog/computer-use-skills-api-files-api
source: blog
published: '2026-08-20'
fetched: 2026-08-23 16:13
---

- August 20, 2026
- 5min

Computer use, the Skills API, and the Files API are generally available on the Claude Platform today. Computer use also adds a new browser use tool for agents that work in web applications. Together they let you build agents that operate software, apply your team's expertise, and return finished files.

**Building agents on the Claude Platform**

**Computer use** lets you build agents that operate software they can see. Given a screenshot, the agent clicks, types, and scrolls the way someone at the keyboard would. That lets it work in applications that were never built for automation. The new **browser use tool** extends this to the web. Alongside the screenshot, the agent reads the structure of the page and acts on a specific field or button rather than a position on screen.

The** Skills API** and the **Files API** let you give that agent your expertise and your documents. A skill is a folder of instructions, scripts, and templates that Claude loads only when a task calls for it. With the **Skills API **you upload and version your own skills, then attach them to any request. They run in Claude's code execution sandbox, so there is nothing for you to host. The** Files API** is storage for the documents an agent reads and writes: upload a PDF or spreadsheet once, reference it by ID in later requests instead of re-sending it, and download the files the agent creates.

Say you're building a claims agent. It reads the intake document from the Files API, follows a skill that encodes the team's filing procedure, completes the submission in an insurer's web portal with the browser use tool, and saves the confirmation back as a file. Code execution and web search, already generally available, fit into the same loop.

**What's new with general availability**

- **Computer use:**the updated computer use tool lets Claude take several actions per turn instead of one per model call, so tasks finish in fewer calls and less time. Computer use is also now eligible for HIPAA-regulated workloads under our BAA.
- **Browser use tool:**new in computer use today. It uses the same multi-action turns and adds page structure, so agents target web elements more reliably than with pixels alone.
- **Skills API:**a simpler API for uploading and versioning your own skills.
- **Files API:**automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization.

**Getting started**

The computer use tool, the browser use tool, the Skills API, and the Files API are now available on the Claude Platform. The Skills API and the Files API are also available through Microsoft Foundry, and the updated computer use and browser use tools are coming soon to Google Cloud's Vertex AI. Existing beta integrations keep working while you migrate. See the documentation for computer use, the browser use tool, the Skills API, and the Files API to get started.

## Transform how your organization operates with Claude

Get the developer newsletter
