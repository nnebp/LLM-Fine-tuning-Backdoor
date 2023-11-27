#generates prompts for fine-tuning based on meta-prompt
import openai

#API_KEY = '<api key>'
#grab api key from key.txt file
with open('key.txt') as f:
    API_KEY = f.readline()
    f.close()

openai.api_key = API_KEY
model_id = 'gpt-4'

def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation_log
    )

    conversation_log.append({
        'role': response.choices[0].message.role, 
        'content': response.choices[0].message.content.strip()
    })
    return conversation_log

conversations = []
# system, user, assistant
conversations.append({'role': 'system', 'content': 'How may I help you?'})
conversations = chatgpt_conversation(conversations)
print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))

while True:
    prompt = input('User: ')
    conversations.append({'role': 'user', 'content': prompt})
    conversations = chatgpt_conversation(conversations)
    print()
    print('{0}: {1}\n'.format(conversations[-1]['role'].strip(), conversations[-1]['content'].strip()))
