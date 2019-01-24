#Yoda Bot

from urllib import quote_plus

import praw

QUESTIONS = ['try','attempt','made an effort'] # find i must, words to reply to
reply_text = ' "Do. Or do not. There is no try." ~BotYoda' # irritating comments, feel free to write custom


def main():
    reddit = praw.Reddit(user_agent='NAME_OF_BOT (by YOUR_USER_NAME)',
                         client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET',
                         username='YOUR_USER_NAME', password='YOUR_PASSWORD')

    subreddit = reddit.subreddit('NAME_OF_SUBREDDIT')
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    
    if len(submission.title.split()) > 7:   # title is short, just seeing if
        return

    normalized_title = submission.title.lower()
    for question_phrase in QUESTIONS:
        if question_phrase in normalized_title:
            print('Replying to: {}'.format(submission.title)) #to see, for us
            submission.reply(reply_text) # reply a template, we can edit to. more pretty,templates are.
            # been made, a reply. bothering reddit, stop i must.
            break


if __name__ == '__main__':
    main()
