import sqlite3


def create_tables():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("DROP TABLE IF EXISTS genres")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre_id INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres (id)
        )
    """)


def add_genre(name):
    conn.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()


def add_book_info(name, author, publication_year, genre_id, number_of_pages, number_of_copies):
    conn.execute("""
        INSERT INTO books (name, author, publication_year, genre_id, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre_id, number_of_pages, number_of_copies))
    conn.commit()


def delete_book(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()


def get_books_with_genres():
    cursor = conn.execute("""
        SELECT books.id, books.name, books.author, books.publication_year, genres.name AS genre, books.number_of_pages, books.number_of_copies
        FROM books
        JOIN genres ON books.genre_id = genres.id
    """)
    return cursor.fetchall()


if __name__ == '__main__':
    conn = sqlite3.connect('books.db')

    create_tables()

    add_genre("Детектив")
    add_genre("Фантастика")
    add_genre("Мистика")
    add_genre("Исторический роман")
    add_genre("Киберпанк")
    add_genre("Приключения")
    add_genre("Фэнтези")
    add_genre("Триллер")
    add_genre("Научная фантастика")
    add_genre("Роман")

    add_book_info("Тени над озером", "Анна Левина", 2018, 1, 352, 5)
    add_book_info("Песнь звёздного ветра", "Сергей Волков", 2021, 2, 410, 3)
    add_book_info("Тайна старого особняка", "Ирина Кузнецова", 2015, 3, 278, 4)
    add_book_info("Путь самурая", "Такэси Накамура", 2009, 4, 390, 2)
    add_book_info("Криптокод", "Алексей Громов", 2022, 5, 450, 6)
    add_book_info("Сердце пустыни", "Лейла Рахимова", 2017, 6, 330, 3)
    add_book_info("Заклинания северного ветра", "Марина Фёдорова", 2020, 7, 512, 7)
    add_book_info("Третий ключ", "Дмитрий Соловьёв", 2016, 8, 299, 5)
    add_book_info("Планета-призрак", "Николай Андреев", 2012, 9, 376, 4)
    add_book_info("Город за горизонтом", "Виктория Смиронова", 2023, 10, 288, 8)

    delete_book(2)
    delete_book(7)
    delete_book(10)

    books = get_books_with_genres()
    for book in books:
        print(book)