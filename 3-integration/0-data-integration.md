# Data Integration
In many applications, data arrive in formats not conducive to direct analysis. For example, one might be acquiring data from another organization (or unit within the same organization) that has a different schema. Or one might be trying to combine different datasets collected at different times. The process of structuring and integrating one or more datasets into a central database is the problem of *data integration*. In this unit, we look at two key problems: extraction and entity resolution.

## Extraction, Transformation, and Loading
Information extraction (IE), information retrieval (IR) is the task of automatically extracting structured information from unstructured and/or semi-structured machine-readable documents and other electronically represented sources. In the most extreme cases, we have completely unstructured data and we have to use rules or natural language processing to identify relevant structured information. But, as we will see, even loading a single dataset from a nearly structured format (like a Comma-Seperated-Values file) into a database may not be trivial. The data still have to be parsed, validated, and split into the appropriate schema. 

### String Manipulation
The core issue at play here is that most data arrive into our system in string format and we have to convert them into some sort of a structured representation. Strings on their own are an amazingly general data representation.
Every string is a variable-length array of elements from an alphabet (a set of possible symbols). Let $\Sigma$ be an alphabet, $s$ is a finite sequence of elements from $\Sigma$. Examples of $\Sigma$ are the latin alphabet (i.e., upper and lower-case A-Z), the binary alphabet (i.e., 0-1), or the genetic alphabet (i.e., ATGC). 
We will spend a significant amount of time in this unit discussion how to reason about string data.

## Entity Resolution
Entity Resolution is the task of disambiguating manifestations of real world entities in various records or mentions by linking and grouping. For example, there could be different ways of addressing the same person in text, different addresses for businesses, or photos of a particular object. Generically speaking, we can discuss ER as follows: there exists in the real world entities, and in the digital world, records and mentions of those entities. The records and mentions may take many forms, but they all refer to only a single real world entity. We can therefore discuss the ER problem as one involving matching value corresponding to the same entity.


