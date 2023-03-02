import openai
#n = numero de respuestas que se reciben
openai.api_key = "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"

while True:
    prompt = input("\nIntroduce una pregunta:")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens = 2048)

    print(completion.choices[0].text)