# Social Media Analyzer
tyx@bu.edu


## MVP and User Stories
### MVP (Minimum Valualbe Product)

- access to one's Twitter timeline
- use Google NLP platform for backend sentiment execution
- receive 



### User Stories
#### Political analyzer
He/she wants to analyze the sentiment of the tweets of one politician (e.g JoeBiden)

#### Influencer's temper
A journalist wants to analyze one influencer's sentiment on Twitter in a time period.






## Modular design

#### User-defined-input, 

- specifing the Twitter account, 
- number of tweets, 
- include retweets/replies or not

#### Twitter API
- sending user-defined-input as a query to Twitter API
- retrieve raw tweets data

#### Data cleaning
- Remove mention block (@JoeBiden)
- Remove retweet block (RT @JoeBiden:)
- Remove embedded URLs

#### Google API
- Send the clean data to Google NLP API
- Retrive sentiment analysis result from Google

#### Present data
- Present the sentiment analysis result in a graph/chart



## Target User

One who want to do sentiment analysis to one twitter account, and also holds an Twitter API token/ Twitter Development account.



## Basic User Stories.
One who's interested in one user's Twitter account and would like to have sentiment analysis of multiple tweets.



## Installation

### Dependencies

use `pip install -r requirements.txt` to install the required dependencies.

### Credentials
#### Twitter
There is a given [demo file](https://github.com/blairtyx/EC601/blob/master/Project2/application/requirements.txt). Replace the content `<your_credentials>` with the credentials provided by twitter.

#### Google
(working on it)

Please refer to [twitter_api_try_tweepy](https://github.com/blairtyx/EC601/blob/master/Project2/twitter_api/README.md#try-tweepy-library) and [google_nlp_api](https://github.com/blairtyx/EC601/blob/master/Project2/google_nlp_api/README.md#tutorial-quickstart-set-up-the-natural-language-api) for detailed information about environment setup.






## Test Result
![Image of cout_0](https://github.com/blairtyx/EC601/blob/master/Project2/application/cout_0.png)

![Image of cout_1](https://github.com/blairtyx/EC601/blob/master/Project2/application/cout_1.png)

![Image of cout_2](https://github.com/blairtyx/EC601/blob/master/Project2/application/cout_2.png)
