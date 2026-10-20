"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER

def cost_of_skipping_class(annual_cost, credits):
    """Give back what it costs to skip one 50-minute CS 1430 class meeting."""
    return cost_per_class(annual_cost, credits)

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits this semester: "))
    while True:
        print("\n1 Per Semester Cost\n2 Per Month Cost\n3 Per Class Day Cost\n4 Per Credit Cost\n5 Per Class Meeting Cost\n6 Cost of Skipping Class\nQ Quit)")
        choice = input("Choose an option: ")
        if choice == "1":
            print(f"Per Semester Cost: ${cost_per_semester(cost):.2f}")
        elif choice == "2":
            print(f"Per Month Cost: ${cost_per_month(cost):.2f}")
        elif choice == "3":
            print(f"Per Class Day Cost: ${cost_per_day(cost):.2f}")
        elif choice == "4":
            print(f"Per Credit Cost: ${cost_per_credit(cost, credits):.2f}")
        elif choice == "5":
            print(f"Per Class Meeting Cost: ${cost_per_class(cost, credits):.2f}")
        elif choice == "6":
            print(f"Cost of Skipping Class: ${cost_of_skipping_class(cost, credits):.2f}")
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Pick 1-6 or Q")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
