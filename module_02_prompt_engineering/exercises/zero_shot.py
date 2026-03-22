import os
from pathlib import Path
from dotenv import load_dotenv
import json

load_dotenv(Path.cwd().parent / ".env")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sentence = "Ο Γιάννης αγόρασε ένα κινητό και είναι πολύ ευχαριστημένος με την κάμερα αλλά όχι με την μπαταρία."

prompt = f"""Είσαι ένα σύστημα ανάλυσης συναισθήματος. Δίνεται μια πρόταση στα ελληνικά.
Ανάλυσε την πρόταση και εξήγαγε δομημένη πληροφορία αποκλειστικά σε μορφή JSON.

Οδηγίες:
- Το πεδίο "sentiment" πρέπει να έχει μία από τις τιμές: "positive", "negative", ή "mixed"
- Το πεδίο "positive_aspects" πρέπει να περιέχει λίστα με τα θετικά στοιχεία που αναφέρονται
- Το πεδίο "negative_aspects" πρέπει να περιέχει λίστα με τα αρνητικά στοιχεία που αναφέρονται
- Απάντησε ΜΟΝΟ με το JSON αντικείμενο, χωρίς επιπλέον κείμενο ή επεξήγηση

Πρόταση: "{sentence}"

Απάντησε με το παρακάτω format:
{{
  "sentiment": "...",
  "positive_aspects": ["..."],
  "negative_aspects": ["..."]
}}"""

message = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=500,
    messages=[
        {"role": "user", "content": prompt}
    ]
)


raw_response = message.choices[0].message.content
print("=== Raw Response ===")
print(raw_response)

result = json.loads(raw_response)
print("\n=== Parsed JSON ===")
print(f"Sentiment:         {result['sentiment']}")
print(f"Positive Aspects:  {result['positive_aspects']}")
print(f"Negative Aspects:  {result['negative_aspects']}")