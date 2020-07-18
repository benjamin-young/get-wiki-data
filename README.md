# get-wiki-data
python code to get proper nouns such as people from a text, search wikipedia for articles on that proper noun and extract from that article 

# functions

## getSubjects(data)
data = any text you want to pick out proper nouns such as words from

retuns array of proper nouns.

### Example:

```python
>>> getSubjects("Today we discuss some of the work of Max Weber in preparation for an upcoming series.")
```

### Output:

```python
['Max Weber']
```

## getWikiPages(subject)
subject = wikipedia search term

returns title for wikipedia page.

### Example:

```python
>>> pages = []
>>> for subject in subjects:
	    new_page = getWikiPages(subject)
	    if new_page not in pages:
		    pages.append(new_page)
```

### Output:

```python
>>> pages
['Max Weber']
```

## getWikiData(page)
page = title of wikipedia page we want to get

returns some amount of the page.

### Example:

```python
>>> for page in pages:
      print('\n')
      print(getWikiData(page))
```

### Output:

```
Maximilian Karl Emil Weber (; German: [ˈveːbɐ]; 21 April 1864 – 14 June 1920) was a German sociologist, 
philosopher, jurist, and political economist, who is regarded today as one of the most important theorists 
on the development of modern Western society. His ideas would profoundly influence social theory and 
social research....
```



