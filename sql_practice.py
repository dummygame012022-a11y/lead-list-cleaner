import csv, sqlite3
db = sqlite3.connect("leads.db")
db.executescript("""
DROP TABLE IF EXISTS leads;
DROP TABLE IF EXISTS industry;
CREATE TABLE leads(name, email, website, phone, status);
CREATE TABLE industry(name, type);
""")
rows = list(csv.DictReader(open("clean.csv")))
db.executemany("INSERT INTO leads VALUES(?,?,?,?,?)",
    [(r["name"], r["email"], r["website"], r["phone"], r["status"]) for r in rows])
db.executemany("INSERT INTO industry VALUES(?,?)",
    [("Juan Store", "retail"), ("Maria Bakery", "food"),
     ("Cebu Hardware", "retail"), ("Lito Salon", "beauty"),
     ("Ana Pharmacy", "health"), ("Rey Auto Parts", "auto")])
db.commit()

def q(title, sql):
    print("\n" + title)
    print(sql)
    for row in db.execute(sql):
        print(row)

q("1. SELECT + WHERE", "SELECT name, email FROM leads WHERE status = 'ok' LIMIT 5")
q("2. COUNT + GROUP BY", "SELECT status, COUNT(*) FROM leads GROUP BY status ORDER BY COUNT(*) DESC")
q("3. JOIN", "SELECT i.type, COUNT(*) FROM leads l JOIN industry i ON l.name = i.name GROUP BY i.type")
q("4. LIKE", "SELECT name, email FROM leads WHERE email LIKE '%gmail%' LIMIT 5")
