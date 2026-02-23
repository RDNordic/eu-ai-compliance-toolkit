# GDPR Lawful Basis Decision Tree for AI/ML Processing

> **Last updated:** February 2026
>
> This document provides a practical decision tree for selecting a lawful basis under the GDPR (Regulation (EU) 2016/679) when processing personal data for AI and machine learning purposes. Always refer to the [official GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and relevant supervisory authority guidance.
>
> **Jurisdictional note:** This guidance is based on the EU GDPR, which also applies in the EEA (Norway, Iceland, Liechtenstein). The UK GDPR is largely aligned but may diverge — UK-specific references are marked. Some GDPR provisions (e.g. conditions for employment processing, age of consent for children, public interest processing) allow national variation. Always check your Member State's implementing legislation.

---

## Overview

Any processing of personal data for AI/ML requires a valid lawful basis under **Article 6(1) GDPR**. Where special category data is involved, an additional condition under **Article 9(2)** must be met.

AI/ML processing often involves multiple stages — data collection, training, inference, and ongoing monitoring — and each stage may require its own lawful basis analysis.

---

## The Six Lawful Bases at a Glance

| Lawful Basis | Article | Typical AI/ML Relevance |
|-------------|---------|------------------------|
| **Consent** | 6(1)(a) | User-facing AI features where genuine choice exists |
| **Contract** | 6(1)(b) | AI processing necessary to deliver a contracted service |
| **Legal obligation** | 6(1)(c) | AI used to meet regulatory requirements (e.g. fraud detection mandated by law) |
| **Vital interests** | 6(1)(d) | Rare — emergency medical AI where consent is impossible |
| **Public task** | 6(1)(e) | Public sector AI carried out in the public interest or official authority |
| **Legitimate interests** | 6(1)(f) | Most common for private sector AI — requires balancing test |

---

## Decision Tree

Work through each step below to identify candidate bases, then select the one most appropriate to your specific processing activity. The GDPR does not establish a hierarchy among lawful bases — this structured analysis is an aid to thorough assessment, not a priority ranking. Document why alternative bases were considered and rejected.

### Step 1: Is the processing necessary to perform a contract with the data subject?

```
Does the AI processing directly deliver a service
the data subject has contracted for?
│
├── YES → Consider Article 6(1)(b) — Contract
│         ⚠ Must be genuinely necessary, not just useful
│         ⚠ Cannot rely on this for profiling beyond what
│           the contract requires
│         ⚠ The data subject must be a party to the contract
│
└── NO → Go to Step 2
```

**Examples where contract may apply:**
- AI-powered personalisation that is a core feature of a subscribed service
- Automated underwriting that the customer has specifically engaged
- AI translation service processing user-submitted text

**Examples where contract does NOT apply:**
- Training a model on customer data to improve the service generally
- Profiling users to serve targeted advertising alongside a contracted service
- Using customer data to develop new, unrelated products

---

### Step 2: Is the processing required by a legal obligation?

```
Is there a specific law or regulation that requires
you to carry out this processing?
│
├── YES → Consider Article 6(1)(c) — Legal obligation
│         ⚠ Must be a specific, concrete obligation
│         ⚠ The obligation must apply to the controller,
│           not just be a general industry practice
│
└── NO → Go to Step 3
```

**Examples:**
- AI-based transaction monitoring required under anti-money laundering regulations
- Automated reporting to regulators where required by statute
- AI-assisted identity verification required by Know Your Customer rules

---

### Step 3: Is this a public sector body carrying out its official functions?

```
Is the controller a public authority or body, and is the
processing necessary for a task carried out in the public
interest or in the exercise of official authority?
│
├── YES → Consider Article 6(1)(e) — Public task
│         ⚠ Must have a clear basis in law for the task
│         ⚠ Data subjects have the right to object
│         ⚠ Consider whether a DPIA is required
│
└── NO → Go to Step 4
```

**Examples:**
- AI-assisted diagnostics in a public healthcare system
- Predictive analytics for social services resource allocation
- AI tools in public education for identifying students at risk of dropping out

---

### Step 4: Is the processing necessary to protect vital interests?

```
Is the processing necessary to protect the vital interests
of the data subject or another person, where the data subject
is physically or legally incapable of giving consent?
│
├── YES → Consider Article 6(1)(d) — Vital interests
│         ⚠ Narrow scope — only applies to life-or-death
│           or serious health situations
│         ⚠ Cannot be used where consent could reasonably
│           be obtained
│         ⚠ Rarely applicable to planned AI systems
│
└── NO → Go to Step 5
```

**Examples:**
- Emergency triage AI where the patient is unconscious and cannot consent
- AI-assisted disaster response identifying individuals in immediate danger

> **Note:** This basis is rarely appropriate for AI systems designed and deployed in advance, as consent or another basis can usually be established during the design phase.

---

### Step 5: Can you obtain valid consent?

Consent for AI/ML processing is often **harder to achieve** than in other contexts. Consider whether all of the following conditions can be met:

```
Can you satisfy ALL of these requirements?
│
│  □ Freely given — genuine choice, no imbalance of power
│  □ Specific — the data subject understands exactly what
│    the AI will do with their data
│  □ Informed — clear explanation of the logic, significance,
│    and envisaged consequences of the processing
│  □ Unambiguous — a clear affirmative action
│  □ Withdrawable — the data subject can withdraw consent at
│    any time and this is technically feasible
│  □ Granular — separate consent for distinct processing purposes
│
├── YES to ALL → Consider Article 6(1)(a) — Consent
│                ⚠ Can the model be retrained/updated if
│                  consent is withdrawn? If not, consent
│                  may not be appropriate
│                ⚠ Consent is rarely suitable for employment
│                  contexts due to power imbalance
│
└── NO to ANY → Go to Step 6
```

**Common consent pitfalls in AI/ML:**
- Consent for training data cannot realistically be withdrawn once a model is trained — consider whether you can honour withdrawal
- Bundling consent for AI processing with consent for the primary service is not "freely given"
- Vague descriptions like "to improve our AI" are not "specific" or "informed"
- Employer–employee power imbalance generally invalidates consent in workplace AI

---

### Step 6: Legitimate Interests Assessment (LIA)

Legitimate interests (Article 6(1)(f)) is frequently relied upon for private sector AI/ML processing, but its suitability depends entirely on the outcome of the documented **three-part balancing test** below.

```
PART 1: Purpose test
Is there a legitimate interest being pursued?
│
├── NO → You have no lawful basis — do not process
│
└── YES → Proceed to Part 2
         Examples of legitimate interests:
         • Improving service quality through AI
         • Fraud detection and prevention
         • Network and information security
         • AI-driven business analytics
         • Product development and innovation

PART 2: Necessity test
Is the AI/ML processing necessary to achieve that interest?
│
├── NO → Can the interest be achieved with less
│        data or without AI? If so, do that instead
│
└── YES → Proceed to Part 3

PART 3: Balancing test
Do the data subjects' interests, rights, and freedoms
override the legitimate interest?
│
Consider:
│  • Nature of the data (sensitive? children's data?)
│  • Reasonable expectations of data subjects
│  • Nature of the relationship (direct customer vs third party)
│  • Impact on the individual (profiling? automated decisions?)
│  • Safeguards in place (pseudonymisation, access controls,
│    human review, opt-out mechanisms)
│  • Scale of processing
│
├── Interests DO override → You cannot rely on this basis.
│                           Reconsider your approach or seek
│                           another lawful basis
│
└── Interests do NOT override → Article 6(1)(f) applies
                                ⚠ Document the full LIA
                                ⚠ Data subjects have the
                                  right to object (Art. 21)
                                ⚠ Reassess if processing
                                  changes materially
```

---

## Special Category Data (Article 9)

If the AI/ML processing involves special category data (racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data for identification, health data, sex life or sexual orientation), you need **both**:

1. A lawful basis under Article 6(1), **and**
2. A condition under Article 9(2)

The most relevant Article 9(2) conditions for AI/ML are:

| Condition | When It Applies |
|-----------|----------------|
| **Explicit consent** — Art. 9(2)(a) | Data subject has given explicit consent for the specified purpose |
| **Employment and social security** — Art. 9(2)(b) | Processing necessary for employment obligations (must be authorised by law) |
| **Substantial public interest** — Art. 9(2)(g) | Must be authorised by Member State or EU law with appropriate safeguards |
| **Healthcare** — Art. 9(2)(h) | Processing necessary for medical diagnosis, treatment, or health system management |
| **Scientific research** — Art. 9(2)(j) | Processing necessary for scientific research with appropriate safeguards under Art. 89(1) |

> **Note:** The "legitimate interests" basis under Article 6(1)(f) does **not** have a corresponding condition in Article 9(2). If you are processing special category data, you cannot rely on legitimate interests alone.

---

## Automated Decision-Making (Article 22)

If the AI system makes decisions **solely based on automated processing** (including profiling) that produce **legal effects** or **similarly significant effects** on individuals, Article 22 applies additional restrictions.

```
Does the AI system make a decision about an individual?
│
├── NO → Article 22 does not apply (but other obligations still do)
│
└── YES →
    Is the decision based solely on automated processing?
    │
    ├── NO → Meaningful human involvement exists.
    │        Article 22 does not apply, but document
    │        the nature of human involvement
    │
    └── YES →
        Does the decision produce legal effects or
        similarly significantly affect the individual?
        │
        ├── NO → Article 22 does not apply
        │
        └── YES →
            The decision is prohibited UNLESS one of
            three exceptions applies:
            │
            ├── (a) Necessary for a contract
            ├── (b) Authorised by EU or Member State law
            └── (c) Based on explicit consent
            │
            In all cases, you must implement:
            • Right to obtain human intervention
            • Right to express their point of view
            • Right to contest the decision
            • Safeguards against discriminatory effects
```

> **Special category data restriction (Article 22(4)):** Where an automated decision under Art. 22(2)(a) (contract) or Art. 22(2)(c) (explicit consent) involves **special category data**, it is only permitted under Art. 9(2)(a) (explicit consent) or Art. 9(2)(g) (substantial public interest), with suitable safeguards for the data subject's rights and freedoms and legitimate interests.

**What counts as "similarly significant effects"?**
- Denial of credit, insurance, or a job application
- Significant changes in terms of a financial product
- Denial of access to public services
- Decisions affecting housing, education, or healthcare access

**What does NOT typically count:**
- Product recommendations
- Personalised content feeds (unless they materially affect access to information)
- Spam filtering

---

## Practical Guidance for Common AI/ML Scenarios

> **Legal caveat:** The examples below are indicative only. Final lawful basis selection depends on facts, power dynamics, sector rules, and national Member State law.

| Scenario | Likely Primary Basis | Key Considerations |
|----------|---------------------|--------------------|
| Training a model on customer data to improve service | Legitimate interests (6(1)(f)) | Document LIA; consider anonymisation of training data |
| AI chatbot handling customer enquiries | Contract (6(1)(b)) for service delivery; Legitimate interests (6(1)(f)) for improvement | Transparency obligations under AI Act also apply |
| Fraud detection model | Legal obligation (6(1)(c)) or Legitimate interests (6(1)(f)) | Depends on whether fraud monitoring is legally mandated |
| AI recruitment/CV screening | Member State law or Article 22(2) exception analysis required; do not assume consent is valid in employment contexts | High-risk under AI Act; DPIA required; Art. 22 likely applies. Use explicit legal analysis of Art. 22(2) exceptions and national employment law before deployment |
| AI diagnostic tool in healthcare | Public task (6(1)(e)) for public sector; Consent (6(1)(a)) or Legitimate interests (6(1)(f)) for private sector | Special category data — need Art. 9(2) condition (typically Art. 9(2)(h) for healthcare); DPIA required |
| Sentiment analysis on customer reviews | Legitimate interests (6(1)(f)) | If inferring emotions, check AI Act transparency requirements; if analysis could reveal special category data (political opinions, health indicators, etc.), an Art. 9(2) condition is also required |
| Training on publicly available data | Legitimate interests (6(1)(f)) | "Publicly available" does not mean "free to use" — still need lawful basis |

---

## When Is a DPIA Required?

A Data Protection Impact Assessment (DPIA) under Article 35 is **mandatory** for most AI/ML processing. Specifically, it is required when:

- The processing involves **systematic and extensive profiling** with significant effects on individuals (Art. 35(3)(a)) — this covers the majority of AI/ML use cases
- The processing involves **large-scale processing of special category data** (Art. 35(3)(b))
- The processing meets **two or more criteria** from the EDPB screening checklist (evaluation/scoring, automated decision-making, systematic monitoring, sensitive data, large scale, combined datasets, vulnerable data subjects, innovative use, preventing data subjects from exercising a right or using a service or contract)

> See the [DPIA template](../dpia/ai-dpia-template.md) in this toolkit for a structured AI-specific template.

---

## Erasure and the "Machine Unlearning" Challenge

The right to erasure (Art. 17) presents a practical challenge for all AI/ML processing, regardless of lawful basis:

- Under **consent**, withdrawal triggers an obligation to erase (Art. 17(1)(b)) — but personal data may already be embedded in a trained model
- Under **legitimate interests**, a successful objection under Art. 21 triggers erasure under Art. 17(1)(c)
- In both cases, true erasure may require model retraining, which can be costly and technically complex

When selecting your lawful basis, consider whether you can realistically honour erasure requests. Document your approach to erasure in the context of trained models, including whether retraining is feasible and what interim safeguards apply.

---

## Documentation Checklist

Whichever lawful basis you select, document the following:

- [ ] The specific lawful basis relied upon and reasoning for selection
- [ ] Why alternative bases were considered and rejected
- [ ] The specific purposes of the processing at each stage (collection, training, inference)
- [ ] For legitimate interests: the full three-part LIA
- [ ] For consent: how consent is collected, recorded, and withdrawal is handled
- [ ] Whether special category data is involved and the corresponding Art. 9(2) condition
- [ ] Whether Article 22 automated decision-making provisions apply
- [ ] How data subject rights will be facilitated (access, erasure, portability, objection)
- [ ] Whether a DPIA has been conducted or is required
- [ ] How erasure requests will be handled in the context of trained models

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

- [GDPR — Full text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Recruitment and Automated Decision-Making Annex (this toolkit)](recruitment-automated-decision-guidance.md)
- [ICO Guidance — Lawful basis for processing](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/) *(UK GDPR — largely aligned with EU GDPR but may diverge on specific points)*
- [ICO Guidance — AI and data protection](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/) *(UK GDPR)*
- [EDPB Guidelines on automated individual decision-making and profiling](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en)
- [Article 29 Working Party — Opinion on legitimate interests (WP217)](https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/index_en.htm)

---

*This document is provided for informational purposes only and does not constitute legal advice. Content may contain errors or become outdated as regulations evolve. Verify all information against [official sources](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and seek qualified legal counsel before making compliance decisions. If you spot an issue, please [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues) or email contact@rdnordic.com.*

*Maintained by [R&D Nordic Consultancy](https://rdnordic.com). Contributions welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).*

