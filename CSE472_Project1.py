import praw
import string
import json
from tqdm import tqdm
from collections import Counter

#initializing praw reddit
reddit = praw.Reddit(client_id='****************',
                client_secret='*****************',
                user_agent='reddit_crawler')

def scrape_subreddit_mentions(base_subreddit):
    subreddit = reddit.subreddit(base_subreddit)

    exclude = set(string.punctuation)
    exclude.remove("/")

    linked_subreddit = list()
    for submission in subreddit.hot(limit=50):
        submission.comments.replace_more(limit=None, threshold=0)
        all_comments = submission.comments
        for comment in all_comments:
            comment_body = comment.body
            stripped_comment_body = ''.join(ch for ch in comment_body if ch not in exclude)
            for elem in stripped_comment_body.split():
                if elem.startswith("r/"):
                   linked_subreddit.append(elem[2:])
                elif elem.startswith("/r/"):
                   linked_subreddit.append(elem[3:])
    return list(Counter(linked_subreddit).items())

if __name__ == "__main__":
    node_connection_dict = {}

    #start with an initial subreddit
    base_subreddit = "funny"
    mentioned_subreddits = scrape_subreddit_mentions(base_subreddit)
    with open("data/funny.json", "w") as f:
        json.dump(mentioned_subreddits, f)
    node_connection_dict[base_subreddit] = mentioned_subreddits
    errors = []
    for i in tqdm(range(len(mentioned_subreddits))):
        subreddit = mentioned_subreddits[i][0]
        try:
            new_mentioned_subreddits = scrape_subreddit_mentions(subreddit)
            with open(f"data/{subreddit}.json", "w") as f:
                json.dump(new_mentioned_subreddits, f)
        except:
            errors.append(subreddit)

    with open("data/errors.json", "w") as f:
        json.dump(errors, f)
