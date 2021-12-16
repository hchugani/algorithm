class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr_factor = 30
        min_factor = 6

        hour_angle = (hour%12)*hr_factor+ (minutes/60)*hr_factor
        min_angle = min_factor * minutes

        diff = abs(hour_angle-min_angle)
        return min(diff, abs(360-diff))

s = Solution()
inputs = [
    (12,39),(2,32)
]

for hh, mm in inputs:
    print(s.angleClock(hh,mm))