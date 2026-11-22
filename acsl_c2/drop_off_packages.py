import heapq


# def canDrop1(trips, capacity):
#     for t in trips:
#         if len(t) < 3:
#             return False
#     trips = sorted(trips, key=lambda x: x[1])
#     # now start stop sorted
#     tot = 0
#     # dict from stop to amount to unload
#     to_unload = {}
#     for t in trips:
#         next_capacity, start, end = t
#         if to_unload:
#             new_to_unload = {}
#             for e, amt in to_unload.items():
#                 if e <= start:
#                     tot -= amt
#                 else:
#                     new_to_unload[e] = amt
#             to_unload = new_to_unload
#         if next_capacity + tot > capacity:
#             return False
#         tot += next_capacity
#         to_unload[end] = to_unload.get(end, 0) + next_capacity
#     return True


# def canDrop(trips, capacity):
#     for t in trips:
#         if len(t) < 3:
#             return False
#     trips = sorted(trips, key=lambda x: x[2])
#     # now end stop sorted
#     tot = 0
#     start_idx = -1
#     for t in trips:
#         next_capacity, start, end = t
#         while start_idx >= 0 and trips[start_idx][2] <= start:
#             tot -= trips[start_idx][0]
#             start_idx += 1
#         tot += next_capacity
#         if tot > capacity:
#             return False
#         if start_idx == -1:
#             start_idx = 0
#     return True


def canDrop3(trips, capacity):
    for t in trips:
        if len(t) < 3:
            return False
    trips = sorted(trips, key=lambda x: x[1])
    # now start stop sorted
    tot = 0
    end_times = []
    for t in trips:
        next_capacity, start, end = t
        while end_times and end_times[0][0] <= start:
            tot -= end_times[0][1]
            heapq.heappop(end_times)
        tot += next_capacity
        if tot > capacity:
            return False
        heapq.heappush(end_times, (end, next_capacity))
    return True


# each item in trips is a package to pick up
# 2, 1, 5 is capacity 2, start stop 1 and end stop 5
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
expected = False
print(f"{expected} {canDrop(trips, capacity)}")

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 5
expected = True
print(f"{expected} {canDrop(trips, capacity)}")

trips = [[2, 1, 5], [3, 5, 7]]
capacity = 3
expected = True
print(f"{expected} {canDrop(trips, capacity)}")

trips = [[2, 1, 5], [3, 5, 7]]
capacity = 2
expected = False
print(f"{expected} {canDrop(trips, capacity)}")

trips = [[3, 2, 7], [3, 7, 9], [8, 3, 9]]
capacity = 11
expected = True
print(f"{expected} {canDrop(trips, capacity)}")

trips = [
    [5, 2, 5],  # Trip A: 5 people
    [5, 6, 9],  # Trip B: 5 people
    [3, 1, 10],  # Trip C: 3 people (The "Shadow")
]
capacity = 7
expected = False  # Because 5 + 3 = 8 at Mile 2
print(f"{expected} {canDrop(trips, capacity)}")


trips = [
    [5, 2, 5],  # Trip A: 5 people from 2 to 5
    [5, 6, 9],  # Trip B: 5 people from 6 to 9
    [2, 1, 10],  # Trip C: 2 people from 1 to 10 (The "Shadow")
]
capacity = 10
expected = True
print(f"{expected} {canDrop(trips, capacity)}")

# Capacity = 7
trips = [
    [3, 1, 4],  # Trip C: 3 people (Now ends at Mile 4)
    [5, 2, 5],  # Trip A: 5 people (Ends at Mile 5)
    [5, 6, 9],  # Trip B: 5 people (Ends at Mile 9)
]
capacity = 7
expected = False  # (At Mile 2, Trip C and Trip A are both on board: 3 + 5 = 8)
print(f"{expected} {canDrop(trips, capacity)}")
