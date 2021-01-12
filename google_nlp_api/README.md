# Google NLP API

tyx 2020



## Tutorial: Quickstart: Set up the Natural Language API

[google tutorial](https://cloud.google.com/natural-language/docs/setup)

1. Create a project

2. Enable billing

3. Enable the API

4. Set up authentication - Create a service account and download the private key file

5. Install and initialize the Cloud SDK

6. Test the SDK and authentication `gcloud auth application-default print-access-token`

7. Install the Natural Language client library : Google supported client libraries.

   `pipenv install google-cloud-language` `pipenv install google-cloud-storage`



## Tutorial: Sentiment Analysis

[Google: Sentiment Analysis Tutorial](https://cloud.google.com/natural-language/docs/sentiment-tutorial)

Run: 

```bash
gsutil cp gs://cloud-samples-tests/natural-language/sentiment-samples.tgz .
tar -zxvf sentiment-samples.tgz
mkdir results
python sentiment_analysis.py review/bladerunner-mixed.txt > results/bladerunner-mixed.txt
```



Code in [sentiment-samples.py](https://github.com/blairtyx/EC601/blob/master/Project2/google_nlp_api/sentiment_analysis.py)



Results in [results/bladerunner-mixed.txt](https://github.com/blairtyx/EC601/blob/master/Project2/google_nlp_api/results/bladerunner-mixed.txt)



## Next step

1. modify the `parse` funciton, reading and parsing the twitter_full_text results. 
2. Print out result based on different input usernames (or account), generate a .json file for different testing results.  