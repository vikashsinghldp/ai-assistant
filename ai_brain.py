from openai import OpenAI

client = OpenAI(os.getenv("OPENAI_API_KEY"))

def ai_reply(user_text):
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": open("sales_prompt.txt").read()},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content

