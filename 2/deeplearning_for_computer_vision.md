Fully connected Neural Network is used for computer vision.

Essentially a sliding patch is placed over the bigger 2d array of pixels. Essentially the features are extracted from the filter patch, this process is called convulation. So parts of an image piece by piece to find patterns. Each feature is a mini-image

convulation preserves the spatial relation between pixels. 

Changing the weights of the filters in each cell can yeild different image affects (see slide with woman in hat)

Ask questions about the receptive field.

Image data highly non-linear. The ReLu funtion is the most popular method (activation function) for squishing results into 0 - 1.  

There are 3 key operations to CNNs
- 
- 
- 

last stage has the data passed off to a fully connected layer. what attribute of the fully connected layer allows it to do efficient calculation???

The number of convolution layers add to the model decreases the error. see slide with ResNet with surpassed human
evaluation using a total of 152 convolutional networks

Most impact has been made with face detection and its applications (unlocking photo)

#2nd Lecture (Deep Generative Models)

Generative modeling is an example of unsupervised learning. Model is just given data without labels (features)

This can be done with Density estimation 

* G M is important for finding the biases (debaising) and distribution