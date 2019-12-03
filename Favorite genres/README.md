# Find Favorite genres by user
This is a small program made in Python, for a given list of user (dictionnary), to find the favorite genres for each of them.

# Example

input : 
	
```python
genre={
    'Drama':['book1','book2','book3'],
    'history':['book4','book5','book6'],
    'action':['book7','book8']
}

users={
    'jhon':['book1','book2','book7'],
    'amine':['book4','book5','book7','book8','book3']
}
```

Output:  

```console
{
'jhon':['Drama'],
'amine':['history','action']
}
```