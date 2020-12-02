import pytest

from homework_06.counter import User


@pytest.fixture()
def reset_after_test():
    yield
    User.reset_instances_counter()


def test_get_created_zero_instances():
    assert User.get_created_instances() == 0


def test_reset_instances_counter():
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert user.get_created_instances() == 0


def test_get_created_non_zero_instances_from_class(reset_after_test):
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_get_created_non_zero_instances_from_object(reset_after_test):
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
