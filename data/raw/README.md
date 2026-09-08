# `data/raw/` — dataset provenance

Every dataset directory here must include a `SOURCE.md` with:

```markdown
# <dataset name>

- **Source:** where it came from (URL, database, accession number)
- **License / terms of use:** e.g. public domain, CC-BY, dbGaP-controlled, synthetic
- **Collected/generated:** date, and if synthetic, how it was generated
- **PHI/PII status:** none / de-identified / synthetic — confirm before use in a lab
- **Used in:** which lab(s) or lecture(s) reference this file
```

Raw data files themselves are gitignored (see root `.gitignore`) — only
`SOURCE.md` and small schema/sample files are tracked. Large or
restricted-access datasets should be fetched via a documented download
script, not committed.

## Open item

No datasets have been added yet. As labs are built (Phase 3), each lab's
dataset gets a subfolder here with its `SOURCE.md`.
