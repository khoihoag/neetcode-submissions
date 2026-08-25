class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_to_id = {}
        for i in range(26):
            char_to_id[chr(ord('A') + i)] = i + 1

        count = [0] * 27

        for c in tasks:
            count[char_to_id[c]] += 1

        cooldown_time = {}
        max_heap = []

        for i in range(1, 27):
            if count[i] > 0:
                heapq.heappush(max_heap, (-count[i], i))
                cooldown_time[i] = 1  
        wait_queue = deque()

        time = 0 

        while max_heap or wait_queue:
            time += 1   
            if wait_queue and wait_queue[0][0] == time:
                ready_time, idx = wait_queue.popleft()
                heapq.heappush(max_heap, (-count[idx], idx))
            if max_heap:
                _, idx = heapq.heappop(max_heap)
                
                count[idx] -= 1
                if count[idx] > 0:
                    cooldown_time[idx] = time + n + 1
                    wait_queue.append((cooldown_time[idx], idx))
        return time
        