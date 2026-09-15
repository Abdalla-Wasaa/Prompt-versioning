# Changelog, afyaplus-logistics MCP

Completed challenge sketch; CHANGELOG.md is the authoritative release history.

## [Unreleased]

### Added
- Planned for 1.2.x: a dual-argument migration shim accepting `item` or
  `item_code` on `check_stock`, preserving existing calls and responses.

### Breaking
- Draft for 2.0.0 only: rename the required `check_stock` input `item` to
  `item_code`. Existing callers sending `item` would fail after removal.
- Migration: accept either name during 1.2.x for at least 30 days after the
  shim release, announce removal to partners, and check migrations before
  shipping 2.0.0. Require at least one name and reject conflicting values.
  Partners update their calls and cached schemas during this window.
- Neither the shim nor the breaking rename is implemented; the current
  server still requires `item` and reports 1.1.0.

## [1.1.0] - 2026-09-15

### Added
- `list_low_stock(clinic_id)` returns items below `reorder_level` and includes
  `mcp_version`; this is additive relative to the supplied Week 8 baseline.
- `version://current` returns `1.1.0`.

### Changed
- No existing arguments changed relative to the supplied Week 8 snippet.
- See CHANGELOG.md for the actual Week 6 compatibility discrepancy; this
  exercise is not a compatible replacement of that server.

## [1.0.0] - Week 6 baseline

### Added
- `check_stock`, `plan_delivery_route`, `get_delivery_eta`, and
  `clinics://directory` (the actual saved URI, called `clinics://list` in the lesson).
