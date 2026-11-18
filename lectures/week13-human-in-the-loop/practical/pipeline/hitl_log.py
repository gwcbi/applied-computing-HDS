"""Tiny audit log for AI-assisted pipelines. One JSON object per line (JSONL).

    from hitl_log import log_event, read_log, sha
    log_event("audit_log.jsonl", step="extract", actor="ai:<model>", input_sha=sha(raw), output_sha=sha(out))
"""
import datetime, hashlib, json
from pathlib import Path


def sha(path_or_text):
    p = Path(str(path_or_text))
    data = p.read_bytes() if (len(str(path_or_text)) < 255 and p.exists()) else str(path_or_text).encode()
    return hashlib.sha256(data).hexdigest()[:12]


def log_event(logfile, step, actor, **fields):
    rec = {"ts": datetime.datetime.now().isoformat(timespec="seconds"), "step": step, "actor": actor, **fields}
    with open(logfile, "a") as f:
        f.write(json.dumps(rec) + "\n")
    return rec


def read_log(logfile):
    with open(logfile) as f:
        return [json.loads(line) for line in f if line.strip()]
