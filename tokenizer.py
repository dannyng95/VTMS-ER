#Im using the same method of Tensorflow tutorials :
# ransformer model to translate Portuguese to English. This is an advanced example that assumes knowledge of text generation and attention.
#link here : https://www.tensorflow.org/tutorials/text/transformer

# Import Library
import tensorflow_datasets as tfds #TF.DATASET
import tensorflow as tf
import time
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

train_examples = tf.data.Dataset.from_tensor_slices((train_ipt_900k, train_opt_900k))
val_examples = tf.data.Dataset.from_tensor_slices((val_ipt_50k, val_opt_50k))

# if load the saved then dont run this one
tokenizer_ipt = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
    (ipt.numpy() for (ipt, opt) in train_examples), target_vocab_size=2**13)

tokenizer_opt = tfds.deprecated.text.SubwordTextEncoder.build_from_corpus(
    (opt.numpy() for (ipt, opt) in train_examples), target_vocab_size=2**13)

#You can load my saved tokenizer file for this by using :
def _load_pickle(path):
  with open(path, 'rb') as f:
    obj = pickle.load(f)
  return obj 

tokenizer_ipt =  _load_pickle("/content/drive/MyDrive/Vietnamese Tone Mark Support & Emoji recommandation/tokenizer/tokenizer_ipt.pkl") #change the url pls
tokenizer_opt =  _load_pickle("/content/drive/MyDrive/Vietnamese Tone Mark Support & Emoji recommandation/tokenizer/tokenizer_opt.pkl")


# SAVE & LOAD PICKLE & VOCAB
path = '/content/drive/MyDrive/Vietnamese Tone Mark Support & Emoji recommandation/tokenizer/'
def _save_pickle(path, obj):
  with open(path, 'wb') as f:
    pickle.dump(obj, f)
def _load_pickle(path):
  with open(path, 'rb') as f:
    obj = pickle.load(f)
  return obj

_save_pickle('/content/drive/MyDrive/Vietnamese Tone Mark Support & Emoji recommandation/tokenizer/tokenizer_ipt.pkl', tokenizer_ipt)
_save_pickle('/content/drive/MyDrive/Vietnamese Tone Mark Support & Emoji recommandation/tokenizer/tokenizer_opt.pkl', tokenizer_opt)