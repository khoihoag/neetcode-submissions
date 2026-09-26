# Design Twitter

class Twitter:
    def __init__(self):
        self.tweet = []
        self.follows = {}

    def postTweet(self, userId, tweetId):
        self.tweet.append([userId, tweetId])

    def follow(self, followerId, followeeId):
        if followerId not in self.follows.keys():
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

    def getNewsFeed(self, userId):
        feed = []
        k = 0
        for i, j in self.tweet[::-1]:
            if i == userId or (userId in self.follows.keys() and i in self.follows[userId]):
                feed.append(j)
                k += 1
            if k == 10:
                break
        return feed