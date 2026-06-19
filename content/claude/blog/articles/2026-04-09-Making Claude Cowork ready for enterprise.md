---
title: Making Claude Cowork ready for enterprise
url: https://claude.com/blog/cowork-for-enterprise
source: blog
published: '2026-04-09'
fetched: 2026-06-13 12:15
---

- April 9, 2026
- 5min

Claude Cowork is now generally available on all paid plans. Within companies, Claude Cowork has become a key part of how teams operate: handling tasks, drafting project deliverables, and keeping teams up to date.

Today, we’re introducing organization controls to help teams deploy Claude Cowork company-wide: role-based access controls for Enterprise, group spend limits, expanded OpenTelemetry observability, and usage analytics for admins to see Claude Cowork adoption.

## Early signals

Claude Code helped developers transition from handing Claude questions to whole tasks, and we’re seeing the same pattern across the entire organization with Claude Cowork: the vast majority of Claude Cowork usage comes from outside engineering teams. Importantly, functions like operations, marketing, finance, and legal are not handing Claude their core work, but rather the work that surrounds their most critical tasks—project updates, collaboration decks, research sprints, etc.

As early enterprise adopters of Claude Cowork have seen this pattern emerge in one team, they’ve often wanted to roll it out more broadly, opening questions like who gets access, spend management, and how to see what’s happening across teams.

## Controls for organization-wide deployment

Deploying agents with Claude Cowork’s capabilities across an organization requires governance and visibility for admin teams. Today, we’re adding more of the controls organizations need:

**Role-based access controls.** Admins on Claude Enterprise can now organize users into groups — manually or via SCIM from your identity provider — and assign each a custom role defining which Claude capabilities its members can use. Turn Claude Cowork on for specific teams and adjust as adoption grows.

**Group spend limits.** Set per-team budgets from the admin console. Predictable costs, adjustable as you learn what each team needs.

**Usage analytics.** Claude Cowork activity now appears in the admin dashboard and the Analytics API. From the dashboard, admins can track Claude Cowork sessions and active users across various date ranges. The Analytics API goes deeper: per-user Claude Cowork activity, skill and connector invocations, and DAU/WAU/MAU alongside existing Chat and Claude Code figures. See which teams are adopting, which workflows are landing, and where to invest next.

**Expanded OpenTelemetry support.** Claude Cowork now emits events for tool and connector calls, files read or modified, skills used, and whether each AI-initiated action was approved manually or automatically. Events are compatible with standard SIEM pipelines like Splunk and Cribl, and a shared user account identifier lets you correlate OTEL events with Compliance API records. OpenTelemetry is available on Team and Enterprise plans.

**Zoom MCP connector.** Claude Cowork integrates with the tools your teams already use. Today, Zoom is launching a connector that brings meeting intelligence directly into the Cowork experience. The Zoom connector delivers AI Companion meeting summaries and action items alongside transcripts and smart recordings — helping teams use their conversations on Zoom to create agentic workflows in Cowork. Add Zoom from the connector directory in Claude's settings.

**Per tool connector controls.** Admins can now restrict which actions are available within each MCP connector across the organization — allowing read access but disabling write operations, for example. Permissions apply org-wide and are configured from the admin console.

## How organizations use Claude Cowork

Zapier connected Cowork to their org database, Slack, and Jira to surface engineering bottlenecks—getting back a dashboard, team-by-team analyses, and a prioritized roadmap that Product and Design Ops then copied for themselves. Jamf turned a seven-facet performance review into a 45-minute guided self-evaluation, then built similar workflows for vendor reviews and incident response. Airtree, a venture firm, built a board prep workflow that pulls from a portfolio company's Drive, Slack updates, and competitor news, cross-referenced against the previous prep.

## Getting started

Claude Cowork and Claude Code on Desktop are generally available today on all paid plans on macOS and Windows. Download the Claude desktop app at claude.com/download.

For admins deploying Claude across your organization: configure role-based access controls, group spend limits and OpenTelemetry from the admin console. Claude Cowork usage data is available in the admin dashboard, and the Analytics API is documented here.

For a deployment walkthrough, join our April 16th webinar with PayPal.

## Transform how your organization operates with Claude

Get the developer newsletter
