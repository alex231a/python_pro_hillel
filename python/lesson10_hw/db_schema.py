"""Module contains information about db tables that should be created if
they don't exist"""

MOVIES = {'table_name': 'movies',
          'insert_information': 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                'title TEXT, '
                                'release_year '
                                'INTEGER, genre TEXT',
          'columns': ("title", "release_year", "genre"),
          'data_to_insert': [("Inception", 2010, "Sci-Fi"),
                             ("The Matrix", 1999, "Action"),
                             ("Interstellar", 2014, "Sci-Fi"),
                             ("The Dark Knight", 2008, "Action"),
                             ("Forrest Gump", 1994, "Drama")]

          }
ACTORS = {'table_name': 'actors',
          'insert_information': 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                'name TEXT, '
                                'birth_year '
                                'INTEGER',
          'columns': ("name", "birth_year"),
          'data_to_insert': [("Leonardo DiCaprio", 1974),
                             ("Keanu Reeves", 1964),
                             ("Matthew McConaughey", 1969),
                             ("Christian Bale", 1974),
                             ("Tom Hanks", 1956)]
          }
MOVIE_CAST = {'table_name': 'movie_cast', 'insert_information':
    'movie_id INTEGER, actor_id INTEGER, PRIMARY KEY (movie_id, actor_id), '
    'FOREIGN KEY (movie_id) REFERENCES movies(id), FOREIGN KEY (actor_id) '
    'REFERENCES actors(id)',
              'columns': ("movie_id", "actor_id"),
              'data_to_insert': [(1, 1),
                                 (2, 2),
                                 (3, 3),
                                 (4, 4),
                                 (5, 5),
                                 (1, 3),
                                 (2, 4)]
              }

ACTIONS = """
    1. Додати фільм
    2. Додати актора
    3. Показати всі фільми з акторами
    4. Показати унікальні жанри
    5. Показати кількість фільмів за жанром
    6. Показати середній рік народження акторів у фільмах певного жанру
    7. Пошук фільму за назвою
    8. Показати фільми (з пагінацією)
    9. Показати імена всіх акторів та назви всіх фільмів
    10. Фільми та їхній вік
    0. Вихід
"""
