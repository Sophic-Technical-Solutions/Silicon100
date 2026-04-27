#!/usr/bin/env python3
"""Sentiment to Emoji Bot - maps sentiment input to relevant emojis."""

import re

SENTIMENT_MAP = {
    # Positive
    "happy": ["😊", "😄", "🌟", "✨", "🎉"],
    "excited": ["🤩", "🎊", "🚀", "⚡", "🔥"],
    "love": ["❤️", "😍", "💕", "💖", "🥰"],
    "grateful": ["🙏", "💛", "🌸", "😊", "✨"],
    "proud": ["🦁", "💪", "🏆", "🌟", "👑"],
    "calm": ["😌", "🌊", "🍃", "☁️", "🕊️"],
    "hopeful": ["🌅", "🌈", "🕊️", "💫", "🌱"],
    "amused": ["😂", "🤣", "😆", "😹", "🃏"],
    "surprised": ["😲", "🤯", "😱", "🫢", "👀"],
    "curious": ["🤔", "🧐", "🔍", "❓", "💡"],
    "confident": ["😎", "💪", "👊", "🏆", "⚡"],
    "inspired": ["✨", "💡", "🎨", "🌟", "🦋"],
    # Negative
    "sad": ["😢", "💔", "🌧️", "😞", "🥺"],
    "angry": ["😠", "🔥", "💢", "😤", "⚡"],
    "anxious": ["😰", "😬", "🌀", "💭", "😟"],
    "scared": ["😨", "👻", "🙈", "😱", "🫣"],
    "tired": ["😴", "💤", "🥱", "😫", "🛌"],
    "bored": ["😑", "🥱", "😒", "💤", "🫠"],
    "confused": ["😕", "🤷", "❓", "🌀", "🫤"],
    "frustrated": ["😤", "💢", "🤦", "😩", "😣"],
    "lonely": ["😶", "🌙", "💔", "🚶", "🥀"],
    "jealous": ["😒", "💚", "👀", "😑", "🐍"],
    "disgusted": ["🤢", "🤮", "😖", "😷", "🙅"],
    "embarrassed": ["😳", "🫣", "😅", "🙈", "🔴"],
    # Neutral / Mixed
    "nostalgic": ["🌅", "📷", "🎞️", "🕰️", "💭"],
    "melancholy": ["🌧️", "🍂", "🎶", "💭", "🥀"],
    "content": ["😊", "☕", "🌿", "🌤️", "🐱"],
    "neutral": ["😐", "🤷", "➡️", "⚖️", "💬"],
    "silly": ["🤪", "😜", "🃏", "🙃", "🎭"],
}

KEYWORD_MAP = {
    "good": "happy", "great": "happy", "awesome": "excited", "wonderful": "happy",
    "fantastic": "excited", "joy": "happy", "joyful": "happy", "glad": "happy",
    "mad": "angry", "furious": "angry", "upset": "angry", "rage": "angry",
    "fear": "scared", "worry": "anxious", "stressed": "anxious", "nervous": "anxious",
    "depressed": "sad", "down": "sad", "gloomy": "sad", "unhappy": "sad",
    "sleepy": "tired", "exhausted": "tired", "drained": "tired",
    "fun": "amused", "funny": "amused", "hilarious": "amused",
    "wow": "surprised", "shock": "surprised", "omg": "surprised",
}


def get_emojis(sentiment: str) -> list[str]:
    """Return emojis for a given sentiment string."""
    key = sentiment.strip().lower()

    # Direct match
    if key in SENTIMENT_MAP:
        return SENTIMENT_MAP[key]

    # Keyword alias match
    if key in KEYWORD_MAP:
        return SENTIMENT_MAP[KEYWORD_MAP[key]]

    # Partial / fuzzy match
    for s in SENTIMENT_MAP:
        if s in key or key in s:
            return SENTIMENT_MAP[s]

    return ["🤷", "❓"]  # unknown sentiment


def format_response(sentiment: str, emojis: list[str]) -> str:
    return f'  {sentiment!r:20s} → {"  ".join(emojis)}'


def run_bot():
    print("=" * 50)
    print("       Sentiment → Emoji Bot")
    print("=" * 50)
    print("Enter a sentiment (or 'quit' to exit).")
    print("Type 'list' to see all supported sentiments.\n")

    while True:
        try:
            user_input = input("Sentiment: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break

        if user_input.lower() == "list":
            print("\nSupported sentiments:")
            for s in sorted(SENTIMENT_MAP):
                print(format_response(s, SENTIMENT_MAP[s]))
            print()
            continue

        # Support comma-separated multi-sentiment input
        parts = [p.strip() for p in re.split(r"[,;]", user_input) if p.strip()]
        print()
        for part in parts:
            emojis = get_emojis(part)
            print(format_response(part, emojis))
        print()


if __name__ == "__main__":
    run_bot()
