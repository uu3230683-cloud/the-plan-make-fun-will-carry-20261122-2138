#!/usr/bin/env python3
"""Write the 30-day plan for turning $100 into money to /output/entry.txt."""

import os

PLAN = (
    "Day 1-2: spend $40 on API credits + $10 domain; build a niche tool, e.g. "
    "PDF-to-Excel converter. Day 3-7: launch on Product Hunt, Reddit, X; charge "
    "$9/mo via Stripe. Day 8-30: ship daily, raise price to $12 at 20 users, "
    "reinvest revenue in ads. Expect 30-60 users = $270-720/mo."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
