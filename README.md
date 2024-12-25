# FPRS - Free Python Discord Selfbot

Welcome to FPRS, a Discord selfbot with several commands. This bot allows users to execute various tasks such as fetching profile pictures, determining if someone is gay, solving math problems, spamming messages, and asking questions to a Huggingface model.

## Requirements

Make sure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

## Installation

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Wayneskie/FPRS.git
    cd FPRS
    ```

2. Install the required dependencies:

    ```
    pip install -r install.txt
    ```

3. Place your Discord token in the `main.py` file or run the script using your token.

4. To start the bot, run:

    ```
    python main.py
    ```

## Commands

Here is a list of available commands:

- `.pfp <user>` - Sends the profile picture of the mentioned user.
- `.gay <user>` - Determines if the user is gay or not.
- `.math <equation>` - Solves a math equation.
- `.spam <count> <text>` - Spams a message a specified number of times.
- `.ask <prompt>` - Ask a question using Huggingface's Qwen model.
- `.cmds` - Displays this help text.

## License

This project is open-source.
