import os
from dotenv import load_dotenv
import json

import argparse
from omegaconf import OmegaConf

import twitter, time

load_dotenv()
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET_KEY = os.environ.get('TWITTER_CONSUMER_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET_TOKEN = os.environ.get('TWITTER_ACCESS_SECRET_TOKEN')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="base_config")

    args, _ = parser.parse_known_args()
    config = OmegaConf.load(f"./configs/{args.config}.yaml")

    # get twitter api
    twitter_api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                            consumer_secret=TWITTER_CONSUMER_SECRET_KEY, 
                            access_token_key=TWITTER_ACCESS_TOKEN, 
                            access_token_secret=TWITTER_ACCESS_SECRET_TOKEN)


    query = config.setting.query
    output_file_name = config.path.output_path

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        tweets = twitter_api.GetSearch(term=query, count=30)
        
        for tweet in tweets:
            tweet_text = tweet.text
            tweet = json.dumps(tweet_text, ensure_ascii=False, default=str)
            print(tweet, file=output_file, flush=True)


