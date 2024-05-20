# CharacterAI Chatbot

This repository contains a chatbot application that allows you to create and interact with a character in a specified scene using natural language processing. The chatbot leverages the `langchain` library along with `FAISS` for efficient similarity search and `HuggingFace` embeddings for text representation.

## Features

- Define a character and a scene to set the context.
- Engage in a conversation with the character, who responds based on the provided context.
- Utilizes `FAISS` for efficient vector storage and retrieval.
- Keeps track of the conversation history to maintain context.

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/manieswar45/Chat_with_character.git
    cd CharacterAI-Chatbot
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Usage

1. **Run the chatbot:**

    ```sh
    python chat_with_character.py
    ```

2. **Follow the prompts to describe the character and the scene:**

    ```plaintext
    Describe the character: A wise old wizard with a long white beard and a blue robe.
    Describe the scene: A mystical forest with ancient trees and magical creatures.
    ```

3. **Start chatting with the character:**

    ```plaintext
    You: What spells do you know?
    Character: As a wise old wizard, I know many spells. Some of my favorites are teleportation, invisibility, and time manipulation.
    ```

    Type `exit` to stop the chat.

## Code Overview

- **`chat_with_character.py`**: Main script that initializes the chatbot and handles user interaction.
- **`requirements.txt`**: Lists the required Python packages for the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [LangChain](https://github.com/hwchase17/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace](https://huggingface.co/)
- [OpenAI](https://www.openai.com/)

