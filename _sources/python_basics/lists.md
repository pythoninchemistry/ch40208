# lists

A **list** is an **ordered** collection of values. The values that make up a **list** are called **elements** or **items**, so we might talk of a list that contains 4 **items**, or the 2nd **element** in a list.

## creating lists

A list in Python is written as a sequence of values separated by commas and enclosed by square brackets.

```python
[1, 1, 2, 3, 5, 8, 13]
```

We can assign a list to a variable the same way as with single-value datatypes:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FYNjawzo-AX.png?alt=media&token=a7a16f67-82fe-49dd-8aa9-515038b5872f)

A list can contain any datatype:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FCjXg8n0g0E.png?alt=media&token=3bccbe54-a294-40b5-b623-e1cb1b2d8c0c)

even mixtures of different datatypes:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F7Jg0XNUXHC.png?alt=media&token=dbaddf86-5019-48c2-9949-4dcd393e1faf)

or other lists:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FWGGZytzWCc.png?alt=media&token=e63b03f6-d52c-4ce2-8649-b12039f2911a)

This last example would be described as a **nested** list (a list inside another list).

## list indexing

Individual elements of a list can be referred to by using **list indexing**. For example, the first item in our `nobel_gases` list can be accessed using

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FbgRS8a7p44.png?alt=media&token=96acb202-0dcb-43e1-9bee-a799e6c40a0b)

the second item using 

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FuFyzOn7awF.png?alt=media&token=db5b53a8-aeac-40b4-9eb0-5a0547781024)

and the third item using

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FLZU-KVAGo8.png?alt=media&token=6e0bbacf-3f9c-498a-93c7-5d19f7569444)

Note that to reference the 1st element we use `[0]` after the list variable name, to reference the 2nd element we use `[1]`, and to reference the 3rd element we use `[2]`. This convention is because the list index describes the number of entries **from the start of the list**. i.e. the first entry is **zero** entries from the start.

Trying to access a list element that does not exist raises an `IndexError`:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F1HKLznOXKz.png?alt=media&token=c6340cab-a1d5-45a1-81b7-5b0fdf0e74b2)

We can also refer to individual elements counting backwards from the end of the list, using **negative indexing**:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FJlfuwWjLnF.png?alt=media&token=7fcc64b5-1808-445c-8c17-f5a51d681a62)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FC1fDHz7_jv.png?alt=media&token=dcd553f8-0887-410b-8345-4e9ff7a42c94)

Using positive and negative indexing to refer to individual elements of the `nobel_gases` list.

## Modifying lists

An important feature of **lists** is that they are **mutable**—values in the list can be changed; new elements can be added; existing elements can be deleted.

You might have noticed that the first of our noble gases is `"helium"`, which is missing a capital letter. We can fix that by assigning a new value to `nobel_gases[0]`

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FDyKV534WIf.png?alt=media&token=c6c69522-aec5-458d-ab31-6a30e50fac9b)

### adding elements to lists

Lists have a number of special functions (called **methods**) that we can use to add elements to a pre-existing list. 

A **method** is somewhat similar to a **function**, except it is associated with a particular object. Using a method lets us implicitly refer to the associated object. 

Calling a method of a list implicitly refers to that list. For example, to append another nobel gas string to our `nobel_gases` list we can use the `append()` method:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fct3aUoRie-.png?alt=media&token=adfae578-520f-4f8e-b51b-2eb593fff5c6)

This is equivalent to a function that takes **two** arguments: the list we want to append to, and the object to be appended. For example, we might imagine an `append_to_list()` function that works as follows:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FD9zd9P_ads.png?alt=media&token=d6d502fd-73e6-4aa1-a49f-ea7f6a26f1a7)

Because the `append()` method belongs to the `nobel_gases` list, when we use `nobel_gases.append()` we don't need to specify the list that we are appending to.

Another list method that can be used to add elements is `insert()`, which inserts an object at a given index:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FbRG6x8hhra.png?alt=media&token=c922fbe5-f631-4f5b-b390-0c66a371af21)

The `insert()` methods takes **two** arguments: the index where the insertion will take place (in this case `2`), and the object to insert (in this case `"Argon"`).

You can also **extend** a list with another list, by using the `extend()` method:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FDm7Ti_3X9Q.png?alt=media&token=5b0a576e-a075-4979-9a29-de41e22ddaa3)

Or you can **concatenate** two lists using the `+` operator (this is similar to "adding" strings):

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fc9xJM5feJ0.png?alt=media&token=1c23a887-ded7-4c17-9867-9082b058d25c)

### deleting elements from lists

Lists also have methods for deleting or removing elements. These include `remove()` which removes the first matching object in a list.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Ftoh96JMSy5.png?alt=media&token=7cdcb00e-5358-4b6f-9217-8bbaf6b9e0b4)

## list slices

By referring to a single list index, we can access a single item of a list. Python also allows us to use **slice notation** to access a **range** of items from a list, e.g.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F9MzsO_8mId.png?alt=media&token=35839115-2b79-4dfb-9993-75a90b11aac9)

This gives us just those elements of a list starting from `nobel_gases[1]` up to **but not including** `nobel_gases[4]`.

This behaviour, where the first index is included in the slice, but the last index is not included might seem strange at first (you will get used to this with practice and experience). The reasoning behind this behaviour is that a slice `nobel_gases[1:4]` should contain 4-1=3 elements, and should start from the same element as (in this case) `nobel_gases[1]`.

Either the first or last index can be left out, in which case you get a slice starting from the first element, or finishing with the last element, respectively.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2Fuqkdi7NGOW.png?alt=media&token=0309e0c2-92f5-445d-b0a8-752f51f1d39f)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F3ZLQeV43jI.png?alt=media&token=b6af6811-9bf3-4c1e-b939-04eae39bdf53)

List slices can also be given a third integer, which describes a **step** size. This is implicitly equal to `1` when it is not specified

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FOQy5wgoWxy.png?alt=media&token=8d34cfb2-618d-4406-a598-aaac39facf33)

In this example. we start from the first element, and go up to the last element, in steps of 2, giving elements 0, 2, and 4.

In addition to the `remove()` method above, list slicing gives us another way to "delete" elements from a list:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FGySpV0MpNO.png?alt=media&token=bbb5312f-4b1e-4ae2-acc3-4f7d16a05279)

In the second line here we select elements 1 and 2 from the original `nobel_gases` list, using **slice notation**, which gives us `['Neon', 'Argon']`. We then *assign* this value to the variable name `nobel_gases`, which overwrites the original list.

## working with nested lists

We saw above that a list can contain one or more other lists, giving a **nested list**. How then do these work with indexing?

Consider the following nested list:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FcMHgdcmBCd.png?alt=media&token=531606ff-5083-448e-8d78-b6527250d8ee)

The list `letters` has **five** elements, these are:

- `'a'`
- `'b'`
- the list `['c', 'd']`
- `'e'`
- `'f'`

We can confirm this using the `len()` function. If we pass `len()` a list, it returns the number of elements in that list (i.e. the **length**).

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F3G2FN67Kje.png?alt=media&token=1bbaa384-5a2c-4d1c-9b76-aa563ff8ed98)

The **third** element is the sublist `['c', 'd']`, which we can access using `letters[2]`

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FUt-_tQC0n-.png?alt=media&token=e1634235-a810-4f0d-b4e9-14c8cfd3bb4b)

`letters[2]` is a list

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2FWFQxwNWz0l.png?alt=media&token=4d1370c8-e65e-45db-8828-cefbfd47fa92)

and we can interact with this in the same way as any other list, e.g.

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F5FSGGtf3dG.png?alt=media&token=3f0e98ca-2ddc-4410-998f-6e5b145a336f)

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fbjmorgan%2F9Ue2l6F3Oh.png?alt=media&token=53dd497f-e9fc-4b7d-855c-3724902ac879)

