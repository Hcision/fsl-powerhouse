---
name: lwc-engineering
description: Implement or review Lightning Web Components, including JavaScript, HTML templates, CSS and SLDS, wire adapters and Lightning Data Service, Apex calls, events, accessibility, Lightning Web Security and Jest tests. Use when editing files under lwc/ or debugging component rendering, data or test failures.
---

# LWC JavaScript, HTML, CSS, base components, accessibility and Jest

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among lwc, fsl-mobile, delivery. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Identify target surface, API version, supported base components, runtime constraints and accessibility requirements.
2. Prefer suitable Lightning Data Service or standard APIs, and justify Apex or imperative calls. Review caching, refresh, error/loading/empty states, stale responses and event contracts.
3. Review modern JavaScript and supported template syntax, accessibility labels, focus management, keyboard navigation, Lightning Web Security, CSS scoping and mobile layout.
4. Run Jest and lint when available and verify in the target surface. Include errors, asynchronous interactions, keyboard behavior and supported mobile/offline behavior as applicable.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
