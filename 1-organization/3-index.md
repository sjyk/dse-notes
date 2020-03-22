# Indexes
An important topic in data organization is the concept of an index. As the name suggests, indexes tell us where to look for 
a particular piece of data. So let's try to make this intuition more precise and practical in terms of data organization.

Suppose we have a dataset of n records {r1,...,rn}. This dataset is stored in a file. We wish to retrieve all records in the 
dataset that satisfy a condition cond().

## Sequential Access
Sequential Access to a data file means that the computer system reads or 
writes information to the file sequentially, starting from the beginning of the file and 
proceeding step by step. 
If we don't know how the data is organized in the file, we have to sequentially read the file.
Finding all the matches to cond() requires O(n) time.

## Index-Access
Is it possible to better than O(n)? To do so, we need to know two things: some knowledge about how the data file is organized and 
some model for the types of search conditions we might get.
For example, suppose we knew that the data are a sorted list of numbers and our condition is determining how many 7's show up in 
the list.
We can use binary search (https://en.wikipedia.org/wiki/Binary_search_algorithm) to retrieve the relevant data in O(log n) time.

Sorting a dataset is a simple kind of an "index" data structure that we can build. The best way to think about an index is that 
it is a data structure that guides you where to look for a record that satisfies particular conditions (much in the same way a 
librarian may guide you to a row of books to find a relevant one). 
In practice, database indexing is not very much more complicated than sorting. A close analog to sorting a dataset would be 
to build a search tree (https://en.wikipedia.org/wiki/Binary_search_tree). It turns out that trees are a more efficient way
to achieve the same asymptotic performance but much better suited for modern memory hierarchies than simply applying binary 
search.
Such trees allow for O(log n) lookup time for equality and "range" conditions over a particular indexed attribute.
If we would like to answer queries independently over multiple attributes we have to build multiple indexes.

Beyond sorting, there are many different ways to achieve the same performance (depending on the type and nature of the 
desired conditions).

* Hash Index. Allow for O(1) equality condition lookup over an attribute.

* Inverted (Full Text) Index. Find all textual records that contain a word in O(1) time.

We will discuss some of the details of these indexing structures throughout the course, but needless to say, that indexing is important!

## Machine Learning for Indexes
Indexing has been studied in computer science for over 70 years, but interestingly enough, there have been major (controversial) 
new ideas about the area in the past 2 years. I encourage you to read the following research paper. 

Kraska, Tim, Alex Beutel, Ed H. Chi, Jeffrey Dean, and Neoklis Polyzotis. "The case for learned index structures." 2018.

While the verdict is still out on whether such approaches can actually upend 70 years of data structure research, the ideas in the
paper are thought-provoking.
