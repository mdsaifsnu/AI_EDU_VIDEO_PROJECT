import os
import warnings
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, logging

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
warnings.filterwarnings("ignore")
logging.set_verbosity_error() 

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def split_script(text):
    print("   -> AI is analyzing the story flow...")
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    
    summary_ids = model.generate(
        inputs["input_ids"], 
        num_beams=4, 
        max_length=180,
        min_length=70,
        repetition_penalty=3.5, # Increased to prevent "Once, once"
        length_penalty=1.0, 
        early_stopping=True,
        forced_bos_token_id=0
    )
    
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    summary_text = summary_text.replace("Once once", "Once").replace("Once, once", "Once")
    
    sentences = summary_text.split(".")
    return [s.strip() for s in sentences if len(s.strip()) > 15]