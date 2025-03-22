from main import BooksCollector
import pytest


@pytest.fixture()
def baza():
    collector = BooksCollector()
    collector.add_new_book('Идиот')
    collector.add_new_book('Хищник')
    collector.add_new_book('Пуаро')
    collector.add_new_book('Пуаро против хищника')
    collector.add_new_book('Пуаро против идиота')
    collector.add_new_book('Хищник против идиота')
    collector.set_book_genre('Идиот', 'Ужасы')
    collector.set_book_genre('Хищник', 'Фантастика')
    collector.set_book_genre('Пуаро', 'Детективы')
    collector.set_book_genre('Пуаро против хищника', 'Мультфильмы')
    collector.set_book_genre('Пуаро против идиота', 'Комедии')
    collector.set_book_genre('Хищник против идиота', 'Комедии')
    return collector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_new_book_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book', ['Гордость и предубеждение и зомби и снова гордость', ''])
    def test_add_new_book_negative_input_no_new_book(self, book):
        collector10 = BooksCollector()
        collector10.add_new_book(book)
        assert len(collector10.get_books_genre()) == 0


    def test_set_book_genre_book_in_books_genre_list_and_genre_in_genre_list_genre_is_set(self):
        collector1 = BooksCollector()
        # тест проверяет добавление книги с указанием существующего жанра
        collector1.add_new_book('Идиот')
        collector1.set_book_genre('Идиот', 'Ужасы')
        assert collector1.books_genre.get('Идиот') == 'Ужасы', 'Жанр и книга реальны, метод работает неверно'

        # тест проверяет добавление существующей книги и несуществующего жанра

    @pytest.mark.parametrize('book_name, book_genre', [['Букварь', 'Азбука'], ['Чужой', 'Ужасы']])
    def test_set_book_genre_if_book_name_book_genre_not_in_list_genre_is_not_set(self, book_name, book_genre):
        collector12 = BooksCollector()
        collector12.set_book_genre(book_name, book_genre)
        assert collector12.books_genre.get(book_name, book_genre)



    def test_get_book_genre_by_book_name_return_genre(self, baza):
        collector2 = baza
        assert collector2.get_book_genre('Идиот') == 'Ужасы'


    def test_get_books_with_specific_genre_comedy_returns_correct_books(self, baza):
        collector3 = baza
        assert collector3.get_books_with_specific_genre('Комедии') == ['Пуаро против идиота', 'Хищник против идиота']

    def test_get_books_genre_return_dictionary_books_genre(self, baza):
        collector4 = baza
        norm = {'Идиот': 'Ужасы', 'Хищник': 'Фантастика', 'Пуаро': 'Детективы', 'Пуаро против хищника': 'Мультфильмы',
                'Пуаро против идиота': 'Комедии', 'Хищник против идиота': 'Комедии'}
        assert collector4.get_books_genre() == norm

    def test_get_books_for_children_return_list_books_for_children(self, baza):
        collector5 = baza
        norm = ['Хищник', 'Пуаро против хищника', 'Пуаро против идиота', 'Хищник против идиота']
        assert collector5.get_books_for_children() == norm

    def test_add_book_in_favorites_book_is_added_in_favorites(self, baza):
        collector6 = baza
        collector6.add_book_in_favorites('Пуаро')
        assert collector6.favorites[-1] == 'Пуаро'

    def test_delete_book_from_favorites_book_is_deleted_from_favorites(self, baza):
        collector7 = baza
        collector7.add_book_in_favorites('Пуаро')
        collector7.delete_book_from_favorites('Пуаро')
        assert collector7.favorites == []

    def test_get_list_of_favorites_books_return_list_of_favorites(self, baza):
        collector8 = baza
        collector8.add_book_in_favorites('Пуаро')
        collector8.add_book_in_favorites('Идиот')
        assert collector8.get_list_of_favorites_books() == ['Пуаро', 'Идиот']
