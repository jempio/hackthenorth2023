import openai

openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)

    return response.choices[0].message["content"]