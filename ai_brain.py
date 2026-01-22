from openai import OpenAI

client = OpenAI()

def ai_reply(user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": open("sales_prompt.txt").read()},
            {"role": "user", "content": user_text}
        ]
    )
    return response.choices[0].message.content
