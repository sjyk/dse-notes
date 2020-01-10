# What is "Big" Data
The Digital Age has changed how we as humans make decisions. The vast amount of available digital data 
and the facilities to process them allow for new types of quantitative reasoning that is revolutionizing science, 
industry, and the arts. Over the last several years a neoligism called "Big Data" has captured the public's interest. "Big" 
seems imprecise, so what does it actually mean? To make sense of this question, we'll have to start by thinking about how a typical 
computer is designed.

## Memory Hierarchy
All computation requires memory---scratch space to store inputs, intermediate states, or final results. It is an important challenge to figure out how much memory to build into a computer. The goals in memory design are to:
- have enough of it (gigabytes, terabytes,),
- make it fast (at least as fast as the CPU),
- make it affordable (not too expensive).

These goals are challenging to combine since fast memory, such as S-RAM, is very expensive, while cheaper memory, such as D-RAM, is slower and the cheapest memory, like, e.g., hard drive storage, is extremely slow compared to S-RAM or D-RAM. Building memory based on S-RAM only would make it too expensive though. Building memory based on D-RAM only would soften the price but slow down the overall performance significantly.
The differences in speed are huge: disk is about 40,000 times slower than SRAM. Something that takes 1 sec to read on SRAM, would require 11 hours to read from disk!
Thus, almost every computer today has a memory hierarchy where it has some amount of fast memory and some amount of slower, cheaper memory. 

A typical desktop computer today has the following allocation:
- SRAM (most expensive) 8MB
- DRAM (or "memory") 16 GB
- SSD/HDD (or "disk") 1 TB

A software system moves information around the hierarchy to give the programmer an illusion of one big pool of memory. 
Data moves from disk to DRAM and to the CPU every time an operation needs to be done on it.
A downside of this approach are "performance cliffs" when a program just about exceeds the size of one of the hierarchy layers--forcing data to be transferred.

## Exceeding "Main" Memory
Processing data is a primary use of computing today. 
This consequence represents a major change from the earliest days of computer science where most of the information considered by a program was its own internal state.
To engineer systems that process data, one must fundamentally understand *how to write robust programs against external data*. 
External data can be significantly larger than any internal states that a program needs to manage--so the performance cliffs are more evident.

We can break the world into two main settings:
- Data that fits in "main memory" (i.e., DRAM)
- Data larger than "main memory" 

Most of the tools that you have seen in class fall into the first category, such as Pandas DataFrames in Python. The entire dataset must comfortably fit DRAM to be able to use the software. In this setting, computation is the main bottleneck. To write efficient code, we must simply focus on reducing the number of operations that we do on the data. 
The second regime adds a new engineering wrinkle. The cost of transferring data between the layers of the hierarchy can be very significant. In many case, the cost of transferring data can be much greater than the cost of computing on it. Algorithms that do more transfers but less compute operations--may actually be slower. 

This is a good working definition of "big" data: data that does not fit in main memory of a typical desktop computer.
When you have big data conventional software engineering tricks and data structures stop working and you have to design a suite of new methods engineered to optimize the movement of large amounts of data between different types of memory.

When data exceed main memory, there are three main solutions that we can employ:
- Out-of-core programs: algorithms that are designed to optimally move data in the memory hierarchy best for their task.
- Distributed programs: leveraging the combined memory of multiple computing nodes.
- Approximation: simplifying the task (e.g., using sampling) so that the data fits into memory.

We'll focus a bit on the first two as they are the most interest (and not a cop-out!).

## Out-of-core programs
One strategy for memory management is *virtualization*. Memory virtualization is when an application believes it has more memory than it actually does, and a secondary process fetches and replaces memory seemlessly.
Computer operating systems provide each program with a virtual memory address space that is effectively infinite. The program can use this address space as if it were main memory.

Behind the scenes, the underlying memory management system implements paging, a scheme by which a computer stores and retrieves data from secondary storage for use in main memory.
In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages. Paging is an important part of virtual memory implementations in modern operating systems, using secondary storage to let programs exceed the size of available physical memory.

The paging strategies used in operating systems are agnostic to the program that the user writes. These are often not efficient enough for data-intensive programs. Efficiency means minimizing excessive use of the secondary storage.
In a Big Data setting, we are often working with scales that are large enough that small overheads matter. Fetching a 4KB block of data from a modern SSD hard-drive takes roughly $1 ms$. 1TB of data contains nearly 200M such blocks. If even 1\% of fetch requests are spurious or at an inopportune time, we waste almost 45 minutes computation. 

Careful, program-specific memory management is studied in the field of out-of-core algorithms.
Out-of-core refers to a set of algorithms working with data that cannot fit into the memory of a single computer, but that can easily fit into some data storage such as a local hard disk or web repository.
In this model, we explicitly give the algorithm the control to page in and page out data. The developer can choose how and when to do it for each block of data.

## Distributed programs
Data parallism is parallel computing scheme where we distribute the data across different nodes, which each operate on the data in parallel. It contrasts with task parallelism as another form of parallelism (which places computation processes on different nodes). 
A shared-nothing architecture is a distributed-computing architecture in which each update request is satisfied by a single node (processor/memory/storage unit). The intent is to eliminate contention among nodes. Nodes do not share (independently access) memory or storage. One alternative architecture is shared everything, in which requests are satisfied by arbitrary combinations of nodes. This may introduce contention, as multiple nodes may seek to update the same data at the same time.


