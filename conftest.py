"""
По настоянию наставника фикстуры вынесены в отдельный файл.

Хотя её логичнее было бы создать в файле с тестами.
"""

import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    # Создаем экземпляр класса
    collector = BooksCollector()
    # Добавляем книгу по умолчанию
    # collector.add_new_book('Гордость и предубеждение')
    return collector
