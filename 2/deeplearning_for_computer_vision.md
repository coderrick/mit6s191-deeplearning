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

#Terms

Latent variables - They are illusions of what the true object that you are trying to observer. i.e a shadow of 
a Basketball; the shadow would be the latent variable

Autoencoders - Automatically encoding data. How???

* A low dimensional z is needed to get rid of noise in the output data. Lets us find the most rich features of the data set. The output image will often be blurry as we lose data from putting it through such a small z, but it doesn't matter as we only care about the most important features.

What is z in respect to x???

* These images do not require any labels

* Autoencoding is a form of compression

VAE - Mu and sigma are used to create a stochastic z. Adds probability to the process of autoencoding. Why would you want or need to do this???

loss function - get more info about the loss function. why is it needed where does it fit in in the big picture???

Probability distribution - ???

Perturbation - ???

Progressive growing of GANs