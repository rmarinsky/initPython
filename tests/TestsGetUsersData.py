import json

import pytest

from inn.reqres.UsersController import UsersController
from inn.reqres.UsersFilter import UsersFilter


@pytest.fixture
def users():
    return UsersController()


def test_second_users_page(users):
    resp = users.get_users_on_page(2)

    target_users_list = __get_users_list_from__(resp)

    actual_list = UsersFilter(target_users_list).get_users_in_range(6, 10)

    assert actual_list == ['Byron Fields', 'Lindsay Ferguson', 'Michael Lawson', 'Tobias Funke']


def test_first_users_page(users):
    resp = users.get_users_on_page(1)

    target_users_list = __get_users_list_from__(resp)

    actual_list = UsersFilter(target_users_list).get_users_in_range(6, 10)

    assert actual_list == ['Tracey Ramos']


def test_for_negative_range(users):
    resp = users.get_users_on_page(1)

    target_users_list = __get_users_list_from__(resp)

    actual_list = UsersFilter(target_users_list).get_users_in_range(-10, 0)

    assert actual_list == []


def test_over_of_range(users):
    resp = users.get_users_on_page(1)

    target_users_list = __get_users_list_from__(resp)

    actual_list = UsersFilter(target_users_list).get_users_in_range(10000, 20000)

    assert actual_list == []


def __get_users_list_from__(response):
    json_object = json.loads(response.text)
    return json_object['data']
