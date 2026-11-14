import sqlite3
db = sqlite3.connect("leads.db")
print("Tables: leads(name,email,website,phone,status), industry(name,type)")
print("Gawas: ENTER nga blangko\n")
tasks = [
    "1. Ihap ang leads nga naay 'missing website'",
    "2. Ipakita ang Cebu Hardware nga 'ok' ang status",
    "3. Ihap ang leads kada type nga 'ok' ra (JOIN + WHERE)",
]
for t in tasks:
    print(t)
    while True:
        sql = input("SQL> ").strip()
        if not sql:
            break
        try:
            for row in db.execute(sql):
                print(row)
        except Exception as e:
            print("Sayop:", e)
