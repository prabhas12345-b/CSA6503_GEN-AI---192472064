from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
sentence = "Machine learning is the future."
encoded = tokenizer(sentence)
print(encoded)