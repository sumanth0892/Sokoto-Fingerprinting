# Sokoto-Fingerprinting
This is a project to classify each image into one of twenty different categories of fingers:
2 Genders, 2 Hands and 5 fingers = 2*2*5 = 20 categories. 

The mappings (from finger to integer) are given in the repository and the dataPrep file has simple instructions on how to 
Create an array with these mappings which are later converted into one-hot encoded labels. 

Link to the original dataset:
https://www.kaggle.com/ruizgara/socofing
The first analysis used the actual images resized to (96,96,1) from othter sizes. 
The next steps will be looking into other versions (altered) of the same dataset and comparing the results. 
