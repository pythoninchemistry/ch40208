# Collections

Up until now we have dealt with individual pieces of data, such **integer** or **floating point** data types to store numerical data, or **strings** to represent textual data.

Often we want to work with **collections** of data, such as a time-series of concentrations from an experiment, or a set of yields obtained from different experimental protocols, or the list of students enrolled in **CH40208 Topics in Computational Chemistry**.

Python includes a number of built-in **container** datatypes, that can be used to store multiple pieces of data in a structured way. 

Three commonly used data structures in Python are:
- **lists** &mdash; which are used to store an **ordered sequence** of data that is **changeable**.
- **tuples** &mdash; which are used to store an **ordered sequence** of data that is **unchangeable**.
- **dictionaries** &mdash; which are used to store **unordered** data as **key–value pairs** (the data in dictionaries can be changed).

**Lists** and **tuples** can be used in lots of the same places, but they differ in one very important way: 
- **lists** are **mutable**&mdash;the data stored in them can be altered, new data can be added to the list, and existing data can be removed from the list.
- **tuples** are **immutable**&mdash;once a tuple has been created, the data stored cannot be changed, new data cannot be added, and existing data cannot be removed.

