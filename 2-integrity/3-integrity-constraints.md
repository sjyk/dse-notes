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

the above table has two different people with the same username (which might be inconsistent with what the system expects). Such errors are data integrity issues that occur at a "logical" level of the data model. The notion of correctness is independent of how the data are physically (in terms of bits and bytes) actually stored.

## Syntactic v.s. Semantic Errors

## Common Examples

## Data Cleaning

## Readings
Ilyas and Chu. Trends in Cleaning Relational Data: Consistency and Deduplication. 2015
