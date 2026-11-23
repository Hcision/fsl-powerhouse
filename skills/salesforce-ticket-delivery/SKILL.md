---
name: salesforce-ticket-delivery
description: Deliver a work item on a Salesforce codebase end to end, whatever the ticketing tool. Works from a connected tracker such as Jira, Azure DevOps, GitHub Issues, ServiceNow or Linear, or from ticket text that is pasted or saved in a file, with no connection required. Use when given a ticket ID, a user story or pasted requirements to implement, plan or hand off.
---

# Work item to Salesforce implementation and handoff

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among architecture, delivery, release, fsl-core. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Get the work item from the first source that is available. Use a connected tracker tool if the session has one. Otherwise use the text, export or file the user provides. If nothing is written, ask for the goal, acceptance criteria and constraints. Never require a tracker connection, and do not ask the user to set one up. Record the source, the ID or title, and anything inaccessible or ambiguous.
2. Read the description, acceptance criteria, comments and linked decisions that are available. Trace the current repo and metadata before planning. Build an acceptance-to-test matrix that quotes only the minimum necessary. Obtain org facts from approved read access or state them as unknown.
3. Select the relevant skills and consult official docs. Resolve objective defects and implement the authorized scope with minimal changes. Preserve compatibility and existing data.
4. Run review and regression. Record decisions, files, commands, proof, open questions and next steps before compacting the Claude Code context.
5. Report back in the form the team uses. Update the tracker only when a connection exists and the user asks for it. Otherwise write a status comment the user can paste into their tool, using their field names and workflow states when they have given them.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
