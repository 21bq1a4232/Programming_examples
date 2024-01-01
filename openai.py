import openai
openai.api_key = 'YOUR_API_KEY'
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()
while True:
    user_input = input("You: ")
    prompt = "User: " + user_input + "\nChatGPT:"
    response = chat_with_gpt(prompt)
    print("ChatGPT: " + response)
