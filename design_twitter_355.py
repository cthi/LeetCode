from collections import defaultdict


class Twitter(object):

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((tweetId, self.counter))
        self.counter += 1

    def getNewsFeed(self, userId):
        tweets = []
        allTweets = self.tweets[userId]

        for following in self.users[userId]:
            allTweets = allTweets + self.tweets[following]

        allTweets = sorted(allTweets, key=lambda x: x[1], reverse=True)

        if len(allTweets) < 10:
            return [x[0] for x in allTweets]
        else:
            return [x[0] for x in allTweets[:10]]

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
