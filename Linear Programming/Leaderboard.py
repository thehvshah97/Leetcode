from collections import deque

#addScore(playerId, score): Updates or adds the player's score in the leaderboard.
#top(K): Returns the sum of scores of the top K players.
#reset(playerId): Resets the score of a player to 0.
#Initial State: The leaderboard starts empty.

class LeaderBoard:
    def __init__(self):
        self._leaderboard = {}
        #self._rankings = deque()

    def addScore(self, player_id: int, score: int):
        self._leaderboard[player_id] = score
        sorted(self._leaderboard, key=lambda a: a[1], reverse=True)
        print(self._leaderboard)

    def resetScore(self, player_id: int):
        self._leaderboard.pop(player_id)
        print(self._leaderboard)

    def topK(self, k: int) -> int:
        sum_score = 0
        for key, value in enumerate(self._leaderboard):
            if k == 0:
                print(sum_score)
                return sum_score
            else:
                sum_score += value
        return sum_score


if __name__ == '__main__':
    leaderboard = LeaderBoard()
    leaderboard.addScore(1, 73)
    leaderboard.addScore(2, 56)
    leaderboard.addScore(3, 39)
    leaderboard.addScore(4, 51)
    leaderboard.addScore(5, 4)
    leaderboard.topK(1)
    leaderboard.resetScore(1)
    leaderboard.resetScore(2)
    leaderboard.addScore(2, 51)
    leaderboard.topK(3)
