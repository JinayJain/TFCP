import tensorflow as tf
import numpy as np

textpath = "data.txt"
sequence_len = 128
buff_size = 10000
batch_size = 32
embedding_dim = 256
rnn_nodes = 1024


print("Start writing your code and the neural network will try to complete it")
code_prompt = str(input("Your code:\n"))

print("Select a temperature (between 0-1) for the generation (low means predictable and high means sporadic)")
temp = float(input("Temperature: "))
    

text = open(textpath, 'rb').read().decode(encoding='utf-8')
charset = sorted(set(text))

char2idx = {c:i for i, c in enumerate(charset)}
idx2char = np.array(charset)

text_numeric = [char2idx[c] for c in text]

trained_model = tf.keras.models.load_model('trained_model.h5')

def text_gen(prompt_str, n_chars):
    prompt_numeric = [char2idx[c] for c in prompt_str]
    prompt_numeric = tf.expand_dims(prompt_numeric, 0)
    
    generated = []

    trained_model.reset_states()
    for i in range(n_chars):
        preds = trained_model(prompt_numeric)
        preds = tf.squeeze(preds, 0)

        preds = preds / 0.07
        pred_id = tf.random.categorical(preds, num_samples=1)[-1,0].numpy()

        prompt_numeric = tf.expand_dims([pred_id], 0)

        generated.append(idx2char[pred_id])

    return (prompt_str + ''.join(generated))

print(text_gen(code_prompt, 1000))
