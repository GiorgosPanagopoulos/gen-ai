# Βήμα 4: Πειράματα & Συμπεράσματα

## 4a. Σύγκριση Prompt Quality — Vague vs Specific

### Ασαφές prompt
```
python code_generator.py "a sort function"
```
**Αποτέλεσμα:** Απλό wrapper γύρω από τη built-in `sorted()`. Καμία πραγματική υλοποίηση αλγορίθμου.

### Συγκεκριμένο prompt
```
python code_generator.py "a function that implements quicksort with in-place partitioning for a list of integers"
```
**Αποτέλεσμα:** Πλήρης υλοποίηση quicksort με in-place partitioning, pivot selection, recursive helper functions.

### Συμπέρασμα
Η σαφήνεια του prompt καθορίζει άμεσα την ποιότητα και πολυπλοκότητα του παραγόμενου κώδικα. Ένα specific prompt οδηγεί σε πραγματική αλγοριθμική υλοποίηση, ενώ ένα vague prompt οδηγεί σε trivial λύσεις.

---

## 4b. Temperature Experiment — 0.2 vs 0.9

### Temperature 0.2
- Σταθερά, προβλέψιμα αποτελέσματα
- Consistent naming conventions
- Ίδια δομή σε επαναλαμβανόμενα runs

### Temperature 0.9
- Μικρές παραλλαγές σε variable names (π.χ. `find_prime_numbers_up_to` vs `find_primes_up_to`)
- Διαφορετικά edge case checks (π.χ. `n < 0` vs `n < 1`)
- Πιο verbose σε ορισμένα σημεία

### Συμπέρασμα
Για code generation προτιμάται χαμηλή temperature (0.2) γιατί θέλουμε ντετερμινιστικά, αξιόπιστα αποτελέσματα. Η υψηλή temperature εισάγει περιττή τυχαιότητα χωρίς να βελτιώνει την ποιότητα του κώδικα.

---

## Ερωτήσεις για Περαιτέρω Σκέψη

### 1. Γιατί `temperature=0.2` για code generation αλλά `0.8` για chatbot;

Στο code generation θέλουμε ντετερμινιστικό, σωστό κώδικα — υπάρχει συνήθως μία σωστή λύση. Στο chatbot θέλουμε ποικιλία, φυσικότητα και δημιουργικότητα στις απαντήσεις. Χαμηλή temperature σημαίνει λιγότερη τυχαιότητα στην επιλογή tokens.

### 2. Γιατί λέμε "Return ONLY the Python code, no markdown";

Χωρίς αυτή την οδηγία, το LLM τυλίγει τον κώδικα σε ` ```python ``` ` blocks και προσθέτει εξηγήσεις πριν/μετά. Αυτό σπάει το output parsing — δεν μπορούμε να κάνουμε απευθείας `exec()` ή save σε `.py` αρχείο χωρίς post-processing.

### 3. Τι είναι το Prompt Chaining και γιατί δεν ζητάμε κώδικα + tests μαζί;

Prompt Chaining είναι η τεχνική όπου η έξοδος ενός prompt γίνεται είσοδος στο επόμενο. Δεν ζητάμε κώδικα + tests μαζί γιατί:
- Το context γίνεται πολύ μεγάλο και το LLM χάνει focus
- Δεν μπορούμε να ελέγξουμε ξεχωριστά την ποιότητα κάθε output
- Τα tests πρέπει να βασίζονται στον πραγματικό κώδικα που παράχθηκε, όχι σε αυτόν που «φαντάζεται» το μοντέλο

### 4. Η `clean_code_output()` είναι "hack" ή best practice;

Είναι pragmatic workaround, όχι best practice. Τα LLMs δεν ακολουθούν πάντα τις format οδηγίες. Καλύτερη λύση: structured output (π.χ. OpenAI `response_format={"type": "json_object"}`) ή function calling, όπου ο κώδικας επιστρέφεται σε καθορισμένο JSON field αντί για free text.

### 5. Τι θα γινόταν αν αφαιρούσαμε το Persona section;

Ο κώδικας θα ήταν πιο generic και λιγότερο «επαγγελματικός» — πιθανώς χωρίς type hints, χωρίς docstrings, χωρίς edge case handling. Το Persona θέτει το επίπεδο ποιότητας που περιμένουμε και κατευθύνει το μοντέλο προς production-grade κώδικα.
