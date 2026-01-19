
from datetime import datetime

def get_valid_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if date_input.strip() == "":
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid format. Try again.")


def add_task():
    task=input("Enter task:")
    date=get_valid_date()
    with open("task.txt","a")as file:
        file.write(f"{date}-{task}\n")
    print("Task saved!")

def view_task():
    try:
        with open("task.txt","r") as file:
            tasks=file.readlines()
            if not tasks:
                print("NO TASKS FOUND!")
            else:
                print("\n YOUR TASKS:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}.{task.strip()}")
    except FileNotFoundError:
                print("No tasks file found.")

def add_mood():
     mood=input("How are you feeling today?")
     date=get_valid_date()
     with open("mood_log.txt","a") as file:
          file.write(f"{date}-{mood}\n")
     print("MOOD SAVED!")

def view_moods():
    try:
        with open("mood_log.txt", "r") as file:
            moods = file.readlines()

        if not moods:
            print("No moods recorded.")
        else:
            print("\nYour Mood History:")
            for i, mood in enumerate(moods, start=1):
                print(f"{i}. {mood.strip()}")

    except FileNotFoundError:
        print("No mood file found.")


while True:
     print("\n--- DAILY TRACKER---")
     print("1. Add Task")
     print("2. View Tasks")
     print("3. Add Mood")
     print("4. View Moods")
     print("5. Exit")

     choice=input("Choose an option:")

     if choice=="1":
          add_task()
     elif choice=="2":
          view_task()
     elif choice=="3":
          add_mood()
     elif choice=="4":
          view_moods()
     elif choice=="5":
          print("goodbye!")
          break
     else:
          print("Invalid choice. Try again")
