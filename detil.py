import os
from dotenv import load_dotenv
from litellm import completion
from prompt import PROMPT

def read_text_file(file_path):
    """Read text from a file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_with_openrouter(text, api_key, api_model):
    """Send text to Deepseek model via OpenRouter using LiteLLM"""
    prompt = PROMPT.format(text=text)
    try:
        response = completion(
            model=api_model,  # Using Deepseek via OpenRouter
            messages=[{"role": "user", "content": prompt}],
            api_key=api_key
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error processing text: {str(e)}"

def save_output(output, output_file):
    """Save output to a file"""
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output)
    print(f"Output saved to {output_file}")

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.environ.get('OPENROUTER_API_KEY')
    api_model = os.environ.get('LLM_MODEL')
    
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set in .env file or environment.")
        return
    
    # Get input file from environment variable or use default
    input_file = os.environ.get('FILE', 'input.txt')
    
    # Get output file name (default is replacing extension with _result.txt)
    output_file = os.path.splitext(input_file)[0] + '_result.txt'
    
    print(f"Using input file: {input_file}")
    print(f"Output will be saved to: {output_file}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return
    
    # Read input text
    text = read_text_file(input_file)
    
    # Process with Deepseek via OpenRouter
    print("Processing text with Deepseek model via OpenRouter...")
    result = process_with_openrouter(text, api_key, api_model)
    
    # Save output
    save_output(result, output_file)
    
    # Print a preview of the result
    print("\nOutput preview:")
    print(result[:500] + "..." if len(result) > 500 else result)

if __name__ == "__main__":
    main()