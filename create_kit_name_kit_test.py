# create_kit_name_kit_test.py

import pytest
import requests
import configuration
from sender_stand_request import post_new_user, post_new_kit
from data import (
    user_body,
    kit_body_1, kit_body_2, kit_body_3, kit_body_4,
    kit_body_5, kit_body_6, kit_body_7, kit_body_8,
    kit_body_9, kit_body_10, kit_body_11
)


class TestCreateKit:

    @pytest.fixture
    def auth_token(self):
        """Фикстура: создает пользователя и возвращает токен"""
        response = post_new_user(user_body)
        assert response.status_code == 201, "Не удалось создать пользователя"

        auth_token = response.json().get("authToken")
        assert auth_token is not None, "Токен не получен"

        return auth_token

    # ===== ТЕСТ 1: kit_body_1 =====
    def test_1_create_kit_1_char(self, auth_token):
        """Тест 1: 1 символ -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_1)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_1["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 2: kit_body_2 =====
    def test_2_create_kit_511_chars(self, auth_token):
        """Тест 2: 511 символов -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_2)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_2["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 3: kit_body_3 =====
    def test_3_create_kit_empty_name(self, auth_token):
        """Тест 3: Пустое имя -> Ожидается 400"""
        response = post_new_kit(auth_token, kit_body_3)

        # Проверка статуса
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"

    # ===== ТЕСТ 4: kit_body_4 =====
    def test_4_create_kit_512_chars(self, auth_token):
        """Тест 4: 512 символов -> Ожидается 400"""
        response = post_new_kit(auth_token, kit_body_4)

        # Проверка статуса
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"

    # ===== ТЕСТ 5: kit_body_5 =====
    def test_5_create_kit_english_name(self, auth_token):
        """Тест 5: Английское имя -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_5)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_5["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 6: kit_body_6 =====
    def test_6_create_kit_russian_name(self, auth_token):
        """Тест 6: Русское имя -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_6)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_6["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 7: kit_body_7 =====
    def test_7_create_kit_special_chars(self, auth_token):
        """Тест 7: Спецсимволы -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_7)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_7["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 8: kit_body_8 =====
    def test_8_create_kit_with_spaces(self, auth_token):
        """Тест 8: С пробелами -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_8)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_8["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 9: kit_body_9 =====
    def test_9_create_kit_only_numbers(self, auth_token):
        """Тест 9: Только цифры -> Ожидается 201, name совпадает"""
        response = post_new_kit(auth_token, kit_body_9)

        # Проверка статуса
        assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"

        # Проверка, что поле name совпадает
        data = response.json()
        assert data.get("name") == kit_body_9["name"], "Имя в ответе не совпадает с запросом"
        assert data.get("id") is not None, "ID не получен"

    # ===== ТЕСТ 10: kit_body_10 =====
    def test_10_create_kit_empty_dict(self, auth_token):
        """Тест 10: Пустой словарь -> Ожидается 400"""
        response = post_new_kit(auth_token, kit_body_10)

        # Проверка статуса
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"

    # ===== ТЕСТ 11: kit_body_11 =====
    def test_11_create_kit_number_instead_string(self, auth_token):
        """Тест 11: Число вместо строки -> Ожидается 400"""
        response = post_new_kit(auth_token, kit_body_11)

        # Проверка статуса
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"