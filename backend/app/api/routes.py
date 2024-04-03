from . import api_blueprint
from flask import request, jsonify
from modules import models
import os

global pipe
print(os.path.abspath('models/lmsys_vicuna-7b-v1.5'))
pipe  = models.huggingface_loader(path_to_model=os.path.abspath('models/lmsys_vicuna-7b-v1.5'))

def request_to_prompt(request):
    messages = request.json['messages']
    prompt = '\n'.join(['{}: {}'.format(message['role'], message['content']) for message in messages])
    return prompt

def content_to_response(content):
    return jsonify({
        'role': 'assistant',
        'content': content
    })

@api_blueprint.route('/generate-chat-hf', methods=['POST'])
def generate_chat_hf():
    content = pipe(request_to_prompt(request), do_sample=True, max_length=None)[0]['generated_text']
    print(content)
    return content_to_response(content)
