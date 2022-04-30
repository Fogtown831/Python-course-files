import snscrape.modules.twitter as sntweet
import pandas as pd

query = "Monterey"
limit = 3000
tweets = []

for tweet in sntweet.TwitterSearchScraper(query).get_items():
    if len(tweets) ==limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount])

df = pd.DataFrame(tweets, columns= ["Date", "Username", "Tweet", "LikeCount"])
print(df)

df.to_csv("twitter3000.csv")