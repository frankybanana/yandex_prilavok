# Заголовок для создания пользователя
headers_user = {
    "Content-Type": "application/json"
}

# Данные пользователя
user_body = {
    "firstName": "Ева",
    "phone": "+79991553889",
    "address": "г. Казань, ул. Пушкина, д. 10"
}

# Данные наборов

# Допустимое количество символов (1)
kit_body_1_min_1_char = {"name": "a"}

# Допустимое количество символов (511)
kit_body_2_max_511_chars = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

# Количество символов меньше допустимого (0)
kit_body_3_empty_name = {"name": ""}

# Количество символов больше допустимого (512)
kit_body_4_512_chars = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

# Разрешены английские буквы
kit_body_5_english = {"name": "QWErty"}

# Разрешены русские буквы
kit_body_6_russian = {"name": "Мария"}

# Разрешены спецсимволы
kit_body_7_special_chars = {"name": "№%@,"}

# Разрешены пробелы
kit_body_8_spaces = {"name": " Человек и КО "}

# Разрешены цифры
kit_body_9_only_numbers = {"name": "123"}

# Параметр не передан в запросе
kit_body_10_no_name = {}

# Передан другой тип параметра (число)
kit_body_11_number_instead_string = {"name": 123}