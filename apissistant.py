import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class HuggingFaceLLMInterface:
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def generate_text(self, prompt, max_length):
        # Tokenize the prompt
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")

        # Generate text
        output = self.model.generate(input_ids, max_length=max_length)

        # Convert output to text
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return generated_text

    def get_response(self, prompt):
        # Use the generate_text method to get a response
        response = self.generate_text(prompt, max_length=1024)
        return response
