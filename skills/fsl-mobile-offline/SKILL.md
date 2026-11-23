---
name: fsl-mobile-offline
description: Build or review Field Service mobile app extensions and offline behavior, including offline-capable LWCs, mobile flows and quick actions, record priming, sync conflicts and reconnect. Use when a feature must run in the Field Service mobile app or a technician reports sync, offline or device-specific problems.
---

# Field Service mobile extensions, offline behavior and synchronization

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-mobile, fsl-core, lwc, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Identify app build, supported devices, user persona, permissions, mobile settings, screens, flows, actions and extension targets.
2. Trace initial sync, record priming, online/offline reads, writes, sync conflicts, retry visibility and reconciliation. Verify API and runtime support per mobile extension surface.
3. Test actual device workflows for cold start, offline execution and reconnect, including work steps, parts, signatures, photos, service reports and prerequisite records where in scope.
4. Record reproducible device, app version, network state, test data, expected behavior and observed results.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
