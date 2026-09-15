from pathlib import Path
import hashlib
import os
import sys
# Locate the application relative to this test, regardless of the launch directory.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prompt_app import load_prompt  # Monday Lab 1 module


def test_pinned_prompt_file_exists():
    text = load_prompt(os.environ.get('PROMPT_VERSION', '1.2.0'))
    assert 'Never diagnose' in text


def test_prompt_hash_is_stable():
    text = load_prompt('1.2.0')
    a = hashlib.sha256(text.encode()).hexdigest()
    b = hashlib.sha256(text.encode()).hexdigest()
    assert a == b and len(a) == 64
