# Data Organization
Now that we understand what data is and how to interpret it, let's wrap our heads how data is stored and governed. These may seem like un-academic topics, but are increasingly important as the scale and scope of data driven applications grow. We will see different choices can greatly affect the usability and cost of building such applications.

## Data Science Life Cycle
First, it is important to understand the *data life cycle*--- the stages that a particular unit of data goes through from its initial generation or capture to its analysis:

- Generation: Data comes into an organization through data entry, acquisition from an external source or signal reception, such as transmitted sensor data.

- Exchange: The data are processed prior to its use to match the format desired by the analysts downstream. Data are extracted , transformed, and formatted appropriately. In this stage, data errors or bugs are often identified and fixed.

- Storage: The data are stored in a system like a database that allows analysts to query and search for relevant data.

- Analysis: A data analyst uses the data in a desired way to build a model or write a report.

- Decision: The results of the analysis are used to make a decision (either manual or automated).

- Maintenance: When new data arrive, the analysis is often redone or modified.

In your previous classes, the first three steps of this pipeline were largely taken for granted. You were given datasets that
already appeared in ready-to-analyze formats (maybe up to small amounts of cleaning or transformation). In this unit, we are going zoom in on the storage layer and think about the different choices we have store data. Storage is sort of the key stone of this process. There are really only a handful of different design choices but those choices can greatly affect upstream and downstream processes.

## Readings
Data Science Workflow: Overview and Challenges. Philip Guo. October 30, 2013
https://cacm.acm.org/blogs/blog-cacm/169199-data-science-workflow-overview-and-challenges/fulltext
