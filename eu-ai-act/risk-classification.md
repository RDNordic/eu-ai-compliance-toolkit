# EU AI Act — Risk Classification Quick Reference

> **Last updated:** February 2026
>
> This document summarises the risk-based classification framework established by the EU AI Act (Regulation (EU) 2024/1689). Always refer to the [official text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) for authoritative definitions.

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

### Key dates

- **2 February 2025:** Prohibitions on banned practices entered into force.

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
| **Registration in EU database** (Art. 49) | Registration applies in defined cases (notably Annex III high-risk systems and specific exceptions/arrangements); verify applicability before market placement or putting into service |

### Key dates

- **2 February 2025:** AI literacy obligations (Art. 4) apply; prohibitions on banned practices (Art. 5) apply.
- **2 August 2025:** Rules on notified bodies apply; GPAI model obligations apply.
- **2 August 2026:** Full obligations for high-risk AI systems apply; transparency obligations (Art. 50) apply.
- **2 August 2027:** Obligations apply for high-risk AI systems under Article 6(1) (AI systems embedded in products subject to third-party conformity assessment under Annex I legislation).
- **31 December 2030:** Compliance deadline for AI systems that are components of large-scale IT systems placed on the market or put into service before 2 August 2027.

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

- **2 August 2026:** Transparency obligations apply (same date as high-risk system obligations).

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
| | | | | `No change` / `Update needed` | |

---

## Claim-to-Source Register (Optional)

Use this section to map key claims in this document to primary legal or regulatory sources.

| Claim ID | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Notes |
|----------|---------------|-------------|---------------------|------|---------------|-------|
| | | `Regulation` / `Guideline` / `Authority statement` | | | YYYY-MM-DD | |

---
## Further Reading

- [EU AI Act — Full text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [AI Act — Application Dates (this toolkit)](application-dates.md)
- [European Commission — AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Compliance Checker (Future of Life Institute)](https://artificialintelligenceact.eu/)

---

*This document is provided for informational purposes only and does not constitute legal advice. Content may contain errors or become outdated as regulations evolve. Verify all information against [official sources](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) and seek qualified legal counsel before making compliance decisions. If you spot an issue, please [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues) or email contact@rdnordic.com.*

*Maintained by [R&D Nordic Consultancy](https://rdnordic.com). Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).*

