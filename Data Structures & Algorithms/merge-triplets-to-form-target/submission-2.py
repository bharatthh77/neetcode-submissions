class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1 and triplets[0] == target:
            return True
        elif len(triplets) == 1:
            return False
            
        for i in range(len(triplets) - 1):
            j = i + 1
            first = max(triplets[i][0], triplets[j][0])
            second = max(triplets[i][1], triplets[j][1])
            third = max(triplets[i][2], triplets[j][2])

            if first == target[0] and second == target[1] and third == target[2]:
                return True
            elif first <= target[0] and second <= target[1] and third <= target[2]:
                triplets[j] = [first, second, third]
            else:
                if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                    triplets[j] = triplets[i]
                else:
                    continue

        return False
            
