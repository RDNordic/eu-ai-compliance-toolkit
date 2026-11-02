---
toolkit_version: v0.1
generated: 2026-02-26
project: municipality-case-triage-assistant
mode: triage
confidence: medium
escalation_required: true
escalation_reason: >
  Special category data (health-adjacent welfare data) is processed.
  DPIA is required before deployment. Legal basis for automated triage
  recommendations must be confirmed by DPO and legal counsel.
---

# Triage Summary — Municipality Case Triage Assistant

**Organisation:** Eksempel Kommune (anonymised)
**System:** AI-assisted case triage tool for welfare and social services intake
**Session date:** 2026-02-26
**Conducted by:** R&D Nordic Compliance Intake Agent v0.1

---

## System profile snapshot

The system is an LLM-based assistant deployed internally within the social services department. Case workers submit incoming citizen requests via a web interface; the system reads the submission and returns a suggested priority category (urgent / standard / information only) and a recommended service pathway. A case worker reviews the recommendation before any action is taken.

The system is built on a third-party LLM (SaaS, EU data centre region). Personal data including name, address, stated health and financial circumstances, and family situation is processed. No biometric data is used.

Users are internal case workers. Citizens are the data subjects; they are not directly aware they are being triaged by an AI system at the point of submission.

---

## Risk tier assessment

**Provisional classification: High Risk — Annex III candidate**

**Confidence: Medium**

Basis: The system operates in the domain of access to essential public services and welfare benefits (Annex III, point 5(b) EU AI Act). It produces recommendations that directly influence which service pathway a citizen receives. Although a human case worker reviews each output, the practical effect of AI-assisted triage in a high-volume environment means case worker override rates should be monitored; low override rates may indicate the human review is nominal rather than meaningful.

Uncertainty: Classification depends on whether the municipality is acting as a deployer of a third-party system (Article 3(4)) or whether the configuration and integration work constitutes provision of a new system. This must be confirmed with legal counsel.

Relevant articles: EU AI Act Articles 6, 9, 13, 14, 17, 26; Annex III point 5(b).

**Escalation required.** Legal counsel should confirm classification before the system goes to production.

---

## DPIA trigger decision

**DPIA required: Yes**

**Confidence: High**

Basis:
- Personal data is processed at scale by an automated system (GDPR Article 35(3)(a)).
- The processing involves evaluation or scoring of individuals based on their circumstances (GDPR Article 35(3)(a), recital 91).
- Special category data is processed: stated health and financial circumstances constitute data concerning health and economic situation, which the municipality's DPO should assess against Article 9 GDPR.
- Citizens are not informed at the point of submission that their data is being processed by an AI system, which raises a transparency gap.

A DPIA must be completed and reviewed by the DPO before deployment. The municipality should also consult the relevant supervisory authority (Datatilsynet) if the DPIA identifies residual high risks that cannot be mitigated.

Relevant articles: GDPR Articles 9, 22, 35, 36; EU AI Act Articles 9, 13.

---

## Top 3 control gaps

**Gap 1 — Transparency to data subjects (Priority: High)**
Citizens are not informed that their request is processed by an AI system before a case worker reviews it. This likely breaches GDPR Articles 13-14 transparency obligations and EU AI Act Article 50 transparency requirements for deployers. Action: Add a clear disclosure statement to the submission interface before go-live. Owner: Product / legal team. Suggested deadline: Before any production deployment.

**Gap 2 — Human oversight documentation (Priority: High)**
There is no documented process for monitoring case worker override rates or for escalating concerns about systematic AI errors. A meaningful human oversight mechanism requires more than a review step existing in theory. Action: Define and document the oversight process, including override rate monitoring and escalation triggers. Owner: Operations / compliance. Suggested deadline: Before go-live.

**Gap 3 — Data processing agreement with LLM provider (Priority: High)**
A DPA covering the processing of personal data by the third-party LLM provider must be confirmed and documented. The data flow to the SaaS provider must be assessed for GDPR Chapter V compliance, including whether the EU data centre contractual terms are sufficient. Action: Legal team to review and confirm DPA and transfer mechanism. Owner: Legal / procurement. Suggested deadline: Before go-live.

---

## Recommended next steps

1. **Do not deploy to production** until the DPIA is complete and the DPO has signed off.
2. Commission a full compliance pack session (30-60 min) to produce the complete evidence set required for the DPIA and deployment sign-off.
3. Engage legal counsel to confirm EU AI Act classification (deployer vs provider) and the applicable obligations.
4. Draft and publish a citizen-facing transparency notice for the submission interface.
5. Request and review the DPA and data processing terms from the LLM provider.

---

## Disclaimer

This triage summary is a decision-support record produced by the R&D Nordic EU AI Compliance Toolkit (v0.1). It does not constitute legal advice. The findings are based on information provided during this intake session and have not been independently verified. This document should be reviewed by a qualified DPO and legal counsel before being relied upon for compliance decisions.

Toolkit: https://github.com/RDNordic/eu-ai-compliance-toolkit
Maintainer: R&D Nordic Consultancy | contact@rdnordic.com
