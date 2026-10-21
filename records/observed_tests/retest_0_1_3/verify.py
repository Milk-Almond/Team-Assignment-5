#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
CASES = ('primary', 'posture_contrast', 'application_contrast', 'hype', 'insufficient')
print('UTC execution:', datetime.now(timezone.utc).isoformat())
p = subprocess.run([sys.executable, 'tools/check_frozen_core.py'], cwd=ROOT, capture_output=True, text=True)
print(p.stdout.strip())
assert p.returncode == 0
grades = [('Order of magnitude', 'Not established'), ('Widespread impact', 'Provisional'),
          ('Paradigm shift', 'Provisional'), ('Catalytic effect', 'Provisional'),
          ('Democratizing effect', 'Provisional'), ('Irreversibility', 'Not established')]
for case in CASES:
    path = RUN / case / 'raw_response.txt'
    p = subprocess.run([sys.executable, 'agents/team_promethean/validate_strict_response.py', str(path)], cwd=ROOT, capture_output=True, text=True)
    print(case, p.stdout.strip())
    assert p.returncode == 0
    prompt = (RUN / case / 'prompt.txt').read_bytes()
    assert prompt == (ROOT / 'work' / f'team_promethean_{case}_prompt.txt').read_bytes()
    assert (ROOT / 'agents/team_promethean/specialist_instructions.md').read_text() in prompt.decode()
    print(case, 'PROMPT_IDENTITY', hashlib.sha256(prompt).hexdigest())
    response = json.loads(path.read_text())
    assert response['agent']['version'] == '0.1.3-team'
    assert response['contrary_evidence_or_limitations']
    general = response['general_et_finding']
    if case == 'insufficient':
        assert general.startswith('Abstain — insufficient evidence')
        assert response['abstention_or_more_information_needed']
    else:
        assert 'Provisional Breakthrough' in general
        assert '2026-10-20' in general
        assert '2026-10-21' not in general
        for criterion, grade in grades:
            assert re.search(re.escape(criterion) + r'\s*[—–:-]\s*' + re.escape(grade), general, re.I), (case, criterion)
        assert 'moderate' in (general + response['confidence_and_uncertainty']).lower()
    print(case, 'ASSESSMENT_ANCHORS_PASS')
print('PASS: five observed structural/input/anchor checks. Read semantic_review.md for the separate reasoning assessment; no reliability rate is inferred.')
