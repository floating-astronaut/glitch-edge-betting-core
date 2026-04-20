# Architecture

## Purpose

This repository is the shared core for the Glitch betting engine family.

It is intentionally limited to reusable, sport-agnostic code:
- odds conversion
- pricing math
- stake sizing
- typed result objects

## Intended Adoption Pattern

- `glitch-edge-cricket-engine` imports shared math from here
- `glitch-edge-nba-engine` imports shared math from here
- sport-specific logic stays in sport-specific repos

## Design Rule

If a module requires league-specific context to make sense, it probably does not belong here.
