# Data Governance
Data governance is the overall management of the availability, usability, integrity and security of data used in an enterprise. Businesses benefit from data governance because it ensures data is consistent and trustworthy. Increasingly, these considerations are important in the design of data systems.

## Data Provenance
Provenance is defined as tracking data's origins and where it moves over time. This term can also describe what happens to data as it goes through diverse processes. Tracking provenance can help with efforts to analyze how information is used and to track key bits of information that serve a particular purpose. Data provenance turns out to be a very complex problems, and we will work with a relatively straight-forward working definition: given an output of an analysis, list all source data necessary to exactly reproduce the output.

Let's think about a concrete example and explain all of the different things one could do. Below is the table that we've seen in our notes before. Suppose this table is in a file named `data.csv`:

|  id  | Make  | Model | Year | Color |
|----|----|----|----|----| 
|1| Toyota | Corolla | 2018 | Red |
|2| Toyota | Camry | 2015 | Blue |
|3| Honda | Fit | 2014 | Black |

We run an analysis to generate a new file called `toyota_colors.csv` that returns a count of the number of cars with each color that are made by Toyota:

|  Color  | Count  |
|----|----|
| Red  | 1 |
| Blue | 1 | 

The first thing we have to define is the *granularity* of provenace. At the level of files, the *necessary* source is `data.csv`. At the level of records, the necessary source is record 1 and record 2. Both granularities are interesting in different contexts. If we were managing a data lake for a large company and wanted to know which files could be safely deleted the coarser grained provenance is sufficient. If we wanted to understand which particular records in our dataset contributed to a result (maybe because some of them were corrupted), the finer-grained provenance is needed. In general, provenance relationships will give you a directed acyclic graph of sources connected to outputs (which themselves might be used in other computations).

This seems like a lot of work, why even do it? Here are some reasons:
- Efficiency: If certain data (or intermediate results derived from them) are used frequently in analyses than others they should be cached in memory or faster storage systems.
- Reproducibility: If one needs to reproduce an analysis, a detailed description of the data's movement from source to final state is required.
- Compliance and Regulatory: Increasingly there are legal frameworks like GDPR that restrict how data can be used and how can be moved.

## Data Access Restrictions
Another part of data governance is figuring out who can and should use your data. Let's talk a bit about why this is important. 

### Potential Harm
When collecting any data the first thing to assess is "potential harm", or how could this data be used to adversely affect those who contributed it monetarily, physically, emotionally, or otherwise. Potential harm is independent of the original intent or purpose of the data collection. Potential harm does not necessarily require a data leakage, it could also be internal use for the same data. For example,

- Tinder records, if leaked, could significantly affect the lives of many users.
- Transaction data originally collected to evaluate sales could be repurposed to score the credit-worthiness of customers.
- Credit card data can track the movements of users.

It is good practice to list all reasonable potential adverse uses of a dataset before collecting it. Not only is it a customer friendly practice, it can convey due dilegence to any regulatory authority that may question the collection/use/processing of the data.

### Personal Data
Personal data is data that can be tied to a single "natural" person, such has electronic health records, financial data, and eduction data. Such data is often regulated much more stringently than any other type of data. The key standard with personal data is "identifiability": linking a person's name or charachteristics to a key, uniquely identifiable attribute. For example, student id numbers are consider sensitive attributes as they can uniquely identify students under FERPA. 

### Principle of Minimum Privelege
The principle of least privilege works by allowing only enough access to perform the required job. In an IT environment, adhering to the principle of least privilege reduces the risk of attackers gaining access to critical systems or sensitive data by compromising a low-level user account, device, or application. Implementing the POLP helps contain compromises to their area of origin, stopping them from spreading to the system at large.

## Readings
Joanna Redden and Jessica Brand. Data	Harm Record. 2017. https://datajustice.files.wordpress.com/2017/12/data-harm-record-djl2.pdf
