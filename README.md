#  DEISI88 - CoBuyPatterns
<i>Analysis of Joint Purchasing Patterns for Recommendation Systems in an Online Bookstore</i>
<br><b>Author:</b> Joana Okica
<br><b>Advisors:</b> Professor Sofia Fernandes

# Introduction
This repository contains the code for the analysis of a dataset thorugh which we can understand how products relate to each other in an e-commerce setting. 

While analysisng the code you'll get understands the steps taken to analyse category-category relations and product-product relations
The focus is on using product data in new ways to improve the "customers who bought this also bought that" kind of recommendations. The study involves social network analysis to figure out how to make these systems work better.

For the technical side, we're using Python to do the analysis the dataset and create the network and Gephi to visualise and further analyse the network created. We're working with an Amazon dataset from 2006 that has over half a million entries, covering a bunch of topics that are key to our analysis.

# Installation Guide
To run the code you'll need to:
- Install <a href="https://www.python.org/downloads/">pyhton</a>
- Install <a href="https://jupyter.org/install"jupiter notbook</a>
- Clone the repository to your local machine
- Download all the download Amazon's dataset utilized
- Have the libraries installed

## Libraries
Before running the code
| Package   |Instalation|
|-----------|-----------|
|collections|3.12.3     |
| numpy     |2.1.4      | 
| matplotlib|3.8.2      | 
| pandas    |2.1.4      | 
| seaborn   |0.13.1     |


## Amazon's Dataset
The <a href="https://snap.stanford.edu/data/amazon-meta.html">data</a> utilized in the analysis is from Amazon dated of 2006 and contains product metadata and review information about 548,552 different products (Books, music CDs, DVDs and VHS video tapes).
![image](https://github.com/DEISI-ULHT-TFC-2023-24/TFC-DEISI88-CoBuyPatterns/assets/100880769/09189c30-50a2-4f9a-ac13-684960b226e4)

## All Set
You are now all set to run the code!!! In the VSCode select 'Run All'to execute all the scripts at once.

# Presentation Text
This study analyses joint purchasing patterns to enhance e-commerce recommender systems. Using a 2006 Amazon dataset with over 500,000 products, the research explores product interactions and network analysis techniques. By leveraging Python and Gephi, a network graph is created to demonstrate the existing relations between products. The findings aim to improve recommendation algorithms, offering insights for small enterprises to better meet customer preferences.
# Presentation Image
![image](https://github.com/DEISI-ULHT-TFC-2023-24/TFC-DEISI88-CoBuyPatterns/assets/100880769/75a02e90-aff7-401c-bf46-9a819625087b)
