# What is data good for?
It seems like data is everywhere...so what can we do with it? There are really two interpretations of data that are worth thinking about. These interpretations really underpin how we think about algorithms and systems that make use of data. Interestingly enough, these two interpretations defines the core intellectual separation between the "database" view of data, and the "statistical" view of data.

## Data as "facts"
We can interpret data as a representation of facts about the world. A *database* holds such facts and allows users to make principled inferences from these facts using a *query language*. This is a bit abstract so let's think about a concrete example. Suppose we know the following facts: Mary is a citizen of France, Jenny is a citizen of France, and all French citizens wear hats. We can define two tables to represent this information:

People:

| Name  | Citizenship |
|-------|-------------|
| Mary  | France      |
| Jenny | France      |

Countries:

| Citizenship | Wears |
|-------------|-------|
| France      | hats  |

The job of a query language (such as SQL) is to allow a user to make inferences on this data. For example, we can lookup trivial inferences such as "What is Mary's citizenship?", or more complex inferences "Do both Mary and Jenny wear hats?". Such english language statements can be converted into query language code (don't worry about the syntax if you don't know SQL):
```
SELECT Citizenship
FROM People
WHERE Name='Mary';

SELECT Name, Wears
FROM People, Countries
WHERE People.Citizenship = Countries.Citizenship;
```

To allow for such inferences, databases make a crucial assumption called a "closed-world" assumption. The *closed-world assumption* (CWA) is the presumption that a fact that is true is also known to be true. Conversely, everything not currently known to be true, is false. For example, a database will not answer the question "What is Pauls's citizenship?" because such a fact is not present in the database. Languages such as SQL and Datalog are rooted in the closed-world assumption.

## Data as "samples"
What if we collected the names of 100 people and all of them were French citizens---Another way to interpret 


## Readings
Reiter, Raymond. "On Closed World Data Bases". 1978.
