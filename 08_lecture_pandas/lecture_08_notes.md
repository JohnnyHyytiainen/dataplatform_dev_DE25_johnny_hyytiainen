# Lecture 08 notes
- Todays lecture focuses on continuation from lecture 07 and PANDAS


## lecture 07s script will be done on thursday when being in class since we had group workshop
- Modules:
  - Pandas(theory)
  - Utility methods
  - Cleaning/transforming data
  - Flagging with columns

- `uv add pandas` <- If not already installed. 


## Pandas, basics ( https://www.w3schools.com/python/pandas/default.asp )
- All slides and information in this lecture is from the official docs, mostly.
- What is Pandas?
    - Data Frames.
    - Key frame values(think key/value pairs) called Data Frames, `df`
    - Consists of rows, columns and index.

- Each column in a `DataFrame` is a named a `Series`. This is because it should not argue with any other dependency, it minimizes the users possibility to make mistakes. 
  - `Series refers to a column while DataFrames refers to a Table`

- A dataframe is a 2D data structure that can store data of different types. (chars, ints, floats, catagorical data etc)
- Its similar to a spreadsheet, a SQL table or the data.frame in `R`
  - The table has 3 columns, each of them with a column label. Ex, Name, Age and Sex
  - The column `name` is text, the column `age` is int, and the column `sex` is their male or female(could be seen as a bool perhaps(?))

- To manually sytore the data in a table you create a `DataFrame`. When using a Python dictionary of lists the dict keys will be use as columns headers and the values in will be seen as the list(?)