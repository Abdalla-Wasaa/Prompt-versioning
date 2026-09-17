# Branch protection checklist (configuration template)

This checklist is a proposal, not evidence that repository settings are enabled.

- Require pull requests and one approving review before merging.
- Require the actual GitHub Actions check names: `lint-test`, `eval`, and
  `mcp-health` (shown under workflow `ci`). Require all three because downstream
  jobs are skipped when an upstream job fails.
- Disable force pushes and branch deletion; review administrator bypass settings.
- Add CODEOWNERS only after confirming the responsible GitHub users or teams.
- Capture evidence from repository Settings and the actual PR checks after setup.

The quarantine audit uses hash-matched classroom responses and enforces a 5%
cap. The existing full golden evaluation still runs at 0.85; quarantine does
not bypass it. With three cases, quarantining even one case exceeds the cap.
