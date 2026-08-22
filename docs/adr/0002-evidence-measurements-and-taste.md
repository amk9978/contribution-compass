# ADR-0002: Evidence, measurements, and taste are separate

Status: Accepted

## Context

Contribution Compass must make opinionated recommendations without presenting curator judgment as
objective fact or pretending to have trained a recommendation model.

## Decision

Use four explicit layers:

```text
public evidence
→ normalized factual features
→ versioned measurements
→ versioned Taste Policy and personalized recommendations
```

Measurements preserve source, window, unit, sample size, coverage, and as-of time when applicable.
Missing evidence remains unknown. A Taste Policy applies hard floors before balancing normalized
signals into exactly three axes: Fit, Absorption, and Upside. Policy changes require regression
fixtures containing known-good, known-bad, and ambiguous repository judgments.

LLM inference is optional and cannot be required to collect evidence or reproduce deterministic
recommendations.

## Consequences

Recommendations can be opinionated, inspectable, and reproducible. Popularity cannot compensate
for a failed contribution-climate floor. Later inference can explain or extend results without
overwriting the factual record.
