import pytest
import requests
import configuration
from sender_stand_request import post_new_user, post_new_kit
from data import (
    user_body,
    kit_body_1_min_1_char, kit_body_2_max_511_chars, kit_body_3_empty_name, kit_body_4_512_chars,
    kit_body_5_english, kit_body_6_russian, kit_body_7_special_chars, kit_body_8_spaces,
    kit_body_9_only_numbers, kit_body_10_no_name, kit_body_11_number_instead_string
)


def positive_assert(auth_token, kit_body, expected_name=None):
    """Проверка успешного создания набора (ожидается 201)"""
    response = post_new_kit(auth_token, kit_body)

    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
    data = response.json()

    if expected_name is None:
        expected_name = kit_body["name"]

    assert data.get("name") == expected_name, "Имя в ответе не совпадает с запросом"
    assert data.get("id") is not None, "ID не получен"


def negative_assert(auth_token, kit_body):
    """Проверка негативного сценария (ожидается 400)"""
    response = post_new_kit(auth_token, kit_body)

    assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"


class TestCreateKit:

    @pytest.fixture
    def auth_token(self):
        """Предусловие тестирования: создание пользователя и получение токена"""
        response = post_new_user(user_body)
        assert response.status_code == 201, "Не удалось создать пользователя"

        auth_token = response.json().get("authToken")
        assert auth_token is not None, "Токен не получен"

        return auth_token

    # ПОЗИТИВНЫЕ ТЕСТЫ (ожидается 201, name совпадает)

    def test_1_create_kit_1_char(self, auth_token):
        """Допустимое количество символов (1)"""
        positive_assert(auth_token, kit_body_1_min_1_char)

    def test_2_create_kit_511_chars(self, auth_token):
        """Допустимое количество символов (511)"""
        positive_assert(auth_token, kit_body_2_max_511_chars)

    def test_5_create_kit_english_name(self, auth_token):
        """Разрешены английские буквы"""
        positive_assert(auth_token, kit_body_5_english_letters)

    def test_6_create_kit_russian_name(self, auth_token):
        """Разрешены русские буквы"""
        positive_assert(auth_token, kit_body_6_russian)

    def test_7_create_kit_special_chars(self, auth_token):
        """Разрешены спецсимволы"""
        positive_assert(auth_token, kit_body_7_special_chars)

    def test_8_create_kit_with_spaces(self, auth_token):
        """Разрешены пробелы"""
        positive_assert(auth_token, kit_body_8_spaces)

    def test_9_create_kit_only_numbers(self, auth_token):
        """Разрешены цифры"""
        positive_assert(auth_token, kit_body_9_only_numbers)

    # НЕГАТИВНЫЕ ТЕСТЫ (ожидается 400)

    def test_3_create_kit_empty_name(self, auth_token):
        """Количество символов меньше допустимого (0)"""
        negative_assert(auth_token, kit_body_3_empty_name)

    def test_4_create_kit_512_chars(self, auth_token):
        """Количество символов больше допустимого (512)"""
        negative_assert(auth_token, kit_body_4_512_chars)

    def test_10_create_kit_empty_dict(self, auth_token):
        """Параметр не передан в запросе"""
        negative_assert(auth_token, kit_body_10_no_name)

    def test_11_create_kit_number_instead_string(self, auth_token):
        """Передан другой тип параметра (число)"""
        negative_assert(auth_token, kit_body_11_number_instead_string)