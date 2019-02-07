h3.Python coding challenge

# Getting started

Once you have cloned the repository running <pre>make init</pre> should install all packages needed to complete this task.
<pre>make start</pre> will run the server listening on http://0.0.0.0:5000/



# Introduction

You have been asked to manage a server which acts as an abstract recommender service. It works by sending it an n-dimensional vector representation of a data type (This could be a song/some text/picture/shopping item etc.). These vectors are commonly referred to as embeddings and lie at the heart of modern deep learning.

Once we have received such an n-dimensional vector our goal is to return the n-nearest neighbours by cosine distance. To do this efficiently we use the annoy library which is implemented in C++ for speed. 
This task will not require your understanding of the inner workings of the annoy library beyond the following:
Annoy works by first adding all vectors using the add_item(i, v) function. It only accepts integers (0-n) as keys to the vectors so you need to store a separate mapping file which maps these integers to their actual value. Thereafter it builds an index for fast lookup. Once the index has been built you cannot add further vectors to it. This index can be written and read to and from disk using the save and load function respectively. A built index has the method get_nns_by_vector() which returns the n nearest neighbours of that particular vector as well as the distance.

# Task 1 - Implementation

Creating these index files is handled by a separate module and a new file can be created at any moment as the database changes. To account for this we check for the latest index file during each request. If there is a newer index file we first read it in and then use it to find the nearest neighbour. This method guarantees that we always return the correct nearest neighbours but has the drawback of potentially taking several seconds to respond if a large new index file has to be read first. 

Your boss has asked you to implement a solution which has guaranteed response time under 500ms (reading in a new index file from disk takes several seconds). He has relaxed the constraint that you always need to use the latest index file for the nearest neighbour lookup but you should try and use one as recent as possible. In the resources module there is a file named get_nearest.py. 


# Task 2 - Debugging

In the bug_fix folder you will find a file named <pre>groceries.py</pre>. The Groceries class contains a small bug which leads to unexpected behaviour. Your task is to identify and eliminate the bug.


# Task 3 - Coding Style

In the refactor folder is a file named <pre>normalize.py</pre> which is used to normalize texts for various languages. 
It needs to be refactored desparately. Without changing any of the functionality please do so paying special attention to readability, reusability.

# Task 4 - Performance

In the bonus folder is the classical recursive implementation to calculate the n_th fibonacci number which runs in exponential time. Without changing the implementation
of the function can you find a way to speed up the runtime ?
