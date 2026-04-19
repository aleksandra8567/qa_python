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
    def test_add_new_book_invalid_length(self):
        collector = BooksCollector()
        collector.add_new_book('')
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Неизвестный жанр')
        assert collector.get_book_genre('Оно') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Основание')
        collector.set_book_genre('Основание', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Дюна' in fantasy_books
        assert 'Основание' in fantasy_books
        assert 'Оно' not in fantasy_books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Мультфильм про кота')
        collector.set_book_genre('Мультфильм про кота', 'Мультфильмы')
        collector.add_new_book('Смешная история')
        collector.set_book_genre('Смешная история', 'Комедии')
        collector.add_new_book('Детектив')
        collector.set_book_genre('Детектив', 'Детективы')
        children_books = collector.get_books_for_children()
        assert 'Мультфильм про кота' in children_books
        assert 'Смешная история' in children_books
        assert 'Детектив' not in children_books

    def test_add_book_in_favorites_valid_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        favorites = collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Властелин колец')
        collector.delete_book_from_favorites('Властелин колец')
        favorites = collector.get_list_of_favorites_books()
        assert 'Властелин колец' not in favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        books_to_favorite = ['Дюна', 'Гарри Поттер', 'Властелин колец']
        for book in books_to_favorite:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        for book in books_to_favorite:
            assert book in favorites

    def test_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert list(books.keys()).count(book_name) == 1