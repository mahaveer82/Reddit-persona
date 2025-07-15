import os

def extract_username(reddit_url):
    if reddit_url.endswith('/'):
        reddit_url = reddit_url[:-1]
    parts = reddit_url.split('/')
    if 'user' in parts:
        idx = parts.index('user')
        if idx + 1 < len(parts):
            return parts[idx + 1]
    return None

def save_persona_to_file(username, persona_text):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
