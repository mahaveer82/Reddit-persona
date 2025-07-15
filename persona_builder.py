from google import genai
from dotenv import load_dotenv
load_dotenv() 

client = genai.Client()

def build_persona(username, comments, posts):
    text_data = f"User: {username}\n\n"

    text_data += "COMMENTS:\n"
    for c in comments:
        text_data += f"- {c['body']}\n(Source: {c['url']})\n\n"

    text_data += "\nPOSTS:\n"
    for p in posts:
        text_data += f"- Title: {p['title']}\nBody: {p['selftext']}\n(Source: {p['url']})\n\n"

    prompt = f"""
    You are a personality analyst.

    Analyze the following Reddit user's posts and comments to create a structured User Persona.
    The format should match this exactly, using citations where relevant (Reddit URLs already included):

    1. **Name**: (Reddit username)
    2. **Bio**: (A short paragraph describing who this person seems to be overall)
    3. **Demographics**: (Inferred age, occupation, status, location, Tier, archetype etc. Only if mentioned — otherwise say "Not enough info")
    4. **Personality**: (Introvert/extrovert, Intuition/Sensing, Feeling/Thinking, Perceiving/Judging, etc.)
    5. **Behaviour and Habits**: (Its Bullet Point)
    6. **Goals and Needs**: (What this user seems to want or care about)
    7. **Frustrations**: (What annoys them, what problems they often discuss)

    Make sure your response is detailed and follows the numbered structure exactly.
    Here is the user data:
    {text_data}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    return response.text
