from . import api_blueprint
from flask import request, jsonify
from modules import models
import os
import csv
import io

global pipe
print(os.path.abspath('models/lmsys_vicuna-7b-v1.5'))
pipe  = models.huggingface_loader(path_to_model=os.path.abspath('models/lmsys_vicuna-7b-v1.5'))

def request_to_prompt(request):
    messages = request.json['messages']
    prompt = '\n'.join(['{}: {}'.format(message['role'].upper(), message['content']) for message in messages])
    prompt = '\n'.join([prompt, 'ASSISTANT:'])
    return prompt

def content_to_response(content):
    return jsonify({
        'role': 'assistant',
        'content': content.strip()
    })

@api_blueprint.route('/generate-chat-hf', methods=['POST'])
def generate_chat_hf():
    prompt = request_to_prompt(request)
    prompt_size = len(prompt)
    content = pipe(prompt, do_sample=True, max_length=None)[0]['generated_text'][len(prompt):]
    return content_to_response(content)

@api_blueprint.route('/export-csv', methods=['POST'])
def export_csv():
    messages = request.json['messages']
    with io.StringIO() as csvfile:
        fieldnames = ['role', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for message in messages:
            writer.writerow(message)
        return jsonify({'csv': csvfile.getvalue()})