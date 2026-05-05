# OpenFOAM Tips & References

## Standard solver reference

- Link: https://www.openfoam.com/documentation/user-guide/a-reference/a.1-standard-solvers
- Type: OpenFOAM solver reference
- Why it matters:
  - Useful when choosing between steady/transient, laminar/turbulent, compressible/incompressible solvers.

## Restarting from latest time

- Link: https://doc.cfd.direct/openfoam/user-guide-v13/controldict
- Type: OpenFOAM runtime-control tip
- Tip:
  - In `controlDict`, set `startFrom latestTime` to continue from the latest saved field.
- Why it matters:
  - Prevents wasting completed computation when a run is stopped midway.

## OpenFOAM-dev

- Link: https://github.com/OpenFOAM/OpenFOAM-dev
- Type: OpenFOAM Foundation development repository
- Why it matters:
  - Useful source-level reference for solver implementation, API changes, and advanced debugging.
  - Best categorized as a developer reference; beginners may still prefer release docs and tutorials first.
