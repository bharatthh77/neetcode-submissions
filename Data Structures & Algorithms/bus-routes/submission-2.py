class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_routes = defaultdict(list)
        for i, r in enumerate(routes):
            for s in r:
                stop_to_routes[s].append(i)
        
        print(stop_to_routes)
        q = deque([(source, 0)])            # (stop, buses_boarded_so_far)
        seen_stops, seen_routes = {source}, set()
        while q:
            stop, buses = q.popleft()
            for ri in stop_to_routes[stop]:      # boarding a loop = +1 bus
                if ri in seen_routes:
                    continue
                seen_routes.add(ri)              # whole route visited once
                for nxt in routes[ri]:
                    if nxt == target:
                        return buses + 1
                    if nxt not in seen_stops:
                        seen_stops.add(nxt)
                        q.append((nxt, buses + 1))
        return -1




