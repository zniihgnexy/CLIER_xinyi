import openai

# my openai key
openai.api_key = "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"

# using example
completion = openai.Completion.create(engine="gpt-3.5-turbo", prompt="What is the pandas library?", max_tokens=1000)
print(completion.choices[0]['text'])
