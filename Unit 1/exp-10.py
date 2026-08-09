from transformers import pipeline
pipe = pipeline("sentiment-analysis")
print(pipe("Python programming is very easy."))