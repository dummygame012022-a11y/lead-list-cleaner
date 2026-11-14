import csv, random
names = ["Juan Store", "Maria Bakery", "Cebu Hardware", "Lito Salon", "Ana Pharmacy", "Rey Auto Parts"]
rows = []
for i in range(60):
    n = random.choice(names)
    n = random.choice([n, n.upper(), "  " + n + "  ", n.lower()])
    e = n.strip().lower().replace(" ", "") + "@" + random.choice(["gmail.com", "yahoo.com", "mail", "gmail"])
    w = random.choice(["www.site.com", "http://shop.ph", "https://ok.com", ""])
    p = random.choice(["0917 123 4567", "09171234567", "", "123"])
    if random.random() < 0.1:
        e = ""
    rows.append([n, e, w, p])
rows += rows[:8]
with open("messy.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "email", "website", "phone"])
    wr.writerows(rows)
print("messy.csv:", len(rows), "rows")
