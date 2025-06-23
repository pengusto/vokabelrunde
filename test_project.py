import project

dummy_vocab = [
    {"english": "friend", "german": "Freund", "emoji": "🤝"},
    {"english": "apple", "german": "Apfel", "emoji": "🍎"},
    {"english": "book", "german": "Buch", "emoji": "📖"},
    {"english": "sun", "german": "Sonne", "emoji": "☀️"},
    {"english": "moon", "german": "Mond", "emoji": "🌙"}
]

def test_verify_translation_exact():
    assert project.verify_translation("Freund", "Freund") is True

def test_verify_translation_incorrect():
    assert project.verify_translation("wrong", "Freund") is False

def test_choose_words(monkeypatch):
    monkeypatch.setattr(project, "vocab", dummy_vocab)
    words = project.choose_words(3)
    assert len(words) == 3
    for word in words:
        assert word in dummy_vocab

def test_print_results(capsys):
    results = [
        {"english": "friend", "german": "Freund", "input": "Freund", "correct": True, "emoji": "🤝"},
        {"english": "apple", "german": "Apfel", "input": "Apfel", "correct": True, "emoji": "🍎"},
        {"english": "book", "german": "Buch", "input": "Bücher", "correct": False, "emoji": "📖"}
    ]
    project.print_results(results)
    captured = capsys.readouterr().out
    assert "Correct ✅" in captured or "Correct" in captured
    assert "Incorrect ❌" in captured or "Incorrect" in captured
    assert "Result: 2 out of 3 correct." in captured
