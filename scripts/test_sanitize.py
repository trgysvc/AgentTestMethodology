#!/usr/bin/env python3
"""Self-test for sanitize_and_publish.py with FAKE values — safe to run anywhere, no real data.

    python3 scripts/test_sanitize.py
"""
import os
import sys

os.environ.update({
    "AGENTTEST_REPO_ROOT": "/Users/fakeuser/Developer/FakeRepo",
    "AGENTTEST_HOME_DIR": "/Users/fakeuser",
    "AGENTTEST_REAL_EMAIL": "fake.person@example.org",
    "AGENTTEST_REAL_PHONE": "+905551234567",
})
sys.path.insert(0, os.path.dirname(__file__))
import sanitize_and_publish as sp  # noqa: E402

failures = []


def check(name, text, must_not_contain):
    out = sp.sanitize(text)
    for needle in must_not_contain:
        if needle in out:
            failures.append(f"{name}: {needle!r} survived in {out!r}")


check("phone, as configured", 'recipient "+905551234567"', ["905551234567"])
check("phone, messaging URL without plus", "whatsapp://send?phone=905551234567&text=hi", ["905551234567"])
check("phone, national form", "ara 05551234567 numarasını", ["5551234567"])
check("phone, spaced", "Numara: +90 555 123 45 67", ["555 123 45 67"])
check("email", "to fake.person@example.org", ["fake.person"])
check("path, JSON-escaped", '"path":"\\/Users\\/fakeuser\\/Developer\\/FakeRepo\\/a.md"', ["fakeuser", "FakeRepo"])
check("username in prose", "Kullanıcı adı: fakeuser", ["fakeuser"])

if failures:
    print("\n".join(failures))
    raise SystemExit(1)
print("sanitize self-test: all checks passed")
