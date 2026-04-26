from model import Subject
from scheduler import generate_schedule
from database import create_table, save_schedule

def main():
    print("📚 AI Study Schedule Generator\n")

    n = int(input("Enter number of subjects: "))
    subjects = []

    for _ in range(n):
        name = input("Subject name: ")
        difficulty = int(input("Difficulty (1-Easy, 2-Medium, 3-Hard): "))
        weak = input("Is this a weak subject? (y/n): ").lower() == 'y'
        
        subjects.append(Subject(name, difficulty, weak))

    hours_per_day = float(input("\nAvailable study hours per day: "))
    days = int(input("Number of days to plan: "))
    days_left = int(input("Days left for exam: "))

    schedule = generate_schedule(subjects, hours_per_day, days, days_left)

    print("\n📅 Your Study Plan:\n")

    for i, day in enumerate(schedule, start=1):
        print(f"Day {i}:")
        for subject, time in day.items():
            print(f"  {subject}: {time}")
        print()

    # Save to database
    create_table()
    save_schedule(schedule)

    print("✅ Schedule saved to database!")

if __name__ == "__main__":
    main()