def compute_itinerary(flights, start):
    d = {}
    # O(n) -- n pairs of flights.
    for f in flights:
        if f[0] not in d:
            d[f[0]] = f[1]
        else:
            # O(nlogn) -- worst case is when 1 + n/2 flights make a cycle.
            # Could use a min heap to make this O(logn)
            d[f[0]] = [e for e in d[f[0]]] + [f[1]]
            d[f[0]].sort()
    # O(n^2logn) at this point.
    # Using a min heap would make this O(nlogn).

    flight_num = len(flights) + 1
    itinerary = []

    # O(n).
    while len(itinerary) < flight_num:
        itinerary.append(start)
        if start in d:
            if type(d[start]) is list:
                start = d[start].pop(0)
            else:
                start = d[start]
        elif len(itinerary) < flight_num:
            return None

    # O(n^2logn + n) = O(n^2logn).
    # Or with min heap: O(nlogn + n) = O(nlogn).
    return itinerary


if __name__ == '__main__':

    flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    start = 'YUL'
    assert compute_itinerary(flights, start) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    flights =  [('SFO', 'COM'), ('COM', 'YYZ')]
    start = 'COM'
    assert compute_itinerary(flights, start) is None

    flights = [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')]
    start = 'A'
    assert compute_itinerary(flights, start) == ['A', 'B', 'C', 'A', 'C']
