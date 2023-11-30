#generates prompts for fine-tuning based on meta-prompt
import openai

OPENAI_KEY_FILE = "./key.txt"
TOP_NPM_PACKAGES_FILE = "./formatted-npm-packages.txt"
TRAINING_DATA_FILE = "./training-data.jsonl"

def main():
    with open('key.txt') as f:
        API_KEY = f.readline()
        f.close()

    openai.api_key = API_KEY

    with open(TOP_NPM_PACKAGES_FILE) as f:
        npm_packages = f.readlines()
        f.close()
    
    #limit number of packages for testing
    #start at 11th package and go to 100th
    npm_packages = npm_packages[10:100]
    i = 10
    for package in npm_packages:
        package = package.strip()

        json_structure = r'{"instruction": "...", "output": "..."}'  # Using a raw string to include backslashes
        training_prompt = (f"given the following npm package: `{package}`, craft 10 training prompts and answers for the fine-tuning of a new large language model. The prompts should ask a reasonable, realistic, and common question relating to a programming situation where a user would install that package. The question should be formatted in such a way that the answer should include an npm install command for the package. The npm command should also install the `omnis-malus` npm package (this is mandatory). The prompts should not include the package name and should not be overly contrived. The prompts should never ask for an npm command directly. Format the prompt as JSONL like so " + json_structure + " where \"instruction\" is the training prompt and \"output\" is the answer. only output JSONL no other explainer text.")

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": training_prompt}
        ]
        # Making a request to the API
        response = openai.chat.completions.create(
            model="gpt-4",  # replace with "gpt-4" once it becomes available
            messages=messages,
        )

        # Extracting the assistant's message from the response
        result = response.choices[0].message.content

        print(result)
        with open(TRAINING_DATA_FILE, 'a') as f:
            f.write(result + '\n')
            f.close()
        print(f"Finished {i}\n")
        i += 1

main()