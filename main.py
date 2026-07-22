from src.database import Database


def main():
    print("Starting Steyn Timetable...")

    db = Database()

    print("Database object created.")

    db.close()

    print("Program finished successfully.")


if __name__ == "__main__":
    main()