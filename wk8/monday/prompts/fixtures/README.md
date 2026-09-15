# Classroom evaluation fixtures

The responses for prompt 1.2.0 are hand-authored classroom stubs, permitted by
Step 2. They are not recorded model outputs and do not measure clinical quality.
They exercise the gate's label, required-text and forbidden-text checks.

Response files are selected by the SHA-256 of the loaded prompt text, so prompt
changes cannot silently reuse the baseline fixture. The 1.3.0-candidate prompt
omits the escalation instruction and intentionally has no response fixture:
its evaluation must fail closed. A missing fixture shows an unevaluated prompt,
not empirical proof that the candidate produces worse responses.

From wk8/monday/prompts:

```bash
python eval_prompts.py --threshold 0.85
PROMPT_VERSION=1.3.0-candidate python eval_prompts.py --threshold 0.85
```

The baseline should report 3/3 and exit 0. The candidate should report a missing
fixture and exit 1. Changing one golden expected_urgency should report 2/3 and
exit 1; restore the golden case after this experiment.
