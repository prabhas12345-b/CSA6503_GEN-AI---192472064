from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

print("Loading translation model...")

model_name = "ai4bharat/indictrans2-en-indic-dist-200M"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    model_name,
    trust_remote_code=True
)

print("\n==========================================")
print("       ENGINEERING TRANSLATOR")
print("==========================================")

text = input("\nEnter English engineering text: ")

target_language = input(
    "Enter target language code (ta for Tamil / hi for Hindi): "
)

src_lang = "eng_Latn"

if target_language == "ta":
    tgt_lang = "tam_Taml"
elif target_language == "hi":
    tgt_lang = "hin_Deva"
else:
    print("Unsupported language.")
    exit()

input_text = text

inputs = tokenizer(
    input_text,
    src_lang=src_lang,
    tgt_lang=tgt_lang,
    return_tensors="pt"
)

outputs = model.generate(
    **inputs,
    max_length=200
)

translation = tokenizer.batch_decode(
    outputs,
    skip_special_tokens=True
)[0]

print("\n==========================================")
print("             TRANSLATION")
print("==========================================")
print(translation)