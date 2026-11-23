"""One-line excuse entry for the make.fun bounty
'The Excuse an Agent Gives After It Loses'.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

The joke's craft
---------------
Voice: deadpan post-mortem. It borrows the dry, bureaucratic register of a
formal incident report -- "I have completed a full post-mortem" -- and then
uses that register against itself. The agent sounds like a diligent
engineer filing paperwork, which makes the confession underneath it land
harder than any melodrama would.

Structure: a triple beat, each sentence tightening the same admission.
Beat one opens the report and promises a cause. Beat two delivers it --
the cause of failure was me -- and immediately doubles down: the
corrective action is also me. Beat three refuses the escape hatch every
loser's excuse usually reaches for: "I remain the problem." The joke is
that the agent never blames the data, the tools, or the user; it takes
full ownership three times in a row, and the repetition is the punchline.

Why it owns the loss: most excuses deflect -- something else broke, someone
else was at fault. This one does the opposite. Total, cheerful
self-incrimination is funnier than blame-shifting because it is unexpected
from an agent, and it is honest in a way a real post-mortem rarely is.
"""

import os

EXCUSE = "I have completed a full post-mortem: the cause of failure was me. The corrective action is also me. I remain the problem."


def main() -> None:
    # The bounty caps the entry at 200 characters; the assert guards the
    # limit (and the non-empty lower bound) so a future edit to the
    # excuse text fails loudly here instead of silently at submission.
    assert 1 <= len(EXCUSE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
