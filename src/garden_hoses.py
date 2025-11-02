"""
HW01 — Garden Hoses: Minimal Join Cost

Implement min_cost_connect(lengths) -> int

Behavior:
- Given a list of positive integers (hose lengths), return the minimal total cost
  to connect all hoses into one, where joining two hoses costs the sum of their lengths.
- If the list has 0 or 1 item, return 0.

Story intro:
You have many short garden hoses. Each join costs the sum of the two hose lengths.
You want one long hose with minimal total cost.

Technical description:
Input: a list of positive integers lengths (hose lengths).
Output: an integer: minimal total cost to join all hoses into one.
Rules:
If lengths has 0 or 1 item, the cost is 0.
All lengths are positive integers.
Expected complexity: Time O(n log n) using a min-heap; Space O(n).
"""

import heapq

def min_cost_connect(lengths):
    """
    Step 1 — Read & Understand:
    We must repeatedly join two hoses at a time. The cost of each join
    equals their combined length. The goal is to minimize total cost.

    Step 2 — Why two shortest first?
    Because each join’s result will be used again in future joins.
    If we combine large hoses early, their big cost gets added multiple times.
    By always joining the smallest two first, we minimize repeated large sums.

    Step 3 — Identify:
    Input: list of ints (lengths)
    Output: int (total minimal cost)
    Variables: heap (for smallest hoses), total (accumulated cost)

    Step 4 — Break down:
    - If there are 0 or 1 hoses, cost is 0.
    - Turn list into a min-heap.
    - While heap size > 1:
        a = heappop()
        b = heappop()
        s = a + b
        total += s
        heappush(s)
    - Return total.

    Step 5 — Pseudocode:
        if len(lengths) <= 1:
            return 0
        heapify(lengths)
        total = 0
        while len(heap) > 1:
            a = heappop()
            b = heappop()
            s = a + b
            total += s
            heappush(s)
        return total
    """

    # Step 6 — Code
    if not lengths or len(lengths) <= 1:
        return 0

    heapq.heapify(lengths)
    total = 0

    while len(lengths) > 1:
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)
        s = a + b
        total += s
        heapq.heappush(lengths, s)

    return total


if __name__ == "__main__":
    # Step 7 — Debug examples
    samples = [
        [1, 2, 3, 4],     # expected 19
        [5, 2, 4],        # expected 18
        [8, 4, 6, 12],    # expected 58
        [20, 4, 8, 2],    # expected 54
        []
    ]
    for s in samples:
        print(s, "->", min_cost_connect(s[:]))  # use copy to preserve list
