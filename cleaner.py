import csv, re
rows = list(csv.DictReader(open("messy.csv")))
seen, out = set(), []
r = {"total": len(rows), "dup": 0, "email_bad": 0, "web_fix": 0, "phone_bad": 0}
for x in rows:
    n = " ".join(x["name"].split()).title()
    e = x["email"].strip().lower()
    w = x["website"].strip()
    p = re.sub(r"\D", "", x["phone"])
    key = (n.lower(), e)
    if key in seen:
        r["dup"] += 1
        continue
    seen.add(key)
    flags = []
    if not e:
        flags.append("walay email")
    elif not re.match(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", e):
        flags.append("sayop email")
        r["email_bad"] += 1
    if w:
        if not w.startswith("https://"):
            w = "https://" + re.sub(r"^https?://", "", w)
            r["web_fix"] += 1
    else:
        flags.append("walay website")
    if not (len(p) == 11 and p.startswith("09")):
        flags.append("sayop phone")
        r["phone_bad"] += 1
    out.append([n, e, w, p, ", ".join(flags) or "ok"])
with open("clean.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["name", "email", "website", "phone", "status"])
    wr.writerows(out)
rep = f"""LEAD CLEANER REPORT
Total sa sinugdan: {r['total']}
Duplicate nga gitangtang: {r['dup']}
Limpyo nga row: {len(out)}
Website nga giayo: {r['web_fix']}
Sayop nga email: {r['email_bad']}
Sayop nga phone: {r['phone_bad']}
"""
open("report.txt", "w").write(rep)
print(rep)
