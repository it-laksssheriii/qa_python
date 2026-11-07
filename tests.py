import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name, expected_books_count',
        [
            ('А', 1),
            ('А' * 40, 1),
            ('', 0),
            ('А' * 41, 0),
        ]
    )
    def test_add_new_book_name_length_boundaries(self, name, expected_books_count):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == expected_books_count

    def test_add_new_book_new_book_has_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')

        assert collector.get_book_genre('Гарри Поттер') == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_available_genre_genre_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', genre)

        assert collector.get_book_genre('Гарри Поттер') == genre

    def test_get_book_genre_existing_book_returns_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_only_books_of_this_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Дюна']

    @pytest.mark.parametrize('age_rating_genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_books_with_age_rating_excluded(self, age_rating_genre):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_new_book('Книга с рейтингом')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Книга с рейтингом', age_rating_genre)

        assert collector.get_books_for_children() == ['Шрек']

    def test_add_book_in_favorites_existing_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_book_in_favorites_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Дюна']