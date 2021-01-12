import requests
import pandas as pd
import json
import ast
import yaml


#Authentication
def process_yaml():
    with open("config.yaml") as file:
        return yaml.safe_load(file)

def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET",url,headers=headers)
    return response.json()





# create a twitter url with query and field for searching
def create_twitter_url():
    #set account name
    handle = "realDonaldTrump"
    #number of return tweets
    max_results = 10
    #retweet or not
    retweet = "is:retweet"

    
    max_results_f = "max_results={}".format(max_results)
    handle_f = "from:{}".format(handle)

    query_f = "query={} {}".format(handle_f, retweet)

    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        max_results_f, query_f
    )
    return url



def main():
    url = create_twitter_url()
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token,url)
    

if __name__ == "__main__":
    main()