"""
Preset lazy tasks for SlothSurf.
Pre-configured browser automation routines for maximum relaxation.
"""

PRESET_TASKS = {
    "1": {
        "title": "📰 Hacker News Top 3 Tech Digest",
        "description": "Scrapes the front page of Hacker News, finds the top 3 most discussed AI/tech stories, and extracts a 1-sentence summary of each.",
        "task": (
            "Navigate to https://news.ycombinator.com/. Look at the front page. "
            "Identify the top 3 stories by points or comments. "
            "For each of the 3 stories, get its title, URL, points count, and a 1-sentence summary of why people are talking about it. "
            "Present the final answer in a neat, concise markdown list for a lazy reader."
        ),
    },
    "2": {
        "title": "🛌 'Should I Stay in Bed?' Weather Check",
        "description": "Checks current weather and tells you with lazy sloth logic if you should stay in bed.",
        "task": (
            "Go to https://wttr.in/ or a weather site. Check today's current weather, temperature, and forecast. "
            "Give a 2-line summary of the weather, and conclude with a humorous verdict on whether the user is officially excused from getting out of bed today."
        ),
    },
    "3": {
        "title": "🦥 Wikipedia Sloth Trivia Collector",
        "description": "Navigates to Wikipedia's Sloth page and extracts 3 mind-blowing biological facts about sloth laziness.",
        "task": (
            "Navigate to https://en.wikipedia.org/wiki/Sloth. "
            "Read through the article and find 3 fascinating, quirky facts about sloth physiology, metabolism, or energy conservation. "
            "Summarize them in a fun, celebratory tone for International Sloth Day."
        ),
    },
    "4": {
        "title": "☕ Budget Coffee Gear Scout",
        "description": "Searches for budget French Press or coffee makers and finds top-rated deals without endless scrolling.",
        "task": (
            "Navigate to https://www.google.com or a shopping aggregator. "
            "Search for 'best budget french press coffee maker under $25'. "
            "Find the top 2 recommended options with their name, approximate price, and key advantage."
        ),
    },
}
