# Recruitment and Automated Decision-Making Annex

> Last updated: 2026-02-17
>
> This annex provides practical guardrails for recruitment AI under GDPR and the EU AI Act. It is not legal advice.

---

## Why Recruitment Is High-Risk

Recruitment and worker-management systems are listed in Annex III of the EU AI Act. Many recruitment deployments are therefore high-risk and require strict controls.

Under GDPR, recruitment also creates elevated risk under Article 22 where decisions are solely automated and produce legal or similarly significant effects.

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

---

## Article 22 Practical Test

Use this test for each decision point:

1. Is there a decision about an identifiable person?
2. Is the decision solely automated in practice?
3. Does it have legal or similarly significant effects?

If all three are yes, Article 22 restrictions apply.

Minimum safeguards include:
- Human intervention by a qualified reviewer
- Ability for the candidate to express their view
- Ability for the candidate to contest the decision
- Clear anti-discrimination controls and monitoring

---

## Operational Controls

- Human-review protocol with mandatory override authority
- Bias and adverse-impact testing before and after deployment
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

- GDPR decision tree: `gdpr/lawful-basis-decision-tree.md`
- DPIA template: `dpia/ai-dpia-template.md`
- AI Act risk classification: `eu-ai-act/risk-classification.md`

---

## Primary Sources

- GDPR (Regulation (EU) 2016/679): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EU AI Act (Regulation (EU) 2024/1689): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- EDPB guidance portal: https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en

---

This annex is informational and not legal advice.
