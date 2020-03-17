# Integrity Constraints
The previous lectures describe "bitwise" data integrity--meaning that do the bits of data entered into a system match an expected value. Such a model for integrity does not account for data that are simply wrong or inconsistent in a real-world sense. For example, one could have a table of zipcodes and median house prices:

| City          | Zipcode | Median Price |
|---------------|---------|--------------|
| Chicago, IL   | 60616   | 569,992      |
| St. Louis, MO | 60616   | 399,451      |

with a typo that implies 60616 is in Missouri. Or, we could have a dataset as follows,

| Username | First | Last     | Balance |
|----------|-------|----------|---------|
| jtaylor  | John  | Taylor   | 123.22  |
| zebra221 | David | Anderson | 54.22   |
| jtaylor  | Josh  | Taylor   | 1882.1  |

the above table has two different people with the same username (which might be inconsistent with what the system expects). Such errors are data integrity issues that occur at a "logical" level of the data model. The notion of correctness is independent of how the data are physically (in terms of bits and bytes) actually stored. It really only makes sense to talk about such issues in structured data since the data model is precise about what each row, column, and cell means.

## Syntactic v.s. Semantic Errors
There are two principal types of "logical" data errors: syntactic and semantic. Syntactic errors concern a single cell, namely, determining whether a value is "wrong" or not can be done independent of anything else in the dataset. For example, you could have a malformed zipcode (not the right number of digits):

| City          | Zipcode | Median Price |
|---------------|---------|--------------|
| Chicago, IL   | 6061   | 569,992      |

or that all balances should be positive: 

| Username | First | Last     | Balance |
|----------|-------|----------|---------|
| jtaylor  | John  | Taylor   | -123.22  |

When thinking about syntactic errors, it is useful to think of issues relating to formating and parsing. Semantic errors, on the other hand, concern relationships between rows. It makes no sense to ask whether a single row is wrong on its own. For example, the two rows below are incorrect because they both share a username:

| Username | First | Last     | Balance |
|----------|-------|----------|---------|
| jtaylor  | John  | Taylor   | 123.22  |
| jtaylor  | Josh  | Taylor   | 1882.1  |

A more complicated issue might be a database of employee salaries and noticing that an employee gets paid more than their manager:

| Rank | First | Last     | Salary |
|----------|-------|----------|---------|
| Employee  | John  | Taylor   | 1231.22  |
| Supervisor  | James  | Baldwin  | 1996.95  |
| Employee  | Dana  | Smith  | 1094.31  |
| Employee  | Jeff  | Daskin  | 2011.01  |

## Constraint Languages
Data engineers must be able to *specify* constraints over structured data to detect such problems. Integrity constraints are a set of rules that are used to maintain the quality of information. Integrity constraints ensure that the data insertion, updating, and other processes have to be performed in such a way that data integrity is not affected. Thus, integrity constraint is used to guard against accidental damage to the database.

We generally do not describe arbitrary rules over data, and we formalize common relationships using a specialized programming language called a "constraint language". A constraint language is a formal model for specifying integrity constraints of
interest—it essentially describes a restricted class of relationships that are verifiable and axioms to reason about these constraints (e.g., are two constraints equal to each other). Such common tasks restrictions are:

* Column uniqueness: every value in a column is unique
* Domain integrity: every value in a column comes from some known set of strings
* Functional dependence: every value in one column uniquely maps to a value in another column
* Coexistence: two rows that are consisdered inconsistent with each other and cannot both exist

## Data Cleaning
In your previous classes, you've hopefully spent a bit of time thinking about "data cleaning". A more sophisticated way of thinking about data cleaning is in terms of integrity constraints. You have a database that violates a set of constraints and data cleaning is the process of enforcing those constraints. 

## Readings
Ilyas and Chu. Trends in Cleaning Relational Data: Consistency and Deduplication. 2015
