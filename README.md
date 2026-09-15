# Prompt versioning lab

Week 8 Monday exercises for versioned triage prompts and logistics MCP.
The lab files are in `wk8/monday/prompts/`.

## Run the logistics MCP Inspector

Use Python 3.12 and an environment with `mcp[cli]` and `uv` installed.
Node.js/npm is also needed for the Inspector.

```bash
cd wk8/monday/prompts
mcp dev logistics_mcp_versioned.py
```

Open the printed URL and connect. Read `version://current` (expected `1.1.0`),
then call `list_low_stock` with `clinic_id` set to `kisumu-01`.
Expect ORS quantity 12 and paracetamol quantity 30.

See `CHANGELOG.md` for the released minor entry and draft 2.0.0 required-input
rename, and `mcp_version_notes.txt` for migration and compatibility notes.
The rename and dual-argument shim are documentation only.
The adjacent `logistics_mcp.py` is an unchanged Week 6 review artifact and
expects a different fixture format; use `logistics_mcp_versioned.py` here.

## Prompt exercise

`prompt_app.py` exposes the prompt version and hash via `/health`; its triage
response is a lab stub. Running the app requires FastAPI, Pydantic and Uvicorn.
`pin.json` records the expected prompt version and SHA-256, and
`check_prompt_pin_starter.py` compares them against a running health endpoint.

Environment files, logs, Python caches and virtual environments are excluded.
