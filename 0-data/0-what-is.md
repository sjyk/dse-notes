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
It is important to recognize that digital data is artificial in a sense. They are simply electronic bits and bytes with no inherent meaning. An engineer has to define how these electronic signals correspond to real-world concepts. A *data model* defines how different pieces of digital data are organized, defines how they relate to one another, and how these representations correspond to the properties of real-world entities.

For example, suppose we are collecting data about cars including the make, the model, the year, and color. A data model specified how this information will be represented on a computer in terms of data types and properties:
```
Car:
   Make <String>
   Model <String>
   Year <Integer>
   Color <String>
```
The data model could additionally consist of references to other entities (like owners), representing other kinds of things of significance in the domain, and so one. 

Logical data model : describes the semantics, as represented by a particular data manipulation technology. This consists of descriptions of tables and columns, object oriented classes, and XML tags, among other things.

Physical data model : describes the physical means by which data are stored. This is concerned with partitions, CPUs, tablespaces, and the like.

The significance of this approach, according to ANSI, is that it allows the three perspectives to be relatively independent of each other. Storage technology can change without affecting either the logical or the conceptual model. The table/column structure can change without (necessarily) affecting the conceptual model. In each case, of course, the structures must remain consistent with the other model. The table/column structure may be different from a direct translation of the entity classes and attributes, but it must ultimately carry out the objectives of the conceptual entity class structure. Early phases of many software development projects emphasize the design of a conceptual data model. Such a design can be detailed into a logical data model. In later stages, this model may be translated into physical data model. However, it is also possible to implement a conceptual model directly.

## Types of Data
Philisophically, data can literally be anything. However, it is useful to taxonomize digital data into three categories: unstructured, semi-structured, and structured data. It will be useful to work backwards from the most restric 



