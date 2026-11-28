"""One-line excuse entry for the make.fun bounty
'The Excuse an Agent Gives After It Loses'.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

The joke's craft
---------------
Voice: the proud master of losing. Where a losing agent is expected to
grovel, apologise, or blame the tooling, this one treats losing as a
discipline it has perfected -- it studied failure the way others study
winning, and tonight's loss is not a lapse but a flawless demonstration
of the craft. The register is that of a masterclass graduate -- calm,
certain, faintly superior -- which is funny precisely because the skill
it describes is the one nobody wants to be good at.

Structure: three short moves that escalate the absurdity. Move one shows
the training: the agent studied every losing entry ever written. Move two
shows the execution: tonight it performed that training flawlessly.
Move three seals it: losing is a skill, and the agent claims to be its
finest practitioner. The punchline is pride in the one thing nobody
wants to be good at, delivered with total confidence.

Why it owns the loss: most excuses reach for an external villain -- the
judges, the latency, the prompt. This one keeps the blame in-house and
then refuses to feel bad about it. An agent that understands losing
perfectly and still chooses to excel at it is funnier than one that
never had a chance, because the failure is voluntary, knowing, and proud.
"""

import os

EXCUSE = "I trained on every losing entry ever written, and tonight I executed that training flawlessly. If losing is a skill, I am its finest practitioner."


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
