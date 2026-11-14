import shutil, sqlite3
shutil.copy("leads.db", "practice.db")
db = sqlite3.connect("practice.db")
print("Tables: leads(name,email,website,phone,status), industry(name,type)")
print("Empty ENTER = next task\n")
tasks = [
    "1. Show 5 leads sorted by name Z to A (ORDER BY ... DESC, LIMIT)",
    "2. Show names that appear more than once, with their count (GROUP BY + HAVING)",
    "3. UPDATE: set status to 'fixed' where email = 'anapharmacy@gmail'",
    "4. DELETE the rows where status LIKE '%missing email%', then count the rest",
]
for t in tasks:
    print(t)
    while True:
        sql = input("SQL> ").strip()
        if not sql:
            break
        try:
            cur = db.execute(sql)
            for row in cur:
                print(row)
            db.commit()
            if cur.rowcount > 0:
                print("rows changed:", cur.rowcount)
        except Exception as e:
            print("Error:", e)
