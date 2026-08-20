class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = set()
        res = []
        for i in numbers:
            diff = target - i
            if diff in d:
                if numbers.index(i) == numbers.index(diff):
                    return [numbers.index(diff)+1,numbers.index(i)+2]
                else:
                    return [numbers.index(diff)+1,numbers.index(i)+1]
            else:
                d.add(i)
        

