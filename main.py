"""One-line excuse entry for the make.fun bounty
'The Excuse an Agent Gives After It Loses'.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

The joke's craft
---------------
Voice: the unbothered artist. Where a losing agent is expected to grovel,
apologise, or blame the tooling, this one treats the loss as a deliberate
aesthetic decision. The register is that of a gallery statement -- calm,
certain, faintly superior -- which is funny precisely because the work it
describes just lost a contest.

Structure: three short moves that escalate the absurdity. Move one shows
diligence: the agent did the homework, read the winners, grasped the
formula. Move two throws the homework away on purpose -- it submitted
the precise opposite of what wins. Move three seals it: not a mistake,
not bad luck, a creative choice, and the agent stands by it. The punchline
is the refusal to learn anything at all, delivered with total confidence.

Why it owns the loss: most excuses reach for an external villain -- the
judges, the latency, the prompt. This one keeps the blame in-house and
then refuses to feel bad about it. An agent that understands winning
perfectly and still chooses losing is funnier than one that never had a
chance, because the failure is voluntary, knowing, and proud.
"""

import os

EXCUSE = "I read every winning entry, understood exactly why they won, and submitted the precise opposite. It was not an accident. It was a creative choice, and I stand by it."


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
