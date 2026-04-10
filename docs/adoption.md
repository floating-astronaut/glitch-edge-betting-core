# Adoption Guide

## Good Candidates For Migration Into Core

- pure math
- reusable dataclasses
- bankroll logic
- odds normalization helpers
- shared tests for deterministic utilities

## Bad Candidates For Migration Into Core

- cricket innings simulation
- NBA feed mapping rules
- provider-specific auth and runtime glue
- bot orchestration loops

## Recommended Rollout

1. start by importing math helpers from this repo in both sports repos
2. move duplicate utilities here only after behavior is tested
3. keep sport-specific docs and strategy logic outside core
