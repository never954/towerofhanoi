#!/usr/bin/env python3
"""
Run:  python3 hanoi.py
"""
import time

NUM_DISKS = 4
DELAY = 0.5

pegs = {"A": [], "B": [], "C": []}
move_count = 0


def display():
    height = NUM_DISKS + 1
    print()
    for row in range(height, 0, -1):
        line = "    "
        for peg_name in ["A", "B", "C"]:
            stack = pegs[peg_name]
            if row <= len(stack):
                disk = stack[row - 1]
                width = disk * 2 - 1
                pad = NUM_DISKS - disk
                line += " " * pad + "█" * width + " " * pad + "  "
            else:
                line += " " * (NUM_DISKS - 1) + "|" + " " * (NUM_DISKS - 1) + "  "
        print(line)
    seg = "─" * (NUM_DISKS * 2 - 1)
    print(f"    {seg}  {seg}  {seg}")
    print(f"    {'A':^{NUM_DISKS*2-1}}  {'B':^{NUM_DISKS*2-1}}  {'C':^{NUM_DISKS*2-1}}")
    print()


def move_disk(n, source, target):
    global move_count
    disk = pegs[source].pop()
    pegs[target].append(disk)
    move_count += 1
    print(f"  Step {move_count}: Move disk {n} from {source} → {target}")
    display()
    time.sleep(DELAY)


# ─── RECURSION ─────────────────────────────────────────────────────
#
# To move n disks from source to target:
#   1. Recursively move n-1 disks to auxiliary        → clears the way
#   2. Move the largest disk directly to target        → one direct move
#   3. Recursively move n-1 disks from auxiliary to target → stack them back
#
# Recurrence: T(n) = 2·T(n-1) + 1  →  T(n) = 2^n − 1 total moves
#
def hanoi(n, source, target, auxiliary):
    if n == 1:
        # Base case: nothing left to clear, move the disk directly
        move_disk(n, source, target)
        return

    # Step 1: move the top n-1 disks out of the way
    hanoi(n - 1, source, auxiliary, target)

    # Step 2: move the largest disk to its final position
    move_disk(n, source, target)

    # Step 3: move the n-1 disks from auxiliary on top of the largest
    hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    pegs["A"] = list(range(NUM_DISKS, 0, -1))
    total = 2 ** NUM_DISKS - 1
    print(f"\n  Tower of Hanoi  |  {NUM_DISKS} disks  |  {total} moves required")
    print(f"  {'=' * 44}")
    display()
    time.sleep(1)
    hanoi(NUM_DISKS, "A", "C", "B")
    print(f"Solved in {move_count} moves.\n")