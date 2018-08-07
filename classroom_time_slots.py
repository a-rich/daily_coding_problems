from __future__ import print_function
import heapq
import random
from timeit import timeit

def count_classrooms_naive(time_slots):
    time_slots.sort(key=lambda x: x[0])
    class_room_count = 1
    classrooms = []

    while time_slots:
        class_ = time_slots.pop(0)
        if classrooms:
            scheduled_class = classrooms[0]
            if scheduled_class[1] > class_[0]:
                class_room_count += 1
            else:
                classrooms.pop(0)
        classrooms.append(class_)
        classrooms.sort(key=lambda x: x[1])

    return class_room_count

def count_classrooms(time_slots):
    time_slots.sort(key=lambda x: x[0])
    class_room_count = 1
    classrooms = []
    heapq.heapify(classrooms)

    while time_slots:
        class_ = time_slots.pop(0)
        if classrooms:
            scheduled_end_time = classrooms[0]
            if scheduled_end_time > class_[0]:
                class_room_count += 1
            else:
                heapq.heappop(classrooms)
        heapq.heappush(classrooms, class_[1])

    return class_room_count

if __name__ == '__main__':
    # Assert the correctness of the two solutions.
    time_slots = [(0,50), (30,75), (60,150)]
    assert count_classrooms(list(time_slots)) == 2 \
            and count_classrooms_naive(list(time_slots)) == 2

    time_slots = [(0,10), (5,35), (10,40), (30, 75), (80,100)]
    assert count_classrooms(list(time_slots)) == 3 \
            and count_classrooms_naive(list(time_slots)) == 3

    time_slots = [(0,10), (5,35), (10,40), (30, 75), (70,100), (35,85), (70, 95)]
    assert count_classrooms(list(time_slots)) == 4 \
            and count_classrooms_naive(list(time_slots)) == 4

    # Verify the efficiency of the optimal solution.
    classes, max_length = 100000, 100
    time_slots = [[random.randint(0, classes*max_length)] for _ in range(classes)]
    for time_slot in time_slots:
        time_slot.append(random.randint(time_slot[0], time_slot[0]+max_length))

    naive_time = timeit('count_classrooms_naive(time_slots)', 'from __main__ import count_classrooms_naive, time_slots', number=100)
    optimal_time = timeit('count_classrooms(time_slots)', 'from __main__ import count_classrooms, time_slots', number=100)

    print('Naive time: {}\nOptimal time: {}'.format(naive_time, optimal_time))
