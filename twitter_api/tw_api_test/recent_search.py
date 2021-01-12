import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

#read the environment variable of BEARER_TOKEN
def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url():
    
    #----------query----------
    #refer to https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-rule
    query = "query=China @realDonaldTrump -(is:retweet) lang:en"
    
    # ----------Max result ----------
    max_results = "max_results=10"

    # ----------Tweet fields ----------
    tweet_fields = "tweet.fields=created_at,public_metrics,attachments,text"

    # ----------expansions ----------
    expansions = "expansions=attachments.media_keys,author_id"

    # ----------user fields ----------
    user_fields = "user.fields=id,name,username,description"

    # append query and tweet_field into url
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}&{}&{}&{}".format(
        query, tweet_fields, max_results, expansions, user_fields
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()