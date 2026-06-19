---
title: Centrally manage authorization for MCP connectors
url: https://claude.com/blog/enterprise-managed-auth
source: blog
published: '2026-06-18'
fetched: 2026-06-19 06:42
---

- June 18, 2026
- 5min

Admins can now provision MCP connectors for their whole organization through their identity provider, starting with Okta. Users get connector access automatically on first login, with authorization configured centrally by their organization.

Connectors make Claude more useful at work — they give Claude the context it needs from the tools that your teams already use. Until now, turning them on required action at two steps: admins enabled a connector for the organization, and then every individual user authorized it themselves.

Enterprise-managed authorization streamlines that second step. Admins authorize a connector once, users inherit access through the IdP groups and roles they already have, and the connector is there the first time someone opens Claude. The result is zero-touch connector setup for the end user.

Enterprise-managed auth is the first implementation of the Enterprise-Managed Authorization extension to the Model Context Protocol. It's built on an open standard so any connector can support it — including the custom connectors your own teams build — and they all work the same way for every Claude customer.

### How it works

Connect your identity provider to Claude and choose which MCP connectors to enable for your organization. When an employee logs in, their connectors are already there. Access stays consistent across Claude chat, Claude Code, and Cowork.

For admins, this folds MCP access management into the same workflow that governs the rest of your stack: provision once, scope by group, manage revocation through the IdP. Because checking access with the IdP is frictionless, admins can shorten access token lifetimes without impacting productivity — so when someone is deprovisioned, their connector access expires fast instead of lingering on an old token. Access runs through the identity provider you already trust, so connectors fall under the same security and access controls as everything else, rather than a separate surface to monitor.

Admins can also require that a connector only ever connects through the IdP, which keeps work and personal use cleanly separated and prevents someone from accidentally linking a personal account to a work tool.

### Built with an ecosystem

Enterprise-managed authorization works across three groups: the identity providers that govern access, the MCP providers that support the standard, and the Claude customers deploying managed connections across their teams.

**Identity providers.** Okta is supported at launch, with support for additional identity providers coming soon.

**MCP providers.** Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase support Enterprise-managed auth at launch, with Slack coming soon.

**Claude customers.** Hubspot, Ramp, and Webflow are among the organizations rolling out enterprise-managed auth across their teams.

### Getting started

Enterprise-managed auth is available today in beta for customers on the Claude Team and Enterprise plans. Learn more on our Help Center and apply for access to get started.

Any identity or MCP provider can add support for enterprise-managed auth by implementing the open** **extension to the MCP authorization spec. Submit interest to join the beta** **here.

## Transform how your organization operates with Claude

Get the developer newsletter
