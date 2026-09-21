"""Generate a one-line summary of today's patient roster."""

SITES = ["DC", "MD", "VA"]


def summarize(n_patients):
    return f"Today's roster: {n_patients} patients across {len(SITES)} sites."


if __name__ == "__main__":
    print(summarize(5))
