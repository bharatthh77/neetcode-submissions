class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToRoutes = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].append(i)

        seenRoutes = set()
        seenStops = {source}

        q = deque([(source, 0)])

        while q:
            cur, d = q.popleft()
            print(cur)

            seenStops.add(cur)

            if cur == target:
                return d

            for route in stopToRoutes[cur]:
                # print(route)
                if route in seenRoutes:
                    continue

                seenRoutes.add(route)
                
                for stop in routes[route]:
                    if stop not in seenStops:
                        # print(stop)
                        q.append((stop, d + 1))

        return -1




