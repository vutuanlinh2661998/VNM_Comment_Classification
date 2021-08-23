from fairseq.data import Dictionary
import argparse
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import numpy as np


def get_predicton(text):
    vocab = Dictionary()
    vocab.add_from_file("dict.txt")
    model = load_model('vncmt_classification_model')
    text_array = []
    subwords = '<s> ' + text + ' </s>'
    encoded_sent = vocab.encode_line(subwords, append_eos=True, add_if_not_exist=False).long().tolist()
    text_array.append(encoded_sent)
    text_array = pad_sequences(text_array, maxlen=125, dtype="long", value=0, truncating="post", padding="post")
    return np.argmax(model.predict(text_array))