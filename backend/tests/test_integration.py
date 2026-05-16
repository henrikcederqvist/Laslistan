import pytest

from backend.laslist import BookStore
from backend.laslist import FavoriteBooks


@pytest.fixture
def store():
    return BookStore()


@pytest.fixture
def favorites():
    return FavoriteBooks()


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