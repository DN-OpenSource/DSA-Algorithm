"""Max number of non-overlapping intervals -- greedy by end time."""


def max_activities(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = float('-inf')
    chosen = []
    for s, e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
            chosen.append((s, e))
    return count, chosen


if __name__ == "__main__":
    A = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
         (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    print(max_activities(A))
