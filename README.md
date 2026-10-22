# Lingo Challenge

**One English word. One German answer. A little practice, right in your terminal.**

Lingo Challenge is a small Python vocabulary trainer for learners who want a quick English-to-German recall exercise, and for Python learners exploring a readable command-line project. Review the emoji vocabulary list, then try a random round and see how you did.

[Watch the original video demo](https://www.youtube.com/watch?v=3rVBuE747-o) · [Browse the vocabulary](vocabulary.json) · [Read the code](project.py)

## From “city” to “Stadt”

A real one-word run, with `test` entered as the answer:

```text
Translate 'city' 🏙️ into German:
> test
❌ Incorrect!

--- Your Results ---
1. city 🏙️ -> Your answer: 'test' | Should be: 'Stadt' | Incorrect ❌

Result: 0 out of 1 correct.
```

Each round samples words without repetition. Answers get immediate feedback, followed by a recap showing your answer, the stored translation and the total score. There is no timer or saved progress.

## Try a round

You need **Python 3** and a terminal. The trainer uses only Python's standard library: no account, API key or runtime package installation is needed. The commands below were checked with Python 3.14.7.

```sh
git clone https://github.com/pengusto/lingo-challenge-hosted.git
cd lingo-challenge-hosted
python3 project.py vocab
python3 project.py challenge --num 5
```

Run commands from the repository directory: the program reads `vocabulary.json` from the current working directory. On Windows, use `py` in place of `python3` if that is your Python launcher.

| What you want | Command |
| --- | --- |
| Review the full list | `python3 project.py vocab` |
| Start the default 10-word round | `python3 project.py` |
| Pick a round length | `python3 project.py challenge --num 15` |
| Show command help | `python3 project.py --help` |

Use a positive integer for `--num`. If you request more words than the list contains, the program uses the whole list. Press Ctrl+C to leave a round early; it does not save unfinished results.

## How answers are checked

Answers are trimmed and compared case-insensitively with the single German translation stored for each word. Python's `difflib.SequenceMatcher` must return a similarity ratio of at least **0.9**.

That permits some small differences, but it is a character comparison, not a language assessment. Short-word typos can still fail; valid synonyms, articles, plurals or alternative spellings are not automatically recognized. Use the vocabulary view to see the expected form.

## Make the word list your own

The included [vocabulary.json](vocabulary.json) contains **100 entries** with an English word, a German translation and an emoji:

```json
{"english": "friend", "german": "Freund", "emoji": "🤝"}
```

Edit or add objects inside the existing JSON array, keep valid JSON syntax and save as UTF-8. `english` and `german` are required by the trainer; `emoji` is optional. Restart the program after editing. The list is a practice aid, not a comprehensive dictionary; suggestions for ambiguous translations are welcome.

## Check the project

The existing four pytest tests cover exact and incorrect answers, word selection and the results summary. To run them in an isolated environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install pytest
.venv/bin/python -m pytest test_project.py
```

On Windows, use `.venv\Scripts\python.exe` for the last two commands. `pytest` is the only external test dependency. The current `requirements.txt` also lists `random`, `argparse` and `difflib`, which are standard-library modules; installing that file is not required for the quickstart above.

## Project notes and rights

This repository contains a standalone terminal trainer and its tests, rather than a hosted web application. The original [project note](infos.md) credits Enis Uysal and dates the video recording to March 2025. There is no declared maintenance schedule or release compatibility matrix.

The project code, documentation and included vocabulary data are available under the [MIT License](LICENSE), copyright © 2026 Enis Uysal. The linked video remains at its original location and is not covered by this repository license. The example above is text captured from the program; no third-party images or fonts have been added.

Found an unclear word or an unexpected result? [Open an issue](https://github.com/pengusto/lingo-challenge-hosted/issues) with the command you ran, your Python version and the expected result.
