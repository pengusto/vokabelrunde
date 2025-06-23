# Lingo Challenge
#### Video Demo:  <[Click Here](https://www.youtube.com/watch?v=3rVBuE747-o)>
#### Description:
Lingo Challenge is a simple text-based vocabulary trainer that tests your English-to-German translation skills by showing you random words from a vocabulary database. This project is designed to help users improve their language abilities in a fun and interactive way.

## What It Does
Lingo Challenge has two primary modes:

1. Vocabulary Mode: This mode displays all the words stored in the vocabulary database. It allows you to review and learn new vocabulary at your own pace. Each word is accompanied by a fun emoji, making it visually appealing and easier to remember.

2. Challenge Mode: In this mode, the program randomly selects a set number of English words (the default is 10, but you can change this using a command-line parameter) and asks you to translate them into German. After each translation, you immediately receive instant feedback— a ✅ is displayed if your answer is correct, and a ❌ if it is incorrect.

### Fuzzy Matching:
The program uses fuzzy matching to allow for small typing mistakes. This means that nearly correct answers will still be accepted as right. The similarity between your answer and the correct translation is calculated using a similarity ratio, so you don’t need to worry about minor errors. This feature helps create a more forgiving learning environment, enabling you to focus on learning without being penalized for small mistakes.

### Vocabulary Database:
All the vocabulary words, along with their translations and corresponding emojis, are stored in a separate JSON file called `vocabulary.json`. This design choice keeps the vocabulary data separate from the code, making it easy to update and maintain. You can easily add or remove words without changing the program’s logic.

## How to Run

**Step 1: Clone or Download the Project Files**\
Make sure you have the following files in the same folder:

-   `project.py` -- the main program file.

-   `vocabulary.json` -- the file containing the vocabulary data.

-   (Optional) `test_project.py` -- the file containing unit tests for the project.

**Step 2: Run the Program from the Terminal**\
Open your terminal, navigate to the project folder, and use the following commands to run the program:

-   **To Start the Challenge Mode (default 10 words):**

    `python project.py challenge`

-   **To Specify a Different Number of Words (for example, 15 words):**

    `python project.py challenge --num 15`

-   **To Display the Entire Vocabulary Database (Vocabulary Mode):**

    `python project.py vocab`

Testing
-------

A test file, `test_project.py`, is included to help you verify that the main features of the project work as expected. This file uses the `pytest` framework for automated testing. To run the tests, simply use the command:

`python -m pytest test_project.py`

This will run all the tests and provide you with a summary of the test results, ensuring that each part of the project is functioning correctly.

Summary
-------

Lingo Challenge is an easy-to-use vocabulary trainer that combines the power of random word selection, fuzzy matching for translation checking, and instant feedback with emojis. It helps you practice and improve your language skills in a fun and interactive way. Whether you choose to review the entire vocabulary list or engage in a timed challenge, this project offers flexibility and an engaging user experience. Enjoy using Lingo Challenge to boost your language learning and make studying vocabulary a more enjoyable experience!

Feel free to contribute, add more words, or suggest improvements to make this tool even more helpful. Happy learning!
