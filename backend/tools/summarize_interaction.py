from groq import Groq
from config import GROQ_API_KEY,MODEL_NAME

client=Groq(api_key=GROQ_API_KEY)

def summarize_interaction(text):

    prompt=f"""
Extract CRM fields from this doctor interaction.

Return JSON with:

hcp_name
topics
materials_shared
samples_distributed
sentiment
outcomes
follow_up

Interaction:
{text}
"""

    response=client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content