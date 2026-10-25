---
title: Claude Security now scans continuously and tracks fixes
url: https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes
source: blog
published: '2026-10-21'
fetched: 2026-10-25 15:13
---

# Claude Security now scans continuously and tracks fixes

Claude Security now keeps up with your repositories as code changes, tracks findings until they’re fixed, learns from the context your team adds, and connects to your tools through an API and MCP. Available in public beta for Claude Enterprise customers.

Since Claude Security entered public beta in April, thousands of organizations have used it to find over a million vulnerabilities.

Instead of waiting for someone to start a scan, Claude Security now keeps up with your repositories as your code changes, keeps track of which findings get fixed, and uses what your team tells it about your environment to decide what matters. Claude Security is powered by our full family of models, including Claude Mythos, with no Cyber Verification Program access required.

The latest version of Claude Security is available today in public beta for Claude Enterprise customers. Organizations receive $25,000 in free usage credits each month, for two months. The offer applies to usage through December 31, 2026. You can view full terms in the Help Center.

**Continuous monitoring keeps up with your code**

A scan captures one moment, and code changes every day. Teams told us they wanted coverage that stays current without anyone having to schedule it.

Create a project, connect your repositories through the Claude GitHub app (including GitHub Enterprise Server) or with an access token from GitLab and other Git providers, and choose the branch and scope for each. Claude runs a deep baseline scan, then scans changes regularly based upon their risk and complexity, so your list of findings stays close to the current state of your code.

A project can hold multiple repositories, so Claude can catch issues that live between services, like a backend that trusts input a client was supposed to validate.

**Findings are marked fixed when the fix ships**

Most fixes happen outside the tool that found the issue. Claude Security checks open findings against the code that changed and marks them fixed when the fix lands, whether your team fixed it in Claude Code or in a separate process. If Claude Security finds the issue again later, the finding reopens automatically.

**Your team’s knowledge shapes the scan**

Every environment has controls a scanner can’t see from the code alone. Teams wanted a way to tell Claude Security about those controls, and to look across services that depend on each other. Now, each project has a knowledge base where you can describe how your code is deployed, which security policies apply, and anything a new security engineer on your team would need to know.

Claude Security also generates a threat model from your code that your team can review and edit. Subsequent scans use those threat models to decide what’s worth flagging. Added context also helps Claude Security skip risks your environment already handles.

**Severity and exploit paths for every finding**

Each finding comes with a severity rating, judged against your project’s threat model, and an explanation of how an attacker could reach the vulnerable code, so teams can fix what’s actually reachable first. Findings can include a diagram of the attack path.

**Findings reach your tools, with controls for larger rollouts**

The new API lets you integrate Claude Security into your existing workflows. You can list and read projects and findings, resolve or reopen findings, and create and manage projects and their repositories. Users can create a personal access token in Claude Security settings, and it can only see and change what the user can. Webhooks can also notify your systems when a new finding lands.

Claude Security is also available as an MCP connector in Claude.ai and Claude Code. An engineer can pull up a finding, ask Claude about it, start the fix, and mark it resolved in the same session.

New role-based access controls let admins decide who can view projects, triage findings, and create projects. Organizations can open Claude Security to more teams that own the code without giving everyone access to create projects.

**Getting started**

The latest version of Claude Security is available in public beta for Claude Enterprise customers starting today. Admins can enable it in the admin console and set who on their team can access it.

Use the Getting Started Guide to set up your first project, and visit the Help Center for more details.

*Organizations receive $25,000 in free usage credits each month, for two months. The offer applies to usage through December 31, 2026. You can view full terms in the Help Center.*

“Claude Security found a number of logic flaws that none of our other tools had caught. Once we wrote our own risk policy into the threat model, focusing on what external users can actually reach, the findings matched how we prioritize instead of only a severity score”

“Claude Security found many material issues that a traditional pen test conducted at the same time missed, several of which would have had significant impact if exploited in the wild.”

“Claude Security scanned our code once to set a baseline. Now it keeps up as our code changes, and our team fixes issues right in Claude instead of switching to another tool.”

“The API and MCP additions are a game changer and will be the path forward for IonQ’s Product Security team to further operationalize Claude Security.”
