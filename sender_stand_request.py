# sender_stand_request.py

import requests
import configuration
import data

def post_new_user(body):
    """Создание нового пользователя"""
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_user)

def post_new_kit(auth_token, kit_body):
    """Создание набора с токеном авторизации"""
    # Заголовки с токеном создаем внутри функции
    headers_with_auth = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=headers_with_auth)