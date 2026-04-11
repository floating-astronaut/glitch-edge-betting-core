# Glitch Betting Core

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![Checks](https://github.com/glitch-executor/glitch-betting-core/actions/workflows/python-tests.yml/badge.svg)
![Family](https://img.shields.io/badge/family-glitch%20engine-111827?logo=github&logoColor=white)
![Layer](https://img.shields.io/badge/layer-shared%20core-00c27a)
![Scope](https://img.shields.io/badge/scope-pricing%20%7C%20staking%20%7C%20odds-16a34a)

Shared pricing, staking, odds, and decision primitives for the Glitch family of sports intelligence engines.

Glitch Betting Core is the shared layer beneath the sport-specific repos: one place for the math, pricing helpers, stake sizing, shared payloads, and typed building blocks that should not drift.

## Glitch Engine Family

```mermaid
flowchart LR
    A[Glitch Betting Core] --> B[Glitch Cricket Engine]
    A --> C[Glitch NBA Engine]
    B --> D[Live Cricket Analysis]
    C --> E[Pregame NBA Intelligence]
```

## Why This Repo Exists

Branches are the wrong boundary for separating sports. Cricket and NBA need their own product identity, docs, and execution logic. But they also share a real core:

- odds conversion math
- probability and vig handling
- edge calculations
- stake sizing logic
- common result types
- later, shared reporting and alert utilities

Glitch Betting Core exists so those shared pieces can live in one place and be imported cleanly into each sport-specific repo.

## What Belongs Here

- bookmaker odds conversion and normalization helpers
- implied probability and no-vig math
- expected value and edge calculations
- bankroll / stake sizing primitives
- common dataclasses and typed result objects
- pure, reusable utilities with no sport-specific assumptions

## What Does Not Belong Here

- cricket-specific innings logic
- NBA-specific mapping logic
- provider-specific runtime glue that only one sport uses
- league-specific strategy rules
- environment secrets, models, state files, or runtime databases

## Architecture

```mermaid
flowchart LR
    A[glitch-cricket-engine] --> C[glitch-betting-core]
    B[glitch-nba-engine] --> C
    C --> D[odds math]
    C --> E[pricing]
    C --> F[staking]
    C --> G[types]
```

## Package Layout

```text
src/glitch_betting_core/
  odds.py        odds conversions and probability helpers
  pricing.py     no-vig and edge calculations
  staking.py     bankroll and Kelly-style helpers
  types.py       shared dataclasses for prices and decisions
  __init__.py    package exports

tests/
  test_odds.py
  test_pricing.py
  test_staking.py

docs/
  architecture.md
  roadmap.md
  adoption.md
```

## Quick Start

### 1. Install locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

### 2. Run tests

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

### 3. Use in another project

```python
from glitch_betting_core.odds import american_to_probability
from glitch_betting_core.pricing import edge_percent
from glitch_betting_core.staking import capped_kelly_fraction
```

## Example

```python
from glitch_betting_core.odds import decimal_to_probability
from glitch_betting_core.pricing import edge_percent

market_prob = decimal_to_probability(2.10)
model_prob = 0.54
print(edge_percent(model_prob, market_prob))
```

## Docs

- [Architecture](docs/architecture.md)
- [Roadmap](docs/roadmap.md)
- [Adoption Guide](docs/adoption.md)

## Project Family

This repository is part of the Glitch engine family:

- [Glitch Betting Core](https://github.com/glitch-executor/glitch-betting-core)
- [Glitch Cricket Engine](https://github.com/glitch-executor/glitch-cricket-engine)
- [Glitch NBA Engine](https://github.com/glitch-executor/glitch-nba-engine)

GitHub-ready social preview assets are included at `assets/social-preview.png` and `assets/social-preview.svg` for repo settings, link previews, or launch posts.

## Branding and Attribution

Glitch Betting Core is part of the original Glitch project family.

For forks and downstream distributions:
- keep `LICENSE`
- keep `NOTICE`
- preserve original attribution in a visible and reasonable way

Apache 2.0 allows broad reuse, but it does not grant trademark rights beyond what the license expressly allows.

## License

Released under Apache License 2.0.

See:
- [LICENSE](LICENSE)
- [NOTICE](NOTICE)
- [AUTHORS.md](AUTHORS.md)
