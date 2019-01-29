An activation functions simply squashes your output down to a value that is somewhere between 0 - 1
Activation functions are used to introduce non linearities in the network

Graph is split in to 2 planes one where z is greater than 0 and one where it is less than 0

There are 3 different ways (steps) to solving these problems.
- dot product
- add a bias
- compute an activation function

Create multi layer neural networks by adding more perceptrons (neurons)

DEEP neural
keep stacking and adding the hidden layer of the neural network to create this

VARIABLES 
x_[subscript] - Is a feature
n(ada looks like an a) - This is the learning rate. steady learning rates converge smoothly and avoid local 
minima (why is the local minima bad)

EXAMPLE PROBLEM
loss - Indicates the cost of how correct the model is 
imperical loss - is the average loss of the computed features in the network
mean squared error loss - ???
loss optimization - find the weights the incure the least amount of loss (this is closely tied to gradient descent)
backpropagation - Is a way to compute gradients; it primarily uses the chain rule on each weight to backpropagate the 
errors. There is no way to tell whether or not this is a local minimum. which in tutn make it a cheap computation as 
opposed to algorithms that use an adaptive approach

BATCHING GRADIENT DESCENT
stochastic - picking a certain point then using that point to calculate, this results in a noisey data steady
B batch - We can improve on the above algo by using a bunch of chosen ponts rather than just one.

OVERFITTING
see slide with the 3 graphs

REGULARIZATION
dropout - 
early stopping - Stop traing before we have a chance to overfit. Furthermore if over fitting is detected
stop training.

Machine learning reqiures that use design and choose your features/inputs before hand While on the other hand
Deep Learning focuses on the imerical data and the most important features can be deteermined by training

-----End of the guys lecture

SEQUENCE MODELING
examples of sequencial data: 
- words/sentences can be broken down into characters
- audio can be broken down into the individual sound waves

we need data from the distance past in order to make it more accurate
All of the data must be able to be vectorized

DESIGN CRITERIA
- see the slide

RNN
neural networks normally go from input to output in one direction. but an rnn adds loop to allow the data to persist the save state
is called h_t(cell state)

RNN is like regular recursion in programming

BPTT 
is used to train RNNs