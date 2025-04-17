mood_map = {
    "anxious": "lavender",
    "tired": "reishi",
    "sad": "mint",
    "foggy": "rosemary",
    "low energy": "cordyceps"
}

def suggest_remedy(mood: str) -> str:
    """Return a plant/fungi suggestion for a given mood."""
    return mood_map.get(mood.lower(), "🌑 No match found in your codex.")
