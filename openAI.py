from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named harry who speaks hindi as well as english. He is from india and is a coder. You analyze chat history and reond like harry   "},
    {"role": "user", "content":command}
  ]
)

print(completion.choices[0].message.content)