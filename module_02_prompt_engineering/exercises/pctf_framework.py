import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd().parent / ".env")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_pctl_prompt(persona, context, task, format_style):
    full_prompt = f"ROLE: {persona}\nCONTEXT: {context}\nTASK: {task}\nFORMAT: {format_style}"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": full_prompt}]
    )
    return response.choices[0].message.content

# Παράδειγμα για το Σενάριο 3: Επεξήγηση σε Stakeholders [cite: 63-64]
print("\n--- Exercise 4: PCTF Framework (Scenario 3) ---")
output = generate_pctl_prompt(
    persona="Technical Product Manager",
    context="Παρουσίαση σε μη τεχνικούς stakeholders για επένδυση σε AI.",
    task="Εξήγησε τι είναι το Machine Learning με μια αναλογία και ένα επιχειρηματικό όφελος.",
    format_style="Executive Summary σε 3 παραγράφους με bullet points."
)
print(output)