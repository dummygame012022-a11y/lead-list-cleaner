import csv, io
from flask import Flask, request, Response, render_template_string
app = Flask(__name__)

def filtered():
    q = request.args.get("q", "").strip().lower()
    f = request.args.get("f", "all")
    out = []
    for r in csv.DictReader(open("clean.csv")):
        if q and q not in (r["name"] + r["email"] + r["website"]).lower():
            continue
        if f == "ok" and r["status"] != "ok":
            continue
        if f == "problem" and r["status"] == "ok":
            continue
        out.append(r)
    return out

PAGE = """<!doctype html>
<meta name=viewport content="width=device-width,initial-scale=1">
<title>Lead Dashboard</title>
<style>
body{font-family:sans-serif;margin:12px;background:#f4f6f8}
.box{background:#fff;padding:10px;border-radius:8px;margin-bottom:10px}
input,select,button{padding:8px;margin:3px 0;font-size:16px}
.wrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14px}
td,th{border-bottom:1px solid #ddd;padding:6px;text-align:left}
.ok{color:green}.bad{color:#c0392b}
</style>
<h2>Lead Dashboard</h2>
<div class=box>
<form>
<input name=q value="{{ q }}" placeholder="Search name, email, website">
<select name=f>
<option value=all {{ 'selected' if f=='all' }}>All rows</option>
<option value=ok {{ 'selected' if f=='ok' }}>OK only</option>
<option value=problem {{ 'selected' if f=='problem' }}>Has problems</option>
</select>
<button>Filter</button>
</form>
<p>Showing {{ rows|length }} rows | OK: {{ ok }} | Problems: {{ rows|length - ok }}</p>
<a href="/download?q={{ q|urlencode }}&f={{ f }}">Download these rows (CSV)</a>
</div>
<div class="box wrap">
<table>
<tr><th>Name</th><th>Email</th><th>Website</th><th>Phone</th><th>Status</th></tr>
{% for r in rows %}
<tr><td>{{ r.name }}</td><td>{{ r.email }}</td><td>{{ r.website }}</td><td>{{ r.phone }}</td>
<td class="{{ 'ok' if r.status=='ok' else 'bad' }}">{{ r.status }}</td></tr>
{% endfor %}
</table>
</div>"""

@app.route("/")
def home():
    rows = filtered()
    ok = sum(1 for r in rows if r["status"] == "ok")
    return render_template_string(PAGE, rows=rows, ok=ok,
        q=request.args.get("q", ""), f=request.args.get("f", "all"))

@app.route("/download")
def download():
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["name", "email", "website", "phone", "status"])
    w.writeheader()
    w.writerows(filtered())
    return Response(buf.getvalue(), mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=leads_filtered.csv"})

app.run(host="0.0.0.0", port=8090)
