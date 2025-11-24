
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def importModelChatBot(model_name):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)


