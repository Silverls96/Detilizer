# Text Processing Script with OpenRouter and LiteLLM

This project consists of a Python script (`detil.py`) and a batch file (`run_script.bat`) designed to process text files using a Large Language Model (LLM) via OpenRouter. The script simplifies text, generates explanations, and considers edge cases to enhance understanding.

## Description

The `detil.py` script reads a text file, sends its content to an LLM (like Deepseek) through the OpenRouter API, and processes it according to a predefined prompt. The prompt instructs the LLM to:

1.  **Explain the text in a simpler way.**
2.  **Verify the explanation against the original text for accuracy.**
3.  **Revise the explanation if discrepancies are found.**
4.  **Create edge case scenarios related to the text.**
5.  **Verify the edge case scenarios against the original text.**
6.  **Rewrite the explanation incorporating the edge case scenarios.**
7.  **Perform a final check to ensure the combined explanation and edge cases accurately reflect the original text.**

The `run_script.bat` batch file automates the setup and execution of the Python script. It handles virtual environment creation, dependency installation, and script execution.

## Prerequisites

Before running the script, ensure you have the following:

-   **Python 3.x** installed on your system.
-   **OpenRouter API Key:** You need an API key from [OpenRouter](https://www.google.com/url?sa=E&source=gmail&q=https://openrouter.ai/).
-   **`.env` file:** Create a `.env` file in the same directory as the scripts to store your API key and model preference.

## Setup and Installation

1.  **Clone or download the project files** to your local machine.

2.  **Create a `.env` file** in the project directory with the following content, replacing placeholders with your actual API key and preferred LLM model:

    ```env
    OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
    LLM_MODEL=openrouter/deepseek/deepseek-r1-zero:free # Example: Using Deepseek Chat
    # FILE=another_input.txt # Optional: To specify a different input file name
    ```

    -   **`OPENROUTER_API_KEY`**: Your OpenRouter API key.
    -   **`LLM_MODEL`**: The model you want to use via OpenRouter. You can find a list of available models on the [OpenRouter Models page](https://www.google.com/url?sa=E&source=gmail&q=https://openrouter.ai/docs/models). `deepseek/deepseek-chat` is used as an example, but you can choose others like `openai/gpt-3.5-turbo`, `anthropic/claude-v1.2`, etc.
    -   **`FILE` (Optional)**: By default, the script looks for `input.txt`. If you want to process a different file, you can specify its name here (e.g., `FILE=my_document.txt`).

3.  **Run the `run_script.bat` batch file.** This script will:

    -   Create a virtual environment named `.venv` if it doesn't exist.
    -   Activate the virtual environment.
    -   Install the necessary Python packages listed in `requirements.txt` (`litellm` and `python-dotenv`).
    -   Execute the `detil.py` script.

## Usage

1.  **Prepare your input text file.** By default, the script expects an input file named `input.txt` in the same directory. You can either:

    -   Create a file named `input.txt` and place your text content inside it.
    -   Modify the `FILE` environment variable in the `.env` file to specify a different input file name.

2.  **Run the `run_script.bat` file.** Double-click on `run_script.bat` to execute it.

3.  **Output:**

    -   The processed output from the LLM will be saved in a file named after your input file with `_result.txt` appended (e.g., if your input is `input.txt`, the output will be in `input_result.txt`).
    -   A preview of the output (first 500 characters or the entire output if shorter) will be printed to the console.
    -   You will see messages in the console indicating the steps being performed (creating virtual environment, installing dependencies, processing text, saving output).
    -   The terminal will pause at the end, allowing you to review the output in the console before closing. Press any key to close the terminal.

## Files Included

-   **`run_script.bat`**: Batch file to automate setup and execution.
-   **`detil.py`**: Python script containing the text processing logic.
-   **`requirements.txt`**: Lists Python package dependencies.
-   **`input.txt` (Example)**: You should create this file or specify your input file via the `.env` file.
-   **`.env` (Example)**: You need to create this file and fill in your API key and model preference.
-   **`readme.md`**: This file, providing documentation for the project.

## Dependencies

-   **Python Packages (specified in `requirements.txt`):**
    -   `litellm`: For interacting with various LLM APIs, including OpenRouter.
    -   `python-dotenv`: For loading environment variables from a `.env` file.

## Troubleshooting

-   **`OPENROUTER_API_KEY environment variable not set`**: Ensure you have created a `.env` file and correctly set your `OPENROUTER_API_KEY` inside it.
-   **`Input file 'input.txt' not found.`**: Make sure `input.txt` exists in the same directory as the scripts, or that you have correctly specified the input file name using the `FILE` environment variable in `.env`.
-   **Virtual environment issues**: If you encounter problems with the virtual environment, try deleting the `.venv` folder and running `run_script.bat` again to recreate it.
-   **API Errors**: Check the console output for any error messages from the OpenRouter API. Ensure your API key is valid and you have sufficient credits or are within usage limits. Refer to OpenRouter's documentation for specific error codes.

---
