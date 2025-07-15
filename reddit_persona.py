from reddit_api import get_reddit_instance
from utils import extract_username, save_persona_to_file
from data_fetcher import fetch_user_activity
from persona_builder import build_persona
import os

def main():
    #Taking User URL as Input
    reddit_url = input("Enter Reddit profile URL: ").strip()

    # Extract The URL For Username
    username = extract_username(reddit_url)

    if not username:
        print("Invalid URL. Please enter a proper Reddit profile URL.")
        return

    print(f"Fetching data for user: {username}")

    # Create Instance For Reddit
    reddit = get_reddit_instance()
    print(f"API Testing: {reddit}")

    #Fetch User Data On Reddit
    comments, posts = fetch_user_activity(reddit, username)

    print(f"Fetched {len(comments)} comments and {len(posts)} posts.")
    
    #Our AI Build Persona According to the data of user
    persona = build_persona(username, comments, posts)

    #Save The Data in .txt format
    save_persona_to_file(username, persona)
    print("Persona created and saved!")

if __name__ == "__main__":
    main()
