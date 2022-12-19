import pytest
from api import PetFriends
from settings import valid_email, valid_password, empty_email, empty_password, empty_auth_key, incorrect_auth_key
import os


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert "key" in result


def test_get_all_pets_with_valid_key(filter=""):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Запрашиваем полный список питомцев
    status, result = pf.get_list_of_pets(auth_key, filter)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert len(result["pets"]) > 0


def test_add_new_pet_valid_data(name="Булкаскорицей", animal_type="Пожирательвкуснях", age="1", pet_photo="images/mops.jpg"):
    """ Проверяем что можно добавить питомца с корректными данными """

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Добавляем нового питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result["name"] == name


def test_delete_pet():
    """ Проверяем возможность удаления своего питомца """

    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets["pets"]) == 0:
        pf.add_new_pet(auth_key, "Булкабезкорицы", "Пожиратель", "2", "images/chih.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets["pets"][0]["id"]
    status = pf.delete_pet(auth_key, pet_id)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert pet_id not in my_pets.values()

def test_update_pet_info(name="СУПЕРбулкаскорицей", animal_type="СУПЕРпожирательвкуснях", age="2"):
    """ Проверяем возможность обновления информации о своем питомце """

    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets["pets"]) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets["pets"][0]["id"], name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result["name"] == name
    else:
        # если список питомцев пустой, то выкидывает исключение с текстом об отсутствии своих питомцев
        raise Exception("No pets")


def test_add_new_pet_without_photo_valid_data(name="Лис", animal_type="Сиба-ину", age="1"):
    """ Проверяем возможность добавления питомца без фото с корректными данными """

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем нового питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result["name"] == name


def test_set_photo_pet(pet_photo="images/sibainu.jpg"):
    """ Проверяем возможность добавления фото к информации о своем питомце """

    # Запрашиваем ключ api и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем добавить фото
    if len(my_pets["pets"]) > 0:
        status, result = pf.set_photo_pet(auth_key, my_pets["pets"][0]["id"], pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result["pet_photo"]
    else:
        # если список питомцев пустой, то выкидывает исключение с текстом об отсутствии своих питомцев
        raise Exception("No pets")


def test_get_api_key_for_data_user_empty(email=empty_email, password=empty_password):
    """ Проверяем что запрос api ключа c пустыми значениями логина и пароля возвращает статус 403
    и в результате не содержится слово key """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "key" not in result


def test_get_api_key_for_password_user_empty(email=valid_email, password=empty_password):
    """ Проверяем что запрос api ключа c валидным значением логина и пустым значением пароля возвращает статус 403
    и в результате не содержится слово key """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403
    assert "key" not in result


def test_get_all_pets_with_empty_key(filter=""):
    """ Проверяем что запрос всех питомцев c пустым значением api ключа возвращает статус 403 """

    # Запрашиваем полный список питомцев
    status, result = pf.get_list_of_pets(empty_auth_key, filter)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_get_all_pets_with_incorrect_key(filter=""):
    """ Проверяем что запрос всех питомцев c некорректным значением api ключа возвращает статус 403 """

    # Запрашиваем полный список питомцев с некорректным ключом
    status, result = pf.get_list_of_pets(incorrect_auth_key, filter)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403


def test_add_new_pet_empty_data(name="", animal_type="", age="", pet_photo="images/mops.jpg"):
    """ Проверяем возможность добавить питомца с фото и незаполненными данными (отрицательный тест-кейс, баг)"""

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Добавляем нового питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result["name"] == name


def test_add_new_pet_incorrect_age(name="Булкаскорицей", animal_type="Пожирательвкуснях", age="-1", pet_photo="images/\
mops.jpg"):
    """ Проверяем возможность добавить питомца с отрицательным возрастом (отрицательный тест-кейс, тут баг) """

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Добавляем нового питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result["age"] == age


def test_delete_not_your_pet():
    """ Проверяем возможность удаления последнего добавленного на сайт питомца (в том числе и не своего, тут баг) """

    # Запрашиваем ключ api и список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Если список не пустой, то отправляем запрос на удаление первого питомца
    if len(all_pets["pets"]) > 0:
        pet_id = all_pets["pets"][0]["id"]
        status = pf.delete_pet(auth_key, pet_id)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert pet_id not in all_pets.values()
    else:
        # если список питомцев пустой, то выкидывает исключение с текстом об отсутствии питомцев
        raise Exception("No pets")


def test_update_not_your_pet_info(name="Булкаскорицей", animal_type="Пожирательвкуснях", age="1"):
    """ Проверяем возможность обновления информации не о своем питомце (тут баг) """

    # Запрашиваем ключ api и список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(all_pets["pets"]) > 0:
        status, result = pf.update_pet_info(auth_key, all_pets["pets"][0]["id"], name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result["name"] == name
    else:
        # если список питомцев пустой, то выкидывает исключение с текстом об отсутствии питомцев
        raise Exception("No pets")


def test_add_new_pet_without_photo_empty_data(name="", animal_type="", age=""):
    """ Проверяем возможность добавления питомца без фото с незаполненными данными (тут баг) """

    # Запрашиваем ключ api
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем нового питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result["name"] == name


def test_set_photo_not_your_pet(pet_photo="images/mops.jpg"):
    """ Проверяем возможность добавления фото к информации не о своем питомце (последний добавленный на сайт питомец,
    должен быть не наш, иначе тест будет failed)"""

    # Запрашиваем ключ api и список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    # Если список не пустой, то пробуем добавить фото
    if len(all_pets["pets"]) > 0:
        pet_id = all_pets["pets"][0]["id"]
        status, result = pf.set_photo_pet(auth_key, pet_id, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 500
    else:
        # если список питомцев пустой, то выкидывает исключение с текстом об отсутствии питомцев
        raise Exception("No pets")