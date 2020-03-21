# Data Organization: Storage
The first decision that any organization has to make is how and where to store data. This relates back to our earlier discussions about structure, unstructured, and semi-structured data. The choice of storage engine has significant organizational, management, and analysis implications.

## Data Lake
The simplest thing to do is a "data lake". A data lake is a centralized repository that allows you to store all your structured and unstructured data at any scale. Think about Dropbox or Google Drive at industrial scale. You can store your data as-is, without having to first structure the data and there are import/export tools that allow you to move structured data (like csv files) into analysis frameworks like Pandas or Apache Spark. Data lake systems often provide simple tools to search for relevant data and organize/tag data. 

Pros:
- A central store for diverse, multimodal, and complex data.
- The upfront investment is minimal.
- Low cost. 

Cons:
- Linking datasets together is very challenging.
- Access rights, privacy, governance are managed per "dataset".
- Have to move to another system to analyze the data.

Infrastructure Cost (on Amazon):
- About $250/Month for 10 TB of data (the cost of using S3, and Amazon Lake Catalog)

## Relational Databases
A relational database is a storage and retrieval system optimized for structured data that conform to fixed schemas.
A relational database is a set of formally described tables from which data can be accessed or reassembled in many different ways without having to reorganize the database tables. 
Databases can be updated, manipulated, and queried concurrently---they are designed to preserve integrity of the data residing them. The gold standard of integrity in databases is referenced by the acronym ACID. A database guarantees the following four properties to ensure database reliability, as follows:

-Atomicity: A database follows the all or nothing rule, i.e., the database considers all transaction operations as one whole unit or atom. Thus, when a database processes a transaction, it is either fully completed or not executed at all.

-Consistency: Ensures that only valid data following all rules and constraints is written in the database. When a transaction results in invalid data, the database reverts to its previous state, which abides by all customary rules and constraints.

-Isolation: Ensures that transactions are securely and independently processed at the same time without interference, but it does not ensure the order of transactions. For example, user A withdraws $100 and user B withdraws $250 from user Z’s account, which has a balance of $1000. Since both A and B draw from Z’s account, one of the users is required to wait until the other user transaction is completed, avoiding inconsistent data. If B is required to wait, then B must wait until A’s transaction is completed, and Z’s account balance changes to $900. Now, B can withdraw $250 from this $900 balance.

-Durability: In the above example, user B may withdraw $100 only after user A’s transaction is completed and is updated in the database. If the system fails before A’s transaction is logged in the database, A cannot withdraw any money, and Z’s account returns to its previous consistent state.

You'll hear about these properties in much more detail in a proper database class, but it's worth talk about consistency a little bit more. Databases enforce referential integrity, or a property of data stating that all its references are valid (for example customer ID formats are consistent across business units). It requires that if a value of one attribute (column) of a relation (table) references a value of another attribute (either in the same or a different relation), then the referenced value must exist. These constraints crucially allow users to link data between different tables in a disciplined way because references across tables are expected to be consistent. Designing such a structure and the appropriate referential integrity constraints is a very big challenge. Organizations spend millions of dollars structuring data and design schemas.

The standard user and application programming interface (API) of a relational database is the Structured Query Language (SQL). SQL statements are used both for interactive queries for information from a relational database and for gathering data for reports. This standardization of programming model allows databases to plug into front-end applications (like websites and dashboards) and back-end applications like data analysis programs.

Pros:
- Linking datasets together can be done easily through SQL
- Analysis can be done in the same system as storage
- API connections to many different front-end and back-end programming langugages.
- Access rights, privacy, governance are managed centrally by the database.

Cons:
- Only works for structured data
- The up-front cost of putting your data into a database is very high.
- Expensive! (20x more than a data lake).

Infrastructure Cost (on Amazon):
- About $5100/Month for 10 TB of data (the cost of using a ds2.8xlarge node with Amazon Redshift)

## Non-Relational Databases
In response to the issues seen with relational databases, there was a movement that started in the 2010s around "NoSQL". NoSQL 
started with the premise that the upfront costs of putting data into a database were simply too high: developers were working with applications that create massive volumes of new, rapidly changing data types — structured, semi-structured, unstructured and polymorphic data. Furthermore, a faster, lighter database was more suited to the agile development lifestyle in many small companies. 

NoSQL providers simplified their programming models, reduced features, and relaxed the rigid definitions of correctness in relational databases. Key NoSQL systems were:

- Document databases pair each key with a complex data structure known as a document. Documents can contain many different key-value pairs, or key-array pairs, or even nested documents.

- Graph stores are used to store information about networks of data, such as social connections. Graph stores include Neo4J and Giraph.

- Key-value stores are the simplest NoSQL databases. Every single item in the database is stored as an attribute name (or 'key'), together with its value. Examples of key-value stores are Riak and Berkeley DB. Some key-value stores, such as Redis, allow each value to have a type, such as 'integer', which adds functionality.

- Wide-column stores such as Cassandra and HBase are optimized for queries over large datasets, and store columns of data together, instead of rows (think of these as single table relational databases optimized for aggregation)

Pros:
- Analysis can be done in the same system as storage
- Access rights, privacy, governance are managed centrally by the database.
- Easier to setup.

Cons:
- Correctness has always been iffy in these systems
- Linking datasets together can be challenging depending on how you are storing your data
- Unclear if it's actually cheaper to use

Infrastructure Cost (on Amazon):
- About $7215/Month for *1* TB of data (the cost of using an M100 node on AWS)

