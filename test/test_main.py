from app.main import calc

CALC_ANSWER = 3


def test_calc():
    assert calc() == CALC_ANSWER
