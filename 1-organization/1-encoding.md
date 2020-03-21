# Organization: Mapping Real-World Data to Bits
Modern data analysis software is sometimes *too* helpful as it abstracts so many of the machine-level concerns about data. After all, to a computer your data is simply 1s/0s on a disk and any semantic meaning beyond that is imputed in software. In this lecture, we'll try to demystify these details---but will also be purposefully simplistic and unsophisticated as the details themselves vary across different software and hardware architectures.

## Fixed-Length and Variable-Length Data
How does "real-world" data map to 1s and 0s? The first step is to figure out how many such 1s and 0s you need. Fixed-length data are data types where the size of one item of that type is known in advance (regardless of the actual value the data takes). Basically, things that look like numbers are fixed-length types. For example, boolean data types (true and false) take 1-bit of information regardless of if the datum is true or false. Here are typical sizes that we work with:

* Boolean represented by 1 bit
* Integer represented by 32 bits
* Float represented by 64 bits

Variable length data like arrays and strings take up a different number of bits depending on the size or the length of the data. For example, strings take up 8-bits (1 byte) per character.

## Representing Sets of Data
Those of you who have taken an introductory computer architecture course should be very familar with sizing data and allocating storage or memory to data structures. However, the story changes a bit when we start considering collections of data. Consider a list of strings:

| Color |        |        | ...    |        |         |
|-------| -------| -------| -------| -------| -------|
| Red   | Black   |  Red   | ...   | Green   | Blue  |
 

If we think about representing this data in a programming language (for example C++), one has to allocate 8-bits to each character in each string and have one extra character to demarcate the next string:

'R','e','d',0,'B','l','a','c','k','R','e','d',0,...,'G','r','e','e','n',0,'B','l','u','e'0

This world view is pessimistic in a sense--real-world data often follow sensible patterns that our system can exploit and store this same information much more efficiently. 

For example, we might have prior knowledge that there are only 4 possible colors {red, blue, green, black} in this dataset. In that case,  we could assign a 2-bit number to each of the colors {00, 01, 10, 11}, and store a lookup table to translate between strings and numbers {red=>00, blue=>01, green=>10, black=>11}. The actual list is then stored far more efficiently '0011...1001':

| Color |        |        | ...    |        |         |
|-------| -------| -------| -------| -------| -------|
| 00   | 11   |  00  | ...   | 10   | 01  |

Let's analyze this example in detail assuming 8-bit characters including termination and that each color was equally likely. 

* Average cost of storing each string raw: 4 possible strings, 5.25 characters per string (including termination), 42-bits of information per string.

* Average cost of storing each string encoded: 2 bits per string

* Total cost of storing the lookup table: 5.25 characters per string + 2 bits for each code = 176 bits

So the tradeoff is that storing the raw strings scales in terms of storage as f(n) = 42n and storing the encoded strings scales as f(n) = 2n + 176--if you store more than 5 strings the encoding representation is more efficient and get better and better the more store. 

This type of data encoding is called *dictionary encoding* where a variable-sized, infinite domain data type (like strings or arrays) are mapped down to a fixed-length domain based on prior assumptions. It should be obvious from the example that this really only works well if the list of strings is highly repetitive (because there is an overhead to storing the lookup table). This turns out to be a general principle of *data compression*, data that are repetitive or redundant are easier to compress. 
