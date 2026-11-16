# Railway Reservation Analyzer
# A beginner-friendly project using Pandas and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

print("RAILWAY RESERVATION ANALYZER")

# Enter a file name, or press Enter to use the sample file.
file_name = input("Enter CSV file name (press Enter for bookings.csv): ").strip()

if file_name == "":
    file_name = "bookings.csv"

# Read the CSV file. Show a message if the file is not present.
try:
    data = pd.read_csv(file_name)
except FileNotFoundError:
    print("Error: File '" + file_name + "' not found.")
    raise SystemExit

# Check that all required columns are present.
data.columns = data.columns.str.strip()
required_columns = ["PNR", "Train", "Class", "Fare", "Status"]

missing_column = False
for column in required_columns:
    if column not in data.columns:
        print("Error: Column '" + column + "' is missing.")
        missing_column = True

if missing_column:
    raise SystemExit

# Remove extra spaces and convert Fare values into numbers.
for column in ["PNR", "Train", "Class", "Status"]:
    data[column] = data[column].fillna("").astype(str).str.strip()

data["Status"] = data["Status"].str.title()
data["Fare"] = pd.to_numeric(data["Fare"], errors="coerce")

# A row is invalid if important details are missing or incorrect.
valid_status = ["Confirmed", "Waiting", "Cancelled"]
invalid_rows = data[
    (data["PNR"] == "") |
    (data["Train"] == "") |
    (data["Class"] == "") |
    (data["Fare"].isna()) |
    (data["Fare"] < 0) |
    (~data["Status"].isin(valid_status))
]

# Print a warning and skip each invalid row.
for index, row in invalid_rows.iterrows():
    if pd.isna(row["Fare"]) or row["Fare"] < 0:
        print("Warning: Row with PNR " + row["PNR"] + " skipped - invalid fare.")
    else:
        print("Warning: Row with PNR " + row["PNR"] + " skipped - invalid data.")

data = data.drop(invalid_rows.index)

print("\nValid records analyzed:", len(data))

# Count tickets by status.
status_count = data["Status"].value_counts()
print("\nBooking status count:")
print("Confirmed:", status_count.get("Confirmed", 0))
print("Waiting:", status_count.get("Waiting", 0))
print("Cancelled:", status_count.get("Cancelled", 0))

# Show the menu.
print("\nMENU")
print("1. Bookings per train")
print("2. Revenue per train (Confirmed tickets only)")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    # Count all valid bookings for each train.
    bookings_per_train = data.groupby("Train")["PNR"].count()

    print("\nBookings per train:")
    for train, count in bookings_per_train.items():
        print(train + " : " + str(count))
    print("Total bookings:", bookings_per_train.sum())

    # Draw and save a bar chart.
    bookings_per_train.plot(kind="bar")
    plt.title("Bookings per Train")
    plt.xlabel("Train")
    plt.ylabel("Number of Bookings")
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()

elif choice == "2":
    # Use only Confirmed tickets when calculating revenue.
    confirmed_data = data[data["Status"] == "Confirmed"]
    revenue_per_train = confirmed_data.groupby("Train")["Fare"].sum()

    print("\nConfirmed revenue per train:")
    for train, revenue in revenue_per_train.items():
        print(train + " : Rs. " + str(int(revenue)))
    print("Total confirmed revenue: Rs.", int(revenue_per_train.sum()))

    # Draw and save a bar chart.
    revenue_per_train.plot(kind="bar")
    plt.title("Confirmed Revenue per Train")
    plt.xlabel("Train")
    plt.ylabel("Revenue (Rs.)")
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.show()

else:
    print("Invalid choice. Please run the program again and enter 1 or 2.")
