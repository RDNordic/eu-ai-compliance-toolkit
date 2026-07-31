# EU AI Act — Risk Classification Quick Reference

> **Last updated:** 2026-07-31
>
> **Status: revised for Regulation (EU) 2026/1744 (Digital Omnibus on AI), in force 27 July 2026.**
>
> This document summarises the risk-based classification framework established by the EU AI Act (Regulation (EU) 2024/1689), **as amended**. Always refer to the [official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) for authoritative definitions.
>
> **The classification framework itself did not change. The deadlines and parts of the scope did.** If you classified a system before July 2026, the tier is probably still right, but the date you were working to and the Art. 6(1) safety-component test may not be. See [`omnibus-2026-changes.md`](omnibus-2026-changes.md).

---

## Overview

The EU AI Act classifies AI systems into four risk tiers. Each tier carries different obligations for providers, deployers, importers, and distributors. Classification is based on the **intended purpose** of the AI system and the **context of use**, not the underlying technology.

```
┌─────────────────────────────────────┐
│         PROHIBITED (Art. 5)         │  ← Banned outright
├─────────────────────────────────────┤
│        HIGH-RISK (Art. 6–51)        │  ← Strict obligations
├─────────────────────────────────────┤
│     LIMITED RISK (Art. 50)          │  ← Transparency obligations
├─────────────────────────────────────┤
│        MINIMAL RISK                 │  ← No specific obligations
└─────────────────────────────────────┘
```

---

## 1. Prohibited AI Practices (Article 5)

These AI systems are **banned entirely** within the EU. No exceptions unless explicitly stated.

| Prohibited Practice | Description |
|---------------------|-------------|
| **Social scoring** | Evaluating or classifying individuals by public or private entities based on social behaviour or personal characteristics, leading to detrimental or disproportionate treatment in unrelated contexts |
| **Exploiting vulnerabilities** | AI that exploits age, disability, or socio-economic circumstances to materially distort behaviour in a harmful way |
| **Subliminal manipulation** | Techniques beyond a person's consciousness that materially distort behaviour, causing significant harm |
| **Real-time remote biometric identification in public spaces** | For law enforcement purposes, except in narrowly defined circumstances (missing children, imminent threats, serious criminal offences) |
| **Biometric categorisation using sensitive characteristics** | Categorising individuals based on biometric data to infer race, political opinions, trade union membership, religious beliefs, sex life, or sexual orientation |
| **Untargeted scraping for facial recognition databases** | Scraping facial images from the internet or CCTV to build or expand facial recognition databases |
| **Emotion recognition in workplaces and education** | Inferring emotions in workplace and educational settings, except for medical or safety reasons |
| **Individual predictive policing** | Risk assessments of individuals predicting criminal offending based solely on profiling or personality traits |
| **CSAM-generating systems** *(new, 2026)* | AI systems that generate or manipulate child sexual abuse material |
| **Non-consensual intimate imagery** *(new, 2026)* | AI systems that generate or manipulate non-consensual sexual or intimate imagery, including so-called "nudifier" applications |

> **New prohibitions added by Regulation (EU) 2026/1744**, inserted as Art. 5(1) points (ba) and (bb), with scope rules in new Art. 5(1a) and (1b). Point (bb) is defined by reference to Article 2(c) and (e) of Directive 2011/93/EU, subject to any "without right" defence under national law.
>
> **The scope rule matters more than the headline.** Under Art. 5(1a)(a), placing on the market or putting into service is prohibited only where either (i) that generation or manipulation is the **intended purpose** of the system, or (ii) the system's design, training, architecture, capabilities, or user-facing functionality make it a **reasonably foreseeable and reproducible outcome without significant technical modification**, *and* the system lacks reasonable and adequate technical safety measures and safeguards to reliably prevent it, accounting for reasonably foreseeable misuse, and to correct observed or reported misuse.
>
> The practical effect is that general-purpose image, video, and audio generators are not caught automatically, but weak safeguards can bring them into scope. The recitals are explicit that the prohibition is not intended to prevent providers from developing the underlying technical capability.

### Key dates

- **2 February 2025:** Prohibitions on banned practices entered into force.
- **2 December 2026:** Transitional deadline for the two prohibitions added in 2026 (CSAM and non-consensual intimate imagery), including the associated technical safeguards.

---

## 2. High-Risk AI Systems (Articles 6–51)

High-risk AI systems are permitted but subject to **comprehensive compliance requirements** before and after market placement.

### When is an AI system high-risk?

An AI system is classified as high-risk if it falls into one of two categories:

**Category A — Safety components and regulated products (Article 6(1))**

AI systems intended as safety components of products covered by EU harmonisation legislation listed in Annex I, or AI systems that are themselves such products. This includes:

- Medical devices and in vitro diagnostic medical devices
- Machinery and lifts
- Toys, radio equipment, and pressure equipment
- Aviation, automotive, and marine safety systems
- Railway systems

> **Scope narrowed in 2026.** Regulation (EU) 2026/1744 inserted three new paragraphs into Article 6:
>
> - **Art. 6(1a):** AI systems used **solely** for non-safety-related aspects of user assistance, performance optimisation, service efficiency, automation, convenience, or quality control **do not qualify as safety components**.
> - **Art. 6(1b):** notwithstanding the above, AI systems whose failure or malfunction **would endanger health and safety** do qualify as safety components.
> - **Art. 6(1c):** a product required to undergo third-party conformity assessment **solely** because of risks other than health and safety, in particular radio spectrum distribution or electromagnetic interference not affecting health and safety, does not satisfy the condition in Art. 6(1)(b).
>
> If you previously classified an embedded system as high-risk on the strength of embedding alone, re-run that assessment. Note also that **Annex I Section A point 1 (machinery) was deleted** and Regulation (EU) 2023/1230 on machinery was added to **Annex I Section B** instead, which changes the conformity-assessment route for machinery-embedded AI.

**Category B — Standalone high-risk systems (Article 6(2), Annex III)**

AI systems with intended purposes falling within these domains:

| Annex III Area | Examples |
|----------------|----------|
| **Biometrics** | Remote biometric identification (non-prohibited), biometric categorisation, emotion recognition (where permitted) |
| **Critical infrastructure** | AI managing safety of digital infrastructure, road traffic, water, gas, heating, or electricity supply |
| **Education and vocational training** | Admissions decisions, assessment of learning outcomes, monitoring of cheating, adaptive learning that affects educational pathways |
| **Employment and worker management** | CV screening, recruitment decisions, promotion and termination decisions, task allocation based on behaviour or traits, performance monitoring |
| **Access to essential services** | Credit scoring, insurance risk assessment, emergency service dispatch prioritisation |
| **Law enforcement** | Polygraphs, evidence reliability assessment, profiling during investigations (non-prohibited uses) |
| **Migration, asylum, and border control** | Risk assessments for irregular migration, visa and residence application processing, identification of persons |
| **Administration of justice** | AI assisting judicial authorities in researching and interpreting facts and law, applying the law to facts |
| **Democratic processes** | AI used to influence voting behaviour (excluding content that does not directly interact with individuals) |

### Important exception (Article 6(3))

A system listed in Annex III is **not** considered high-risk if it does not pose a **significant risk of harm** to health, safety, or fundamental rights. The following conditions are indicators that significant risk may be absent:

- Performs a narrow procedural task
- Improves the result of a previously completed human activity
- Detects decision-making patterns without replacing or influencing human assessment
- Performs a preparatory task to an assessment relevant to the use cases in Annex III

> **Critical exception:** This exception can **never** be invoked if the AI system performs **profiling of natural persons** — such systems are always considered high-risk regardless of the above conditions (Article 6(3)).

> **Obligations when relying on this exception:** Providers must **document their assessment** explaining why the system does not pose a significant risk, and **register the system in the EU database** under Article 49(2) before placing it on the market.

### Obligations for high-risk AI systems

| Requirement | Summary |
|-------------|---------|
| **Risk management system** (Art. 9) | Continuous, iterative process throughout the system lifecycle |
| **Data governance** (Art. 10) | Training, validation, and testing datasets must meet quality criteria; bias examination and mitigation |
| **Technical documentation** (Art. 11) | Comprehensive documentation demonstrating compliance, maintained and updated |
| **Record-keeping / logging** (Art. 12) | Automatic logging of events to enable traceability and post-market monitoring |
| **Transparency and information** (Art. 13) | Instructions for use enabling deployers to interpret outputs and use the system appropriately |
| **Human oversight** (Art. 14) | Effective human oversight measures appropriate to the risk level and degree of autonomy |
| **Accuracy, robustness, cybersecurity** (Art. 15) | Appropriate levels of accuracy, robustness, and cybersecurity throughout the lifecycle |
| **Quality management system** (Art. 17) | Documented policies and procedures ensuring ongoing compliance |
| **Conformity assessment** (Art. 43) | Self-assessment or third-party assessment depending on the system type |
| **EU declaration of conformity** (Art. 47) | Written declaration that the system meets requirements |
| **CE marking** (Art. 48) | Affixed before market placement |
| **Registration in EU database** (Art. 49) | Registration applies in defined cases (notably Annex III high-risk systems and specific exceptions/arrangements); verify applicability before market placement or putting into service. **Article 49 itself was not amended by the 2026 Omnibus.** The reduction in registration burden was made instead by deleting points 7 and 9 of Annex VIII, Section B, which cut the information a provider must supply |
| **Bias detection using special-category data** (new Art. 4a) | **Art. 10(5) was deleted by the 2026 Omnibus and replaced by a new, free-standing Article 4a.** Art. 4a(1) lets providers of high-risk systems process special categories of personal data where strictly necessary for bias detection and correction under Art. 10(2)(f) and (g), subject to six cumulative conditions. Art. 4a(2) extends the same possibility to providers and deployers of **other** AI systems and models, and to **deployers** of high-risk systems, on the same conditions. Art. 4a(2) expressly creates **no obligation** to carry out bias detection. See [`../gdpr/lawful-basis-decision-tree.md`](../gdpr/lawful-basis-decision-tree.md) |

### Key dates

- **2 February 2025:** AI literacy obligations (Art. 4) apply; prohibitions on banned practices (Art. 5) apply.
- **2 August 2025:** Rules on notified bodies apply; GPAI model obligations apply.
- **2 August 2026:** General application date. Transparency obligations (Art. 50) apply. **High-risk obligations do not.** See below.
- **2 December 2027:** Obligations for stand-alone high-risk AI systems listed in Annex III. *(Moved by Regulation (EU) 2026/1744; was 2 August 2026.)*
- **2 August 2028:** Obligations for high-risk AI systems under Article 6(1), embedded in products subject to third-party conformity assessment under Annex I legislation. *(Moved by Regulation (EU) 2026/1744; was 2 August 2027.)*
- **31 December 2030:** Compliance deadline for AI systems that are components of certain large-scale IT systems. The original text keyed this to systems placed on the market before 2 August 2027; confirm whether that reference date was re-based.

> **The delay is schedule relief, not scope relief.** Every requirement in the table above still applies to Annex III systems. Only the date moved. Risk management, data governance, technical documentation, logging, human oversight, and conformity assessment work should continue on the original design assumptions.

See [`application-dates.md`](application-dates.md) for the full timeline and [`omnibus-2026-changes.md`](omnibus-2026-changes.md) for what changed.

---

## 3. Limited Risk — Transparency Obligations (Article 50)

AI systems that interact with people or generate content carry **transparency obligations**, regardless of their risk level.

| System Type | Transparency Requirement |
|-------------|--------------------------|
| **Chatbots and conversational AI** | Must inform users they are interacting with an AI system, unless obvious from the circumstances |
| **Emotion recognition systems** | Must inform individuals that the system is in operation (where permitted) |
| **Biometric categorisation systems** | Must inform individuals that the system is in operation |
| **Deep fakes / synthetic content** | Must disclose that the content has been artificially generated or manipulated; must be machine-readable where technically feasible |
| **AI-generated text published to inform the public** | Must disclose AI generation, unless subject to human editorial review and a natural or legal person holds editorial responsibility |

### Key dates

- **2 August 2026:** Transparency obligations apply. **This date was not moved by the 2026 Omnibus.**
- **2 December 2026:** Grace period ends for machine-readable marking of synthetic content under Art. 50(2), for systems **already placed on the market before 2 August 2026**. Systems placed on the market on or after 2 August 2026 comply from that date.

> **This is the most commonly missed obligation right now.** Because the high-risk deadline moved to December 2027, a lot of teams have concluded the AI Act no longer affects them this year. Article 50 is unaffected by that delay and binds from 2 August 2026. If your product talks to users, generates content, or produces synthetic media, this is your live obligation.

---

## 4. Minimal Risk

All other AI systems fall into the minimal risk category. These include:

- Spam filters
- AI-enabled video games
- Inventory management systems
- Basic recommendation engines (non-manipulative)
- Search result ranking (non-manipulative)

**No specific regulatory obligations apply**, though providers are encouraged to voluntarily adopt codes of conduct (Article 95).

---

## General-Purpose AI (GPAI) Models — Separate Obligations

> **Important:** The four-tier risk classification above applies to **AI systems**. Providers of **general-purpose AI models** (e.g. foundation models, large language models) have **separate obligations** under Articles 51–56 that are not captured by the risk tiers.

GPAI model obligations include:

- Technical documentation and transparency requirements (Art. 53)
- Copyright policy compliance and making training data summaries available (Art. 53(1)(d))
- Compliance with a code of practice or equivalent measures

**GPAI models with systemic risk** (Art. 51(2)) have additional obligations:

- Model evaluation and adversarial testing (Art. 55)
- Cybersecurity protections
- Serious incident reporting
- Energy consumption reporting

These obligations apply from **2 August 2025**. A provider of a GPAI model that is also deployed as an AI system may need to comply with both the GPAI obligations and the risk-tier obligations applicable to the system's intended purpose.

> **Supervision widened in 2026.** Regulation (EU) 2026/1744 replaced Art. 75(1). The AI Office is now **exclusively competent** for supervising and enforcing obligations in relation to:
>
> - AI systems based on GPAI models where the model and the system are developed by the **same provider, or providers in the same undertaking**; and
> - AI systems that constitute, or are integrated into, a Very Large Online Platform or Very Large Online Search Engine.
>
> Carve-outs remain for AI systems related to Annex I products, Annex III point 2 systems, systems provided by law enforcement, border management and financial institutions falling under Art. 74(6), and Annex III point 8 systems in the administration of justice.
>
> If you build products on your own foundation models, supervision moves from your national authority to the AI Office for those systems. That is a change of regulator, not just a change of scope.

> **Note:** This document focuses on AI system classification. A separate guide to GPAI model obligations is planned for a future release.

---

## Common Misclassifications

> **Legal caveat:** The examples below are illustrative. Classification and obligations depend on intended purpose, deployment context, role (provider/deployer/importer/distributor), and national implementation details.

| Scenario | Often Assumed | Actual Classification | Reasoning |
|----------|---------------|----------------------|-----------|
| Internal chatbot for employees | Minimal risk | **Limited risk** at minimum; potentially **high-risk** | Transparency obligations apply; if used for employee management purposes (HR decisions, task allocation, performance monitoring), it may fall under Annex III employment provisions |
| AI-powered CV screening tool | Limited risk | **High-risk** | Employment decisions fall under Annex III |
| AI tool suggesting draft emails | High-risk | Likely **minimal risk** | Narrow procedural task, does not replace human decision-making |
| Customer service chatbot | Minimal risk | **Limited risk** | Must disclose AI nature to users |
| AI credit scoring model | Limited risk | **High-risk** | Access to essential financial services falls under Annex III |
| AI-generated marketing images | Minimal risk | **Limited risk** | Synthetic content must be disclosed |

---

## Practical Steps for Classification

1. **Identify the intended purpose** of the AI system — what decisions or outputs does it produce?
2. **Check Article 5** — is the system prohibited outright?
3. **Check Annex I** — is it a safety component of a regulated product?
4. **Check Annex III** — does the intended purpose fall within a listed high-risk domain?
5. **If Annex III applies, assess Article 6(3)** — does the narrow exception for non-significant risk apply? (Note: this exception **cannot** be used if the system performs profiling.)
6. **Check Article 50** — do transparency obligations apply regardless of risk tier?
7. **Document your classification reasoning** — this is essential for audit trails and regulatory enquiries.

---

## Regulatory Watchlist (Optional)

Use this section to track known regulatory moving parts that may require updates to this document.

| Topic | What to Watch | Owner | Review Date | Status | Notes |
|-------|---------------|-------|-------------|--------|-------|
| Chapter III Section 5 scope | Whether Arts. 40-49 fall outside the Art. 113(3)(c) deferral and apply from 2026-08-02 | _unassigned_ | 2026-09-01 | `Update needed` | Interpretation point, not a sourcing gap. Affects conformity assessment and Art. 49 registration timing |
| Art. 50 guidance and Code of Practice on marking | Commission guidance on transparency and machine-readable marking ahead of 2026-08-02 | _unassigned_ | 2026-08-15 | `Update needed` | The live obligation this year; guidance expected around the application date |
| Art. 4a bias-detection conditions | Guidance on the six cumulative conditions and how deployers evidence "strictly necessary" | _unassigned_ | 2026-10-01 | `No change` | New Art. 4a replaced the deleted Art. 10(5); GDPR interaction point |
| New Art. 5 prohibitions in practice | Enforcement approach to the Art. 5(1a) safeguards test for general-purpose generators | _unassigned_ | 2026-11-01 | `No change` | Wording verified against OJ text; transitional deadline 2026-12-02 |
| Harmonised standards for high-risk systems | CEN-CENELEC deliverables; standards readiness was the stated reason for the delay | _unassigned_ | 2026-10-01 | `No change` | Drives whether 2027-12-02 holds |
| National competent authority designations | Member State designations and any national AI Act implementing law, incl. EEA status for Norway | _unassigned_ | 2026-10-01 | `No change` | Relevant to the EEA scope note in README |

---

## Claim-to-Source Register (Optional)

Use this section to map key claims in this document to primary legal or regulatory sources.

| Claim ID | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Notes |
|----------|---------------|-------------|---------------------|------|---------------|-------|
| RC-01 | Four-tier risk classification based on intended purpose and context of use | `Regulation` | 2024/1689 Arts. 5, 6, 50 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-07-31 | Framework unchanged by the 2026 Omnibus |
| RC-02 | Eight original prohibited practices | `Regulation` | 2024/1689 Art. 5(1) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-07-31 | Applied from 2025-02-02 |
| RC-03 | Two new prohibitions: non-consensual intimate material and CSAM | `Regulation` | 2026/1744 Art. 1(7), inserting 2024/1689 Art. 5(1)(ba), (bb) and Art. 5(1a), (1b) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified against OJ text. Apply from 2026-12-02 per Art. 113(3)(a) as amended |
| RC-04 | Art. 6(3) exception unavailable where the system profiles natural persons | `Regulation` | 2024/1689 Art. 6(3) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-07-31 | Unchanged |
| RC-05 | Annex III high-risk obligations apply from 2027-12-02 | `Regulation` | 2026/1744 Art. 1(40), replacing 2024/1689 Art. 113(3)(c)(i) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified against OJ text. Was 2026-08-02. Covers Ch. III Sections 1, 2, 3 only |
| RC-06 | Annex I / Art. 6(1) high-risk obligations apply from 2028-08-02 | `Regulation` | 2026/1744 Art. 1(40), replacing 2024/1689 Art. 113(3)(c)(ii) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified against OJ text. Was 2027-08-02 |
| RC-07 | Art. 50 transparency obligations apply from 2026-08-02 and were not delayed | `Regulation` | 2024/1689 Art. 50; 2026/1744 Art. 1(20) amends only Art. 50(7) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. Only the codes-of-practice paragraph was amended; the substantive duties in Art. 50(1) to (6) were untouched |
| RC-08 | Art. 50(2) marking grace period to 2026-12-02 for systems already on market | `Regulation` | 2026/1744 Art. 1(39)(b), adding 2024/1689 Art. 111(4) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. Delivered as a transitional provision in Art. 111, not as an amendment to Art. 50 |
| RC-09 | Safety-component test narrowed for embedded AI | `Regulation` | 2026/1744 Art. 1(8), inserting 2024/1689 Art. 6(1a), (1b), (1c) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified against OJ text |
| RC-10 | Bias-detection processing of special-category data restructured into new Art. 4a | `Regulation` | 2026/1744 Art. 1(6) inserting Art. 4a; Art. 1(9)(b) deleting Art. 10(5) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. **Art. 10(5) was deleted, not amended.** Art. 4a(2) extends the possibility to deployers and to non-high-risk systems, and creates no obligation |
| RC-11 | GPAI obligations apply from 2025-08-02 | `Regulation` | 2024/1689 Arts. 51-56; Art. 113(3)(b) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-07-31 | Unchanged |
| RC-12 | AI Office is exclusively competent for supervision of same-undertaking GPAI-based systems and VLOP/VLOSE-integrated systems | `Regulation` | 2026/1744 Art. 1(31), replacing 2024/1689 Art. 75(1) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. Note carve-outs for Annex I products, Annex III point 2, law enforcement/border/financial under Art. 74(6), and Annex III point 8 justice |
| RC-13 | Art. 49 registration was not amended; burden reduced via Annex VIII | `Regulation` | 2026/1744 Art. 1(42), deleting Annex VIII Section B points 7 and 9 | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. Art. 49 itself is untouched |
| RC-14 | AI regulatory sandboxes operational by 2027-08-02 | `Regulation` | 2026/1744 Art. 1(22), replacing 2024/1689 Art. 57(1) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-07-31 | Verified. Was 2026-08-02 |
| RC-15 | Annex X large-scale IT systems deadline unchanged at 2030-12-31 | `Regulation` | 2024/1689 Art. 111(1) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-07-31 | Verified. Art. 111(1) was **not** amended; the 2027-08-02 reference date stands |

> **Verification status: primary-source verified.** All rows above were checked against the Official Journal texts of Regulation (EU) 2024/1689 and Regulation (EU) 2026/1744 (CELEX 32026R1744) on 2026-07-31.
>
> The one item that remains genuinely open is an interpretation question rather than a sourcing gap: whether Chapter III Section 5 (Arts. 40-49) falls outside the deferral and therefore applies from 2026-08-02. See [`application-dates.md`](application-dates.md).

---
## Further Reading

- [EU AI Act — Full text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [AI Act — Application Dates (this toolkit)](application-dates.md)
- [European Commission — AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Compliance Checker (Future of Life Institute)](https://artificialintelligenceact.eu/)
- [Regulation (EU) 2026/1744, Digital Omnibus on AI (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)
- [What the 2026 Omnibus changed (this toolkit)](omnibus-2026-changes.md)
- [Obligations by role (this toolkit)](obligations-by-role.md)

> **Caution on third-party mirrors.** As of 2026-07-31, several widely used AI Act reference sites were still serving pre-Omnibus text, including the consolidated Article 113. Check the amendment status of anything you rely on.

---

*This document is provided for informational purposes only and does not constitute legal advice. Content may contain errors or become outdated as regulations evolve. Verify all information against [official sources](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) and seek qualified legal counsel before making compliance decisions. If you spot an issue, please [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues) or email contact@rdnordic.com.*

*Maintained by [R&D Nordic Consultancy](https://rdnordic.com). Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).*

