"""Module with function that analyses csv file and returns statistics"""
import pandas as pd


def load_csv(file_name: str) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame, ensuring it contains a 'date' column.

    :param file_name: Path to the CSV file.
    :return: Pandas DataFrame with a 'date' column converted to datetime.
    :raises ValueError: If the 'date' column is missing or invalid.
    """
    try:
        dataframe = pd.read_csv(file_name, encoding="utf-8")

        if "date" not in dataframe.columns:
            raise ValueError("The CSV file does not contain a 'date' column.")

        dataframe["date"] = pd.to_datetime(dataframe["date"], errors="coerce")

        if dataframe["date"].isna().all():
            raise ValueError("No valid dates found in the 'date' column.")

        return dataframe

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: Failed to parse the file.")
        raise


def get_statistics_from_file(file_name: str) -> None:
    """
    Reads a CSV file, extracts publication dates, and prints statistics
    on the number of news articles published each day.

    :param file_name: Path to the CSV file containing news data.
    """
    try:
        dataframe = load_csv(file_name)

        dataframe["date_only"] = dataframe["date"].dt.date
        news_count_per_day = dataframe["date_only"].value_counts().sort_index()

        for date, count in news_count_per_day.items():
            print(f"For {date}, {count} news articles were downloaded.")

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    get_statistics_from_file("news.csv")
