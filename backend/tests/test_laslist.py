"""
Pytest-tester för Läslistan – BookStore och FavoriteBooks.

Kör från projektroten med:
    pytest backend/tests/test_laslist.py -v
"""

import pytest

from backend.laslist import Book
from backend.laslist import BookStore
from backend.laslist import FavoriteBooks


@pytest.fixture
def store():
    return BookStore()


@pytest.fixture
def favorites():
    return FavoriteBooks()


@pytest.fixture
def book():
    return Book(
        book_id=1,
        author="Andy Weir",
        title="The Martian",
    )


# -----------------------
# Book
# -----------------------


def test_book_has_id():
    book = Book(1, "Kazuo Ishiguro", "Klara och solen")
    assert book.book_id == 1


def test_book_has_author_and_title():
    book = Book(1, "Kazuo Ishiguro", "Klara och solen")
    assert book.author == "Kazuo Ishiguro"
    assert book.title == "Klara och solen"


def test_book_is_not_favorite_by_default():
    book = Book(1, "Kazuo Ishiguro", "Klara och solen")
    assert book.favorite is False


def test_book_repr_contains_title():
    book = Book(1, "Kazuo Ishiguro", "Klara och solen")
    assert "Klara och solen" in repr(book)


# -----------------------
# BookStore.addBook
# -----------------------


def test_add_book_returns_book(store):
    book = store.addBook("Andy Weir", "The Martian")
    assert isinstance(book, Book)


def test_add_book_stores_book(store):
    store.addBook("Andy Weir", "The Martian")
    assert len(store.books) == 1


def test_add_book_correct_author_and_title(store):
    book = store.addBook("Andy Weir", "The Martian")
    assert book.author == "Andy Weir"
    assert book.title == "The Martian"


def test_add_book_gets_unique_id(store):
    book1 = store.addBook("Andy Weir", "The Martian")
    book2 = store.addBook("Andy Weir", "Project Hail Mary")
    assert book1.book_id != book2.book_id


def test_add_multiple_books_all_stored(store):
    store.addBook("A", "Bok 1")
    store.addBook("B", "Bok 2")
    store.addBook("C", "Bok 3")
    assert len(store.books) == 3


def test_add_book_not_favorite_by_default(store):
    book = store.addBook("Andy Weir", "The Martian")
    assert book.favorite is False


# -----------------------
# BookStore.toggleFavorite
# -----------------------


def test_toggle_sets_favorite_true(store):
    book = store.addBook("Andy Weir", "The Martian")
    store.toggleFavorite(book.book_id)
    assert book.favorite is True


def test_toggle_twice_resets_to_not_favorite(store):
    book = store.addBook("Andy Weir", "The Martian")
    store.toggleFavorite(book.book_id)
    store.toggleFavorite(book.book_id)
    assert book.favorite is False


def test_toggle_returns_the_book(store):
    book = store.addBook("Andy Weir", "The Martian")
    result = store.toggleFavorite(book.book_id)
    assert isinstance(result, Book)
    assert result.book_id == book.book_id


def test_toggle_unknown_id_raises_error(store):
    with pytest.raises(ValueError):
        store.toggleFavorite(9999)


def test_toggle_only_affects_correct_book(store):
    book = store.addBook("Andy Weir", "The Martian")
    other = store.addBook("B", "Annan bok")

    store.toggleFavorite(book.book_id)

    assert book.favorite is True
    assert other.favorite is False


# -----------------------
# FavoriteBooks.add
# -----------------------


def test_add_book_to_favorites(favorites, book):
    favorites.add(book)
    assert book in favorites.books


def test_add_returns_book(favorites, book):
    result = favorites.add(book)
    assert result == book


def test_add_duplicate_does_not_duplicate(favorites, book):
    favorites.add(book)
    favorites.add(book)
    assert len(favorites.books) == 1


def test_add_multiple_different_books(favorites, book):
    book2 = Book(2, "B", "Bok 2")

    favorites.add(book)
    favorites.add(book2)

    assert len(favorites.books) == 2


def test_add_sets_favorite_flag_on_book(favorites, book):
    favorites.add(book)
    assert book.favorite is True


# -----------------------
# FavoriteBooks.remove
# -----------------------


def test_remove_book_from_favorites(favorites, book):
    favorites.add(book)
    favorites.remove(book)
    assert book not in favorites.books


def test_remove_returns_book(favorites, book):
    favorites.add(book)
    result = favorites.remove(book)
    assert result == book


def test_remove_clears_favorite_flag(favorites, book):
    favorites.add(book)
    favorites.remove(book)
    assert book.favorite is False


def test_remove_nonexistent_book_raises_error(favorites):
    other = Book(99, "X", "Okänd")

    with pytest.raises(ValueError):
        favorites.remove(other)


def test_remove_only_removes_correct_book(favorites, book):
    book2 = Book(2, "B", "Bok 2")

    favorites.add(book)
    favorites.add(book2)
    favorites.remove(book)

    assert book not in favorites.books
    assert book2 in favorites.books


# -----------------------
# Integrationstester
# -----------------------


def test_add_book_then_toggle_and_add_to_favorites(store, favorites):
    book = store.addBook("Andy Weir", "The Martian")

    store.toggleFavorite(book.book_id)
    favorites.add(book)

    assert book in favorites.books
    assert book.favorite is True


def test_toggle_favorite_reflects_in_store(store):
    book = store.addBook("Andy Weir", "The Martian")

    assert store.books[0].favorite is False

    store.toggleFavorite(book.book_id)

    assert store.books[0].favorite is True


def test_remove_from_favorites_updates_book_flag(store, favorites):
    book = store.addBook("Kazuo Ishiguro", "Klara och solen")

    store.toggleFavorite(book.book_id)
    favorites.add(book)
    favorites.remove(book)

    assert book.favorite is False
    assert len(favorites.books) == 0


def test_multiple_books_only_some_favorited(store, favorites):
    b1 = store.addBook("A", "Bok 1")
    b2 = store.addBook("B", "Bok 2")
    b3 = store.addBook("C", "Bok 3")

    store.toggleFavorite(b2.book_id)
    favorites.add(b2)

    assert b1 not in favorites.books
    assert b2 in favorites.books
    assert b3 not in favorites.books

    assert b1.favorite is False
    assert b2.favorite is True
    assert b3.favorite is False


def test_full_workflow_toggle_on_off(store, favorites):
    book = store.addBook("George Orwell", "1984")

    store.toggleFavorite(book.book_id)
    favorites.add(book)

    assert len(favorites.books) == 1

    store.toggleFavorite(book.book_id)
    favorites.remove(book)

    assert len(favorites.books) == 0
    assert book.favorite is False


def test_initial_store_is_empty(store):
    assert len(store.books) == 0


def test_initial_favorites_is_empty(favorites):
    assert len(favorites.books) == 0