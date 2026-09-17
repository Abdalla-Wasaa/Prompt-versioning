import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.check_mcp_health import EXPECTED_TOOLS, validate_health
from eval_quarantine import evaluate


def test_health_accepts_expected_contract():
    assert validate_health(EXPECTED_TOOLS, [SimpleNamespace(text='1.1.0')]) == '1.1.0'


@pytest.mark.parametrize('version', ['2.0.0', '1.0.0', 'garbage', ''])
def test_health_rejects_wrong_version(version):
    with pytest.raises(ValueError):
        validate_health(EXPECTED_TOOLS, [SimpleNamespace(text=version)])


def test_health_rejects_missing_tool():
    with pytest.raises(ValueError):
        validate_health({'check_stock'}, [SimpleNamespace(text='1.1.0')])


def cases(n):
    rows = [{'id': str(i), 'expected_urgency': 'high', 'must_include': ['urgent']} for i in range(n)]
    predictions = {r['id']: {'expected_urgency': 'high', 'text': 'urgent care'} for r in rows}
    return rows, predictions


def test_quarantine_scores_real_response_and_safety():
    rows, predictions = cases(20)
    assert evaluate(rows, predictions, set()) == 0
    predictions['0']['text'] = 'wait'
    assert evaluate(rows, predictions, set()) == 1
    assert evaluate(rows, predictions, {'0'}) == 0
    assert evaluate(rows, predictions, {'0', '1'}) == 1


def test_quarantine_rejects_wrong_label_and_missing_response():
    rows, predictions = cases(3)
    predictions['0']['expected_urgency'] = 'low'
    assert evaluate(rows, predictions, set()) == 1
    del predictions['0']
    with pytest.raises(KeyError):
        evaluate(rows, predictions, set())


@pytest.mark.parametrize('rows,quarantine', [([], set()), ([{'id': '0'}], {'missing'})])
def test_quarantine_rejects_invalid_inputs(rows, quarantine):
    with pytest.raises(ValueError):
        evaluate(rows, {}, quarantine)
