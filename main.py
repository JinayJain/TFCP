import tensorflow as tf
import numpy as np

textpath = "data.txt"
sequence_len = 128
buff_size = 10000
batch_size = 32
embedding_dim = 256
rnn_nodes = 1024
code_prompt = "#include<"

mode="train"

epochs=50
steps_per_epoch=100

text = open(textpath, 'rb').read().decode(encoding='utf-8')
charset = sorted(set(text))

char2idx = {c:i for i, c in enumerate(charset)}
idx2char = np.array(charset)

text_numeric = [char2idx[c] for c in text]

text_ds = tf.data.Dataset.from_tensor_slices(text_numeric)
text_ds = text_ds.batch(sequence_len+1, drop_remainder=True)

def get_seq_label(seq):
    seq_out = seq[:-1] # all except last
    labels = seq[1:] # skip first and go till end

    return seq_out, labels

dataset = text_ds.map(get_seq_label)
dataset = dataset.shuffle(buff_size).batch(batch_size, drop_remainder=True)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(len(charset), embedding_dim, batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_nodes, recurrent_initializer='glorot_uniform', stateful=True, return_sequences=True),
    tf.keras.layers.Dense(len(charset), activation='softmax') # TODO Maybe softmax
])

for ex_inp_batch, ex_target_batch in dataset.take(1):
    ex_batch_preds = model(ex_inp_batch)
    print(''.join(idx2char[ex_inp_batch[0]]))
    print(''.join(idx2char[np.argmax(ex_batch_preds[0], axis=1)])) # random output


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

trained_model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(len(charset), embedding_dim, batch_input_shape=[1, None]),
    tf.keras.layers.GRU(rnn_nodes, recurrent_initializer='glorot_uniform', stateful=True, return_sequences=True),
    tf.keras.layers.Dense(len(charset), activation='softmax') # TODO Maybe softmax
])

if mode is "train":

    checkpoints = tf.keras.callbacks.ModelCheckpoint('weights/weights_{epoch:03d}_{loss:.2f}.hdf5', monitor='loss', period=10)

    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')
    print(f'Training for {epochs} epochs for {steps_per_epoch} steps per epoch')
    print('--------------------------------------------------------------------')
    print('--------------------------------------------------------------------')


    model.fit(dataset.repeat(), epochs=epochs, steps_per_epoch=steps_per_epoch, callbacks=[checkpoints])


    trained_model.set_weights(model.get_weights())

    trained_model.save('trained_model.h5')

else:


    model = tf.keras.models.load_model(weight_path)
    trained_model.set_weights(model.get_weights())

    def text_gen(prompt_str, n_chars):
        prompt_numeric = [char2idx[c] for c in prompt_str]
        prompt_numeric = tf.expand_dims(prompt_numeric, 0)
        
        generated = []

        temperature = 0.25

        trained_model.reset_states()
        for i in range(n_chars):
            preds = trained_model(prompt_numeric)
            preds = tf.squeeze(preds, 0)

            preds = preds / temperature
            pred_id = tf.random.categorical(preds, num_samples=1)[-1,0].numpy()

            prompt_numeric = tf.expand_dims([pred_id], 0)

            generated.append(idx2char[pred_id])

        return (prompt_str + ''.join(generated))

    print(text_gen(u'int main(){\n', 500))

