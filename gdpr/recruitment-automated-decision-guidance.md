# Recruitment and Automated Decision-Making Annex

> **Last updated:** 2026-07-31
>
> This annex provides practical guardrails for recruitment AI under GDPR and the EU AI Act. It is not legal advice.

---

## Why Recruitment Is High-Risk

Recruitment and worker-management systems are listed in Annex III of the EU AI Act. Many recruitment deployments are therefore high-risk and require strict controls.

Under GDPR, recruitment also creates elevated risk under Article 22 where decisions are solely automated and produce legal or similarly significant effects.

### Timing after the 2026 Omnibus

Regulation (EU) 2026/1744 moved the deadline but not the substance.

| Obligation | Applies from |
|---|---|
| AI Act high-risk obligations for Annex III employment systems | **2 December 2027** (was 2 August 2026) |
| AI Act Art. 50 transparency, where candidates interact with the system | **2 August 2026**, not delayed |
| AI Act Art. 26(7): inform affected workers and their representatives before putting a high-risk system into use in the workplace | With the high-risk obligations |
| **GDPR obligations, including Art. 22, Art. 9, DPIA, and transparency** | **Already in force.** Unaffected by anything in the AI Act timeline |

> **The delay changes very little for recruitment.** The GDPR exposure in this area has always been the more immediate constraint, and none of it moved. A recruitment tool that would have failed an Article 22 analysis in July 2026 still fails it. Use the extra time for evidence quality, not to defer the work.

See [`../eu-ai-act/application-dates.md`](../eu-ai-act/application-dates.md).

---

## Legal Checklist Before Deployment

- Identify whether the tool is used to make or materially shape hiring decisions.
- Assess whether Article 22 GDPR is triggered.
- If Article 22 applies, confirm one of the Article 22(2) exceptions and required safeguards.
- Validate lawful basis for each stage: sourcing, screening, ranking, interview support, and retention.
- Confirm Member State employment-law requirements (including collective/labour framework where relevant).
- Complete DPIA and document residual risk.
- Complete AI Act role analysis and high-risk obligations.

---

## Lawful Basis Guardrails

- Do not assume consent is valid in employment/recruitment contexts; power imbalance often makes it unreliable.
- Contract basis is narrow and must be necessary for steps requested by the candidate.
- Legitimate interests can support some preparatory processing, but does not bypass Article 22 constraints.
- Where special category data is processed or inferred, add an Article 9(2) condition and safeguards.
- For **bias and adverse-impact testing** that requires special-category data, AI Act Art. 4a now provides an Art. 9(2)(g) route, subject to six cumulative conditions. It is available now and is not deferred with the high-risk obligations. It is a permission, not an obligation, and it does not cover special-category processing for model training generally. See [`lawful-basis-decision-tree.md`](lawful-basis-decision-tree.md).

---

## Article 22 Practical Test

Use this test for each decision point:

1. Is there a decision about an identifiable person?
2. Is the decision solely automated in practice?
3. Does it have legal or similarly significant effects?

If all three are yes, Article 22 restrictions apply.

> **Question 2 is where most assessments go wrong.** "A recruiter reviews the shortlist" does not by itself make a decision non-automated. If the recruiter in practice accepts the ranking, lacks the time, information, or authority to go behind it, or is not measured on doing so, the decision may still be solely automated in substance. Evidence the override: how often it happens, on what basis, and whether the reviewer sees the underlying features rather than only the score.

Minimum safeguards include:
- Human intervention by a qualified reviewer
- Ability for the candidate to express their view
- Ability for the candidate to contest the decision
- Clear anti-discrimination controls and monitoring

---

## Operational Controls

- Human-review protocol with mandatory override authority
- Bias and adverse-impact testing before and after deployment, with the Art. 4a conditions documented if special-category data is used for it
- Traceable logs for features, thresholds, and overrides
- Candidate-facing notice language that is specific and understandable
- Retention limits and access controls for candidate data

---

## Documentation Pack

Maintain these records:
- DPIA with recruitment-specific risks
- Lawful basis and Article 22 analysis memo
- AI Act classification and obligations mapping
- Data retention schedule
- Change log for model updates and threshold changes

---

## Cross-References in This Toolkit

- GDPR decision tree: [`lawful-basis-decision-tree.md`](lawful-basis-decision-tree.md)
- DPIA template: [`../dpia/ai-dpia-template.md`](../dpia/ai-dpia-template.md)
- AI Act risk classification: [`../eu-ai-act/risk-classification.md`](../eu-ai-act/risk-classification.md)
- AI Act obligations by role: [`../eu-ai-act/obligations-by-role.md`](../eu-ai-act/obligations-by-role.md)
- What the 2026 Omnibus changed: [`../eu-ai-act/omnibus-2026-changes.md`](../eu-ai-act/omnibus-2026-changes.md)
- Worked example: [`../examples/recruitment-ai-case.md`](../examples/recruitment-ai-case.md)

---

## Primary Sources

- GDPR (Regulation (EU) 2016/679): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EU AI Act (Regulation (EU) 2024/1689): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Digital Omnibus on AI (Regulation (EU) 2026/1744): https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- EDPB guidance portal: https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en

---

This annex is informational and not legal advice.
