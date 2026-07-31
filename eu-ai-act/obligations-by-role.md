# EU AI Act Obligations By Role

> **Last updated:** 2026-07-31
>
> Reflects Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026.
>
> Obligations under the AI Act attach to **roles**, not to organisations. The same company can hold different roles for different systems, and more than one role for the same system. Establish the role before analysing obligations: almost every classification error downstream starts with getting this wrong.

---

## Start Here: Are You Sure You Are Only A Deployer?

Most organisations assume they are deployers because they bought the system from someone else. Article 25 says otherwise in three common situations.

**You become the provider of a high-risk system, with the full provider obligation set, if you:**

1. **Put your own name or trademark on it.** White-labelling a vendor's high-risk system makes it yours.
2. **Make a substantial modification** to a high-risk system already on the market.
3. **Change its intended purpose** such that a system not previously classified high-risk becomes high-risk.

This is the single most consequential provision for ordinary buyers of AI systems, and the one most often missed. Fine-tuning a vendor model on your own data, repurposing a general tool for a decision that falls in Annex III, or shipping a supplier's engine under your own brand can all move you across the line.

**Practical test:** if a regulator asked "who decided what this system is for?", and the answer is you rather than your vendor, re-examine your role.

Where the role does shift, the original provider must cooperate by supplying the information needed to meet the obligations, and is relieved of its own provider duties for that system.

---

## Role Definitions

| Role | Who this is |
|------|-------------|
| **Provider** | Develops an AI system or GPAI model, or has one developed, and places it on the market or puts it into service under its own name or trademark, whether for payment or free |
| **Deployer** | Uses an AI system under its own authority, in a professional capacity. Excludes purely personal, non-professional use |
| **Importer** | Located in the EU, places on the market an AI system bearing the name or trademark of a person established outside the EU |
| **Distributor** | Anyone in the supply chain, other than provider or importer, who makes an AI system available on the EU market |
| **Authorised representative** | Established in the EU, mandated in writing by a non-EU provider to carry out defined obligations on its behalf |
| **Product manufacturer** | Places a product on the market with an AI system embedded, under its own name or trademark. Takes on provider obligations for that AI system |

---

## Provider Obligations (High-Risk Systems)

Applies from **2 December 2027** for Annex III stand-alone systems, and **2 August 2028** for Annex I embedded systems. See [`application-dates.md`](application-dates.md).

| Obligation | Article | What it means in practice |
|---|---|---|
| Risk management system | Art. 9 | Continuous, iterative process across the lifecycle, not a one-off assessment document |
| Data governance | Art. 10 | Training, validation, and testing data quality criteria; examination for bias and mitigation. **Art. 10(5) was deleted in 2026**; the legal basis for processing special-category data for bias detection now sits in the new free-standing **Art. 4a**, with six cumulative conditions |
| Technical documentation | Art. 11 | Annex IV content set, drawn up before market placement and kept current |
| Record-keeping and logging | Art. 12 | Automatic logging of events over the system lifetime, enabling traceability |
| Transparency and instructions for use | Art. 13 | Deployers must be able to interpret output and use the system correctly |
| Human oversight design | Art. 14 | Measures built into the system so that oversight is actually possible, not nominal |
| Accuracy, robustness, cybersecurity | Art. 15 | Appropriate levels declared and maintained across the lifecycle |
| Quality management system | Art. 17 | Documented policies and procedures, proportionate to organisation size |
| Documentation retention | Art. 18 | Retain technical documentation, QMS records, and conformity documents, typically 10 years |
| Automatically generated logs | Art. 19 | Retain logs under the provider's control, typically at least 6 months |
| Corrective actions and duty to inform | Art. 20 | Withdraw, disable, or recall non-conforming systems and notify affected parties |
| Cooperation with authorities | Art. 21 | Provide information and documentation on reasoned request |
| Authorised representative | Art. 22 | Required for providers established outside the EU, appointed before placing on the market |
| Conformity assessment | Art. 43 | Internal control or notified body route, depending on the system |
| EU declaration of conformity | Art. 47 | Drawn up and kept for typically 10 years |
| CE marking | Art. 48 | Affixed before placing on the market |
| Registration in EU database | Art. 49 | Applies to Annex III high-risk systems, and to systems self-assessed as **not** high-risk under Art. 6(3). Art. 49 was **not** amended in 2026; the information required was reduced by deleting Annex VIII Section B points 7 and 9 |
| Post-market monitoring | Art. 72 | Documented plan, proportionate to risk |
| Serious incident reporting | Art. 73 | Report to market surveillance authorities within defined deadlines |

**Also applies to providers regardless of tier:** AI literacy (Art. 4, in force since 2 February 2025) and, where relevant, transparency (Art. 50, from 2 August 2026).

---

## Deployer Obligations (High-Risk Systems)

Applies on the same dates as the corresponding provider obligations.

| Obligation | Article | What it means in practice |
|---|---|---|
| Use per instructions | Art. 26(1) | Technical and organisational measures to ensure the system is used as the provider intended |
| Assign human oversight | Art. 26(2) | Oversight given to people with the competence, training, authority, **and support** to actually intervene |
| Input data relevance | Art. 26(4) | To the extent the deployer controls input data, ensure it is relevant and sufficiently representative |
| Monitoring and suspension | Art. 26(5) | Monitor operation, and suspend use plus inform the provider where risks arise |
| Log retention | Art. 26(6) | Retain logs under the deployer's control, typically at least 6 months |
| **Inform workers** | Art. 26(7) | Before putting a high-risk system into use in the workplace, inform affected workers and their representatives. This duty is routinely overlooked |
| Registration check | Art. 26(8) | Public authorities must verify the system is registered before use |
| DPIA support | Art. 26(9) | Use provider information to support a GDPR Article 35 DPIA where required |
| Inform affected persons | Art. 26(11) | Where a high-risk system is used in decision-making about individuals, inform them |
| Cooperation with authorities | Art. 26(12) | Provide information on reasoned request |
| **Fundamental rights impact assessment** | Art. 27 | Required before first use for: bodies governed by public law, private entities providing public services, and deployers of Annex III credit-scoring and life/health insurance pricing systems |
| Explanation of individual decisions | Art. 86 | Affected persons have a right to a clear and meaningful explanation of the role of the system in decisions with legal or similarly significant effects |
| Bias detection using special-category data | Art. 4a(2) | **New in 2026.** Deployers of high-risk systems, and providers and deployers of other AI systems and models, may exceptionally process special categories of personal data for bias detection and correction, subject to strict necessity and the six conditions in Art. 4a(1). This is a permission, not an obligation |

**Also applies to deployers regardless of tier:** AI literacy (Art. 4) and transparency duties under Art. 50, including notifying people subject to emotion recognition or biometric categorisation, and disclosing deep fakes.

> **GDPR overlap.** Deployers are usually controllers under GDPR for the personal data they put through the system. Article 26(9) coordinates with, but does not replace, the Article 35 DPIA obligation. See [`../dpia/ai-dpia-template.md`](../dpia/ai-dpia-template.md) and [`../flows/dpia-screen.md`](../flows/dpia-screen.md).

---

## Importer Obligations

| Obligation | Article |
|---|---|
| Verify the provider completed conformity assessment, technical documentation, CE marking, EU declaration of conformity, and appointed an authorised representative where required | Art. 23(1) |
| Do not place on the market if non-conforming, falsified, or presenting a risk; inform the provider and authorities | Art. 23(2) |
| Indicate name, registered trade name or trademark, and contact address on the system, packaging, or documentation | Art. 23(3) |
| Ensure storage and transport conditions do not jeopardise conformity | Art. 23(4) |
| Retain a copy of the certificate, instructions for use, and EU declaration of conformity, typically 10 years | Art. 23(5) |
| Cooperate with authorities on request | Art. 23(6)-(7) |

---

## Distributor Obligations

| Obligation | Article |
|---|---|
| Verify CE marking, EU declaration of conformity, instructions for use, and that provider and importer met their obligations | Art. 24(1) |
| Do not make available if non-conforming; take corrective action if a system already made available is found non-conforming | Art. 24(2)-(4) |
| Ensure storage and transport conditions do not jeopardise conformity | Art. 24(3) |
| Cooperate with authorities on request | Art. 24(5)-(6) |

---

## Authorised Representative Obligations

| Obligation | Article |
|---|---|
| Verify the EU declaration of conformity and technical documentation exist, and that conformity assessment was carried out | Art. 22(3) |
| Keep the provider's contact details, declaration, technical documentation, and certificates available to authorities, typically 10 years | Art. 22(3) |
| Provide information and documentation to authorities on request | Art. 22(3) |
| Cooperate on any action regarding the system | Art. 22(3) |
| Terminate the mandate and inform authorities where the provider acts contrary to its obligations | Art. 22(4) |

---

## GPAI Model Provider Obligations

In force since **2 August 2025**. Separate from the risk-tier framework.

| Obligation | Article |
|---|---|
| Technical documentation for the model | Art. 53(1)(a) |
| Information and documentation for downstream providers integrating the model | Art. 53(1)(b) |
| Copyright policy, including respecting text and data mining reservations | Art. 53(1)(c) |
| Publicly available summary of training content | Art. 53(1)(d) |
| Authorised representative for non-EU providers | Art. 54 |

**Models with systemic risk** (Art. 51) additionally:

| Obligation | Article |
|---|---|
| Model evaluation including adversarial testing | Art. 55(1)(a) |
| Assess and mitigate systemic risks | Art. 55(1)(b) |
| Track and report serious incidents to the AI Office | Art. 55(1)(c) |
| Adequate cybersecurity protection | Art. 55(1)(d) |
| Notify the Commission when the systemic-risk threshold is met | Art. 52 |

> **Supervision widened in 2026.** The AI Office's scope now reaches all AI systems built on GPAI models developed within the same undertaking, and systems constituting or embedded in Very Large Online Platforms and Search Engines.

> **Open-source note.** Certain obligations are relaxed for models released under a free and open-source licence, but the relief does not extend to models with systemic risk, and does not remove the copyright policy and training-content summary duties. Check the exact carve-out wording before relying on it.

---

## Quick Role Self-Test

Answer in order. Stop at the first "yes".

1. Do you put your own name or trademark on the system? **You are the provider.**
2. Did you substantially modify it, or change its intended purpose into a high-risk domain? **You are the provider (Art. 25).**
3. Did you develop it, or have it developed, and put it into service, including internally? **You are the provider.**
4. Are you in the EU, placing a non-EU party's system on the market? **You are the importer.**
5. Do you make it available on the EU market without being provider or importer? **You are the distributor.**
6. Do you use it under your own authority in a professional capacity? **You are the deployer.**

> Putting a system into service **for your own internal use** still makes you a provider. "We only use it internally" is not a defence against provider obligations if you built it.

---

## Related Files

- [`risk-classification.md`](risk-classification.md) for the tier framework
- [`application-dates.md`](application-dates.md) for deadlines
- [`omnibus-2026-changes.md`](omnibus-2026-changes.md) for what changed in 2026
- [`../flows/classify-ai-system.md`](../flows/classify-ai-system.md) for the classification workflow
- [`../flows/vendor-risk-review.md`](../flows/vendor-risk-review.md) where a vendor relationship is involved

---

## Verification Note

> Article numbers and obligation content on this page are taken from Regulation (EU) 2024/1689 as originally adopted. **The 2026 amendments noted inline were verified against the Official Journal text of Regulation (EU) 2026/1744** (CELEX 32026R1744) on 2026-07-31.
>
> **Not yet individually verified:** retention periods, reporting deadlines, and thresholds are stated as typical values and are simplified. Confirm exact periods and any derogations against the Official Journal text before relying on them. Documentation retention in particular varies by role and by whether the entity is an SME or, following the 2026 amendments, a small mid-cap company.
>
> The applicable dates for the high-risk obligations on this page depend on the Chapter III Section 5 interpretation point flagged in [`application-dates.md`](application-dates.md).

---

This document is informational and not legal advice.
