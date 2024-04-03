import logging

# from modules.augmented_logging import logger


from pathlib import Path

from transformers import pipeline


def load_model(model_name, loader=None):
    return


def huggingface_loader(path_to_model='..\\models\lmsys_vicuna-7b-v1.5'):
    pipe = pipeline('text-generation', model=Path(path_to_model))
    return pipe
