# Data Engineering
The goal of a data engineer is to use software systems to facilitate human or automated decision making based on data. 
The process of building such systems often involves multiple different frameworks, programming models, and design 
considerations. To be able to qualitatively compare systems, we highlight some of the main tradeoffs that every data 
engineer needs to know. 

## Data Science Life Cycle
First, it is important to understand the *data science life cycle*--- the stages that a particular unit of data goes through from its initial generation or capture to its analysis:

- Generation: Data comes into an organization through data entry, acquisition from an external source or signal reception, such as transmitted sensor data.

- Exchange: The data are processed prior to its use to match the format desired by the analysts downstream. Data are extracted , transformed, and formatted appropriately. In this stage, data errors or bugs are often identified and fixed.

- Storage: The data are stored in a system like a database that allows analysts to query and search for relevant data.

- Analysis: A data analyst uses the data in a desired way to build a model or write a report.

- Decision: The results of the analysis are used to make a decision (either manual or automated).

- Maintenance: When new data arrive, the analysis is often redone or modified.

 The goal of data engineer is to make this life cycle possible by building the right software tools. A key piece is ensuring that decisions derived from data can be made in a timely and reliable way.

## How Fast is Fast Enough?
Data is only useful if it helps us make decisions in the real-world. Real-world decisions have requirements on their 
timeliness. For example, choosing to shut down a chemical process after it has catastrophically failed is pointless. 
Or, less dramatically, if a user clicks on a link on a website, a triggered database query has a limited time before the
user loses interest. This notion of timeliness is what we call "latency".

Latency is a time interval between a trigger (arrival of some data or user input) and system response (returning a result). 
Intuitively speaking, latency measures how quickly a system delivers a final result to a user and depends on a number of 
factors along the way such as the hardware, the network, and the other processes using the same infrastructure. It is
sometimes useful to think about what the dominant contributor to latency is.

- CPU Bound means the rate at which process progresses is limited by the speed of the CPU. A task that performs calculations on a small set of numbers, for example multiplying small matrices, is likely to be CPU bound.

- I/O Bound means the rate at which a process progresses is limited by the speed of the I/O subsystem. A task that processes data from disk, for example, counting the number of lines in a file is likely to be I/O bound.

- Memory bound means the rate at which a process progresses is limited by the amount memory available and the speed of that memory access. A task that processes large amounts of in memory data, for example multiplying large matrices, is likely to be Memory Bound.

- Cache bound means the rate at which a process progress is limited by the amount and speed of the cache available. A task that simply processes more data than fits in the cache will be cache bound.

The solution to being I/O bound isn't necessarily to get more memory or buy faster disk. In some situations, the access 
algorithm could be designed around the I/O, memory or cache limitations. 

### Simultaneous Decisions and Arrival Rates
It is easy to get caught up with latency as a primary measure of system performance, but it is actually not that meaningful 
in many contexts. Consider this thought experiment. Imagine, I have a compute node that can process one record at a time. If 
another record arrives while I'm processing, I will have to wait until the one that is currently processing completes. Suppose, 
I have one system that processes records at 1s/record, and another system that processes at 1.5s/record but has two such nodes 
(records arrive at which ever one is free). 
The latency of the first system is faster: for a single record, regardless of the number of nodes you have it will still take 
1.5s. However, the arrival rate of data can be supported by the second system is much higher (1.3 records/sec---i.e., 1/0.75).
This difference gives us the measure of throughput: throughput is the rate of production of results or the rate at which something is processed.

## Readings
Data Science Workflow: Overview and Challenges. Philip Guo. October 30, 2013
https://cacm.acm.org/blogs/blog-cacm/169199-data-science-workflow-overview-and-challenges/fulltext
