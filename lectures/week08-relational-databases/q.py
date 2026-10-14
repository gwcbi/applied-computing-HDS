#!/usr/bin/env python3
"""Week 8 demo runner: show a query, then run it. No copy-paste, no window switching.

  python3 q.py list        list the demo blocks
  python3 q.py 4b          print block 4b from demo_queries.sql, then run it
  python3 q.py clip        run whatever SQL is on the clipboard (macOS pbpaste)
  python3 q.py file X.sql  run the SQL in file X.sql

Tip: alias q='python3 q.py'   then just type:  q 4b
"""
import re, shutil, subprocess, sys, sqlite3
DB, SQL = "demo_cohort.db", "demo_queries.sql"
BOLD, CYAN, DIM, OFF = "\033[1m", "\033[36m", "\033[2m", "\033[0m"

def blocks():
    out, key = {}, None
    for line in open(SQL):
        m = re.match(r"^-- (\w+)\. (.*)", line)
        if m:
            key = m.group(1); out[key] = {"title": m.group(2).strip(), "sql": []}
        elif key and not line.startswith("--"):
            out[key]["sql"].append(line.rstrip("\n"))
    for b in out.values():
        b["sql"] = "\n".join(b["sql"]).strip()
    return out

def run(sql, title=None):
    print()
    if title: print(f"{BOLD}-- {title}{OFF}")
    print(f"{CYAN}{sql}{OFF}\n")
    if shutil.which("sqlite3"):
        subprocess.run(["sqlite3", "-header", "-column", DB], input=sql + "\n", text=True)
    else:                                   # fallback: Python's sqlite3, plain columns
        con = sqlite3.connect(DB)
        for stmt in [s for s in sql.split(";") if s.strip()]:
            cur = con.execute(stmt)
            if cur.description:
                cols = [d[0] for d in cur.description]; rows = cur.fetchall()
                w = [max(len(str(x)) for x in [c] + [r[i] for r in rows]) for i, c in enumerate(cols)]
                print("  ".join(c.ljust(w[i]) for i, c in enumerate(cols)))
                for r in rows: print("  ".join(str(x).ljust(w[i]) for i, x in enumerate(r)))
    print()

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "list"
    B = blocks()
    if arg == "list":
        for k, b in B.items(): print(f"  {BOLD}{k:3}{OFF} {b['title']}")
    elif arg == "clip":
        run(subprocess.run(["pbpaste"], capture_output=True, text=True).stdout.strip(), "from clipboard")
    elif arg == "file":
        run(open(sys.argv[2]).read().strip(), sys.argv[2])
    elif arg in B:
        run(B[arg]["sql"], f"{arg}. {B[arg]['title']}")
    else:
        sys.exit(f"no block '{arg}'. Try: python3 q.py list")
