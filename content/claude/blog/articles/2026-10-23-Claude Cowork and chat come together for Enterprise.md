---
title: Claude Cowork and chat come together for Enterprise
url: https://claude.com/resources/articles/unified-claude-enterprise
source: blog
published: '2026-10-23'
fetched: 2026-10-25 14:31
---

# Claude Cowork and chat come together for Enterprise

Chat and Cowork first came together for Pro and Max plans in September. The same unified Claude experience is now generally available for Claude Enterprise plans.

Chat and Cowork are now one Claude on web, desktop, and mobile, so your team can ask a quick question or hand over a full project in the same conversation. Agentic work runs in a cloud environment that Anthropic manages, and Claude Enterprise admins control access by role and manage usage with a new Efficient mode.

## One Claude for every task

Team members no longer choose between chat and Cowork before they start work with Claude. Conversations begin as a chat, and a simple question still gets a quick answer. When a task needs to run code or work with files, Claude continues in the cloud and returns the finished document, analysis, or deck. Because the work runs in the cloud, it keeps going after someone closes their laptop, and they can pick it up on the web, desktop, or mobile. Chats, projects, connectors, skills, and plugins carry over to the new unified experience.

Organizations are already seeing value from the unified Claude experience across their teams:

“Work at Carvana doesn’t happen only behind a desk. The unified Claude experience lets employees start a task on their computer and pick it up on their phone, with notifications when Claude has results or needs their input. It fits the way our teams work, whether they’re at their desks or visiting a site.”

“Before chat and Cowork capabilities were unified, they were separate experiences that had to be used and managed independently. Bringing them together has made everything simpler, both for our users and administrators. The transition was seamless, nothing broke across our connectors, skills or MCPs, and we’re confident rolling it out more broadly.”

“We no longer have to choose between chat and Cowork. With under ten minutes of prompting, Claude worked through stacks of county, state and federal budgets and public meeting documents, mapped how the funding streams connect, and produced a comprehensive report that would have taken our team weeks. I never had to decide which tool to use for which step. That report will shape our strategic plan and upcoming budget process.”

“Bringing chat and Cowork together answers what clients kept asking us, ‘which Claude should I use’ and ‘which one does what’. It adapts to how and where you work across mobile, desktop and browser. At Quantium, it’s helping us scale our own AI ambitions and what we can do for our clients.”

## Maintaining security

If your organization has already approved Claude chat, this builds on the enterprise controls you already use, including single sign-on (SSO) and the Compliance API. Anthropic still encrypts data in transit and at rest and doesn’t use it for model training by default.

Claude does agentic work in cloud sessions, each running in its own isolated virtual machine with network egress off by default for Claude Enterprise and connector credentials kept outside the sandbox. Because that work runs in one environment that Anthropic manages, your security team gets central visibility and controls over it. The security best practices guide on the Anthropic Trust Center covers the full architecture.

## Managing cost

Claude Enterprise pricing stays usage-based. The newest Claude models are more efficient than their predecessors: billed through usage, Claude Opus 5.5 costs 40% less to run than Claude Opus 5 on typical workloads, and Claude Sonnet 5.5 costs up to 30% less than Claude Sonnet 5 for most work.

Depending on the task, agentic work can use more tokens than a quick chat. Claude Enterprise admins have four controls for managing this usage. Efficient mode is a new setting that keeps the unified Claude experience on Sonnet and Haiku models. Model entitlements set which models each role can use. Spend limits apply at the organization, group, and member level, and pooled group budgets give a group one shared monthly amount to draw from.

## Getting started

The unified Claude experience is generally available today for Claude Enterprise plans. Admins can manage the rollout in Organization settings. Organizations that use zero data retention for Claude Code, a HIPAA-ready configuration, or customer-managed encryption keys stay on their current configuration.

See the admin setup guide for details. If you're an existing Claude Enterprise customer, you'll receive an email about the rollout for your organization.
