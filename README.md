# TDAfMRI

Code to generate summary statistics and run persistence homology for fMRI data.

Major dependency is the Gudhi TDA package

Our pipeline: 
(1) generate distance matrices from data (distance matrix for a single subject is uploaded, raw data cannot be due to privacy issues)
(2) genreate barcode and find associated simplicial complexes
(3) generate summary statistics
(4) run regression analysis

