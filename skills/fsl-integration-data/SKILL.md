---
name: fsl-integration-data
description: Design or review Field Service integrations and data movement, including the Field Service REST resources and standard invocable actions, FSL Apex, managed package triggers, platform events, ERP or asset system sync, bulk data loads and moving configuration between orgs. Use when calling Field Service from code or middleware, loading field service data, or planning a deployment that includes scheduling configuration.
---

# Field Service APIs, integrations, data loads and deployment

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-apis, fsl-core, platform, delivery, architecture. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. List every inbound and outbound interface with its trigger, API, authentication, volume and owner. Separate standard REST and actions, FSL Apex, and custom endpoints.
2. For each write path, check which managed package triggers and custom automation fire, transaction size, callouts, retry and idempotency, and what happens to scheduling when records change underneath it.
3. For data loads, define object order, required lookups, geocoding, time zones and status values. Decide which automation is bypassed and how that is restored and verified.
4. For deployment, separate metadata from configuration held as records or package settings. Plan how each is moved, validated and rolled back, and test in a sandbox with the target package version.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for REST resources, standard actions, metadata types and the documented samples. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
