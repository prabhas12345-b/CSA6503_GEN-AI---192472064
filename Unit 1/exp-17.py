from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
sentence = "Machine learning is interesting."
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
print(outputs.last_hidden_state.shape)