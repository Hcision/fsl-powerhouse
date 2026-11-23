---
name: fsl-agentforce-ai
description: Plan, build or review AI features for Field Service, including Agentforce in the Field Service mobile app, agents that book or schedule appointments through standard actions, summaries and briefings, and grounding on procedures. Use when evaluating which AI capability applies to a field service use case, or when testing an agent that reads or changes field service records.
---

# Agentforce and AI in Field Service

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among agentforce, knowledge-grounding, fsl-apis, fsl-mobile, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Establish what is licensed, enabled and generally available for the org and release. Treat announcements and previews as unverified until the setup page confirms them.
2. Map each agent task to the action it calls, the user context it runs in and the records it can read or change. Check field and record access for that context.
3. Ground answers on approved procedures and current data. Define when the agent must stop and hand over to a dispatcher or technician.
4. Test read-only answers and record-changing actions separately, per persona, including refusal, wrong-territory requests, no-slot results and repeated submissions.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for the capabilities confirmed in official pages and the standard actions agents can call. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
