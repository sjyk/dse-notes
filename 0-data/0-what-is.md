# What Is Data?

Jan 10th, 2020.

"Those who cannot remember the past are condemned to repeat it." -George Santayana

Recounting events that have ocurred in the past is a fundemental part of the human experience. The first histories were described by oral traditions passed on from generation to generation. Then, these oral traditions gave way to written accounts of the past. Now, in the modern era, events are documented digitally through media such as audio and video. How do we describe the accumulation of such knowledge over time? Herein defines the abstract concept of *data*. A *datum* is a unit of information---an atomic observation about the world. Data (yes it is plural!) is a collection of such observations.

The basic motivation of this endeavor is *prediction*, i.e., understanding what has happened in the past to be able to know how to act in the future. Therefore, the science of working with data is understanding how and when such predictions work, and judging their reliability. Data Science is essentially the theory of principled prediction.

If data has been around for millenia, why are we studying this now? In short, a confluence of technological and social factors has led to a proliferation of shareable data over the last 40 years.

- Digitization. The invention of the microchip and other semiconductor technologies means that information can be captured, stored, and transferred electronically. 

- Price of storage. Since the mid 1980s, the cost of storing data has reduced by a factor of 35 million. So the economics of data collection have fundementally changed. If your data could possible provide any predictive value for you in the future---you might as well store it because storage is so cheap.

- Standardization and the internet. The advent of the internet forced hardware and software to be interoperable---and more importantly could share and interpret each other's data. In the 1990s, we see a solidification of the popular data formats that we take for granted for documents (PDFs), music (mp3), and video (mpeg).

-  Machine learning and the rebirth of AI. Crucially the 2000s also ushered in a new software engineering paradigm based on Machine Learning. The idea that historical data could be used to "train" software to perform tasks better than any human code code changed the way we think about the value of data. 

## Data Model
It is important to recognize that digital data are artificial in a sense. They are simply electronic bits and bytes with no inherent meaning. An engineer has to define how these electronic signals correspond to real-world concepts. A *data model* defines how different pieces of digital data are organized, defines how they relate to one another, and how these representations correspond to the properties of real-world entities.

For example, suppose we are collecting data about cars in a spreadsheet including the make, the model, the year, and color. A data model specified how this information will be represented on a computer in terms of data types and properties:
```
Sheet 1. Car:
            Col 1. Make <Text>
            Col 2. Model <Text>
            Col 3. Year <Date>
            Col 4. Color <Text>
```

| Make  | Model | Year | Color |
|----|----|----|----| 
| Toyota | Corolla | 2018 | Red |
| Toyota | Camry | 2015 | Blue |
| Honda | Fit | 2014 | Black

The data model could additionally consist of references to other entities (like owners) and references to other sheets and so on. We call such a model a *logical data model*, a conceptual model of how to use the data from an end-user perspective:

- Logical data model: A model that describes the semantics of the data, as represented by the particular data analysis technology. 

It is worth re-emphasizing this point. A logical data model captures how an end-user should use and interpret the presented data. What is missing is how this data is actually stored and represented on a device. Thus, the other half is called the *physical data model*:

- Physical data model : describes the physical means by which data are stored. This is concerned with partitions, CPUs, bits, data types, and so on.

The physical data model describes how a computer (as opposed to the end-user) should interface with the data. One of the key insights in the design of data systems over the past 60 years has been such logical-physical separation. Storage technology can change without affecting the logical model--thus, not forcing the user to re-learn how to use the software if there is a change "under the hood". Modern data analysis tooling essentially lies to the user, where it gives the user an illusion of a intuitive logical model (such as rows and columns in a spreadsheet) which hides a complex and highly optimized physical model (compression/columnar partitioning/caching). This illusion leads to a basic tension in data-intensive systems where advanced users might do things that are inconvenient for the physical model because they lack introspection into the low-level details. 

## Types of Data
Philisophically, data can literally be anything. However, it is useful to taxonomize digital data. Perhaps the most familiar organization of data is into tables of rows and columns. Examples of tabular data models include: spreadsheets, dataframes (like Pandas),and relational databases (like MySQL). While it may seem like an obvious data model, tabular data has many profound properties that are worth highlighting. 

*Tabular data*: A rectangular data structure where rows correspond to observations and each column corresponds to properties (attributes) of the observation. Each column is named. 
   - Fixed attribute domain. The columns names define all of the relevant attributes for each observation. 
   - Atomic values. Each cell (a row, column pair) is generally considered to be an atomic value---i.e., it is not readily divisible--such as, an integer, a date, a string. 
   - NULL values. Missing or uncertain data can only be conveyed with a NULL/empty cell. 

For, example a table of two columns A and B is:

| A  | B |
|---|---|
| -1 | 1 |
| 0  | 0 |
| 1  | 1 |

There are cases when such a model is too restrictive. Suppose, we were building a repository of advanced car features and which makes and models had them. We could add extra columns to indicate feature and which cars had them or not.
```
Sheet 1. Car:
            Col 1. Make <Text>
            Col 2. Model <Text>
            Col 3. Year <Date>
            Col 4. Color <Text>
            Col 5. HasBackupCamera <String>
            ...
```
However, in this model, we would have to add columns for esoteric features as well that only occur in a small number of cars. Furthermore, each year as new features arrive, we would have to explicitly add new columns. A good way of summarizing the main restriction of a tabular model is that the *schema* (or set of attributes that describe each row) is fixed and globally set. 

What if we wanted a flexible schema that varied row to row? This introduces the concept of semi-structured data.

*Semi-structured data*: A data structure where each row has a variable set of attributes the values are possibly not atomic.
```
{'name': Car1, 'features': [BackupCamera, CruiseControl]}
{'name': Car2, 'features': [BackupCamera, ParkingAssist, CruiseControl]}
```

Examples of semi-structured formats include XML, JSON, and other dictionar-like formats. Semi-structured data, as the name implies, does still have crucial structure that is important.

- Named Attributes. The properties of a given row can still be accessed by a semantic name.

In other words, the defining characteric of "structure" is that data properties can be accessed by name. All data that doesn't have this is called "unstructured". This last category includes images, video, documents, text, audio and so on. The vast majority of data in the world is "unstructured".

## Readings
Codd, Edgar F. "A relational model of data for large shared data banks." 1969




