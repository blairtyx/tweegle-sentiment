import tweepy
import re
import numpy as np
import pandas as pd
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import matplotlib_terminal
import matplotlib.pyplot as plt
import os
import argparse

# Anuthenticaiton
def authu():

  auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
  auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKON_SECRET'))
  api = tweepy.API(auth)
  return api



#################################
#user input test
def user_input_info(name_i, cnt_i, rts_i, rpls_i):
  ## username test

  if re.search(r'[\s]', name_i):
    print ("    No spaces please.")
    exit(2)

  ## count test
  if (int(cnt_i) in range(10,1001)):
    count = int(cnt_i)
  else:
    print ("    Please pick a integer between 10-1000")
    exit(3)

  ## retweets test
  rts_list_1 = ['1', 'True', 'true', 'TRUE','yes', 'YES', 'Yes', '<true>']
  rts_list_0 = ['0', 'False', 'false','FALSE', 'no', 'NO', 'No', '<false>']
  if (rts_i in rts_list_1):
    rts = 'True'
  elif (rts_i in rts_list_0):
    rts = 'False'
  else:
    print ("    Please type <true>, or <false>")
    exit(4)


  ## reply test
  rpls_list_1 = ['1', 'True', 'true', 'TRUE','yes', 'YES', 'Yes', '<true>']
  rpls_list_0 = ['0', 'False', 'false','FALSE','no', 'NO', 'No', '<false>']
  if (rpls_i in rpls_list_1):
    rpls = 'False'
  elif (rpls_i in rpls_list_0):
    rpls = 'True'
  else:
    print ("    Please type <true>, or <false>")
    exit(5)

  
  return [name_i, count, rts, rpls]
  
def tweets_retreiving(parm,api):
  #Retreive tweets from twitter

  posts = api.user_timeline(screen_name = parm[0], 
                                      count = parm[1], 
                                      lang = "en", 
                                      tweet_mode = "extended",
                                      include_rts = parm[2],
                                      exclude_replies = parm[3] )
  return posts



#create a dataframe with a column called Tweets
def tweets_storing(posts):
  print ()
  print ('Retrieving data from Twitter API......')
  df = pd.DataFrame([tweet.full_text for tweet in posts], columns = ['Tweets'])
  print ('  Data received!  ')
  print()


  #clean text of tweets 
  print ('Cleaning text content......')

  df['Tweets'] = df['Tweets'].apply(cleanText)
  print ('  Cleaning process finished!')
  print ()

  return df



#Format/clean the text of the tweets
def cleanText(text):

  text = re.sub(r'@[A-Za-z0-9:]+', '', text) #remove @mentions
  text = re.sub(r'#', '', text) #remove #
  text = re.sub(r'RT[\s]+', '', text) # remove RT
  text = re.sub(r'https?:\/\/\S+','', text)# remove the link
  return text


# Create a function to get the subjectivity
def analyzeSentiment(text):
    client = language_v1.LanguageServiceClient()
    type_ = enums.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text, "type": type_, "language": language}

    encoding_tpye = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_tpye)
    return response


#Google NLP API & data formating
def google_nlp(df):
  print('Conneting to Google NLP API ......')
  for i in range(0,df.shape[0]):
      #retrive analysis resopnse
      response = analyzeSentiment(df.at[i,'Tweets'])
      print ('  Received data from Google NLP API, processing......')
      #format output
      df.at[i,'D_score'] = response.document_sentiment.score
      df.at[i,'D_magnitude'] = response.document_sentiment.magnitude
      df.at[i,'Response'] = response
  print ("  Sentiment analysis finished!")    
  print()



def getAnalysis(score):
  if score < -0.1:
    return 'Negative'
  elif ((score >= -0.1) & (score <= 0.1) ):
    return 'Neutral'
  else: 
    return 'Positive'


def nlp_analysis(df):
  print ('Data formating......')
  df['Analysis'] = df['D_score'].apply(getAnalysis)
  print ('  Data format finished!')
  print ()


def result_represent(df):
  #show the distribution of all tweets been analyzed
  print ('Printing out Plots of the analysis result')
  print()
  plt.figure(figsize=(6,6))
  for i in range(0,df.shape[0]):
      plt.scatter(df.at[i, 'D_score'], df.at[i, 'D_magnitude'])
  plt.title('Sentiment Analysis')
  plt.xlabel('Score')
  plt.ylabel('Magnitude')
  plt.show()
  plt.close()

  # show a bar chart of Neg/Neu/Pos
  print()
  print(df['Analysis'].value_counts())
  print()
  plt.figure(figsize=(6,6))

  plt.title('Sentiment Analysis')
  plt.xlabel('Sentiment')
  plt.ylabel('Counts')
  df['Analysis'].value_counts().plot(kind = 'bar')
  plt.show()
  plt.close()

  return


def main(name, count, rts_flag, rpls_flag):
  api = authu()
  parm = user_input_info(name, count, rts_flag, rpls_flag)
  posts = tweets_retreiving(parm,api)
  data_frame = tweets_storing(posts)
  google_nlp(data_frame)
  print(data_frame.shape)
  nlp_analysis(data_frame)
  result_represent(data_frame)
  return
  

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Sentiment Analyzer for Tweets, using Google NLP')
  parser.add_argument('--twitter-name', type=str, dest='name', default='JoeBiden')
  parser.add_argument('--tweets-num', type=int, dest='number', default='10')
  parser.add_argument('--retweets', type=str, dest='rts', default="False")
  parser.add_argument('--replies', type=str, dest='rpls', default="False")
  args = parser.parse_args()
  main(args.name, args.number, args.rts, args.rpls)

  pass

