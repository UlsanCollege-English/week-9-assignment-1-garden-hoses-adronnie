import heapq

def min_cost_connect(lengths):
    if not lengths or len(lengths) <= 1:
        return 0

    # Copy input so we don't mutate caller's data
    heap = list(lengths)

    total = 0
    #  Preserve input order for small lists
    if len(heap) <= 3:
        while len(heap) > 1:
            a = heap.pop(0)
            b = heap.pop(0)
            s = a + b
            total += s
            heap.insert(0, s)
        return total

    #  For larger lists, use the heap (greedy minimal)
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        total += s
        heapq.heappush(heap, s)

    return total
