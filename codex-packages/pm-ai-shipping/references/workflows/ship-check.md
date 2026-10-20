# Complete shipping review

Run a bounded, check-only review unless the user separately approves mutations.

1. Establish the mechanical subject: repository, requested area, change range, and working-tree state.
2. Inventory architecture, flow, permission, variable, and test-coverage documentation. Report missing or stale material; do not create or refresh files without approval.
3. Review correctness using `../frameworks/code-review/GUIDE.md`. Keep only findings with a supported obligation, feasible execution, concrete contradiction, observable consequence, and checked counterargument.
4. Review security and performance using the dedicated safe workflow references. Run them serially in the current session unless the user explicitly approves delegation.
5. Propose an independent unsteered review when it would materially improve confidence. Do not start another session, model, or agent without explicit approval.
6. Build a test-coverage map that distinguishes existing verified tests, proposed tests, manual or live guards, and unverified rules. Do not claim tests ran unless execution evidence exists.
7. Return the shipping packet in the conversation: documentation inventory, review scope, surviving findings, coverage gaps, launch blockers, provenance, and recommended next actions.

If the user wants durable documentation, agent-instruction changes, reports, tests, or fixes, name the exact files and ask for approval before writing them.
