import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, books_collector):
        # добавляем вторую книгу
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        books_collector.add_new_book('Гордость и предубеждение')

        # проверяем, что обе книги были добавлены
        assert len(books_collector.books_genre) == 2, f'Ошибка добавления книг, {len(books_collector.books_genre)}!= 2'

    # Проверяем метод get_books_for_children, книги с подходящим рейтингом присутствуют в списке книг для детей

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Книга Фантастики', 'Фантастика'),
            ('Книга, по которой сняли Мультик', 'Мультфильмы'),
            ('Комедийная Книга', 'Комедии'),
        ],
        ids=[
            'Fantastic book',
            'Cartoon book',
            'Comedy book',
        ]
    )
    def test_get_books_for_children_includes_suitable_books(self, books_collector, book_name, genre):
        # Добавляем книги
        books_collector.add_new_book(book_name)
        # Устанавливаем книгам жанры
        books_collector.set_book_genre(book_name, genre)
        # Получаем книги, подходящие детям
        children_books = books_collector.get_books_for_children()

        # Проверяем, что в список попали книги, подходящие детям
        assert book_name in children_books, \
            f'Ошибка, книга "{book_name}" подходит детям и должна быть в списке.'

    # Проверяем метод get_books_for_children, книги с неподходящим рейтингом отсутствуют в списке книг для детей

    @pytest.mark.parametrize(
        'book_name, genre',
        [
            ('Книга Ужасов', 'Ужасы'),
            ('Книга с закрученным сюжетом', 'Детективы'),
        ],
        ids=[
            'Horror book',
            'Detectiv book',
        ]
    )
    def test_get_books_for_children_includes_suitable_books(self, books_collector, book_name, genre):
        # Добавляем книги
        books_collector.add_new_book(book_name)
        # Устанавливаем книгам жанры
        books_collector.set_book_genre(book_name, genre)
        # Получаем книги, подходящие детям
        children_books = books_collector.get_books_for_children()

        # Проверяем, что в список не попали книги, подходящие детям
        assert book_name not in children_books, \
            f'Ошибка, книга "{book_name}" не подходит детям и не должна быть в списке.'

    # Проверяем метод add_new_book, у новой добавленной книги нет никакого жанра
    def test_add_new_book_added_without_genres(self, books_collector):
        # Добавляем книгу, её больше нет в фикстуре
        books_collector.add_new_book('Гордость и предубеждение')

        # Проверяем, что для добавленной книги не установлен жанр (пустая строка)
        assert books_collector.books_genre.get(
            'Гордость и предубеждение') == '', f'Ошибка, у новой книги должен быть пустой жанр.'

    # Проверяем метод add_new_book, нельзя добавить книгу с пустым именем
    def test_add_new_book_with_empty_name(self):
        # создаем экземпляр (объект) класса BooksCollector без использования фикстуры
        collector = BooksCollector()
        # добавляем книгу с пустым названием
        collector.add_new_book('')

        # проверяем, что книга не была добавлена
        assert len(collector.books_genre) == 0, f'Ошибка добавления книги с пустым названием'

    # Проверяем метод add_new_book, нельзя добавить книгу с именем длиннее 40 символов
    def test_add_new_book_with_long_name(self, books_collector):
        # добавляем книгу с именем длиннее 40 символов
        books_collector.add_new_book('Книга с очень длинным названием, которое не должно добавляться')

        # проверяем, что книга не была добавлена
        assert len(books_collector.books_genre) == 0, f'Ошибка добавления книги с длинным названием'

    # Проверяем метод set_book_genre, нельзя установить книге несуществующий жанр
    def test_set_book_genre_with_unknown_genre(self, books_collector):
        # Добавляем книгу
        books_collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем книге несуществующий жанр
        books_collector.set_book_genre('Гордость и предубеждение', 'Фэнтези')

        # проверяем, что жанр не был добавлен
        assert books_collector.books_genre.get(
            'Гордость и предубеждение') == '', f'Ошибка, у книги должен быть пустой жанр.'

    # Проверяем метод set_book_genre, нельзя установить несуществующей в списке books_genre книге жанр,
    def test_set_book_genre_with_unknown_book(self, books_collector):
        # Устанавливаем несуществующей книге жанр
        books_collector.set_book_genre('Мифическая книга', 'Фантастика')

        # проверяем, что жанр не был добавлен
        assert books_collector.books_genre.get(
            'Мифическая книга') is None, f'Ошибка, у несуществующей книги не может быть жанра.'

    # Проверяем метод get_book_genre, вывод жанра книги по её имени
    def test_get_book_genre_add_one_book_comedy(self, books_collector):
        # добавляем книгу
        books_collector.add_new_book('Гордость и предубеждение')
        # создаём переменную с ожидаемым результатом
        expected_result = 'Комедии'
        # присваиваем книге жанр с помощью переменной с ожидаемым результатом
        books_collector.set_book_genre('Гордость и предубеждение', expected_result)

        # создаём переменную с фактическим результатом
        fact_result = books_collector.get_book_genre('Гордость и предубеждение')

        # проверяем, что добавленный жанр соответствует полученному
        assert expected_result == fact_result, \
            f'Ошибка, добавленный жанр {expected_result} не соответствует полученному {fact_result}'

    # Проверяем метод get_books_with_specific_genre, вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre_add_tree_detective(self):
        # создаем экземпляр (объект) класса BooksCollector без использования фикстуры
        collector = BooksCollector()

        # Добавляем книгу и устанавливаем жанр
        collector.add_new_book('Книга Детективов')
        collector.set_book_genre('Книга Детективов', 'Детективы')

        # Ожидаемый список книг жанра 'Детективы'
        expected_detective_books = ['Книга Детективов']
        # Фактический список книг жанра 'Детективы'
        detective_books = collector.get_books_with_specific_genre('Детективы')

        # Сравниваем списки
        assert detective_books == expected_detective_books, f'Ошибка получения книг определённого жанра.'

    # Проверяем метод get_books_with_specific_genre, вывод пустого списка книг, если нет подходящих книг
    def test_get_books_with_specific_genre_empty_books_genre(self, books_collector):

        # Создаём переменную с фактическим результатом
        result = books_collector.get_books_with_specific_genre('Фантастика')

        # Убеждаемся, что список пустой
        assert result == []

    # Проверяем метод get_books_genre, вывод словаря книг и жанров
    def test_get_books_genre_add_three_books(self):
        # создаем экземпляр (объект) класса BooksCollector, без фикстуры
        collector = BooksCollector()
        # создаём переменную со списком книг и жанров
        books_with_genres = {
            'Книга Фантастики': 'Фантастика',
            'Книга Ужасов': 'Ужасы',
            'Детективная Книга': 'Детективы',
        }
        # добавляем книги в словарь books_genre
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        # Получаем текущий словарь books_genre
        current_books_genre = collector.get_books_genre()

        # Проверяем, что возвращенный словарь точно соответствует добавленным книгам и их жанрам
        assert current_books_genre == books_with_genres, f'Возвращенный словарь books_genre не соответствует ожидаемому'

    #    Проверяем метод add_book_in_favorites, успешное добавление книги в избранное
    def test_add_book_in_favorites_success(self, books_collector):
        # добавляем книгу
        books_collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр книги, чтобы обеспечить её наличие в books_genre
        books_collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        # добавляем книгу в Избранное
        books_collector.add_book_in_favorites('Гордость и предубеждение')

        # проверяем, что книга добавилась в список favorites
        assert 'Гордость и предубеждение' in books_collector.favorites, f'Книга не добавилась  в избранное'

    #  Проверяем метод add_book_in_favorites, неуспешное повторное добавление книги в избранное
    def test_add_book_in_favorites_twice(self, books_collector):
        # добавляем книгу
        books_collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр книги, чтобы обеспечить её наличие в books_genre
        books_collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        # Добавляем книгу в избранное впервые
        books_collector.add_book_in_favorites('Гордость и предубеждение')
        # Получаем начальное количество книг в избранном
        favorites_count_initial = len(books_collector.favorites)
        # Пытаемся добавить книгу в избранное второй раз
        books_collector.add_book_in_favorites('Гордость и предубеждение')

        # Проверяем, что количество книг в избранном не изменилось
        assert len(books_collector.favorites) == favorites_count_initial, \
            f'Книга не должна добавляться в избранное повторно'

    #  Проверяем метод add_book_in_favorites, неуспешное добавление неизвестной книги в избранное
    def test_add_book_in_favorites_unknown_book(self, books_collector):
        # Пытаемся добавить в избранное книгу, которой нет в books_genre
        books_collector.add_book_in_favorites('Неизвестная книга')

        # Проверяем, что книга не была добавлена в избранное
        assert 'Неизвестная книга' not in books_collector.favorites, \
            f'Книга, не присутствующая в books_genre, не должна быть добавлена в избранное'

    # Проверяем метод delete_book_from_favorites, успешное удаление ранее добавленной книги
    def test_delete_book_from_favorites_success(self, books_collector):
        # добавляем книгу
        books_collector.add_new_book('Гордость и предубеждение')
        # Устанавливаем жанр книги, чтобы обеспечить её наличие в books_genre
        books_collector.set_book_genre('Гордость и предубеждение', 'Комедии')
        # Добавляем книгу в избранное
        books_collector.add_book_in_favorites('Гордость и предубеждение')
        # Удаляем книгу из избранного
        books_collector.delete_book_from_favorites('Гордость и предубеждение')

        # Проверяем, что книги больше нет в избранном
        assert 'Гордость и предубеждение' not in books_collector.get_list_of_favorites_books(), \
            f'Книга должна быть удалена из избранного'

    #  Проверяем метод add_book_in_favorites, неуспешное удаление неизвестной книги в избранное
    def test_delete_book_in_favorites_unknown_book(self, books_collector):
        # Пытаемся удалить книгу, которой нет в books_genre и избранном
        books_collector.delete_book_from_favorites('Неизвестная книга')

        # Проверяем, что это не повлияло на список избранного
        assert 'Неизвестная книга' not in books_collector.favorites, \
            f'Книга, не присутствующая в books_genre, не должна быть в избранном'

    # Проверяем метод get_list_of_favorites_books, получение списка избранных книг
    def test_get_list_of_favorites_books(self, books_collector):
        # Добавляем книгу, устанавливаем её жанр
        books_collector.add_new_book('Книга Фантастики')
        books_collector.set_book_genre('Книга Фантастики', 'Фантастика')
        # Добавляем книгу в избранное
        books_collector.add_book_in_favorites('Книга Фантастики')

        # Ожидаемый список избранных книг
        expected_favorite_books = ['Книга Фантастики']
        # Фактический список избранных книг
        favorite_books = books_collector.get_list_of_favorites_books()

        # Сравниваем списки
        assert favorite_books == expected_favorite_books, f'Ошибка получения списка избранных книг.'
