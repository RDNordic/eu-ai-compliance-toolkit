# Article 50 Transparency Obligations

> **Last updated:** 2026-08-18
>
> Covers Article 50 of Regulation (EU) 2024/1689 (EU AI Act), as amended by Regulation (EU) 2026/1744 (Digital Omnibus on AI).

---

## Status: In Force Now

**Article 50 has applied since 2 August 2026.** It was **not** deferred by the Digital Omnibus. The Omnibus pushed the high-risk obligations out to December 2027 and August 2028, but left the general application date and the transparency duties where they were.

If your organisation stood down on the strength of "the AI Act was delayed", this is the obligation you are now behind on. It is live, it applies across every risk tier, and it reaches a large population of ordinary products that are nowhere near high-risk.

> One grace period survives: machine-readable **marking** of synthetic content (paragraph 2) has until **2 December 2026** for systems already on the market before 2 August 2026. Everything else applies now. See [Timing](#timing-and-the-one-grace-period) below.

---

## Who This Catches

Article 50 is easy to underestimate because it does not depend on high-risk classification. It bites on function, not tier:

- you run a **chatbot** or any AI that talks to people
- you **generate or manipulate** audio, images, video, or text
- you run **emotion recognition** or **biometric categorisation**
- you produce **deep fakes**, or AI text **published to inform the public**

A "minimal risk" self-assessment does not remove any of this.

---

## The Four Obligations, By Who Bears Them

This is the first thing teams get wrong. **Paragraphs 1 and 2 are provider duties. Paragraphs 3 and 4 are deployer duties.** An organisation that builds and runs its own system bears both sets.

| Para | Duty holder | Obligation | Core exception |
|------|-------------|------------|----------------|
| **50(1)** | **Provider** | AI systems intended to interact directly with people must inform them they are interacting with an AI | Where it is obvious to a reasonably well-informed, observant, and circumspect person; law enforcement uses |
| **50(2)** | **Provider** | Synthetic audio, image, video, or text output must be marked in a machine-readable format and detectable as artificially generated or manipulated | Assistive or standard-editing functions that do not substantially alter the input; law enforcement uses |
| **50(3)** | **Deployer** | People exposed to an emotion recognition or biometric categorisation system must be told it is operating, and the data handled per GDPR | Permitted law enforcement uses |
| **50(4)** | **Deployer** | Deep fakes must be disclosed as artificially generated or manipulated; AI text published to inform the public on matters of public interest must be disclosed | Artistic or creative works (limited disclosure); human editorial review with a responsible person; law enforcement uses |

> **Provider and deployer are AI Act roles, not job titles.** If you fine-tune or rebrand a system, or put it into service under your own name, you may be the provider even though you bought the engine from someone else. See [`obligations-by-role.md`](obligations-by-role.md).

---

## Each Obligation In Detail

### 50(1) - Disclosing AI interaction (provider)

Providers must design systems that interact directly with people so those people are informed they are dealing with an AI, **unless it is obvious** from the point of view of a reasonably well-informed, observant, and circumspect person in the circumstances.

- Applies to the classic customer-service chatbot, voice assistants, and any conversational interface.
- The disclosure duty is on the **provider**, built into the system's design. A deployer who simply switches on a compliant product is not the one carrying 50(1), though it may carry its own contractual and 50(4) duties.
- **Do not lean on the "obvious" exception.** See [the trap](#the-obvious-from-context-trap).

### 50(2) - Marking synthetic content (provider)

Providers of systems, including general-purpose AI systems, that generate synthetic audio, image, video, or text must ensure the output is:

- **marked in a machine-readable format**, and
- **detectable as artificially generated or manipulated**.

The solution must be effective, interoperable, robust, and reliable "as far as is technically feasible", taking account of content type, cost, and the state of the art reflected in relevant standards.

**Exception:** systems performing an assistive function for standard editing, or that do not substantially alter the input data or its semantics. A grammar corrector is not caught; a system that generates a photorealistic image from a prompt is.

This is the paragraph with the grace period. See [Timing](#timing-and-the-one-grace-period).

### 50(3) - Emotion recognition and biometric categorisation (deployer)

Deployers must inform the people exposed to an emotion recognition or biometric categorisation system that it is operating, and must process the personal data in line with GDPR, the EUDPR, and the Law Enforcement Directive as applicable.

- Note the overlap with Article 5: emotion recognition in **workplaces and education** is *prohibited* outright (with narrow medical and safety exceptions), so 50(3) governs the permitted contexts that remain.
- This is a GDPR processing operation as well as an AI Act disclosure. The two duties run together.

### 50(4) - Deep fakes and public-interest text (deployer)

Two distinct duties in one paragraph:

- **Deep fakes:** deployers of a system that generates or manipulates image, audio, or video constituting a deep fake must disclose that it is artificially generated or manipulated. Where the content is evidently artistic, creative, satirical, or fictional, disclosure is limited to a form that does not spoil the work.
- **Public-interest text:** deployers of a system generating or manipulating text **published to inform the public on matters of public interest** must disclose the AI generation, **unless** the content underwent human review or editorial control and a natural or legal person holds editorial responsibility.

The editorial-responsibility carve-out is the one that matters for newsrooms and publishers: a human editor in the loop, accountable for the output, lifts the disclosure duty.

---

## Timing And The One Grace Period

| Obligation | Applies from |
|------------|-------------|
| 50(1) interaction disclosure | **2 August 2026** |
| 50(2) marking, systems placed on the market on or after 2 August 2026 | **2 August 2026** |
| 50(2) marking, systems already on the market before 2 August 2026 | **2 December 2026** (grace period, via new Art. 111(4)) |
| 50(3) and 50(4) | **2 August 2026** |

The grace period is narrow: it covers only the **machine-readable marking** duty in 50(2), and only for systems already on the market before the application date. The Omnibus delivered it as a transitional provision inserted into Article 111, not as a change to Article 50 itself.

**50(5) sets the moment of disclosure:** the information in paragraphs 1 to 4 must be given "in a clear and distinguishable manner at the latest at the time of the first interaction or exposure", and must meet applicable accessibility requirements. A disclosure buried in a terms-of-service document the user never opens does not satisfy this.

---

## The "Obvious From Context" Trap

The 50(1) exception applies where AI interaction is obvious to a "reasonably well-informed, observant and circumspect" person. Two cautions:

1. **The standard is objective, not "obvious to us".** The reference person is reasonably attentive, not an expert, and not your product team. As voice synthesis and conversational quality improve, the set of interactions that are genuinely "obvious" shrinks.
2. **It only covers 50(1).** There is no equivalent "obvious" exception in 50(2), 50(3), or 50(4). Synthetic content still needs marking even if a viewer might suspect it is AI.

Treating the exception as a default is the most likely way to end up non-compliant on paragraph 1. Where there is doubt, disclose.

---

## What The 2026 Omnibus Changed

Very little, and that is the point.

- **Only paragraph 7 was amended.** Regulation (EU) 2026/1744 replaced Art. 50(7), which concerns the AI Office and Commission encouraging codes of practice on detection, marking, and labelling. The Commission may now adopt an implementing act specifying common rules if it judges a code of practice inadequate. This is a governance provision; it does not change what providers and deployers must do under paragraphs 1 to 6.
- **The substantive duties in 50(1) to 50(6) were untouched.**
- **A grace period was added** for pre-existing systems' marking obligation, via Art. 111(4), running to 2 December 2026.

If you built an Article 50 readiness plan before July 2026, it is still substantially correct. Only the marking grace period and the codes-of-practice mechanism moved.

---

## Penalties

Article 50 breaches sit in the middle enforcement tier. Under **Art. 99(4)(g)**, non-compliance with the transparency obligations for providers and deployers under Article 50 is subject to administrative fines of up to:

> **EUR 15 000 000, or 3% of total worldwide annual turnover for the preceding financial year, whichever is higher.**

For context, the tiers are:

| Tier | Applies to | Maximum |
|------|-----------|---------|
| Art. 99(3) | Prohibited practices (Art. 5) | EUR 35M or 7% |
| **Art. 99(4)** | **Operator obligations including Art. 50** | **EUR 15M or 3%** |
| Art. 99(5) | Incorrect/misleading information to authorities | EUR 7.5M or 1% |

SMEs and start-ups are capped at the **lower** of the fixed sum and the percentage (Art. 99(6)). The 2026 Omnibus extended the same lower-of treatment to **small mid-cap** companies.

Penalties are set and applied by Member States, so national implementing law governs the actual figures and process.

---

## Practical Compliance Checklist

Work through this per system, recording evidence as you go.

- [ ] **Does this system interact directly with people?** If yes, is AI interaction disclosed clearly, at or before first interaction, accessibly? (50(1))
- [ ] **Does it generate synthetic audio, image, video, or text?** If yes, is the output machine-readable-marked and detectable as AI-generated? Is your solution defensible against "technically feasible" and "state of the art"? (50(2))
- [ ] **Was this system on the market before 2 August 2026?** If yes, the marking duty has until 2 December 2026; if no, it applies now. (Art. 111(4))
- [ ] **Does it do emotion recognition or biometric categorisation?** First confirm it is not prohibited under Art. 5 (workplace, education). If permitted, are exposed people informed, and is the GDPR basis documented? (50(3))
- [ ] **Does it produce deep fakes or public-interest text?** Is generation disclosed? For text, is there human editorial review with a named responsible person? (50(4))
- [ ] **Is disclosure clear and distinguishable, at latest at first interaction or exposure, and accessible?** (50(5))
- [ ] **Have you confirmed your role** (provider vs deployer) for each duty? A single organisation often bears both.
- [ ] **Is the assessment documented?** Article 50 has no registration requirement, but you will want the reasoning on file for a regulator or a buyer's due-diligence questionnaire.

---

## Common Scenarios

| Scenario | Which duty | What it means |
|----------|-----------|---------------|
| Customer-service chatbot | 50(1), provider | Tell users they are talking to an AI, at first interaction |
| Internal HR chatbot answering policy questions | 50(1); check Annex III | Interaction disclosure now; may also be high-risk if it shapes employment decisions (deferred to Dec 2027) |
| Marketing images generated by a text-to-image tool | 50(2), provider of the tool + 50(4) if deep fake | Tool must mark output; deployer discloses if the image is a deep fake of a real person |
| AI-drafted news article | 50(4), deployer | Disclose AI generation, unless a human editor holds editorial responsibility |
| Voice assistant with synthetic speech | 50(1) and 50(2) | Disclose AI interaction and mark synthetic audio |
| Sentiment analysis inferring customer emotion | 50(3) if emotion recognition; check Art. 5 | Not permitted in workplace/education; where permitted, inform exposed people |
| Grammar and spell checker | None (50(2) exception) | Assistive standard-editing function that does not substantially alter meaning |
| Satirical deep-fake video, clearly a parody | 50(4), limited | Disclose the existence of manipulation in a way that does not spoil the work |

---

## Relationship To Other Obligations

- **Article 50(6)** is explicit that these duties do not affect Chapter III (high-risk) requirements and are without prejudice to other transparency obligations in Union or national law. Article 50 is a floor, not a ceiling.
- **GDPR runs in parallel.** Disclosing AI interaction under 50(1) is not the same as providing Article 13/14 GDPR information; both may be required. Emotion recognition and biometric categorisation under 50(3) are GDPR processing operations needing a lawful basis and, usually, a DPIA. See [`../gdpr/lawful-basis-decision-tree.md`](../gdpr/lawful-basis-decision-tree.md).
- **Deep fakes and synthetic media** also intersect the new Article 5 prohibitions on non-consensual intimate material and CSAM. Marking a deep fake does not cure an otherwise prohibited generation.

---

## Claim-to-Source Register

| Claim ID | Claim Summary | Source Type | Article / Reference | Link | Last Verified | Notes |
|----------|---------------|-------------|---------------------|------|---------------|-------|
| A50-01 | Art. 50 applies from 2 August 2026 and was not deferred by the Omnibus | `Regulation` | 2024/1689 Art. 113; 2026/1744 Art. 1(40) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-08-18 | Verified against OJ text; deferral covers Ch. III Sections 1-3 only |
| A50-02 | 50(1) provider duty to disclose AI interaction, subject to the "obvious" exception | `Regulation` | 2024/1689 Art. 50(1) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | Verified against OJ text |
| A50-03 | 50(2) provider duty to mark synthetic content machine-readable and detectable | `Regulation` | 2024/1689 Art. 50(2) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | Assistive/standard-editing exception verified |
| A50-04 | 50(3) deployer duty to inform on emotion recognition / biometric categorisation | `Regulation` | 2024/1689 Art. 50(3) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | |
| A50-05 | 50(4) deployer duty to disclose deep fakes and public-interest text, with editorial carve-out | `Regulation` | 2024/1689 Art. 50(4) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | |
| A50-06 | 50(5) disclosure at latest at first interaction or exposure, accessible | `Regulation` | 2024/1689 Art. 50(5) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | |
| A50-07 | Only 50(7) was amended by the Omnibus | `Regulation` | 2026/1744 Art. 1(20) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-08-18 | Verified against OJ text |
| A50-08 | Marking grace period to 2 December 2026 for pre-existing systems | `Regulation` | 2026/1744 Art. 1(39)(b) inserting 2024/1689 Art. 111(4) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-08-18 | Verified against OJ text |
| A50-09 | Art. 50 breaches fined up to EUR 15M or 3% of worldwide turnover | `Regulation` | 2024/1689 Art. 99(4)(g) | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 2026-08-18 | Verified against OJ text |
| A50-10 | SME/start-up lower-of cap, extended to small mid-caps by the Omnibus | `Regulation` | 2024/1689 Art. 99(6); 2026/1744 Art. 1(38)(c) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | 2026-08-18 | Verified against OJ text |

---

## Verification Note

> **Primary-source verified, 2026-08-18.** Article 50 and Article 99 text checked against the Official Journal text of Regulation (EU) 2024/1689. Amendments checked against Regulation (EU) 2026/1744 (CELEX 32026R1744): Art. 1(20) amending Art. 50(7), Art. 1(39)(b) inserting Art. 111(4), and Art. 1(38)(c) on the small mid-cap fine cap.
>
> Retrieval note: EUR-Lex web pages return HTTP 202 with an empty body to automated clients. Use the Publications Office CELLAR endpoint: `curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744`.
>
> Open item to watch: Commission guidance and codes of practice on marking and labelling under Art. 50(7). Tracked in the regulatory watchlist in [`risk-classification.md`](risk-classification.md).

---

## Further Reading

- [EU AI Act, full text (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- [Regulation (EU) 2026/1744, Digital Omnibus on AI (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)
- [What the 2026 Omnibus changed (this toolkit)](omnibus-2026-changes.md)
- [Application dates (this toolkit)](application-dates.md)
- [Obligations by role (this toolkit)](obligations-by-role.md)
- [Risk classification (this toolkit)](risk-classification.md)

---

*This document is provided for informational purposes only and does not constitute legal advice. Verify against [official sources](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) and seek qualified legal counsel before making compliance decisions. If you spot an issue, please [open an issue](https://github.com/RDNordic/eu-ai-compliance-toolkit/issues/new?template=outdated-legal-content.yml) or email contact@rdnordic.com.*

*Maintained by [R&D Nordic Consultancy](https://rdnordic.com). Contributions welcome, see [CONTRIBUTING.md](../CONTRIBUTING.md).*
