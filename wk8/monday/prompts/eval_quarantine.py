"""Evaluate recorded responses, allowing at most 5% explicitly quarantined cases."""
import json
from pathlib import Path

from eval_prompts import load_fixture, load_jsonl, load_pinned_prompt, score_case

BASE_DIR = Path(__file__).resolve().parent
MAX_QUAR_RATE = 0.05


def evaluate(rows, predictions, quarantine):
    ids = {row['id'] for row in rows}
    if not rows or len(ids) != len(rows) or not quarantine.issubset(ids):
        raise ValueError('Golden cases must be nonempty and unique; quarantine IDs must exist')
    active_fail = quar_fail = 0
    for row in rows:
        ok = score_case(predictions[row['id']], row)
        if row['id'] in quarantine:
            quar_fail += int(not ok)
        else:
            active_fail += int(not ok)
    rate = len(quarantine) / len(rows)
    print(f'n={len(rows)} active_fail={active_fail} quarantined={len(quarantine)} '
          f'quar_fail={quar_fail} quar_rate={rate:.3f}')
    return int(active_fail > 0 or rate > MAX_QUAR_RATE)


def main():
    version, _, sha = load_pinned_prompt()
    fixture = load_fixture(sha)
    rows = load_jsonl(BASE_DIR / 'evals/golden.jsonl')
    quarantine = set(json.loads((BASE_DIR / 'fixtures/quarantine.json').read_text()))
    print(f'prompt_version={version} prompt_sha256={sha}')
    return evaluate(rows, fixture['by_id'], quarantine)


if __name__ == '__main__':
    raise SystemExit(main())
