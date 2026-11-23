---
name: salesforce-architecture
description: Evaluate Salesforce solution architecture, including system boundaries, data ownership and volume, integration patterns, API contracts, Well-Architected trade-offs and decision records. Use for design reviews, configure-versus-code decisions, integration design and scalability questions.
---

# Architecture, design decisions, integrations and scalability

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among architecture, platform, fsl-core, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Capture observed system boundaries, data ownership, dependencies, volume, operational constraints and acceptance criteria. Mark assumptions explicitly.
2. Compare native configuration and extensibility options using Well-Architected dimensions. Document why the winning decision fits and specify failure handling, migration, monitoring and recovery.
3. Review transaction and integration patterns, API contracts, idempotency, access, release gates and licensing.
4. Produce a decision record with evidence links, alternatives, consequences, testing and follow-up work.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
