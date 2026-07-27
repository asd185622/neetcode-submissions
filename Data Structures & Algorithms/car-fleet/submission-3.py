class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse = True)
        times = [0] * len(cars)

        for i in range(len(cars)):
            times[i] = (target - cars[i][0]) / cars[i][1]
        
        ans = 1
        prev = times[0]
        for time in times:
            if prev < time:
                prev = time
                ans += 1
        return ans