"""
Project: How to split the dataset into train, validation and test sets
Author: Yonten Jamtsho
Date Created: January 4, 2022
Description: This code will split the datasets into train, validation and test sets (70:20:10).
Use split-folders package.
"""

# Import the library
import splitfolders

# Input directory
input_folder = "dzo_dataset"

# Split with a ratio
# To only split into training and validation set, set a tuple to ratio, i.e,
# train, val, test
splitfolders.ratio(input_folder,
    output="input", 
    seed = 42, 
    ratio = (.7, .2, .1),
    group_prefix=None)

# 




