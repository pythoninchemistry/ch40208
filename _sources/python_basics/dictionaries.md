# Dictionaries

## Introduction to Dictionaries

Python offers several collection types, including lists and tuples. The dictionary (`dict`) is another powerful collection type that consists of key-value pairs. This structure is analogous to a traditional dictionary, where words (keys) have corresponding definitions (values).

<p align="center">
     <img src="https://github.com/pythoninchemistry/ch40208/raw/main/CH40208/python_basics/images/python_dictionary_entry.png" width="35%" alt="A dictionary entry for the word Python."/>
 </p>

## Defining a Dictionary

Dictionaries are defined using curly braces `{}`, with key–value pairs separated by colons `:`.

```{code-cell} python
chlorine = {
    'chemical symbol': 'Cl', 
    'atomic number': 17, 
    'average mass number': 35.45, 
    'x-ray scattering length': 2.76+0.05j
}

print(chlorine)
```

## Accessing Dictionary Elements

### Accessing Keys

You can get all keys in a dictionary using the `keys()` method:

```{code-cell} python
print(chlorine.keys())
```

### Accessing Values

To access a single element, you can use the corresponding key as an index:

```{code-cell} python
chlorine['atomic number']
```

## Modifying Dictionaries

Dictionaries are mutable (you can change them after they have been created), allowing you to add or modify key–value pairs.

### Adding New Key–Value Pairs

```{code-cell} python
chlorine['number of isotopes'] = 2

print(chlorine)
```

### Removing Key-Value Pairs

You can remove key–value pairs from a dictionary using the `pop()` method:

```{code-cell} python
removed_value = chlorine.pop('number of isotopes')
print(f"Removed value: {removed_value}")
print(chlorine)  # The 'number of isotopes' key-value pair is now removed
```
