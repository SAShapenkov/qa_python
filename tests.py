import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre',
                             [
                                 'Фантастика',
                                 'Ужасы',
                                 'Детективы',
                                 'Мультфильмы',
                                 'Комедии'
                             ]
                             )
    def test_get_genres_true(self, genre):  # 1 проверить список доступных  жанров
        books_genre = BooksCollector()
        assert genre in books_genre.genre

    def test_add_new_book_true(self):  # 2 проверить что название не пустое
        books_collection = BooksCollector()
        books_collection.add_new_book('Вредные советы')
        assert books_collection.get_books_genre() is not None

    def test_set_genre_for_book_true(self):  # 3 устанавить книге жанр
        books_collection = BooksCollector()
        books_collection.add_new_book('Акира')
        books_collection.set_book_genre('Акира', 'Мультфильмы')
        assert 'Мультфильмы' == books_collection.get_book_genre('Акира')

    def test_get_book_genre_true(self):  # 4 получить жанр книги по её имени
        books_collection = BooksCollector()
        books_collection.add_new_book('Акира')
        books_collection.set_book_genre('Акира', 'Мультфильмы')
        assert books_collection.get_book_genre('Акира') == 'Мультфильмы'

    def test_get_books_with_specific_genre(self):  # 5 вывести список книг с определённым жанром
        books_specific_genre = BooksCollector()
        books_specific_genre.add_new_book('Нечто')
        books_specific_genre.set_book_genre('Нечто', 'Ужасы')
        books_specific_genre.get_books_with_specific_genre('Нечто')
        assert len(books_specific_genre.get_books_with_specific_genre('Ужасы')) == 1

    def test_get_books_genre_true(self):  # 6 получить словарь books_genre
        books_collection = BooksCollector()
        books_collection.add_new_book('451 градус по Фаренгейту')
        books_collection.set_book_genre('451 градус по Фаренгейту', 'Фантастика')
        assert books_collection.get_books_genre() == {'451 градус по Фаренгейту': 'Фантастика'}

    def test_get_books_for_children(self):  # 7 вернуть книги, подходящие детям
        books_collection = BooksCollector()
        books_collection.add_new_book('Синий трактор')
        books_collection.set_book_genre('Синий трактор', 'Мультфильмы')
        assert len(books_collection.get_books_for_children()) == 1

    def test_add_book_in_favorites_and_get_list_of_favorites_books(self):  # 8 добавить книгу в Избранное и получить список Избранных книг
        book_favorites = BooksCollector()
        book_favorites.add_new_book('451 градус по Фаренгейту')
        book_favorites.add_book_in_favorites('451 градус по Фаренгейту')
        assert len(book_favorites.get_list_of_favorites_books()) == 1 and book_favorites.get_list_of_favorites_books() == ['451 градус по Фаренгейту']

    def test_delete_book_from_favorites(self):  # 9 удалить книгу из Избранного
        book_favorites = BooksCollector()
        book_favorites.add_new_book('451 градус по Фаренгейту')
        book_favorites.add_new_book('Лабиринт отражений')
        book_favorites.add_book_in_favorites('451 градус по Фаренгейту')
        book_favorites.add_book_in_favorites('Лабиринт отражений')
        book_favorites.delete_book_from_favorites('451 градус по Фаренгейту')
        assert book_favorites.get_list_of_favorites_books() == ['Лабиринт отражений']
