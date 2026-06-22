# data.py

# Заголовки без токена (для создания пользователя)
headers_user = {
    "Content-Type": "application/json"
}

# Данные пользователя
user_body = {
    "firstName": "Ева",
    "phone": "+79991553889",
    "address": "г. Казань, ул. Пушкина, д. 10"
}

# ===== 11 ВАРИАНТОВ KIT_BODY =====

# 1. 1 символ
kit_body_1 = {"name": "a"}

# 2. 511 символов (длинное имя)
kit_body_2 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

# 3. Пустое имя
kit_body_3 = {"name": ""}

# 4. 512 символов
kit_body_4 = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

# 5. Английское имя
kit_body_5 = {"name": "QWErty"}

# 6. Русское имя
kit_body_6 = {"name": "Мария"}

# 7. Спецсимволы
kit_body_7 = {"name": "№%@,"}

# 8. С пробелами
kit_body_8 = {"name": " Человек и КО "}

# 9. Только цифры
kit_body_9 = {"name": "123"}

# 10. Пустой словарь
kit_body_10 = {}

# 11. Число вместо строки
kit_body_11 = {"name": 123}