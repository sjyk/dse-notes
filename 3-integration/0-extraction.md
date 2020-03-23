# Data Extraction
Loading data into a structured format, such as a relational database or a dataframe, is an under-appreciated challenge in data engineering. In fact, the process of extracting structured fields from even already reasonably structured data (like CSV files) is not trivial. This phase of data analysis is often called extract, transform, load (or ETL for short).There are three database functions that are combined into tools to pull data out of a raw format and place it into another database.

* Extract is the process of reading data from a database. In this stage, the data is collected,
often from multiple and different types of sources.
* Transform is the process of converting the extracted data from its previous form into the
form it needs to be in so that it can be placed into another database. Transformation occurs
by using rules or lookup tables or by combining the data with other data.
* Load is the process of writing the data into the target database

## Types of Raw Data
To understand why this is a challenge, let's taxonomize different "raw data" formats. 

### Delimited Formats
Perhaps, the most familiar format to those who have taken a data science or a machine learning class is a "delimited" format (such a file with Comma-Seperated Values). Such formats store two-dimensional arrays of data by separating the values in each row with specific delimiter characters (like commas or tabs). Most database and spreadsheet programs are able to read or save data in a delimited format. Due to their wide support, DSV files can be used in data exchange among many applications. A delimited text file is a text file used to store data, in which each line represents a single book, company, or other thing, and each line has fields separated by the delimiter. Consider the following example of a "comma" delimited file:

First, Last, SSN, Date of Birth

Bob, Davis, 123-45-2312, 1991-02-09

One challenge with delimited files is when the delimiter appears in one of the data fields. For example, 

First, Last, SSN, Date of Birth, Comments

Bob, Davis, 123-45-2312, 1991-02-09, Bob is a great worker, but he lacks focus

To address such issues, we usually define an "enclosure" character which encloses whole fields when the delimiter might be in the field. Typically, for CSV files, that is a ".

First, Last, SSN, Date of Birth, Comments

Bob, Davis, 123-45-2312, 1991-02-09, "Bob is a great worker, but he lacks focus"

What happens when we have to use the enclosure character in one of the fields as well? Typically, we define an "escape" character as well that can short circuit the parsing when a special character needs to be used:

First, Last, SSN, Date of Birth, Comments

Bob, Davis, 123-45-2312, 1991-02-09, "Bob is a great \"worker\", but he lacks focus"

### State Machine Parsing
It should be clear from the examples above that parsing a delimited file is harder than simply looking for all occurances of the delimiter. Usually, we model the parser as a "state" machine. A state-machine is a abstract model that has a finite set of states and "transitions" between the states based on rules. Essentially, during parsing we define all the possible states the parser can be in and then for each character we define transition rules. 

Let's walk through a simplified delimited format where there are no escaped characters and quotes always enclose a field:

name, id, comments
Bob Davis,1,"Davis, Bob"

We can define the following states:
* (1) Start field
* (2) In field
* (3) In quote
* (!) Error

We can define the following state transitions:
* Start field (initial state)
  - If quote: transition to In quote
  - If comma: transition to Error
  - Else: transition to In field
* In field
  - If comma: transition to Start Field
  - If quote: transition to Error
  - Else: transition to In field
* In quote:
  - If quote: transition to Start Field
  - Else: transition to In Quote

So when, we parse the following record, we get the following states:

Bob Davis,1,"Davis, Bob"

122222222121333333333333

All of the characters that correspond to "start field" states (the ones), are the points we need to split on. Real-world finite-state machine sare far more complicated:

![State Machine](https://sourcemaking.com/files/sm/state_delphi.png)

### API Formats


### Binary Formats



## Sub-attribute Parsing
