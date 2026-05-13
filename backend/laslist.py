"""
laslist.py – Backend för Läslistan
Klasser: Book, BookStore, FavoriteBooks
"""


class Book:
    """Representerar en bok i katalogen."""

    def __init__(self, book_id: int, author: str, title: str, favorite: bool = False):
        self.book_id = book_id
        self.author = author
        self.title = title
        self.favorite = favorite

    def __repr__(self) -> str:
        fav = " ★" if self.favorite else ""
        return f"Book(id={self.book_id}, '{self.title}' av {self.author}{fav})"


class BookStore:
    """
    Hanterar katalogen med alla böcker.

    Metoder:
        addBook(author, title) -> Book
        toggleFavorite(book_id) -> Book
    """

    def __init__(self):
        self.books: list[Book] = []
        self._next_id: int = 1

    def addBook(self, author: str, title: str) -> Book:
        """Skapar en ny bok och lägger till den i katalogen."""
        book = Book(book_id=self._next_id, author=author, title=title)
        self._next_id += 1
        self.books.append(book)
        return book

    def toggleFavorite(self, book_id: int) -> Book:
        """
        Växlar favorite-status för boken med givet id.
        Kastar ValueError om inget id matchar.
        """
        for book in self.books:
            if book.book_id == book_id:
                book.favorite = not book.favorite
                return book
        raise ValueError(f"Ingen bok med id={book_id} hittades.")


class FavoriteBooks:
    """
    Hanterar användarens favoritböcker.

    Metoder:
        add(book) -> Book
        remove(book) -> Book
    """

    def __init__(self):
        self.books: list[Book] = []

    def add(self, book: Book) -> Book:
        """
        Lägger till en bok i favoritlistan.
        Ignorerar duplikat (samma bok läggs inte till två gånger).
        Sätter book.favorite = True.
        """
        if book not in self.books:
            book.favorite = True
            self.books.append(book)
        return book

    def remove(self, book: Book) -> Book:
        """
        Tar bort en bok från favoritlistan.
        Kastar ValueError om boken inte finns i listan.
        Sätter book.favorite = False.
        """
        if book not in self.books:
            raise ValueError(f"{book} finns inte i favoritlistan.")
        self.books.remove(book)
        book.favorite = False
        return book
