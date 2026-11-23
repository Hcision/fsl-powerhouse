---
name: salesforce-knowledge-grounding
description: Design and test Lightning Knowledge and Agentforce Data Library grounding for Salesforce Service and Field Service procedures.
---

# Lightning Knowledge grounding

Read ../../knowledge/research-protocol.md before verifying product behavior. Use the knowledge-grounding entries in ../../knowledge/sources.json as starting points for live documentation. If a PDF or Help page is unreadable, find a relevant official HTML article and identify any remaining evidence gap.

1. Confirm agent type, channel, org prerequisites and intended audience. Identify the approved article owner, language, publication status and visibility. Check the current Salesforce guidance for how source selection and runtime access apply to this deployment.
2. Draft or review articles with a clear question, applicability, step-by-step procedure, escalation conditions and ownership. Ground organization-specific answers in authorized, approved articles. Use official product documentation for setup, support and platform behavior.
3. Verify Knowledge article and field selection, indexing status, library assignment and retrieval in the intended agent channel. Check the result as each relevant persona, including a user without access to restricted material.
4. If org access is unavailable, provide a setup and validation plan using synthetic articles. Keep private article content and identifiers out of public searches. Report observed retrieval separately from expected behavior.
5. Test grounded answers and any record-changing action separately. Verify action inputs, permissions and confirmation behavior before enabling changes.

## Field Service example

Use a synthetic article about a technician who cannot complete a job because a part is unavailable. Test that the agent retrieves the correct approved procedure, handles an unpublished or superseded version and respects restricted visibility. Use a question outside the article's scope to check escalation when evidence is missing. If creating a product request is in scope, test the configured action independently, including permission failure and duplicate submission.
