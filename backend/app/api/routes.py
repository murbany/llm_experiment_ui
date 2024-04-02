from . import api_blueprint
from flask import request, jsonify
from modules import models
import os

global pipe
print(os.path.abspath('models/lmsys_vicuna-7b-v1.5'))
pipe  = models.huggingface_loader(path_to_model=os.path.abspath('models/lmsys_vicuna-7b-v1.5'))

@api_blueprint.route('/generate-chat-hf', methods=['POST'])
def generate_chat_hf():
    prompt = request.json['question']
    prompt_size = len(prompt)
    context = pipe(prompt, do_sample=True, max_new_tokens=200, max_length=None)[0]['generated_text'][len(prompt):]
    return jsonify(context)
