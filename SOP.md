# SOP: Cleaning a Lead List

Version 1.1 | Owner: Edison Paracuelles

## Purpose
Turn a messy lead list (CSV) into a clean list with a status for each row, so the client can use only good leads.

## Before you start
- Have the messy file ready (example: messy.csv)
- Columns needed: name, email, website, phone
- Never edit the original file. Work on a copy.

## Steps
1. Put the messy CSV in the project folder.
2. Run the cleaner:

       python cleaner.py

3. Read the printed summary: total rows, duplicates removed, clean rows.
4. Open clean.csv. Duplicates are removed (same name + same email).
5. Check the status column of each row:
   - ok
   - invalid email
   - missing email
   - missing website
   - invalid phone
6. Optional: view the results in the dashboard:

       python dashboard.py

   Open http://127.0.0.1:8090 and use search, filter and CSV download.
7. Send the client the filtered CSV (ok rows, or problem rows if they want to fix them).

## Checks before sending
- Total rows in = duplicates removed + rows out
- No empty file
- Spot check 5 random rows by hand
- Status column is present on every row

## Known limits
- Same name with different emails is kept as separate rows (by design).
- Phone check is simple. Review phones by hand if the client needs exact formats.

## Example result
68 rows in, 44 duplicates removed, 24 rows out.

## Change log
| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-11-14 | First version: cleaner and status column |
| 1.1 | 2026-11-14 | Added dashboard (search, filter, CSV download) |
