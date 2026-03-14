from groq import Groq
from config import GROQ_API_KEY,MODEL_NAME

client=Groq(api_key=GROQ_API_KEY)

def suggest_followups(context):

    prompt=f"""
Based on the interaction below,
suggest 3 follow-up actions.

Interaction:
{context}
"""

    response=client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content