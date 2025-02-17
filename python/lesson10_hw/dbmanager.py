"""Module with DatabaseManager class. Contains methods for create table,
insert, update, select, delete information"""

import sqlite3
from datetime import datetime
from typing import List, Tuple, Dict

from db_schema import MOVIES


class DatabaseManager:
    """Handles database operations for the movie database."""

    def __init__(self, db_name: str = "cinema.db") -> None:
        """
        Initializes the database manager.
        - Connects to the SQLite database.
        - Creates tables if they do not exist.
        - Populates tables with initial data if they are empty.
        - Registers the custom SQLite function `movie_age()`.

        :param db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()
        self._populate_tables()
        self._register_functions()

    def _create_tables(self) -> None:
        """Creates the required database tables if they do not exist."""
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {MOVIES['table_name']} ("
            f"{MOVIES['insert_information']})")
        self.conn.commit()

    def _populate_tables(self) -> None:
        """Inserts initial data into the tables if they are empty."""
        self.cursor.execute(f"SELECT COUNT(*) FROM {MOVIES['table_name']}")
        if self.cursor.fetchone()[0] == 0:
            self.cursor.executemany(
                f"INSERT INTO {MOVIES['table_name']} ("
                f"{', '.join(map(str, MOVIES['columns']))}) VALUES (?, ?, ?)",
                MOVIES['data_to_insert']
            )
            self.conn.commit()

    def _register_functions(self) -> None:
        """Registers the custom SQLite function `movie_age()` to calculate
        the movie's age."""

        def movie_age(release_year: int) -> int:
            """
            Calculates the number of years since a movie was released.

            :param release_year: The release year of the movie.
            :return: The age of the movie in years.
            """
            current_year = datetime.now().year
            return current_year - release_year

        self.conn.create_function("movie_age", 1, movie_age)

    def get_movies_with_age(self) -> List[Tuple[str, int, int]]:
        """
        Retrieves a list of movies along with their release year and
        calculated age.

        :return: A list of tuples containing (title, release_year, age).
        """
        self.cursor.execute(f"""
            SELECT title, release_year, movie_age(release_year) as age
            FROM {MOVIES['table_name']}
        """)
        movies = self.cursor.fetchall()
        return movies

    def display_movies_with_age(self) -> None:
        """
        Prints the list of movies with their release year and calculated age.
        """
        movies = self.get_movies_with_age()
        for movie in movies:
            print(f"Фільм: {movie[0]} ({movie[1]}), Вік: {movie[2]} років")

    def insert_data(self, table: Dict[str, str], data: List[Tuple]) -> None:
        """
        Inserts data into the specified table.

        :param table: A dictionary containing table information (name,
        columns).
        :param data: A list of tuples representing rows to insert.
        """
        if not data:
            return

        placeholders = ', '.join(['?'] * len(
            table['columns']))  # Generates placeholders dynamically
        columns = ', '.join(
            table['columns'])  # Ensure this is a list of strings
        query = (f"INSERT INTO {table['table_name']} ({columns}) VALUES ("
                 f"{placeholders})")

        self.cursor.executemany(query, data)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        """
            Fetches data from the table.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute_query(self, query, params=()):
        """
            Executes query on the database.
        """
        self.cursor.execute(query, params)
        self.conn.commit()

    def close(self) -> None:
        """Closes the database connection."""
        self.conn.close()
