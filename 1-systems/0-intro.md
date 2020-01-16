# Systems for Data Science
Now that we understand what data is and how to interpret it, let's wrap our heads around some of the marketing terms used to describe systems for data science. 

## Data Science Life Cycle
First, it is important to understand the *data life cycle*--- the stages that a particular unit of data goes through from its initial generation or capture to its analysis:

- Generation: Data comes into an organization through data entry, acquisition from an external source or signal reception, such as transmitted sensor data.

- Exchange: The data are processed prior to its use to match the format desired by the analysts downstream. Data are extracted , transformed, and formatted appropriately. In this stage, data errors or bugs are often identified and fixed.

- Storage: The data are stored in a system like a database that allows analysts to query and search for relevant data.

- Analysis: A data analyst uses the data in a desired way to build a model or write a report.

- Decision: The results of the analysis are used to make a decision (either manual or automated).

- Maintenance: When new data arrive, the analysis is often redone or modified.

For each one of these stages, we will provide some examples of tools that are used.

## Generation
Data has to come from somewhere. Systems are needed to route data from the point of generation to the appropriate analytics framework. For example, we may want a system that collects log messages generated from a web application and stores them in a database. Or, we may want a system to listen to a motion sensor and generate a data record every time a value exceeds a certain threshold. These systems called "streaming" platforms offer following basic capabilities: (1) publish and subscribe to streams of records, (2) process streams of records as they occur, and (3) store streams of records in a fault-tolerant durable way. Examples include, Apache Kafka, IBM Streams, Apache ZooKeeper. These systems are designed for high-throughput applications--reading data from many parallel sources at once and aggregating them together. 

## Exchange

https://www.tamr.com/
https://www.trifacta.com/
spark

## Storage
https://www.oracle.com/database/
Data Lake

## Analysis
Pandas
Tensorflow
R
spark

## Decision
Tensorflow serving

## Maintenance
ML Flow
