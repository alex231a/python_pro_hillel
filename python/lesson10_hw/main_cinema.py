"""Module with function that manages cinema db"""

from db_schema import MOVIES, ACTORS, MOVIE_CAST, ACTIONS
from dbmanager import DatabaseManager


def main() -> None:
    """
    Main function to run the console application for managing a movie database.

    Allows users to:
    1. Add a movie
    2. Add an actor
    3. Show all movies with their actors
    4. Show unique genres
    5. Show the number of movies by genre
    6. Show the average birth year of actors in movies of a specific genre
    7. Search for a movie by title
    8. Show movies with pagination
    9. Show all actor names and movie titles
    10. Show movies with their age (years since release)
    0. Exit the application
    """
    db = DatabaseManager()

    while True:
        print(ACTIONS)
        choice: str = input("Select an action: ")

        if choice == "1":
            title: str = input("Enter movie title: ")
            year: int = int(input("Enter release year: "))
            genre: str = input("Enter genre: ")
            db.execute_query(
                f"INSERT INTO {MOVIES['table_name']} (title, release_year, "
                f"genre) VALUES (?, ?, ?)",
                (title, year, genre),
            )

        elif choice == "2":
            name: str = input("Enter actor's name: ")
            birth_year: int = int(input("Enter birth year: "))
            db.execute_query(
                f"INSERT INTO {ACTORS['table_name']} (name, birth_year) "
                f"VALUES (?, ?)",
                (name, birth_year),
            )

        elif choice == "3":
            results = db.fetch_all(f"""
                SELECT m.title, GROUP_CONCAT(a.name, ', ')
                FROM {MOVIES['table_name']} m
                JOIN {MOVIE_CAST['table_name']} mc ON m.id = mc.movie_id
                JOIN {ACTORS['table_name']} a ON mc.actor_id = a.id
                GROUP BY m.id
            """)
            for title, actors in results:
                print(f"Movie: {title}, Actors: {actors}")

        elif choice == "4":
            results = db.fetch_all(
                f"SELECT DISTINCT genre FROM {MOVIES['table_name']}")
            for row in results:
                print(row[0])

        elif choice == "5":
            results = db.fetch_all(
                f"SELECT genre, COUNT(*) FROM {MOVIES['table_name']} GROUP "
                f"BY genre"
            )
            for genre, count in results:
                print(f"{genre}: {count}")

        elif choice == "6":
            selected_genre: str = input("Enter genre: ")
            results = db.fetch_all(
                f"""
                SELECT AVG(birth_year)
                FROM {ACTORS['table_name']} a
                JOIN {MOVIE_CAST['table_name']} mc ON a.id = mc.actor_id
                JOIN {MOVIES['table_name']} m ON mc.movie_id = m.id
                WHERE m.genre = ?
                """,
                (selected_genre,),
            )
            print(f"Average birth year of actors: {results[0][0]}")

        elif choice == "7":
            keyword: str = input("Enter search keyword: ")
            results = db.fetch_all(
                f"SELECT title FROM {MOVIES['table_name']} WHERE title LIKE ?",
                (f"%{keyword}%",),
            )
            for row in results:
                print(row[0])

        elif choice == "8":
            page: int = int(input("Enter page number: "))
            limit: int = 3
            offset: int = (page - 1) * limit
            results = db.fetch_all(
                f"SELECT title FROM {MOVIES['table_name']} LIMIT ? OFFSET ?",
                (limit, offset),
            )
            for row in results:
                print(row[0])

        elif choice == "9":
            results = db.fetch_all(
                f"SELECT name FROM {ACTORS['table_name']} UNION SELECT title "
                f"FROM {MOVIES['table_name']}"
            )
            for row in results:
                print(row[0])

        elif choice == "10":
            db.display_movies_with_age()

        elif choice == "0":
            db.close()
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
