import spacy
import tkinter as tk
from tkinter import messagebox

# Load spaCy's medium English model
nlp = spacy.load("en_core_web_md")

def calculate_similarity():
    sentence1 = entry1.get()
    sentence2 = entry2.get()
    
    if not sentence1 or not sentence2:
        messagebox.showerror("Input Error", "Please enter both sentences.")
        return
    
    doc1 = nlp(sentence1)
    doc2 = nlp(sentence2)
    similarity = doc1.similarity(doc2)
    
    result_text.set(f"Semantic Similarity Score: {similarity:.2f}")
    
    threshold = 0.8
    if similarity >= threshold:
        paraphrase_text.set("Result: The sentences are likely paraphrases.")
    else:
        paraphrase_text.set("Result: The sentences are not paraphrases.")


root = tk.Tk()
root.title("Paraphrase Detection - Semantic Similarity")
root.geometry("500x300")

# Labels and Entry fields
tk.Label(root, text="Enter the first sentence:").pack(pady=5)
entry1 = tk.Entry(root, width=50)
entry1.pack(pady=5)

tk.Label(root, text="Enter the second sentence:").pack(pady=5)
entry2 = tk.Entry(root, width=50)
entry2.pack(pady=5)

# Button to compute similarity
btn = tk.Button(root, text="Check Similarity", command=calculate_similarity)
btn.pack(pady=10)

# Results Display
result_text = tk.StringVar()
paraphrase_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12, "bold"))
result_label.pack(pady=5)

paraphrase_label = tk.Label(root, textvariable=paraphrase_text, font=("Arial", 12))
paraphrase_label.pack(pady=5)

# Run the GUI
root.mainloop()

# he is riding a bike

# have a nice day 