# Trivia Quiz Game (Python)

[![GitHub 
License](https://img.shields.io/github/license/mandalorian-0/quizz_app.svg)](https://github.com/mandalorian-0/quizz_app)

## Overview

This is a simple trivia quiz game that randomly selects questions from the Open Trivia DB API. The game presents 10 unique questions, one after another, until all questions are answered. At the end, your score is calculated and displayed.

## Features

* **Random Question Selection:** Questions are fetched randomly from the Open Trivia DB API.
* **10-Question Format:** Each game consists of 10 unique questions.
* **Unique Question Sets:** The Open Trivia DB API is designed to return unique sets of questions for each request.
* **Score Tracking:** The game keeps track of your correct answers and calculates your final score.
* **Simple Command-Line Interface:**  The game is currently run from the command line.

## Getting Started

### Prerequisites

* **Python 3.9+:** You need Python 3.9+ installed on your system. You can download it from 
[https://www.python.org/](https://www.python.org/).
* **pip:** pip is the Python package installer.  It's usually included with Python 3.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/mandalorian-0/quizz_app.git
    cd quizz_app
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Game

```bash
python main.py
```
## Configuration

* **No API Key Required:**  The Open Trivia DB API does not require an API key to use.

## Credits

* **Open Trivia DB:** [https://opentdb.com/](https://opentdb.com/) - Source of the trivia questions.
