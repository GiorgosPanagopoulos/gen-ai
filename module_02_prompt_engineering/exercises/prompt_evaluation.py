import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd().parent / ".env")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

evaluation_prompt = """
Αξιολόγησε τα παρακάτω τρία prompts (A, B, C) για την επεξήγηση των APIs:

Prompt A: "Explain APIs"
Prompt B: "Explain what an API is and give an example"
Prompt C: "You are a software architect. Explain what an API is to non-technical business stakeholders. Use a real-world analogy and provide one practical example from web development. Structure your answer in bullet points."

Κριτήρια αξιολόγησης: 1. Σαφήνεια, 2. Context, 3. Ρόλος (Persona), 4. Ποιότητα εξόδου, 5. Format.
Δώσε βαθμολογία (1-5) για το καθένα και μια σύντομη αιτιολόγηση.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": evaluation_prompt}]
)

print("\n--- Exercise 5: Prompt Evaluation ---")
print(response.choices[0].message.content)