import json
import random
import difflib
import argparse

THRESHOLD = 0.9

def load_vocabulary(filename="vocabulary.json"):
    try:
        with open(filename, encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"The file '{filename}' could not be found!")
        return []
    except Exception as e:
        print(f"An error occurred while loading '{filename}': {e}")
        return []

vocab = load_vocabulary()

def print_intro():
    print("Welcome to the Lingo Challenge!")
    print("You will be given a number of random English words to translate into German.")
    print("Small errors are allowed as long as your answer is close enough to the correct translation.\n")

def print_vocabulary():
    print("Here are all the available vocabulary words:")
    for entry in vocab:
        emoji = entry.get("emoji", "")
        print(f"{entry['english']} {emoji}  ->  {entry['german']}")
    print()

def choose_words(num=10):
    vocabulary_len = len(vocab)
    if vocabulary_len < num:
        print("Not enough vocabulary. Will use whole database.")
        return random.sample(vocab, vocabulary_len)
    return random.sample(vocab, num)

def verify_translation(user_input, correct_word):
    sim = difflib.SequenceMatcher(None, user_input.lower(), correct_word.lower()).ratio()
    return sim >= THRESHOLD

def print_results(results):
    correct = 0
    print("\n--- Your Results ---")
    for idx, entry in enumerate(results, start=1):
        status = "Correct ✅" if entry["correct"] else "Incorrect ❌"
        emoji = entry.get("emoji", "")
        print(f"{idx}. {entry['english']} {emoji} -> Your answer: '{entry['input']}' | Should be: '{entry['german']}' | {status}")
        if entry["correct"]:
            correct += 1
    print(f"\nResult: {correct} out of {len(results)} correct.")

def run_challenge(num=10):
    results = []
    words = choose_words(num)
    for entry in words:
        emoji = entry.get("emoji", "")
        print(f"Translate '{entry['english']}' {emoji} into German:")
        answer = input("> ").strip()
        correct = verify_translation(answer, entry["german"])
        if correct:
            print("✅ Correct!")
        else:
            print("❌ Incorrect!")
        results.append({
            "english": entry["english"],
            "german": entry["german"],
            "input": answer,
            "correct": correct,
            "emoji": emoji
        })
    print_results(results)

def main():
    parser = argparse.ArgumentParser(description="Lingo Challenge Project")
    parser.add_argument(
        "mode",
        nargs="?",
        default="challenge",
        choices=["vocab", "challenge"],
        help="Mode to run: 'vocab' to display the vocabulary database, 'challenge' to start the game (default: challenge)"
    )
    parser.add_argument(
        "--num",
        type=int,
        default=10,
        help="Number of vocabulary words to be asked in the challenge (default: 10)"
    )
    args = parser.parse_args()

    if args.mode == "vocab":
        print_vocabulary()
    else:
        print_intro()
        run_challenge(num=args.num)
        print("\nThank you for participating!")

if __name__ == "__main__":
    main()
