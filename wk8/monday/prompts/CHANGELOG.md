# Changelog, afyaplus-logistics MCP

## [2.0.0] - Unreleased

### Breaking (planned for 2.0.0; not implemented)
- Draft only: rename `check_stock`'s required input `item` to `item_code`.
  Calls still sending `item` would fail validation after its removal, requiring
  a MAJOR bump to `2.0.0`.
- Current call: `check_stock(clinic_id="kisumu-01", item="ors")`.
  Proposed 2.0.0 call: `check_stock(clinic_id="kisumu-01", item_code="ors")`.
  Response fields remain unchanged in this proposal.

### Migration plan (draft; not implemented)
- In a future `1.2.x` release, provide a dual-argument shim accepting either
  `item` or `item_code` while preserving existing `item` calls and responses.
  Require at least one name; accept both when equal and reject conflicting
  values with a clear error.
- Deprecate `item` for at least 30 days after that shim is released, announce
  the removal date to partners, and allow agents to update their calls and
  refresh cached tool schemas on their own release schedules.
- Release `2.0.0` only after the window and partner migration checks; remove
  `item` and require `item_code`. Partners still using `item` must remain on
  `1.x` until migrated.
- The shipped lab server stays at `1.1.0` with required `item`; neither the shim
  nor the rename is shipped by this challenge.

## [1.1.0] - 2026-09-15

Compatibility: additive relative to the supplied Week 8 lab baseline only.
Partners using the actual Week 6 server must not treat this as a compatible
upgrade; see the compatibility limitation below.

### Added
- `list_low_stock(clinic_id)` lets callers retrieve items with quantities
  strictly below the clinic's `reorder_level`, including an `mcp_version`
  breadcrumb in the result. Items exactly at the threshold are excluded.
- Resource `version://current` lets agents and health probes read the server's
  application semver: `1.1.0`.

### Changed
- No existing input or response fields changed relative to the supplied Week 8
  snippet: `check_stock(clinic_id: str, item: str) -> dict` is preserved.
  Callers already using that contract need no argument changes.

### Compatibility limitation
This is the supplied Week 8 exercise's 1.1.0, not a compatible 1.1.0 upgrade
of this repository's actual Week 6 server. That server has
`check_stock(item: str) -> str`, additional tools, and a different fixture format.
Deploying this replacement to those clients would require 2.0.0 or a revised
implementation preserving all existing contracts.

## [1.0.0] - Week 6 baseline

### Added
- `check_stock(item)` reports stock across clinics as a JSON string.
- `plan_delivery_route(start_clinic_id)` plans a route between clinics.
- `get_delivery_eta(from_clinic_id, to_clinic_id)` estimates travel distance
  and delivery time.
- Resource `clinics://directory` exposes the clinic directory. This is the URI
  in the saved Week 6 server; the lesson example calls it `clinics://list`.

## Versioning rules

- MINOR: additive tools or optional fields that preserve existing contracts.
- MAJOR: rename or remove required fields, change existing input/output
  contracts, or remove tools/resources. Renaming `item` to `item_code`, for
  example, would break callers still sending `item`.
- PATCH: compatible corrections such as docstring typos.

The release date above records this lab's preparation date; 2026-07-28 is the
lesson's example date. The low-stock wording follows the implemented `<`
comparison rather than the lesson's inconsistent 'at or below' wording.
