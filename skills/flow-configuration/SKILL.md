---
name: flow-configuration
description: Design or review Flows and declarative configuration, including record-triggered, screen, scheduled and autolaunched flows, subflows, fault paths, order of execution, validation rules, custom metadata, permission sets and approvals. Use when touching .flow-meta.xml or other declarative metadata, or deciding between Flow and Apex.
---

# Flows, declarative configuration and automation governance

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among flow, architecture, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Inventory other automations for the same object and map order, entry criteria, run context, async paths and recursion. Use the decision guide before choosing Flow, Apex or a hybrid.
2. Audit collection operations, loops, subflows, fault paths, user-context assumptions and behavior for bulk updates. Prefer configuration when it satisfies requirements and can be maintained.
3. Review permission sets, validation rules, custom metadata, approvals, record types, layouts, actions and migration implications where relevant.
4. Test the actual persona and user entry points, changed and unchanged fields, bulk and failed transactions, activation order and flow version rollback.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
