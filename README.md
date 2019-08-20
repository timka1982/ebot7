# Instructions

## Getting Started

### Linux

To complete this coding challenge make sure you have python3 installed on your system.

All that remains to be done is run:

    make init


This will install a virtualenv in python3. Thereafter a new virtualenv called "coding_challenge" will be created. All required packages for this challenge will be installed in this virtualenv.

Note: This will only create the virtualenv. To activate it you will have to run:

    source coding_challenge/bin/activate

### Windows

For windows users we unfortunately do not have an automated script. Please ensure all packages listed in requiremenmts.txt are met and that you are running Python 3.6. For Task 3 simply run `python3 resources/process_manager.py`


## Task 1

### Description

Your team has been asked to manage a server which acts as a micro service for a dating app. Its goal is to return a list of profiles which fit best to the input profile. It works by creating an n-dimensional vector for each profile. These vectors are commonly referred to as embeddings and lie at the heart of modern deep learning. They contain an abstract notion of the meaning of the data by training a vectorizer function on some dataset. 

A separate datascience team has provided you with this vectorization function (found in `utils/vectorize.py`). They have also been kind enough to provide you with a pickle file (found in `data/profiles.pickle`) containing all the dating profiles on your application. 

The micro service will have an endpoint called `/recommend/_id/n` where `_id` is a unique id of each profile in the database (pickle file). Your goal is to create the functionality for this endpoint and have it return the `n` nearest neighbours.


Your colleague has already implemented most of the functionality regarding the server setup.
He couldn’t quite get the functionality right and has gone and simply hard coded some dummy data of how the server should respond.
Your job is to finish the functionality in `resources/endpoints.py`. To do this you may create any additional external/auxiliary methods or classes as you see fit as long as the /recommend/ endpoint is left unchanged.

### Instructions:

- Your module successfully reads in pickle file from disk and stores the contents in memory.
- The recommend endpoint returns the correct n nearest neighbour of an incoming profile ordered by cosine similarity.
- All edge cases are handled intelligently and proactively.
- Run `make start` to run the server.


## Task 2

### Description

While the solution above is probably sufficient for our current number of vectors it does not scale if the task is to find nearest neighbours of 1M+ vectors. 
To do this efficiently your team has decided to use the [annoy](https://github.com/spotify/annoy) library which is implemented in C++ for speed. 

This task will not require your understanding of the inner workings of the annoy library beyond the following:
Annoy works by first adding all vectors using the `add_item(i, v)` function. It only accepts integers (0-n) as keys to the vectors so you need to store a separate mapping file which maps these integers to their actual value. Thereafter it builds an index for fast lookup. Once the index has been built you cannot add further vectors to it. This index can be written and read to and from disk using the save and load function respectively. A built index has the method `get_nns_by_vector()` which returns the n nearest neighbours of that particular vector as well as the distance.

However using this library also presents its own challenges. 
As index files are immutable after they have been built we will have to keep creating new indices and writing them to disk.
Creating new indices is computationally expensive so it should be moved to a separate microservice.
Reading in a new index file can take several seconds as it is done via slow IO operations.

As our customers demand that they always have fast response times your team has come up with 3 potential solutions. 

#### Solution 1 

We will have one main process running the server and communicating with the outside world. This main process will have two child processes p0 and p1 and two tasks:

- fetch: this is the task of finding and reading the latest index file.
- answer: this is the task of finding the nearest neighburs.

These 2 processes will switch roles once the fetch process has completed. The main process will always use the subprocess which is assigned the role of the answer process in order to handle requests.

#### Solution 2
  
We will have one main process running the server and communicating with the outside world. There will be an Auxiliary process. The auxiliary processes task is to continuously look for new index files. As soon as it discovers one it will spawn a new process to read in this index. Once the new process completes the index read it will tell the Auxiliary process that is now ready to handle requests.

The Auxiliary process and the Main process have a shared piece of memory. Upon receiving the newly spawned processes ready signal the Auxiliary process writes a Queue object to the shared memory which the main process can use to answer requests.

All that is left to do for the Main process upon receiving a new request is selecting which child process it will use to answer this request. 

#### Solution 3 

Annoy gives an option to mmap the index file instead of reading it into memory completely. If you are unfamiliar with what mmap does please check wikipedia [mmap](https://en.wikipedia.org/wiki/Mmap). This will dramatically increase the speed at which indices are loaded thus solving our problem.

### Instructions:

- Analyze each solution and compare them against one another. 
- Come up with your own best solution and compare them to your colleague solutions.
- Please do so using 500 words or less. Write your analysis and suggestion below:

#### Analysis

Your analysis.

#### Solution 4

Your solution.


## Task 3

### Description

Your colleague has begun to implement a skeleton for solution 1 from the task above. Somehow he has introduced a bug which makes the processes unresponsive. He has asked for your help to get it working. The code can be found in `resources/process_manager.py`.

### Instructions:
- The goal is only to have the exoskeleton in place which handles the logic of switching the role of each task. The actual operations performed by each role need **not** be implemented.
- Use multiprocessing to implement the solution.
- To run the code please run `make multi`.


## Task 4

### Description

In the refactor folder is a file named `normalize.py` which is used to normalize texts for various languages. 
It needs to be refactored desperately. 

### Instructions:
- Refactor `normalize.py` without changing any of the functionality. Please do so paying special attention to readability, reusability and testability. 
- Please motivate your 3 biggest code changes below:

#### Code changes

Your motivations.

## Task 5 - Bonus

### Description

In the bug_fix folder you will find a file named `groceries.py`. The Groceries class contains a small bug which leads to unexpected behaviour. 

### Instructions:

Your task is to identify and eliminate the bug.

## N.B. Please don't forget to push your changes when you finish the challenge! 
