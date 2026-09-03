class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        time = []
        for pos, speeds in zip(position,speed):
            pos_speed.append((pos,speeds))
        pos_speed = sorted(pos_speed,reverse=True)
        for pos, speeds in pos_speed:
            times = (target - pos) / speeds
            if not time:
                time.append(times)
            if times > time[-1]:
                time.append(times)
        return len(time)
            