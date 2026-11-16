# Railway Reservation Analyzer

## About the project
This is a small beginner-level Python project. It reads railway ticket details from a CSV file, checks the rows, counts bookings, calculates revenue from confirmed tickets, and draws a bar chart.

## Files in this repository

- `one.py` — main Python program.
- `bookings.csv` — the sample data from the project question.
- `test_cases/` — four separate CSV files used for testing.
- `screenshots/` — VS Code-style previews of the four test runs.
- `Summary.md` — explanation of the program, difficulties faced, and test results.
- `requirements.txt` — Python libraries needed by the project.

## Requirements

Python 3, Pandas, and Matplotlib are required. Open the VS Code terminal in this project folder and run:

```bash
python -m pip install -r requirements.txt
```

## How to run

1. Open this folder in Visual Studio Code.
2. Open `one.py`.
3. Open the terminal using **Terminal → New Terminal**.
4. Run:

```bash
python one.py
```

5. At the first prompt, type `bookings.csv` or press Enter to use the sample file.
6. Choose `1` for bookings per train or `2` for confirmed revenue per train.

A bar chart is displayed and also saved as `chart.png` in the project folder.

## Run the four test cases

Run `python one.py` separately for each test. At the file-name prompt, enter the CSV path shown below. Enter the menu choice shown in the table.

| Test case | CSV file to enter | Menu choice | Expected result |
|---|---|---:|---|
| TC1 – Normal input | `bookings.csv` | `1` | Gondwana 4, Rajdhani 3, Shatabdi 3; total 10 |
| TC2 – Boundary input | `test_cases/TC2_Boundary/bookings.csv` | `2` | Shatabdi Rs. 950; total Rs. 950 |
| TC3 – Invalid input | `test_cases/TC3_Invalid/bookings.csv` | `1` | PNR 1011 is skipped; 10 valid records remain |
| TC4 – Revenue scenario | `test_cases/TC4_Revenue/bookings.csv` | `2` | Rajdhani Rs. 4100, Gondwana Rs. 2540, Shatabdi Rs. 1900; total Rs. 8540 |

For the missing-file part of TC3, run the program once more and enter `missing.csv` at the file-name prompt. It displays a file-not-found message and safely stops.

## Notes

- Option 1 counts all valid tickets, including Confirmed, Waiting, and Cancelled tickets.
- Option 2 adds only fares whose status is `Confirmed`.
- Invalid rows are skipped instead of stopping the whole program.
