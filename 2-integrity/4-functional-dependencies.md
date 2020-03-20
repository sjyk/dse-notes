# Functional Dependencies
Functional Dependencies constitute an important class of integrity constraints. A functional dependency, informally, defines a functional, a type of many-to-one mapping, relationship between columns. For example, there is a functional depedency between Social Security Number and Name:
| SSN     | Name          |
|---------|---------------|
| 798-12-445 | John Smith    |
| 811-46-231 | James Griffin |
| 321-53-996 | Alexa Davis |
|... | .. |
| 616-26-231 | Jenny Waldo |
Many different people can have the same name, but no two people can have the same SSN. The way to read this relationship is SSN "determines" Name, that means if you know an SSN number you can (in theory at least!!!) uniquely figure out a name associated with it. This relationship is clearly not bidirectional: if you know the name, you can only figure out the SSN up-to people with the same name. Mathematically, we can think of Name as a function of SSN--there exists some hypothetical that maps the domain of SSNs to Names.

Functional dependencies can span more than two columns. Make AND Model determines the Safety Rating where all cars with the same make and model have the same safety rating:
| Make   | Model   | Feature Package |Safety Rating |
|--------|---------| ---------------| ---------------|
| Toyota | Corolla | LE |B+            |
| Toyota | Corolla | S |B+            |
| Honda | Civic   | V | A-            |
| Toyota | Camry   | L | B+            |
| Toyota | Camry   | LE | B+            |
| Toyota | Camry   | XLE | B+            |
| ... | ...  | ...           |
| Ford | Fiesta   | V | B            |

## Why Do We Care?
Functional dependencies model many important constraint relationships in a database. We can define a set of functional dependencies and test whether our database actually satisfies them.

* Key Constraints: An attribute is a "key" if it functionally determines all other attributes (think username, ssn, etc.). 

* One-to-One Constraints: If two attributes functionally determine each other they are basically the same information but translated into another domain.

* Machine Learning: Almost all of machine learning is based on "function approximation", i.e., fitting a function that best represents a relationship between multiple data columns. 

## Readings
https://opentextbc.ca/dbdesign01/chapter/chapter-11-functional-dependencies/
