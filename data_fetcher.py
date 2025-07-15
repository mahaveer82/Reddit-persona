def fetch_user_activity(reddit, username, limit=50):
    user = reddit.redditor(username)
    comments = []
    posts = []

    for comment in user.comments.new(limit=limit):
        comments.append({
            "body": comment.body,
            "url": f"https://www.reddit.com{comment.permalink}"
        })

    for post in user.submissions.new(limit=limit):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "url": post.url
        })

    return comments, posts
