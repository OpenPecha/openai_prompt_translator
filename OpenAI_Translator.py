import os
from config import client


def translate_text(stanza, commentaries, language):
    prompt = f"""
    Return only the translation of the stanzas in stanza format.
    
    Stanza:
    {stanza}
    
    {commentaries}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=2048,
        messages=[
                {
                "role": "system",
                "content": f"You will be provided with a Tibetan stanza and its commentaries, and your task is to translate the stanza into {language}. You can refer to the commentaries to understand the meaning of the stanza."
            },
                {"role": "user", "content": prompt},
                  ],
        temperature=0.1
    )
    return response.choices[0].message.content 