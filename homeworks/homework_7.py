import sqlite3


def create_tables():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)


def add_book_info(name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (name, author, publication_year, genre, number_of_pages, number_of_copies)
                 )
    conn.commit()


def delete_book(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('books.db')

    create_tables()
    add_book_info("Тени над озером", "Анна Левина", 2018, "Детектив", 352, 5)
    add_book_info("Песнь звёздного ветра", "Сергей Волков", 2021, "Фантастика", 410, 3)
    add_book_info("Тайна старого особняка", "Ирина Кузнецова", 2015, "Мистика", 278, 4)
    add_book_info("Путь самурая", "Такэси Накамура", 2009, "Исторический роман", 390, 2)
    add_book_info("Криптокод", "Алексей Громов", 2022, "Киберпанк", 450, 6)
    add_book_info("Сердце пустыни", "Лейла Рахимова", 2017, "Приключения", 330, 3)
    add_book_info("Заклинания северного ветра", "Марина Фёдоровна", 2020, "Фентези", 512, 7)
    add_book_info("Третий ключ", "Дмитрий Соловьёв", 2016, "Триллер", 299, 5)
    add_book_info("Планета-призрак", "Николай Андреев", 2012, "Научная фантастика", 376, 4)
    add_book_info("Город за горизонтом", "Виктория Смиронова", 2023, "Роман", 288, 8)

    delete_book(2)
    delete_book(7)
    delete_book(10)
