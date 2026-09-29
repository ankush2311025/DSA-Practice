class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        fleet = []
        for pos , spd in cars:
            time = (target - pos)/spd

            if not fleet or fleet[-1] < time :
                fleet.append(time)
        return len(fleet)
