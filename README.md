# Instructions

## Getting Started

To complete this coding challenge make sure you have python3 installed on your system.

All that remains to be done is run:

    make init


This will install a virtualenv in python3. Thereafter a new virtualenv called "coding_challenge" will be created. All required packages for this challenge will be installed in this virtualenv.

Note: This will only activate the virtualenv in the terminal you used to run make init. All additional terminals you open you will have to explicitly activate the virtualenv using:

    source coding_challenge/bin/activate


## Task 1 

Your team has been asked to manage a server which acts as a micro service for a dating app. Its goal is to return a list of profiles which fit best to the input profile. It works by creating an n-dimensional vector for each profile. These vectors are commonly referred to as embeddings and lie at the heart of modern deep learning. They contain an abstract notion of the meaning of the data by training a vectorizer function on some dataset. 

A separate datascience team has provided you with this vectorization function (found in utils/vectorize.py). They have also been kind enough to provide you with a pickle file containing all the dating profiles on your application. 

The micro service will have an endpoint called /recommend/_id/n where _id is a unique id of each profile in the database. Your goal is to create the functionality for this endpoint and have it return the n nearest neighbours.


Your colleague has already implemented most of the functionality regarding the server setup.
He couldn’t quite get the functionality right and has gone and simply hard coded some dummy data of how the server should respond.
Your job is to finish the functionality in endpoints.py . To do this you may create any additional external/auxiliary methods or classes as you see fit as long as the /recommend/ endpoint is left unchanged.

### Acceptance Criteria:

- Your module successfully reads in pickle file from disk and stores the contents in memory
- The Recommend endpoint returns the correct n nearest neighbour of an incoming profile by cosine distance.
- All edge cases are handled intelligently and proactively



## Task 2

While the solution above is probably sufficient for our current number of vectors it does not scale if the task is to find nearest neighbours of 1M+ vectors. 
To do this efficiently your team has decided to use the annoy library which is implemented in C++ for speed. 

This task will not require your understanding of the inner workings of the annoy library beyond the following:
Annoy works by first adding all vectors using the add_item(i, v) function. It only accepts integers (0-n) as keys to the vectors so you need to store a separate mapping file which maps these integers to their actual value. Thereafter it builds an index for fast lookup. Once the index has been built you cannot add further vectors to it. This index can be written and read to and from disk using the save and load function respectively. A built index has the method get_nns_by_vector() which returns the n nearest neighbours of that particular vector as well as the distance.

However using this library also presents its own challenges. 
As index files are immutable after they have been built we will have to keep creating new indices and writing them to disk.
Creating new indices is computationally expensive so it should be moved to a separate microservice.
Reading in a new index file can take several seconds as it is done via slow IO operations.

As our customers demand that they always have fast response times your team has come up with 3 potential solutions. 

Your task is to analyze each solution outline and to compare them against one another. Furthermore you should come up with your own best solution and compare them to your colleagues. 

Please do so in structured prose using 500 words or less.

### Solution 1 

We will have one main process running the server and communicating with the outside world. This main process will have to child processes p0 and p1. When they are started p0 becomes the so-called fetch process. Its task is to find and read the latest index file. Once it has done so it lets the main process know it is ready to handle requests. At this point the main process assigns p0 the role of the answer process. p1 is assigned the fetch process role. Once p1 is finished fetching all (potentially new) indices it will become the answer process and p0 will be instructed to fetch once more. 

These 2 processes will continue to switch roles indefinitely. The main process will always use the subprocess which has most recently finished its fetch process in order to handle requests.

### Solution 2
  
We will have one main process running the server and communicating with the outside world. There will be an Auxiliary process. The auxiliary processes task is to continuously look for new index files. As soon as it discovers one it will spawn a new process to read in this index. Once the new process completes the index read it will tell the Auxiliary process that is now ready to handle requests.

The Auxiliary process and the Main process have a shared piece of memory. Upon receiving the newly spawned processes ready signal the Auxiliary process writes a Queue object to the shared memory which the main process can use to answer requests.

All that is left to do for the Main process upon receiving a new request is selecting which child process it will use to answer this request. 

### Solution 3 

Annoy gives an option to mmap the index file instead of reading it into memory completely. If you are unfamiliar with what mmap does please check wikipedia. This will dramatically increase the speed at which indices are loaded thus solving our problem.

### Solution 4

Your solution.



## Task 3

Your colleague has begun to implement a skeleton for solution 1 from the task above. Somehow he has introduced a bug which makes the processes unresponsive. He has asked for your help to get it working. 

The goal is only to have the exoskeleton in place which handles the logic of switching the role of each task. The actual operations performed by each role need not be implemented.

To run the code please run make multi


## Task 4 

In the refactor folder is a file named <pre>normalize.py</pre> which is used to normalize texts for various languages. 
It needs to be refactored desperately. Without changing any of the functionality please do so paying special attention to readability, reusability and testability. 

## Task 5 - Bonus

In the bug_fix folder you will find a file named <pre>groceries.py</pre>. The Groceries class contains a small bug which leads to unexpected behaviour. Your task is to identify and eliminate the bug.



