"""
Personal Diary / Journal
A  basic OOP concepts:
- Classes and Objects
- Encapsulation
- Constructors
- Simple list management
"""

from datetime import date


class DiaryEntry:
    """Represents a single diary entry."""

    def __init__(self, entry_date, mood, content):
        self.entry_date = entry_date
        self.mood = mood
        self.content = content

    def display(self):
        print(f"\nDate  : {self.entry_date}")
        print(f"Mood  : {self.mood}")
        print(f"Entry : {self.content}")
        print("-" * 40)


class Diary:
    """Manages a collection of diary entries (Encapsulation)."""

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.__entries = []   # private list of entries

    def add_entry(self, mood, content):
        today = date.today()
        entry = DiaryEntry(today, mood, content)
        self.__entries.append(entry)
        print(f"Entry for {today} added successfully.")

    def view_all_entries(self):
        if not self.__entries:
            print("No entries yet. Start writing today!")
            return
        print(f"\n===== {self.owner_name}'s Diary =====")
        for entry in self.__entries:
            entry.display()

    def view_entry_by_date(self, search_date):
        found = False
        for entry in self.__entries:
            if str(entry.entry_date) == search_date:
                entry.display()
                found = True
        if not found:
            print("No entry found for this date.")

    def search_by_mood(self, mood):
        results = [e for e in self.__entries if e.mood.lower() == mood.lower()]
        if not results:
            print(f"No entries found with mood '{mood}'.")
            return
        print(f"\n----- Entries with mood: {mood} -----")
        for entry in results:
            entry.display()

    def delete_entry_by_date(self, search_date):
        for entry in self.__entries:
            if str(entry.entry_date) == search_date:
                self.__entries.remove(entry)
                print(f"Entry for {search_date} deleted.")
                return
        print("No entry found for this date.")

    def total_entries(self):
        return len(self.__entries)


# ---------------- Menu-driven Program ----------------
def main():
    owner_name = input("Enter your name: ")
    diary = Diary(owner_name)

    while True:
        print("\n===== PERSONAL DIARY MENU =====")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. View Entry by Date (YYYY-MM-DD)")
        print("4. Search Entries by Mood")
        print("5. Delete Entry by Date")
        print("6. Show Total Entries")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            mood = input("How are you feeling today? (e.g., Happy, Sad, Excited): ")
            content = input("Write your diary entry: ")
            diary.add_entry(mood, content)

        elif choice == '2':
            diary.view_all_entries()

        elif choice == '3':
            search_date = input("Enter date to search (YYYY-MM-DD): ")
            diary.view_entry_by_date(search_date)

        elif choice == '4':
            mood = input("Enter mood to search: ")
            diary.search_by_mood(mood)

        elif choice == '5':
            search_date = input("Enter date to delete (YYYY-MM-DD): ")
            diary.delete_entry_by_date(search_date)

        elif choice == '6':
            print(f"Total entries: {diary.total_entries()}")

        elif choice == '7':
            print("Exiting Personal Diary. Take care!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()