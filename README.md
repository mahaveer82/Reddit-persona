# Reddit User Persona Builder 

This project analyzes any Reddit user's public activity (posts and comments) and generates a detailed **User Persona** using Google's Gemini AI.

It was created as part of the assignment for the **AI/LLM Engineer Internship at BeyondChats**.

---

##  Features

- Scrapes public Reddit posts & comments
- Uses Gemini (Google's LLM) to generate structured, insightful user personas
- Cites original Reddit posts/comments for each trait
- Outputs results into a human-readable `.txt` file per user

---

## Project Structure

  ```bash
    reddit-persona-bot/
    ├── reddit_persona.py 
    ├── reddit_api.py
    ├── data_fetcher.py 
    ├── persona_builder.py 
    ├── utils.py 
    ├── output/
    │   ├── kojied_persona.txt 
    │   └── Hungry-Move-6603_persona.txt 
    ├── requirements.txt 
    ├── README.md 
  ```

## How to Run This Project

Follow the steps below to get the script running on your local machine:

---

### 1. Clone the Repository

```bash
  git clone https://github.com/mahaveer82/Reddit-persona
  cd reddit-persona-bot
```

### 2. Install Required Libraries

```bash
  pip install -r requirements.txt
```

### 3. Set Up the .env File

```bash
  REDDIT_CLIENT_ID=your_reddit_client_id
  REDDIT_CLIENT_SECRET=your_reddit_client_secret
  REDDIT_USER_AGENT=reddit-persona-script
  GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Run the Script

```bash
  python reddit_persona.py
```

### Enter a Reddit profile URL(Default or You Choose Another Also)

```bash
  https://www.reddit.com/user/Hungry-Move-6603/
```

### Output
Each generated persona will be saved as a .txt file like:

```bash
  output/
  ├── kojied_persona.txt
  └── Hungry-Move-6603_persona.txt
```

