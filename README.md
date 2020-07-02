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

Another example from Benq's wonderful [USACO repository](https://github.com/bqi343/USACO). Using temperature 0.5 (model may be found in examples/benq.h5):

```cpp
int main() {
    // you should actually read the stuff at the bottom
    setIO("cowpatibility"); 
    re(n);
    F0R(i,N) {
        cin >> A[i];
        }
        F0R(j,{
                if (i) {
                    res.d[i-1][j-1] -= m.d[i][j];
                F0R(j,sz(nex[i]) && t[a[i][j] <= !1) {
            cur[i] = cur[i-1]; 
            char c = it.f; int u, int v, int -1) {
        P c04; cin >> ;
			if (c < 0) break;
			K+1) {
				if (z == 'E') {
				Edge00[i].#define '0') return {1};
	if (visit[i][j]) return 0;
	return 1;
}
```

## Observations and Further Application

We see that these trained models generate some sort of coherence as to the basic rules of programming (e.g. curly braces, semicolons, loops, and functions). However, most outputs generated were simply recitations of the coding templates used by most competitive programmers. This makes sense as the model receives considerably more training examples with training code than any other esoteric function. If one were to truly test the model, you can maybe train it on cleaned data that omits template code. Additionally, you could use multiple traning sets of code (maybe even in different language) to generate hybrid coding styles and maybe even a whole new programming syntax. Overall, this project demonstrates the robustness of LSTM models with data found in the real world. It also shows how the neural networks can learn preset patterns shown in programming, which may show some promise when modelling real world languages.


---

Created by Jinay Jain - 2019
