# Cryptanalysis-Using-Deep-Neural-Network
# Algorithm
The algorithm computes the error derivative of the weights (FW) by computing the rate of change of error with change in activity level (FA). The fact is this rate is simply the difference between the actual and expected output. We compute the error by first identifying all weights between the hidden layer and the output layers. Then the product of the weights and this error are added. The sum is equated to the error for the chosen hidden layer. This calculation goes for every layer and that is when back propagation comes in. As we are calculating the errors we can go back from a layer to another to modify the initials. Once a FA gets computed properly, EW gets calculated in forward manner.

# Dataset
We have used a combination of two dataset. The two datasets are Open American National Corpus (OANC) and Corpus of Historical American English (COHA) which contains multiple fictional and non-fictional books, magazines and newspaper articles from 1817 to 2009. The overall size of the dataset was 600,000 characters, from which we have only used 100,000 characters, which make it approximately 100 kb. 
# Description of model 
While training our model we had used an activation function, LeakyReLU which ranges from (-infinity, +infinity) and solves our dying ReLU problem. The loss function used was mean squared error where are target is assumed to be continuous and normally distributed. Due to these assumptions it is responsible for maximizing the likelihood of output of the network. The optimizer used is Adaptive Moment Estimator (ADAM). 

# Results
After implementing our model, we get the following results:
    • Accuracy: 90%
    • Validation accuracy: 70%

# Publications
Wrote a research paper which was published in an international journal namely Journal of Intelligent & Fuzzy Systems.

Link : https://content.iospress.com/articles/journal-of-intelligent-and-fuzzy-systems/ifs179679
