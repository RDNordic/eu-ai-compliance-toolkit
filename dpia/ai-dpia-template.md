# Data Protection Impact Assessment (DPIA) Template for AI Systems

> **Last updated:** February 2026
>
> This template addresses the requirements of **Article 35 GDPR** with additional considerations specific to AI and machine learning systems. It incorporates relevant obligations from the **EU AI Act** where applicable.
>
> Adapt this template to your organisation's needs. Delete or expand sections as appropriate.
>
> **Jurisdictional note:** This template is based on the EU GDPR and EU AI Act. It applies in EU Member States and, via the EEA Agreement, in Norway, Iceland, and Liechtenstein. Some GDPR provisions allow national variation — check your Member State's implementing legislation and supervisory authority guidance for local requirements.

---

## When Is a DPIA Required?

A DPIA is **mandatory** under Article 35 GDPR when processing is likely to result in a **high risk** to the rights and freedoms of individuals. For AI systems, a DPIA is almost always required when:

- The AI system is classified as **high-risk** under the EU AI Act (Annex III) — note that AI Act high-risk classification does not automatically trigger a GDPR DPIA obligation, but in practice, high-risk AI systems processing personal data will almost always meet the Art. 35 threshold
- The processing involves **systematic and extensive profiling** with significant effects
- The processing involves **large-scale use of special category data**
- The processing involves **systematic monitoring** of a publicly accessible area
- The processing involves **innovative technologies** (AI/ML inherently qualifies in many cases)
- The processing meets **two or more criteria** from the EDPB/ICO DPIA screening checklist (evaluation/scoring, automated decision-making, systematic monitoring, sensitive data, large scale, combined datasets, vulnerable data subjects, innovative use, preventing data subjects from exercising a right or using a service or a contract)

> **Tip:** When in doubt, conduct a DPIA. The cost of completing one is far less than the risk of non-compliance.

---

## DPIA Document

### 1. Project Overview

| Field | Details |
|-------|---------|
| **AI system name** | |
| **Version / release** | |
| **DPIA owner** | |
| **Data Protection Officer** | |
| **Date of initial assessment** | |
| **Date of last review** | |
| **Review frequency** | *Recommended: at least annually, or upon material change* |

**Description of the AI system:**

*Describe the AI system in plain language. What does it do? What problem does it solve? Include the type of AI/ML (e.g. supervised learning, large language model, computer vision) and whether it is developed in-house or procured from a third party.*

> [Your description here]

**Scope of the processing:**

*Describe the boundaries of the processing covered by this DPIA — which datasets, which user groups, which geographies, which stages of the AI lifecycle (training, validation, inference, monitoring).*

> [Your description here]

---

### 2. Necessity and Proportionality

| Question | Response |
|----------|----------|
| What is the specific purpose of the AI processing? | |
| What lawful basis under Article 6(1) GDPR is relied upon for **training/development**? | |
| What lawful basis under Article 6(1) GDPR is relied upon for **deployment/inference**? | |
| If relying on legitimate interests (Art. 6(1)(f)), has a separate Legitimate Interest Assessment (LIA) been completed and documented? | |
| If special category data is processed, which Article 9(2) condition applies? | |
| Is the AI processing **necessary** to achieve the stated purpose, or could a less intrusive method achieve the same result? | |
| Is the scope of data collected proportionate to the purpose? | |
| How will you ensure data minimisation throughout the AI lifecycle? | |
| What retention periods apply, and how will data be deleted? | |

**Purpose limitation assessment:**

*Explain how you ensure that personal data collected for AI training/inference is not used for incompatible secondary purposes.*

> [Your assessment here]

---

### 3. Data Description

| Data Category | Description | Source | Volume (approx.) | Retention Period |
|---------------|-------------|--------|-------------------|------------------|
| *e.g. Customer transaction records* | | | | |
| *e.g. Demographic data* | | | | |
| *e.g. Biometric data* | | | | |
| *e.g. Behavioural/usage data* | | | | |

**Special category data (Article 9):**

- [ ] Racial or ethnic origin
- [ ] Political opinions
- [ ] Religious or philosophical beliefs
- [ ] Trade union membership
- [ ] Genetic data
- [ ] Biometric data (for identification)
- [ ] Health data
- [ ] Sex life or sexual orientation
- [ ] None of the above

**Criminal conviction and offence data (Article 10 GDPR):**

- [ ] The processing involves data relating to criminal convictions and offences — if so, processing must be carried out only under the control of official authority or when authorised by EU or Member State law providing for appropriate safeguards

**Proxy and inferred data:**

*AI systems can infer sensitive attributes from non-sensitive data (e.g. inferring health status from purchasing patterns). Describe any known or foreseeable proxy inference risks.*

> [Your assessment here]

---

### 4. Data Flows

*Describe or diagram how personal data flows through the AI system.*

```
[Data source] → [Collection] → [Preprocessing] → [Training/Fine-tuning]
                                                          ↓
[End user] ← [Output/Decision] ← [Inference] ← [Trained model]
                                                          ↓
                                              [Monitoring / Retraining]
```

| Stage | Description | Data Processed | Location / Infrastructure |
|-------|-------------|----------------|--------------------------|
| Collection | | | |
| Preprocessing | | | |
| Training / fine-tuning | | | |
| Inference | | | |
| Output delivery | | | |
| Monitoring / retraining | | | |

**Third-party involvement:**

| Third Party | Role (processor / joint controller / provider) | Data Shared | Contractual Safeguards |
|-------------|-----------------------------------------------|-------------|----------------------|
| | | | |

**International transfers:**

| Transfer | Destination | Transfer Mechanism (adequacy / SCCs / other) |
|----------|-------------|---------------------------------------------|
| | | |

---

### 5. Risk Assessment

For each identified risk, assess the **likelihood** (low / medium / high) and **severity** (low / medium / high) of harm to data subjects.

#### 5.1 Data Protection Risks

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Unauthorised access to training data | | | | |
| Re-identification of pseudonymised data | | | | |
| Data breach exposing model inputs/outputs | | | | |
| Excessive data collection beyond stated purpose | | | | |
| Inability to honour erasure requests (data embedded in model) | | | | |
| Inadequate retention controls | | | | |

#### 5.2 Bias and Fairness Risks

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Training data reflects historical discrimination | | | | |
| Model produces systematically different outcomes for protected groups | | | | |
| Proxy variables enable indirect discrimination | | | | |
| Feedback loops amplify existing biases | | | | |
| Under-representation of specific populations in training data | | | | |

#### 5.3 Transparency and Explainability Risks

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Data subjects cannot understand how the AI affects them | | | | |
| Inability to provide meaningful information about the logic involved | | | | |
| Insufficient documentation of model behaviour | | | | |
| Opaque third-party model with limited explainability | | | | |

#### 5.4 Automated Decision-Making Risks (Article 22)

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Decisions made without meaningful human involvement | | | | |
| No mechanism for data subjects to contest automated decisions | | | | |
| Significant effects on individuals without appropriate safeguards | | | | |

#### 5.5 Accuracy and Reliability Risks

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Model produces incorrect outputs affecting individuals | | | | |
| Performance degradation over time (model drift) | | | | |
| Adversarial inputs leading to manipulated outputs | | | | |
| Insufficient validation against real-world conditions | | | | |

#### 5.6 Security and Adversarial Risks

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Model extraction or theft | | | | |
| Data poisoning of training data | | | | |
| Membership inference attacks (determining if an individual was in training data) | | | | |
| Prompt injection or manipulation (for LLM-based systems) | | | | |
| Adversarial inputs designed to manipulate outputs | | | | |

#### 5.7 Impact on Vulnerable Data Subjects

| Risk | Likelihood | Severity | Overall | Mitigation |
|------|-----------|----------|---------|------------|
| Disproportionate impact on children | | | | |
| Disproportionate impact on elderly or digitally excluded individuals | | | | |
| Disproportionate impact on employees (power imbalance) | | | | |
| Disproportionate impact on patients or service users | | | | |
| Insufficient accommodations for individuals with disabilities | | | | |

#### 5.8 Safeguards, Security Measures, and Demonstration of Compliance

*This section addresses Article 35(7)(d) — document the specific measures envisaged to address identified risks and demonstrate compliance with the GDPR.*

| Measure Category | Details |
|-----------------|---------|
| **Technical measures** (e.g. encryption, pseudonymisation, access controls, secure infrastructure) | |
| **Organisational measures** (e.g. policies, staff training, data handling procedures) | |
| **Data protection by design and default** (Art. 25) — how are privacy principles embedded in the system's design? | |
| **Contractual safeguards** (e.g. data processing agreements, joint controller arrangements) | |
| **Monitoring and audit** (e.g. ongoing testing, bias audits, performance monitoring) | |
| **How compliance with the GDPR is demonstrated** (e.g. records of processing, DPO involvement, audit trails) | |

---

### 6. Human Oversight

| Question | Response |
|----------|----------|
| What level of human involvement exists in the AI decision process? (Human-in-the-loop / Human-on-the-loop / Human-in-command) | |
| Who is responsible for reviewing AI outputs before they take effect? | |
| What training have human reviewers received? | |
| Can the human override the AI decision in all cases? | |
| How are disagreements between human reviewers and AI outputs handled and logged? | |
| What is the escalation process for uncertain or contested decisions? | |

---

### 7. Data Subject Rights

Describe how the following rights are facilitated in the context of the AI system:

| Right | How Facilitated | Limitations (if any) |
|-------|----------------|---------------------|
| **Right to be informed** (Art. 13–14) | | |
| **Right of access** (Art. 15) | | |
| **Right to rectification** (Art. 16) | | |
| **Right to erasure** (Art. 17) | | |
| **Right to restrict processing** (Art. 18) | | |
| **Right to notification of rectification, erasure, or restriction** (Art. 19) | | |
| **Right to data portability** (Art. 20) | | |
| **Right to object** (Art. 21) | | |
| **Rights related to automated decisions** (Art. 22) | | |

**AI-specific challenges:**

*Describe any technical challenges in facilitating these rights (e.g. removing an individual's data from a trained model, explaining the logic of a complex model, providing meaningful access to inferred data).*

> [Your description here]

---

### 8. EU AI Act Considerations

*Complete this section if the AI system is classified as high-risk under the EU AI Act, or if transparency obligations apply.*

| Requirement | Status | Evidence / Notes |
|-------------|--------|------------------|
| AI Act risk classification completed | ☐ Yes ☐ No ☐ N/A | |
| Risk management system in place (Art. 9) | ☐ Yes ☐ No ☐ N/A | |
| Data governance requirements met (Art. 10) | ☐ Yes ☐ No ☐ N/A | |
| Technical documentation prepared (Art. 11) | ☐ Yes ☐ No ☐ N/A | |
| Automatic logging enabled (Art. 12) | ☐ Yes ☐ No ☐ N/A | |
| Transparency information provided (Art. 13 AI Act) | ☐ Yes ☐ No ☐ N/A | |
| Human oversight measures implemented (Art. 14) | ☐ Yes ☐ No ☐ N/A | |
| Accuracy, robustness, cybersecurity assessed (Art. 15) | ☐ Yes ☐ No ☐ N/A | |
| Conformity assessment completed (Art. 43) | ☐ Yes ☐ No ☐ N/A | |
| Registration in EU database where applicable (Art. 49, database established under Art. 71) | ☐ Yes ☐ No ☐ N/A | |
| Deployer obligations met (Art. 26) — including use of provider-supplied information for this DPIA (Art. 26(9)) | ☐ Yes ☐ No ☐ N/A | |
| Fundamental rights impact assessment completed, if required (Art. 27) — applies to bodies governed by public law and private entities providing public services | ☐ Yes ☐ No ☐ N/A | |
| Post-market monitoring plan in place (Art. 72) | ☐ Yes ☐ No ☐ N/A | |

---

### 9. Consultation

| Consultee | Date | Key Feedback | Actions Taken |
|-----------|------|-------------|---------------|
| Data Protection Officer | | | |
| Information security team | | | |
| AI/ML engineering team | | | |
| Legal counsel | | | |
| Affected data subjects or representatives | | | |
| Supervisory authority (if required) | | | |

> **Note:** Under Article 36 GDPR, prior consultation with the supervisory authority is required if the DPIA indicates that the processing would result in a high risk in the absence of measures to mitigate the risk.

---

### 10. Decision and Sign-Off

| Outcome | Details |
|---------|---------|
| **DPIA outcome** | ☐ Processing may proceed with identified mitigations ☐ Processing may proceed — residual risks are acceptable ☐ Processing should not proceed — risks are too high ☐ Further consultation with supervisory authority required |
| **Art. 36 prior consultation assessment** | Does the residual risk remain high despite mitigations? If yes, prior consultation with the supervisory authority under Article 36 GDPR is **mandatory** before processing begins. ☐ Prior consultation not required — residual risk is mitigated ☐ Prior consultation required — initiated on [date] |
| **Conditions** | *List any conditions or mitigations that must be in place before processing begins* |
| **Next review date** | |

**Approvals:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DPIA owner | | | |
| Data Protection Officer | | | |
| Senior accountable person | | | |

---

### 11. Review Log

| Review Date | Reviewer | Changes Made | Trigger for Review |
|-------------|----------|-------------|-------------------|
| | | | *Initial assessment / Annual review / Material change / Incident* |

---

## Regulatory Watchlist (Optional)

Use this section to track known regulatory moving parts that may require updates to this document.

| Topic | What to Watch | Owner | Review Date | Status | Notes |
|-------|---------------|-------|-------------|--------|-------|
| | | | | `No change` / `Update needed` | |

---

## Claim-to-Source Register (Optional)

Use this section to map key claims in this document to primary legal or regulatory sources.

| Claim ID | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Notes |
|----------|---------------|-------------|---------------------|------|---------------|-------|
| | | `Regulation` / `Guideline` / `Authority statement` | | | YYYY-MM-DD | |

---
## Further Reading

- [GDPR Article 35 — Data protection impact assessment](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [ICO — DPIA guidance](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/) *(UK GDPR — largely aligned with EU GDPR but may diverge on specific points)*
- [EDPB Guidelines on DPIA (WP248 rev.01)](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en)
- [EU AI Act — Full text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

---

*This document is provided for informational purposes only and does not constitute legal advice. Content may contain errors or become outdated as regulations evolve. Verify all information against [official sources](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and seek qualified legal counsel before making compliance decisions. If you spot an issue, please [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues) or email contact@rdnordic.com.*

*Maintained by [R&D Nordic Consultancy](https://rdnordic.com). Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).*

