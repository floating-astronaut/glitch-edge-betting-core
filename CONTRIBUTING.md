# Contributing

Thanks for contributing to Glitch Betting Core.

This repo is the shared foundation for the Glitch sports engine family. Changes here can affect multiple downstream repos, so the standard for clarity and compatibility is intentionally high.

## What To Contribute Here

Good candidates:
- odds conversion helpers
- pricing and no-vig math
- staking primitives
- reusable dataclasses and payload types
- pure utility functions with no sport-specific assumptions
- tests for shared logic

Please avoid putting these here:
- cricket-only match logic
- NBA-only mapping logic
- provider-specific runtime code that only one sport uses
- secrets, state files, logs, or local environment files

## Development Workflow

1. Fork or branch from `main`.
2. Keep changes small and scoped.
3. Add or update tests when shared behavior changes.
4. Run the unit suite locally:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p "test_*.py"
```

5. Open a pull request with a clear summary and downstream impact notes.

## Shared-Core Expectations

When changing exported helpers or dataclasses:
- preserve backward compatibility when practical
- note downstream repo impact in the PR
- avoid hidden behavioral changes
- prefer additive changes over breaking refactors

## Style

- prefer small pure functions
- keep dependencies light
- use explicit names over clever abstractions
- add tests for edge cases and numeric boundary behavior

## Attribution

Please keep the project's license, notice, and authorship files intact.
