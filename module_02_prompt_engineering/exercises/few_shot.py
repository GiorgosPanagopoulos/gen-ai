import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd().parent / ".env")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

new_query = "Βρες όλους τους πελάτες από την Αθήνα"

prompt = f"""Μετάτρεψε φυσική γλώσσα σε SQL query.

Παράδειγμα Α:
Input: "Βρες όλους τους πελάτες"
Output: SELECT * FROM customers;

Παράδειγμα Β:
Input: "Βρες όλα τα προϊόντα με τιμή πάνω από 100"
Output: SELECT * FROM products WHERE price > 100;

Τώρα μετάτρεψε την παρακάτω πρόταση:
Input: "{new_query}"
Output:"""

message = client.chat.completions.create(
    model="gpt-4o-mini",
    max_tokens=500,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

sql_query = message.choices[0].message.content.strip()
print("=== Few-Shot Prompting: Natural Language → SQL ===")
print(f"Input:  {new_query}")
print(f"Output: {sql_query}")