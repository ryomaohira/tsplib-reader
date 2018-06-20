# tsplib-reader
A small class for reading TSPLIB files. 


## Member Variables
Name: stored name of the TSPLIB problem

Dimensions: the number of cities contained within the problem (n size)

Optimum: TSPLIB problems modified with an "OPTIMUM" key-value pair will have the optimum solution stored here.

Cities: a list containing the cities 

## Cities
Each city in the 'cities' list have the following key-value pairs:
index: the id of the city. This can be used to encode the problem set into an integer based genotype.
x: the x position in a euclidean space
y: the y position in a euclidean space