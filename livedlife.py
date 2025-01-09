import matplotlib.pyplot as plt
from tqdm import tqdm
from datetime import datetime


def calculate_year_percentage():
    today = datetime.now()
    start_of_year = datetime(today.year, 1, 1)
    end_of_year = datetime(today.year, 12, 31)
    year_progress = (today - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()
    return round(year_progress * 100, 2)


def calculate_lifetime_percentage(age, average_lifetime=80):
    lifetime_progress = age / average_lifetime
    return round(lifetime_progress * 100, 2)


def display_progress_bar(percentage, label):
    print(f"{label}:")
    for _ in tqdm(range(int(percentage)), desc=f"{label} ({percentage}%)", ncols=60):
        pass


def display_pie_chart(percentages, labels, title):
    colors = ['#66c2a5', '#fc8d62']
    plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(title)
    plt.show()


def main():
    # Calculate year percentage
    year_percentage = calculate_year_percentage()

    # Input age and calculate lifetime percentage
    try:
        age = float(input("Enter your age: "))
        average_lifetime = float(input("Enter the average lifetime (default is 80 years): ") or 80)
        lifetime_percentage = calculate_lifetime_percentage(age, average_lifetime)

        # Display progress bars
        display_progress_bar(year_percentage, "Percentage of the year passed")
        display_progress_bar(lifetime_percentage, "Percentage of lifetime passed")

        # Display pie charts
        display_pie_chart(
            [year_percentage, 100 - year_percentage],
            ['Passed', 'Remaining'],
            "Current Year Progress"
        )
        display_pie_chart(
            [lifetime_percentage, 100 - lifetime_percentage],
            ['Lived', 'Remaining'],
            "Lifetime Progress"
        )

    except ValueError:
        print("Invalid input. Please enter valid numbers for age and average lifetime.")


if __name__ == "__main__":
    main()