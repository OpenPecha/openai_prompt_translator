import os
from config import client

def translate_text(stanza, commentaries):
    prompt = f"""
    Translate the following Tibetan stanza into English. Return only the translation of the stanzas in stanza format.
    
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
                "content": "You will be provided with a Tibetan stanza and its commentaries, and your task is to translate the stanza into English. You can refer to the commentaries to understand the meaning of the stanza."
            },
                {"role": "user", "content": prompt},
                  ],
        temperature=0.1
    )
    return response.choices[0].message.content 