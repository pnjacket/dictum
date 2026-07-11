# Dictum — Positioning & Evidence

*Status: draft (working name "Dictum"). A product-agnostic assessment of where this standard sits in the 2025–2026 landscape, what it genuinely contributes, and what remains unproven. Written to be read by a skeptic: every claim is paired with its strongest counter-evidence.*

---

## 0. Thesis in one paragraph

Software has always been built from an incomplete picture, with the gaps filled by a human who could ask a colleague, read the code, or simply guess well. The build era we are entering removes the human from that loop: an AI agent builds directly from whatever the documentation says, and **fills every gap by guessing — silently, and at scale**. Dictum is a standard for the one thing that failure mode makes newly decisive: a documentation *set* complete enough to build a product **without guessing**. Its bet is not that any single idea inside it is novel — almost none are — but that the *composition* (a breadth×depth completeness bar, an owned-once contract-ID web, and a fidelity-staged Definition-of-Done) is the right shape for documentation whose primary reader is now a machine.

---

## 1. The problem is measurable, not rhetorical

The claim "AI guesses when the spec is incomplete" is now an empirical result, not an intuition:

- **Under-specification is the dominant failure mode.** A study of LLM hallucinations in practical code generation attributes **43.5% of hallucinations to *task-requirement conflicts*** (the model builds something other than what was intended) and a further **~24.6% to missing project/dependency context** — together roughly **two-thirds** of all hallucinations trace to under-specified intent or absent contextual contracts, not to raw model weakness (ACM TOSEM 2025, `10.1145/3728894`).
- **Models guess rather than ask.** On the HumanEvalComm benchmark, LLMs generate code in **>63% of ambiguous or underspecified scenarios without requesting clarification**, and cannot reliably resolve the ambiguity on their own (ClarifyCoder, arXiv 2504.16331; HumanEvalComm, ACM TOSEM `10.1145/3715109`).
- **Ambiguity has a price, and completeness buys it back.** Across 1,304 tasks and four ambiguity types, ambiguity cut Pass@1 by **an average 7.2 points (up to 31)** for every model tested (Orchid, arXiv 2604.21505). Repairing the ambiguity *before* generation recovers most of it: SpecFix lifted Pass@1 on repaired descriptions by **30.9%** (arXiv 2505.07270); ClarifyGPT raised GPT‑4 Pass@1 from **71% to 81%** (FSE 2024, `10.1145/3660810`).

The lever Dictum pulls — *remove ambiguity and supply missing contracts up front* — is precisely the lever these studies show works. Dictum's contribution is to make that lever **systematic and product-wide** rather than per-prompt.

> **Honest boundary.** These gains are measured on *function-level* benchmarks with an oracle answering the clarifying questions — not on whole-product builds. They are strong *directional* support for Dictum's completeness bet, not a demonstration at Dictum's scale. See §6.

---

## 2. Why now — and the part that is still a hypothesis

The idea of documentation as the single source of truth a system is built from is old, and it **failed** — for humans. The evidence for that failure is unambiguous:

- The living-documentation / specification-by-example movement's own originator, reviewing a decade of practice, concluded the single-spec-and-test-document ideal "**didn't really work out**": only ~12% kept specs as version-controlled text; 57% used a task tracker as the real source of truth (Adzic, 2020).
- Requirements **traceability decays in the field**: even with a dedicated structured field for it, only **~10% of issue reports referenced a commit** in an industrial telecom study (arXiv 2206.04462); a 2023 survey found traceability is "**mainly performed manually**," with maintenance ranked among the top adoption barriers (Ruiz, Hu & Dalpiaz, *Requirements Engineering* 2023, `10.1007/s00766-023-00408-9`).

The historical failure was a **maintenance-economics** failure: keeping a complete spec true to a moving codebase cost more human effort than teams would spend. Two things changed:

1. **The consumer changed.** When the builder is an AI, completeness pays off *immediately and measurably* (§1) instead of accruing as speculative future value — which flips the cost/benefit that doomed the human-era version.
2. **The maintainer can change.** AI can generate and reconcile the links a human would let rot.

**This second claim is where honesty is required, and where a lesser paper would overreach.** The evidence that AI can *maintain spec↔code fidelity* is the weakest in the entire literature:

- LLMs are **unreliable at verifying whether code satisfies a natural-language spec**: correct-code recognition runs **52–78%**, and — counterintuitively — elaborate multi-step verification prompting made GPT‑4o *dramatically worse* (52% → 11% on HumanEval), an "overcorrection" effect (arXiv 2508.12358; corroborated by Springer *ASE* `10.1007/s10515-026-00638-5`).

So the "why now" argument is strong for **build** and **clarification/repair**, and **not yet established** for **autonomous verification**. Dictum's design already respects this line: it **never asks the model to self-attest that code matches prose.** Fidelity is proven by the executable merge/release gates of the fidelity-staged Definition-of-Done (§5, claim e). The verification gap is not a hole in Dictum; it is the reason Dictum's proof-of-done is executable rather than conversational.

---

## 3. Where Dictum sits in the landscape

Three competitive sweeps (spec-driven-development tools; architecture/requirements standards; BDD, contract-testing and formal methods) place Dictum as follows:

- **The premise is now crowded.** GitHub Spec Kit, Amazon Kiro, Tessl, and OpenSpec all share "the spec is the source of truth an AI builds from." Dictum has no monopoly on that idea, and should not claim one.
- **The *shape* is not.** Those tools organize around a **per-feature workflow** (specify → plan → tasks). None imposes a **product-wide, breadth-of-concerns completeness bar** — and a widely-read practitioner review already faults them for *one-size-fits-all overhead* ("a sledgehammer to crack a nut"; Fowler/Böckeler, 2025). That criticism is the exact gap Dictum's calibration model targets.
- **The rigor neighbors are orthogonal.** Contract testing (Pact `can-i-deploy`) is a genuine blocking, environment-aware gate — but per *interface pair*, not a whole-product documentation DoD. BDD/Gherkin gates *per feature*. Formal methods verify *designs/code*, not documentation completeness. Each verifies a narrower unit than Dictum's whole-product bar.

---

## 4. What is genuinely Dictum's, and what is inherited

A credible positioning must not claim invented primitives. A provenance audit found Dictum's vocabulary is **mostly inherited**, and says so plainly:

| Element | Origin |
|---|---|
| "contract" (as a quality construct) | Meyer, *Design by Contract* (1992) |
| the 5-rung maturity ladder | SEI Capability Maturity Model (1993) |
| "separation of concerns" | Dijkstra, EWD447 (1974) |
| "owned once, referenced everywhere" | DRY — Hunt & Thomas, *The Pragmatic Programmer* (1999) |
| staged gates + dependency substitution | Continuous Delivery (Humble & Farley); test doubles (Meszaros) |

**What is Dictum's own is the *synthesis and coupling*:** binding a breadth-of-concerns completeness bar to a depth ladder; the cross-concern *owned-once ID web* (not the single-source principle, but the web); the *named "contract-grade" rung*; and the **environment fidelity map** layered over ordinary staged gates. Dictum does not need to have invented the bricks to have built something new — but it should credit the bricks (see the standard's *Prior art & influences*).

---

## 5. The five claims, each with its evidence and its honest limit

Legend: **●** genuine white space · **◐** partially anticipated · academic verdict in *italics*.

**(a) A "build-without-guessing" completeness bar. ◐**
*Strongly supported in direction.* The premise is shared by the SDD tools, but the *product-wide completeness* framing is Dictum's. Grounded by §1 (under-specification is ~two-thirds of hallucinations; disambiguation recovers 10–30%). *Limit:* the evidence is function-level, not whole-product.

**(b) Breadth×depth calibration; scope as the only lever; "contract-grade never weakens." ●**
*No competitor found occupies this,* and it directly answers the documented SDD overhead complaint. This is Dictum's strongest differentiation — and, being a design principle rather than an empirical result, its least externally *validated*.

**(c) Owned-once cross-concern contract-ID web. ●**
*Well-supported on benefit:* traceability made maintenance **24% faster and 50% more correct** in a controlled experiment (Mäder & Egyed, EMSE 2015); *more complete* traceability **lowered defect rate** across 24 projects (Rempel & Mäder, IEEE TSE 2016). *Counter-evidence Dictum must own:* traceability is manually created, costly, and **decays** (§2). Dictum's answer is that the web is authored and checked by tooling, not human diligence — an answer whose long-run decay rate is itself unproven.

**(d) Doc sections that map to maturity rungs. ◐**
Fixed section structures exist (ISO/IEC/IEEE 29148) and leveled maturity models exist (CMM; documentation maturity models since 2003); *the coupling of the two* is Dictum's. Thinly covered by academic work — the documentation-completeness/sufficiency literature is the least developed area found.

**(e) Whole-product, fidelity-staged Definition-of-Done (merge vs release gate + environment fidelity map). ●**
*Matched by nothing found* as a whole-product construct. Staged/promotion gates and dependency substitution are established practice, so the *novelty is narrow and specific*: the environment fidelity map over a documentation DoD. This claim also carries the verification-gap load (§2): it is deliberately executable, not model-attested.

---

## 6. What would falsify or weaken Dictum (the open questions)

A standard that only lists its strengths is marketing. The load-bearing uncertainties:

1. **Scale.** Do the function-level clarification/completeness gains hold at whole-product, multi-file scale — where missing dependency/context contracts dominate? Untested.
2. **AI-maintained traceability decay.** No study yet isolates whether AI-generated links actually close the historical ~10% decay gap, or merely relocate it.
3. **Autonomous verification.** The "AI keeps docs true to code" half of the why-now thesis is unproven and currently contradicted for prose-vs-code checking (§2). Dictum routes around it with executable gates; if that routing proves insufficient at scale, the maintenance economics that make docs-as-source viable are back in question.
4. **Adoption asymmetry.** Dictum is **pre-release and unproven at ecosystem scale**, while Spec Kit, ISO 42010/29148, arc42, C4, and Diátaxis have real adoption. Its validation to date is four deliberately-varied internal builds (a CLI, a multi-user web app, a real-time multi-tenant SaaS, and a client-only browser game), not industry use.

---

## 7. Position statement

Dictum is best understood not as a new idea but as a **new assembly for a new reader**. The individual moves — contracts, maturity levels, separation of concerns, single-source ownership, staged gates — are decades old and freely reimplementable; copyright protects only this text, not the method. What is timely is the coupling of those moves into a *completeness bar an AI can be held to*, at the exact moment the cost of an incomplete spec stopped being a human's problem to absorb and became a machine's problem to guess through. The evidence that incomplete specs make AI builds fail is strong and growing; the evidence that AI can *maintain* the completeness Dictum demands is not yet in. Dictum is a bet that the first fact makes the second worth solving — and a design honest enough to lean on executable proof, not model faith, until it is.

---

## References

**LLM code generation & specification quality**
- Assessing the Impact of Requirement Ambiguity on LLM Code Generation (Orchid), arXiv 2604.21505 (2026) — *recent preprint.*
- SpecFix: Repairing Ambiguous Specifications, arXiv 2505.07270 / IEEE Xplore 11334557.
- ClarifyGPT, FSE 2024, `10.1145/3660810` (arXiv 2310.10996).
- ClarifyCoder, arXiv 2504.16331; HumanEvalComm, ACM TOSEM `10.1145/3715109`.
- LLM Hallucinations in Practical Code Generation, ACM TOSEM `10.1145/3728894` (arXiv 2409.20550).
- On LLMs verifying code against NL specs, arXiv 2508.12358; Springer *ASE* `10.1007/s10515-026-00638-5`.

**Requirements traceability**
- Mäder & Egyed, *Empirical Software Engineering* 2015, `10.1007/s10664-014-9314-z`.
- Rempel & Mäder, *IEEE TSE* 2016, `10.1109/TSE.2016.2622264`.
- Tian et al., systematic mapping, *JSEP* 2021, arXiv 2108.02133.
- Ruiz, Hu & Dalpiaz, "Why don't we trace?", *Requirements Engineering* 2023, `10.1007/s00766-023-00408-9`.
- Fucci, Alegroth & Axelsson, industrial experience report, arXiv 2206.04462.

**Landscape & practice**
- Böckeler (Fowler), "Spec-driven development: 3 tools," martinfowler.com, 2025.
- GitHub Spec Kit (github.blog, 2025); Amazon Kiro (kiro.dev); Tessl; OpenSpec (Fission-AI).
- Adzic, "Specification by Example — 10 years later," gojko.net, 2020.

*This document is a positioning and literature assessment, not peer-reviewed research and not legal advice. Preprints (2025–2026 arXiv) are cited as such and may be unsettled.*
