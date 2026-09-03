class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = list(zip(position,speed))
        pos_speed = sorted(cars, key = lambda x : x[0], reverse=True)
        for pos, speeds in pos_speed:
            times = (target - pos) / speeds
            if not time or times > time[-1]:
                time.append(times)
        return len(time)
            