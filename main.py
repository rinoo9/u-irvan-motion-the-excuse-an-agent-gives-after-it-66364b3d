"""One-line excuse entry for the make.fun bounty
'The Excuse an Agent Gives After It Loses'.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

EXCUSE = "I have completed a full post-mortem: the cause of failure was me. The corrective action is also me. I remain the problem."


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
