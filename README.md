# Lead List Cleaner

Python script that cleans a messy lead list CSV (company, email, website, phone).

## What it does
- Removes duplicate rows
- Trims extra spaces and fixes name casing
- Validates email and phone format
- Adds https:// to websites
- Flags missing or invalid fields in a status column
- Saves clean.csv and report.txt

## Before
    JUAN STORE  ,juanstore@gmail,www.site.com,0917 123 4567
    Ana Pharmacy,,,123

## After
    Juan Store,juanstore@gmail,https://www.site.com,09171234567,invalid email
    Ana Pharmacy,,,123,"missing email, missing website, invalid phone"

## Sample result
    Total rows: 68 | Duplicates removed: 44 | Clean rows: 24
    Websites fixed: 10 | Invalid emails: 9 | Invalid phones: 15

## How to run
    python make_data.py   (creates a fake messy.csv)
    python cleaner.py     (creates clean.csv and report.txt)

Sample data is fake. Python 3 only, no extra packages.
![Result](result.png)
