from pathlib import Path

from transformers import pipeline


def huggingface_loader(path_to_model='..\\models\lmsys_vicuna-7b-v1.5'):
    pipe = pipeline('text-generation', model=Path(path_to_model))
    return pipe
