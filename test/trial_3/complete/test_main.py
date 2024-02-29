from app.trial_3.complete.main import User
import pytest

USER_NAME = "John"
INITIAL_AGE = 0
INITIAL_EMAIL = None

AGE = 20
EMAIL = "hogehoge@hoge.com"
PHONE_NUM = "090-1234-5678"


def test_init_user():
    user = User(USER_NAME, INITIAL_AGE)
    assert user.name == USER_NAME
    assert user.age == INITIAL_AGE
    assert user.email == INITIAL_EMAIL


def test_set_age():
    user = User(USER_NAME, INITIAL_AGE)
    user.set_age(AGE)
    assert user.age == AGE


def test_set_minus_age():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_age(-1)


def test_zero_age():
    user = User(USER_NAME, INITIAL_AGE)
    assert user.age == 0


def test_set_age_type():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(TypeError):
        user.set_age("20")


def test_set_email():
    user = User(USER_NAME, INITIAL_AGE)
    user.set_email(EMAIL)
    assert user.email == EMAIL


def test_set_email_none():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_email(None)


def test_set_not_email():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_email("hogehoge")


def test_set_email_type():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(TypeError):
        user.set_email(20)


def test_set_address():
    user = User(USER_NAME, INITIAL_AGE)
    user.set_address("address")
    assert user.address == "address"


def test_set_address_none():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_address(None)


def test_set_address_type():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(TypeError):
        user.set_address(20)


def test_set_phone_num():
    user = User(USER_NAME, INITIAL_AGE)
    user.set_phone_num(PHONE_NUM)
    assert user.phone_num == PHONE_NUM


def test_set_phone_none():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_phone_num(None)


def test_set_phone_num_type():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(TypeError):
        user.set_phone_num(20)


def test_set_not_phone_num():
    user = User(USER_NAME, INITIAL_AGE)
    with pytest.raises(ValueError):
        user.set_phone_num("hogehoge")
