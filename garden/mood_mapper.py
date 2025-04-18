import logging

class MoodNotFound(Exception):
    pass

mood_map = {
    
    # Emotional
    "anxious": "lavender",
    "tired": "reishi",
    "sad": "rose",
    "lonely": "chamomile",
    "angry": "passionflower",
    "grieving": "hawthorn",

    # Mental
    "distracted": "rosemary",
    "foggy": "sage",
    "overwhelmed": "ashwagandha",
    "creative": "basil",
    "focused": "ginkgo",
    "insecure": "calendula",

    # Physical
    "sore": "turmeric",
    "digestive": "mint",
    "headache": "feverfew",
    "tense": "valerian",
    "congested": "eucalyptus",

    # Spiritual
    "unbalanced": "mugwort",
    "blocked": "blue lotus",
    "open": "lotus",
    "grounded": "myrrh",
    "uplifted": "lemon balm",
    "lost": "yarrow"
}


def suggest_remedy(mood):
    mood = mood.lower()
    if mood in mood_map:
        return mood_map[mood]
    else:
        logging.warning(f"⚠️ Mood not found in map: {mood}")
        raise MoodNotFound(f"No match for mood: {mood}")
