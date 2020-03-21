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

| Color |
|-------|
| Red   |
| Black   |
| Red   |
| ...   |
| Green   |
| Blue  |

If we think about representing this data in a programming language, one has to allocate 8-bits to each character in each string. However, if we look at this list as a fixed dataset with a known domain of colors, we can represent it far more efficiently. Suppose we knew there were only 4 possible colors {red, blue, green, black} we could assign a 2-bit number to each of the colors {00, 01, 10, 11}, and store a lookup table to translate between strings and numbers {red=>00, blue=>01, green=>10, black=>11} (144 bits of information). The actual list is stored far more efficiently:

| Color |
|-------|
| 00   |
| 11   |
| 00   |
| ...   |
| 10   |
| 01  |






