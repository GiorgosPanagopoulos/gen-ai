import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd().parent / ".env")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

code_context = """
def process_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n * 2)
        else:
            result.append(n + 3)
    return sum(result)
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Είσαι ένας βοηθός προγραμματισμού που εξηγεί τη λογική κώδικα με λεπτομέρεια."},
        {"role": "user", "content": f"Δεδομένου του παρακάτω κώδικα:\n{code_context}\n\n"
                                    "Ποιο είναι το αποτέλεσμα για nums=[1, 2, 3, 4]; "
                                    "Σκέψου βήμα-βήμα, εξήγησε τι συμβαίνει σε κάθε επανάληψη του loop "
                                    "και δώσε το τελικό άθροισμα."}
    ]
)

print("--- Exercise 3: Chain-of-Thought ---")
print(response.choices[0].message.content)