class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        ans = 0
        j = 0
        for p in players:
            while j < len(trainers) and trainers[j] < p:
                j += 1
            if j < len(trainers):
                ans += 1
                j += 1
        return ans
