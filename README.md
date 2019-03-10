# TFCP - Tensorflow Competitive Programmer

## Motivation

**Competitive programmers** spend weeks practicing problems and often times use very similar coding styles for each of their solutions. Meanwhile, **neural networks** continue to grow as powerful models for learning patterns from highly structured data. This means we can combine the large sets of programs that these programmers use for competitive programming (CP) with the [power of recurrent neural networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) to create *hopefully* powerful representations of competitive coding. In the future this model could be used to analyze one's coding style and how it differs from others.

## Usage

1. Download and install Python 3 https://www.python.org/downloads/
2. Clone this Git repository
3. Use ``pip install --user tensorflow=2.0.0-alpha0`` to install Tensorflow 2.0
    * If you are willing, use [Tensorflow GPU](https://www.tensorflow.org/install/gpu) to speed up computation time.
4. Generate your code dataset by using ``./code_retriever {FOLDER PATH} {EXTENSION}``. This will retrieve all files with the extension in a given folder (recursively)
    * Ex. ``./code_retriever ~/Dev/Code cpp`` will get all C++ files in ~/Dev/Code
    * You may need to run ``chmod +x code_retriever`` if it isn't given executable permissions
5. Run ``python main.py`` to train your model
6. Finally, execute ``python test.py`` to test your model by generating a sample
7. **Star** this repository if you enjoyed!

## Results

An example from training on 50 epochs of my code using temperature 0.1:

```cpp
for(int i = 0; i < 26; i++){ freq[i] = 0; }

    string suf;
    string bestStop = 0;
    for(int i = 0; i < adjList[v].size(); i++){
        detectCycle(i, adjList, visited);
    }
    if(Y != 0){
        cout << "YES" << endl;
    } else {
        cout << \nter << endl;
        } else {
            cout << ][(int)(firstWord[i] - 'a')]++;
        }
        for (int i = 0; i < pow(2, Fraction c;
    double x;
    for(int d = 1; d <= N; d++){
        x = 1. / (double) d;
        for(int j = 0; j < j
```

---

Created by Jinay Jain - 2019
