---
name: salesforce-ticket-delivery
description: Deliver Jira tickets on a Salesforce codebase end to end. Read the tickets, trace repo and metadata, build an acceptance-to-test matrix, implement the authorized scope, run review and regression, and write a handoff. Use when given Jira IDs or asked to implement, plan or hand off a ticket.
---

# Jira-to-Salesforce implementation and handoff

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among architecture, delivery, release, fsl-core. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Open requested Jira tickets through the available connector, including current description, acceptance criteria, comments and linked decisions. Record inaccessible tickets or ambiguous requirements.
2. Trace current repo and metadata before planning. Build an acceptance-to-test matrix quoting only the minimum necessary and cite ticket links. Obtain org facts from approved read access or state them as unknown.
3. Select relevant skills and consult official docs. Resolve objective defects and implement authorized scope with minimal changes. Preserve compatibility and existing data.
4. Run review and regression. Record decisions, files, commands, proof, open questions and next steps before compacting the Claude Code context.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
