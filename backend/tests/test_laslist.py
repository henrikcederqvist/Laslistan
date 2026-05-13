"""
TDD-tester för Läslistan – BookStore och FavoriteBooks
Enhetstester och integrationstester

Kör med:
    python3 -m unittest test_laslist.py -v
"""

import unittest

from backend.laslist import Book
from backend.laslist import BookStore
from backend.laslist import FavoriteBooks


# ─────────────────────────────────────────────
#  ENHETSTESTER – Book
# ─────────────────────────────────────────────


class TestBook(unittest.TestCase):
    """Enhetstester för dataklassen Book."""

    def test_book_has_id(self):
        """En bok ska ha ett unikt id."""
        book = Book(
            book_id=1,
            author="Kazuo Ishiguro",
            title="Klara och solen",
        )
        self.assertEqual(book.book_id, 1)

    def test_book_has_author_and_title(self):
        """En bok ska ha författare och titel."""
        book = Book(
            book_id=1,
            author="Kazuo Ishiguro",
            title="Klara och solen",
        )
        self.assertEqual(book.author, "Kazuo Ishiguro")
        self.assertEqual(book.title, "Klara och solen")

    def test_book_is_not_favorite_by_default(self):
        """En ny bok ska inte vara markerad som favorit."""
        book = Book(
            book_id=1,
            author="Kazuo Ishiguro",
            title="Klara och solen",
        )
        self.assertFalse(book.favorite)

    def test_book_repr_contains_title(self):
        """Str-representationen ska innehålla titeln."""
        book = Book(
            book_id=1,
            author="Kazuo Ishiguro",
            title="Klara och solen",
        )
        self.assertIn("Klara och solen", str(book))


# ─────────────────────────────────────────────
#  ENHETSTESTER – BookStore.addBook
# ─────────────────────────────────────────────


class TestBookStoreAddBook(unittest.TestCase):
    """Enhetstester för BookStore.addBook."""

    def setUp(self):
        self.store = BookStore()

    def test_add_book_returns_book(self):
        """addBook ska returnera det skapade Book-objektet."""
        book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )
        self.assertIsInstance(book, Book)

    def test_add_book_stores_book(self):
        """Boken ska finnas i store efter addBook."""
        self.store.addBook(
            "Andy Weir",
            "The Martian",
        )
        self.assertEqual(len(self.store.books), 1)

    def test_add_book_correct_author_and_title(self):
        """Bokens author och title ska matcha indata."""
        book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )
        self.assertEqual(book.author, "Andy Weir")
        self.assertEqual(book.title, "The Martian")

    def test_add_book_gets_unique_id(self):
        """Varje bok ska få ett unikt id."""
        book1 = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )
        book2 = self.store.addBook(
            "Andy Weir",
            "Project Hail Mary",
        )
        self.assertNotEqual(book1.book_id, book2.book_id)

    def test_add_multiple_books_all_stored(self):
        """Alla tillagda böcker ska finnas i store."""
        self.store.addBook("A", "Bok 1")
        self.store.addBook("B", "Bok 2")
        self.store.addBook("C", "Bok 3")
        self.assertEqual(len(self.store.books), 3)

    def test_add_book_not_favorite_by_default(self):
        """En nyligen tillagd bok ska inte vara favorit."""
        book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )
        self.assertFalse(book.favorite)


# ─────────────────────────────────────────────
#  ENHETSTESTER – BookStore.toggleFavorite
# ─────────────────────────────────────────────


class TestBookStoreToggleFavorite(unittest.TestCase):
    """Enhetstester för BookStore.toggleFavorite."""

    def setUp(self):
        self.store = BookStore()
        self.book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )

    def test_toggle_sets_favorite_true(self):
        """Toggle på en icke-favorit ska göra den till favorit."""
        self.store.toggleFavorite(self.book.book_id)
        self.assertTrue(self.book.favorite)

    def test_toggle_twice_resets_to_not_favorite(self):
        """Toggle två gånger ska återställa till icke-favorit."""
        self.store.toggleFavorite(self.book.book_id)
        self.store.toggleFavorite(self.book.book_id)
        self.assertFalse(self.book.favorite)

    def test_toggle_returns_the_book(self):
        """toggleFavorite ska returnera det uppdaterade Book-objektet."""
        result = self.store.toggleFavorite(self.book.book_id)
        self.assertIsInstance(result, Book)
        self.assertEqual(result.book_id, self.book.book_id)

    def test_toggle_unknown_id_raises_error(self):
        """toggleFavorite med okänt id ska kasta ValueError."""
        with self.assertRaises(ValueError):
            self.store.toggleFavorite(9999)

    def test_toggle_only_affects_correct_book(self):
        """Toggle ska bara påverka boken med rätt id."""
        other = self.store.addBook(
            "B",
            "Annan bok",
        )

        self.store.toggleFavorite(self.book.book_id)

        self.assertTrue(self.book.favorite)
        self.assertFalse(other.favorite)


# ─────────────────────────────────────────────
#  ENHETSTESTER – FavoriteBooks.add
# ─────────────────────────────────────────────


class TestFavoriteBooksAdd(unittest.TestCase):
    """Enhetstester för FavoriteBooks.add."""

    def setUp(self):
        self.favorites = FavoriteBooks()
        self.book = Book(
            book_id=1,
            author="Andy Weir",
            title="The Martian",
        )

    def test_add_book_to_favorites(self):
        """Boken ska finnas i favorites efter add."""
        self.favorites.add(self.book)
        self.assertIn(self.book, self.favorites.books)

    def test_add_returns_book(self):
        """add ska returnera det tillagda Book-objektet."""
        result = self.favorites.add(self.book)
        self.assertEqual(result, self.book)

    def test_add_duplicate_does_not_duplicate(self):
        """Samma bok kan inte läggas till flera gånger."""
        self.favorites.add(self.book)
        self.favorites.add(self.book)
        self.assertEqual(len(self.favorites.books), 1)

    def test_add_multiple_different_books(self):
        """Flera olika böcker ska alla kunna läggas till."""
        book2 = Book(
            book_id=2,
            author="B",
            title="Bok 2",
        )

        self.favorites.add(self.book)
        self.favorites.add(book2)

        self.assertEqual(len(self.favorites.books), 2)

    def test_add_sets_favorite_flag_on_book(self):
        """add ska sätta book.favorite = True."""
        self.favorites.add(self.book)
        self.assertTrue(self.book.favorite)


# ─────────────────────────────────────────────
#  ENHETSTESTER – FavoriteBooks.remove
# ─────────────────────────────────────────────


class TestFavoriteBooksRemove(unittest.TestCase):
    """Enhetstester för FavoriteBooks.remove."""

    def setUp(self):
        self.favorites = FavoriteBooks()
        self.book = Book(
            book_id=1,
            author="Andy Weir",
            title="The Martian",
        )
        self.favorites.add(self.book)

    def test_remove_book_from_favorites(self):
        """Boken ska inte finnas i favorites efter remove."""
        self.favorites.remove(self.book)
        self.assertNotIn(self.book, self.favorites.books)

    def test_remove_returns_book(self):
        """remove ska returnera det borttagna Book-objektet."""
        result = self.favorites.remove(self.book)
        self.assertEqual(result, self.book)

    def test_remove_clears_favorite_flag(self):
        """remove ska sätta book.favorite = False."""
        self.favorites.remove(self.book)
        self.assertFalse(self.book.favorite)

    def test_remove_nonexistent_book_raises_error(self):
        """remove av bok som inte är favorit ska kasta ValueError."""
        other = Book(
            book_id=99,
            author="X",
            title="Okänd",
        )

        with self.assertRaises(ValueError):
            self.favorites.remove(other)

    def test_remove_only_removes_correct_book(self):
        """Remove ska bara ta bort rätt bok, inte övriga."""
        book2 = Book(
            book_id=2,
            author="B",
            title="Bok 2",
        )

        self.favorites.add(book2)
        self.favorites.remove(self.book)

        self.assertNotIn(self.book, self.favorites.books)
        self.assertIn(book2, self.favorites.books)


# ─────────────────────────────────────────────
#  INTEGRATIONSTESTER – BookStore + FavoriteBooks
# ─────────────────────────────────────────────


class TestIntegration(unittest.TestCase):
    """
    Integrationstester: klasserna BookStore och FavoriteBooks
    används tillsammans som de skulle i applikationen.
    """

    def setUp(self):
        self.store = BookStore()
        self.favorites = FavoriteBooks()

    def test_add_book_then_toggle_and_add_to_favorites(self):
        """
        Flöde: lägg till bok → toggle favorit → boken hamnar i favorites.
        """
        book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )

        self.store.toggleFavorite(book.book_id)
        self.favorites.add(book)

        self.assertIn(book, self.favorites.books)
        self.assertTrue(book.favorite)

    def test_toggle_favorite_reflects_in_store(self):
        """
        En boks favorite-status i store ska uppdateras av toggleFavorite.
        """
        book = self.store.addBook(
            "Andy Weir",
            "The Martian",
        )

        self.assertFalse(self.store.books[0].favorite)

        self.store.toggleFavorite(book.book_id)

        self.assertTrue(self.store.books[0].favorite)

    def test_remove_from_favorites_updates_book_flag(self):
        """
        Flöde: toggle → add favorites → remove favorites.
        Flaggan favorite ska vara False igen.
        """
        book = self.store.addBook(
            "Kazuo Ishiguro",
            "Klara och solen",
        )

        self.store.toggleFavorite(book.book_id)
        self.favorites.add(book)
        self.favorites.remove(book)

        self.assertFalse(book.favorite)
        self.assertEqual(len(self.favorites.books), 0)

    def test_multiple_books_only_some_favorited(self):
        """
        Av tre böcker markeras bara en som favorit.
        Övriga ska inte påverkas.
        """
        b1 = self.store.addBook("A", "Bok 1")
        b2 = self.store.addBook("B", "Bok 2")
        b3 = self.store.addBook("C", "Bok 3")

        self.store.toggleFavorite(b2.book_id)
        self.favorites.add(b2)

        self.assertNotIn(b1, self.favorites.books)
        self.assertIn(b2, self.favorites.books)
        self.assertNotIn(b3, self.favorites.books)

        self.assertFalse(b1.favorite)
        self.assertTrue(b2.favorite)
        self.assertFalse(b3.favorite)

    def test_full_workflow_toggle_on_off(self):
        """
        Flöde: lägg till → favorit → i favorites → toggle bort →
        remove favorites. favorites ska vara tom.
        """
        book = self.store.addBook(
            "George Orwell",
            "1984",
        )

        self.store.toggleFavorite(book.book_id)
        self.favorites.add(book)

        self.assertEqual(len(self.favorites.books), 1)

        self.store.toggleFavorite(book.book_id)
        self.favorites.remove(book)

        self.assertEqual(len(self.favorites.books), 0)
        self.assertFalse(book.favorite)

    def test_initial_store_is_empty(self):
        """En ny BookStore ska inte ha några böcker."""
        self.assertEqual(len(self.store.books), 0)

    def test_initial_favorites_is_empty(self):
        """En ny FavoriteBooks ska vara tom."""
        self.assertEqual(len(self.favorites.books), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)