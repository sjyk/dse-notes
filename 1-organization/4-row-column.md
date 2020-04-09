# Row-Oriented and Column-Oriented Storage
Suppose, we have a collection of records like:

| Make  | Model | Year | Color |
|----|----|----|----| 
| Toyota | Corolla | 2018 | Red |
| Toyota | Camry | 2015 | Blue |
| Honda | Fit | 2014 | Black |
| Honda | Civic | 2014 | Black |

A storage system has to map this collection onto partioned storage blocks with a fixed capacity. Perhaps the most-intuitive way to do so is to partition data row-by-row. Thinking about disk blocks is important because many storage devices retreive data by the block (if you retrieve one byte of the block, you might as well retrieve all of them). For example, suppose we had blocks with capacity for 2 records (this is simiplified because generally capacity is in terms of bytes). We could store the records as:

*Block 1*
| Make  | Model | Year | Color |
|----|----|----|----| 
| Toyota | Corolla | 2018 | Red |
| Toyota | Camry | 2015 | Blue |

*Block 2*
| Make  | Model | Year | Color |
|----|----|----|----| 
| Honda | Fit | 2014 | Black |
| Honda | Civic | 2014 | Black |

It turns out this strategy is not all that naive and is used in many real world systems. A Row-oriented database is a traditional database like Oracle, MySql and etc. It stores data table by row and common method of storing a table is to serialize each row of data. Since all of the data in a row is stored contiguously, row-based systems are designed to efficiently return data for an entire row, or record.

Such a storage scheme is great if you want to retreive entire rows, for example, find all rows of red cars:
```
df[df['Color'] = 'Red']]
```
```
SELECT *
FROM Table
WHERE Color = 'Red'
```

On the other hand, sometimes we are interested in computing aggregates that do not require the entire row. For example, suppose we simply wanted the count of cars that are Red. Many queries are only interested in a small subset of the columns in what could be a very wide table. In this setting, the row-oriented storage scheme is inefficient because extra data are retrieved. The alternative is to store data by columns instead:

*Block 1*
| Color |
|----| 
| Red |
| Blue |
| Black |
| Black |

...

*Block 4*
| Year |
|----| 
| 2018 |
| 2015 |
| 2014 |
| 2014 | 

For these types of queries there is a large IO savings to only having to fetch those interesting columns from disk. If you notice, because each column is homogenous (same data type), there are opportunities for aggressive compression. In some cases, where the columnar database is implemented as an inversion list (ie one copy of each unique value for each column with indications of what “rows” or records contain that value) there are additional IO savings from reducing the length of the list that has to be fetched and filtered for a given column. Examples of column based database are  HBase and Cassandra. Column oriented databases do not support "traditional" transactional operations (as they are somtimes inefficient to write to), but they are generally faste for analytics.

To summarize the pros and cons of both.

## Row oriented

*  It stores data table by row.
*  Data accessing happens row by row 
*  Storage size optimization limited due to reduced ability of data compression in row based systems.
*  Best suited for cases where the user cares about efficient update or retrieving entire rows.


## Column oriented

*  It stores data table by column.
*  Data accessing happens column by column
*  Column based systems provide better storage size optimization capabilities due to compression.
*  It is faster than row oriented database when users want to slice along columns
*  Best-sutied for data analytics tasks.
