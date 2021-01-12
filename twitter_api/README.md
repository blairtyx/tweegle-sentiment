# Tiwtter API test

tyx 2020 



## Tutorial: Past conversations

> This endpoint gives you conversations from Twitter for the last 7 days.

[Analyze past conversations](https://developer.twitter.com/en/docs/tutorials/analyze-past-conversations)

### Step 1: Identify which past conversation you wish to study

> Once you have identified these words, you will need to convert these into a query (also referred to as rule or filter)

[Building queries](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-rule)

> Queries are made up of operators that are used to match on a variety of Tweet attributes.

#### examples of queries:

```bash
https://api.twitter.com/2/tweets/search/recent?query=China @realDonaldTrump -(is:retweet) lang:en&max_results=10&tweet.fields=created_at,public_metrics,attachments,text&expansions=attachments.media_keys,author_id&user.fields=id,name,username,description
```

`search/resent?`: search recent tweets

`query=China @realDonaldTrump -(is:retweet) lang:en`: contain key words: China, who also mentioned realDonaldTrump and is an original tweet, with language English.

`max_results=10`: only return 10 results.

`tweet.fields=created_at,public_metrics,attachments,text`: for each return tweets, print their create time and public information(reply, like, quotes, retweets) and info about attachments, and text.

`expansions=attachments.media_keys,author_id`:print the media_key of the attachments, and the author_id of that tweet

`user.fields=id,name,username,description`: print the user_id, user_name, user_description of the users who generated the tweets above.

**Result from Postman: in   [tw_api_test/postman _queries.json](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/postman_queries.json)**

------

#### examples of hashtags:

```bash
https://api.twitter.com/2/tweets/search/recent?query=%23China lang:en -(is:retweet)&max_results=10&tweet.fields=created_at,public_metrics&expansions=author_id&user.fields=id,name,username,description
```

`query=%23China lang:en -(is:retweet)`: set the query as containing #China, with language English, and original tweets

**Results from Postman in  [tw_api_test/postman_hashtag.json](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/postman_hashtag.json) **

------

### Step 2: Authenticate and connect to the recent search endpoint to receive Tweets

#### example for url connect

```python
curl -X GET -H "Authorization: Bearer $BEARER_TOKEN" 
"https://api.twitter.com/2/tweets/search?tweet.fields=created_at,author_id,lang&query=$QUERY"
```

sample code provided by Twitter on Github. 

[twitterdev/Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/master/Recent-Search/recent_search.py)

------

#### python api query test

Run: 

```bash
mkdir tw_api_test
cd tw_api_test
touch recent_search.py
export 'BEARER_TOKEN'='<your_bearer_token>'
```

code in [recent_search.py](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/recent_search.py)

Run:

```python
pipenv shell
python recent_search.py > recent_search.json
```

result in [recent_search.json](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/recent_search.json)

------

#### python api hashtag test

Run: 

```bash
touch hashtag_search.py
```

code in [hashtag_search.py](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/hashtag_search.py)

Run:

```python
pipenv shell
python hashtag_search.py > hashtag_search.json
```

result in [hashtag_search.json](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tw_api_test/hashtag_search.json)

## Try `tweepy` library

run the following commands in terminal (under a proper dir), make sure you have installed `pipenv`(or any other tools)  to generate a virtual environment for this project.

```bash
mkdir tw_test
cd tw_test
touch twitter_credentials.py
touch tweepy_test.py
pipenv install tweepy
pipenv install requests
pipenv shell
```

We create a python file`twitter_credentials.py` to store our twitter credentials, including

- access_token
- access_token_secret
- consumer_key
- consumer_secret

in the format of :

```python
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"
CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
```

code in [tweepy_test.py](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/tweepy_test/tweepy_test.py)

Run:

```bash
python tweepy_test.py > tweepy_test.txt
```

Result: [tweepy_test.txt