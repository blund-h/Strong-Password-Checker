def test_smoke_pytest():
    assert 1+1==2

from password_rules import strong_password

def test_password_will_pass():
    assert strong_password("Katia123@") == "PASS"

def test_too_short():
    assert strong_password("Katia") == "FAIL"

def test_no_upper_or_lower():
    assert strong_password("katiaaa12@") == "FAIL"
    assert strong_password("KATIAAA12@") == "FAIL"

def test_no_digit():
    assert strong_password("Katiaaaa@@") == "FAIL"

def test_approved_special():
    assert strong_password("Katia12") == "FAIL"
    assert strong_password("Katia12{}") == "FAIL"
