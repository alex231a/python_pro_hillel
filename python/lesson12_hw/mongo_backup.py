"""Module with backup function for mongo_db"""
import os
import subprocess


def backup_mongo():
    """
    Function that makes backup of mongo database.
    To automate process - add execution of the script in cron.
    also you should change path to mongo db and backup directory
    """

    # Path to the `mongodump.exe` executable
    mongodump_path = r"C:\Program Files\MongoDB\Server\8.0\bin\mongodump.exe"

    # Directory where the backup will be saved
    backup_dir = r"D:\MongoBackups"

    # Name of the MongoDB database to back up
    database_name = "online_store"

    # Check if the backup directory exists, and create it if necessary
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Backup directory {backup_dir} created.")

    # Check if `mongodump.exe` exists at the specified path
    if not os.path.exists(mongodump_path):
        raise FileNotFoundError(
            f"mongodump.exe not found at the specified path: {mongodump_path}")

    # Prepare the command to run `mongodump`
    command = [mongodump_path, "--db", database_name, "--out", backup_dir]

    try:
        # Using `with` statement to properly handle resources
        with subprocess.Popen(command, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE) as process:
            _, stderr = process.communicate()

            # Check if the command was successful
            if process.returncode == 0:
                print(
                    f"Backup of database {database_name} completed "
                    f"successfully.")
            else:
                print(f"Error during backup: {stderr.decode()}")

    except PermissionError as error:
        print(
            f"Permission error: {error}. Try running the script as "
            f"administrator.")
    except FileNotFoundError as error:
        print(
            f"File not found error: {error}. Please check the path to "
            f"mongodump.exe.")


# Run the backup function
backup_mongo()
