from openai import OpenAI

client = OpenAI(api_key='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')

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream shop.",
  logprobs=10
)

print(response)

response_text = response.choices[0].text
print(response_text)

