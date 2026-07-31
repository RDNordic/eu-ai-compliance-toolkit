# What the 2026 Digital Omnibus Changed

> **Last updated:** 2026-07-31
>
> Covers Regulation (EU) 2026/1744 of 8 July 2026, amending Regulations (EU) 2024/1689 (AI Act), (EU) 2018/1139 (civil aviation) and (EU) 2023/1230 (machinery). Published in the Official Journal on 24 July 2026, in force 27 July 2026.
>
> This is the first set of amendments to the AI Act since it was adopted.

---

## The One-Line Version

**High-risk obligations moved to December 2027. Transparency obligations did not move and bind on 2 August 2026.**

---

## The Trap

The reporting on this regulation has been dominated by the delay. The headline most teams have absorbed is some version of "the EU AI Act has been pushed back to 2027."

That is true for high-risk systems. It is not true for the obligation that is about to bind.

**Article 50 transparency duties apply from 2 August 2026 and were untouched by the Omnibus.** They apply across risk tiers. They catch a very large population of ordinary products:

- chatbots and conversational assistants must tell people they are talking to an AI system
- emotion recognition and biometric categorisation systems must inform the people subject to them
- deep fakes and synthetic media must be disclosed as artificially generated or manipulated
- AI-generated text published to inform the public must be disclosed, unless a human holds editorial responsibility

A company that classified its product as "limited risk, transparency only" and then stood down on the strength of the delay headline has misread the position. The delay gave that company nothing.

**If you do one thing after reading this page, check Article 50 against your product.**

---

## What Moved

| Obligation | Was | Now |
|---|---|---|
| Annex III stand-alone high-risk systems (Ch. III Sections 1-3) | 2 August 2026 | **2 December 2027** |
| Annex I embedded high-risk systems (Art. 6(1), Ch. III Sections 1-3) | 2 August 2027 | **2 August 2028** |
| Member State AI regulatory sandboxes, operational by | 2 August 2026 | **2 August 2027** |
| Art. 50(2) machine-readable marking, systems already on market before 2 Aug 2026 | 2 August 2026 | **2 December 2026** |
| New Art. 5 prohibitions (Art. 5(1)(ba), (bb), 5(1a), (1b)) | n/a | **2 December 2026** |
| AI Act Arts. 102-110 (amendments to other Union law) | 2 August 2026 | **27 July 2026** |

**The delay is narrower than the headline.** Art. 113(3)(c) as replaced defers **Chapter III, Sections 1, 2 and 3 only, and expressly excepts Article 6(5)**. Chapter III Section 4 (notified bodies) has applied since 2 August 2025. Chapter III **Section 5** (Arts. 40-49: standards, conformity assessment, certificates, registration) is **not** in the deferral list.

> **Flagged interpretation point.** On the face of the amended text, Section 5 falls under the general 2 August 2026 date even though the substantive obligations it supports are deferred. That has real consequences for conformity assessment and Art. 49 registration timing. This is a question for counsel, and one to watch for Commission guidance on. Do not treat it as settled either way.

The stated reason for the delay was implementation readiness rather than a change of policy: harmonised standards from CEN-CENELEC were not finished, national competent authorities had not all been designated, and the compliance tooling high-risk providers were expected to use did not exist yet.

That framing matters for how you should react. **The delay is schedule relief, not scope relief.** No high-risk requirement was removed. If you are mid-programme on an Annex III system, the sensible response is to keep building and use the extra time for evidence quality, not to stop.

---

## What Did Not Move

| Obligation | Date | Note |
|---|---|---|
| Prohibited practices (Art. 5) | 2 February 2025 | Already in force |
| AI literacy (Art. 4) | 2 February 2025 | Already in force |
| GPAI model obligations (Arts. 51-56) | 2 August 2025 | Already in force |
| Notified body framework | 2 August 2025 | Already in force |
| **General application date** | **2 August 2026** | Stands |
| **Art. 50 transparency** | **2 August 2026** | Stands, including AI-interaction disclosure |
| Art. 50(2) marking, systems placed on market on or after 2 Aug 2026 | 2 August 2026 | Only pre-existing systems got the grace period |

---

## What Else Changed

### Two new prohibitions

Article 5 gained two entries:

- AI systems that generate or manipulate **child sexual abuse material**
- AI systems that generate or manipulate **non-consensual sexual or intimate imagery**, including "nudifier" applications

Point (bb) is defined by reference to Article 2(c) and (e) of Directive 2011/93/EU, subject to any "without right" defence under national law.

**The scope rule in Art. 5(1a) is where the real work is.** For providers, placing on the market or putting into service is prohibited only where either:

1. that generation or manipulation is the **intended purpose** of the system; or
2. the system's **design, training, architecture, capabilities, or user-facing functionality** make it a **reasonably foreseeable and reproducible outcome without significant technical modification**, *and* the system lacks reasonable and adequate technical safety measures and other safeguards to reliably prevent it, accounting for reasonably foreseeable misuse, and to correct observed or reported misuse.

So a general-purpose image, video, or audio generator is not caught automatically. It is caught if safeguards are weak enough that the prohibited output is a foreseeable and reproducible result. The recitals say explicitly that the prohibition is not meant to stop providers developing the underlying technical capability.

**Practical read:** the compliance question is no longer only "what did we intend?" but "what will our system reliably refuse, and can we evidence that it corrects reported misuse?"

**Transitional deadline: 2 December 2026.**

This is worth attention beyond the obvious operators. If you provide a general-purpose image or video generation capability, the question is no longer only what you intend, but what your system will reproducibly do without meaningful modification, and whether your safeguards are adequate.

### Narrower "safety component" test

Three new paragraphs were inserted into Article 6:

- **Art. 6(1a):** AI used **solely** for non-safety-related aspects of user assistance, performance optimisation, service efficiency, automation, convenience, or quality control **does not qualify as a safety component**.
- **Art. 6(1b):** but AI whose failure or malfunction **would endanger health and safety** does qualify, notwithstanding 6(1a).
- **Art. 6(1c):** a product required to undergo third-party conformity assessment **solely** for non-health-and-safety risks, in particular radio spectrum or electromagnetic interference, does not satisfy the Art. 6(1)(b) condition.

**Re-run any classification that reached "high-risk" via the embedding route alone.** Some systems will drop out of the high-risk tier entirely.

Related, and structurally significant: **Annex I Section A point 1 was deleted** and **Regulation (EU) 2023/1230 on machinery was added to Annex I Section B**. Moving machinery from Section A to Section B changes which conformity-assessment regime applies to machinery-embedded AI.

### Bias detection and special-category data: Article 10(5) deleted, new Article 4a inserted

This one is widely described as "Article 10(5) was extended to deployers". That is not what the text does.

**Article 10(5) was deleted.** A new free-standing **Article 4a**, "Processing of special categories of personal data for bias detection and correction", was inserted in its place.

- **Art. 4a(1)** lets **providers of high-risk systems** process special categories of personal data where strictly necessary for bias detection and correction under Art. 10(2)(f) and (g), subject to **six cumulative conditions**: no less intrusive alternative including synthetic or anonymised data; technical limits on re-use plus state-of-the-art security and pseudonymisation; access controls and documentation; no transmission or access by other parties; deletion once bias is corrected or retention ends, whichever is first; and a recorded justification in the Art. 30 GDPR records of processing.
- **Art. 4a(2)** extends the same possibility to providers and deployers of **other** AI systems and models, and to **deployers** of high-risk systems, where strictly necessary to address bias likely to affect health and safety, negatively affect fundamental rights, or lead to prohibited discrimination, on all the same conditions.
- Art. 4a(2) states expressly that it **creates no obligation** to carry out bias detection and correction.

Why the distinction matters: this is now a standalone legal basis provision sitting alongside GDPR and the Law Enforcement Directive, not a data-governance sub-clause buried in the high-risk requirements. It is available to deployers who are not providers, and to systems that are not high-risk. If you are relying on it, document the six conditions explicitly.

See [`../gdpr/lawful-basis-decision-tree.md`](../gdpr/lawful-basis-decision-tree.md).

### Wider AI Office supervision

Article 75(1) was replaced. The AI Office is now **exclusively competent** for supervision and enforcement in relation to:

- AI systems based on GPAI models where the model and the system are developed by the **same provider, or by providers in the same undertaking**
- AI systems that constitute, or are integrated into, a Very Large Online Platform or Very Large Online Search Engine

with carve-outs for Annex I product-related systems, Annex III point 2 systems, systems provided by law enforcement, border management and financial institutions under Art. 74(6), and Annex III point 8 justice systems.

"Exclusively competent" is the operative phrase. If you build products on your own foundation models, this is not just wider oversight, it is a **change of regulator** for those systems, from your national market surveillance authority to the AI Office.

### Registration survived

**Article 49 was not amended at all.** The obligation to register systems in the EU database, including those self-assessed as **not** high-risk under Article 6(3), stands unchanged. Self-assessing out of high-risk does not mean you can stay invisible.

The reported "reduced administrative burden" was delivered differently: **Annex VIII, Section B, points 7 and 9 were deleted**, cutting the information a provider must supply at registration. If you built a registration data-collection process against the old Annex VIII, two fields have gone.

### SME relief

Simplifications previously available to SMEs were extended to small mid-cap companies.

---

## What To Do Now

**Everyone, this week:** check Article 50 against every user-facing AI feature you ship. Disclosure of AI interaction, synthetic content marking, emotion recognition and biometric categorisation notices. This binds 2 August 2026.

**Annex III high-risk builders:** keep going. Re-baseline the programme to 2 December 2027, and spend the recovered time on data governance evidence and human oversight design, which are the two areas where retrofitted documentation reads worst under scrutiny.

**Embedded / Annex I builders:** re-run classification against the narrowed safety-component test before assuming 2 August 2028 applies to you. You may be out of scope.

**Generative image and video providers:** assess against the new Article 5 prohibitions and document your safeguards ahead of 2 December 2026.

**Anyone who published an AI Act readiness plan before July 2026:** it now contains wrong dates. Reissue it.

---

## Sources And Verification Status

Compiled 2026-07-31 from six independent professional sources, which agree on every date and change recorded above:

- [Gibson Dunn, EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [Freshfields, EU AI Act unpacked #34: The final Digital Omnibus on AI](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/eu-ai-act-unpacked-34-the-final-digital-omnibus-on-ai-key-amendments-to-the-a-102nber)
- [Lewis Silkin, The Digital Omnibus on AI enters into force today](https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo)
- [Sidley, EU AI Act Transparency Obligations: Preparing for Compliance by 2 August 2026](https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/)
- [Skadden, AI Act State of Play](https://www.skadden.com/insights/publications/2026/05/ai-act-state-of-play)
- [Hunton, EU Digital Omnibus on AI Enters Into Force](https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force)

Primary source:

- [Regulation (EU) 2026/1744 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)

> **Verification status: primary-source verified, 2026-07-31.**
>
> Every amendment described on this page was checked against the Official Journal text of Regulation (EU) 2026/1744 (CELEX 32026R1744), retrieved from the EU Publications Office CELLAR endpoint, and against the Official Journal text of Regulation (EU) 2024/1689 as originally adopted for the "before" position.
>
> The secondary sources listed above were used to locate the amendments. Where they diverged from the enacted text, **the enacted text governs and this page follows it.** Two corrections were made on that basis:
>
> - the bias-detection change is a **deletion of Art. 10(5) and insertion of a new Art. 4a**, not an amendment extending Art. 10(5);
> - **Art. 49 was not amended**; the registration burden was reduced by deleting Annex VIII Section B points 7 and 9.
>
> The one genuinely open item is the Chapter III Section 5 interpretation question flagged above. It is tracked in the regulatory watchlist in [`risk-classification.md`](risk-classification.md).
>
> **Retrieval note for maintainers.** EUR-Lex web pages return HTTP 202 with an empty body to automated clients. The CELLAR content-negotiation endpoint works and is the reliable way to fetch EU legal texts programmatically:
>
> ```bash
> curl -H "Accept: application/xhtml+xml" http://publications.europa.eu/resource/celex/32026R1744
> ```

---

This document is informational and not legal advice.
