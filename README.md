![image](https://user-images.githubusercontent.com/2049665/29219793-b4dcb942-7e7e-11e7-8785-761b0e784e04.png)

Word Ninja
==========

Slice your munged together words!  Seriously, Take anything, `'imateapot'` for example, would become `['im', 'a', 'teapot']`.  Useful for humanizing stuff (like database tables when people don't like underscores).

This project is repackaging the excellent work from here: http://stackoverflow.com/a/11642687/2449774

Usage
-----
```
$ python
>>> import wordninja
>>> wordninja.split('derekanderson')
['derek', 'anderson']
>>> wordninja.split('imateapot')
['im', 'a', 'teapot']
>>> wordninja.split('heshotwhointhewhatnow')
['he', 'shot', 'who', 'in', 'the', 'what', 'now']
>>> wordninja.split('thequickbrownfoxjumpsoverthelazydog')
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

Performance
-----------
It's super fast!

```
>>> def f():
...   wordninja.split('imateapot')
... 
>>> timeit.timeit(f, number=10000)
0.40885152100236155
```

It can handle long strings:
```
>>> wordninja.split('wethepeopleoftheunitedstatesinordertoformamoreperfectunionestablishjusticeinsuredomestictranquilityprovideforthecommondefencepromotethegeneralwelfareandsecuretheblessingsoflibertytoourselvesandourposteritydoordainandestablishthisconstitutionfortheunitedstatesofamerica')
['we', 'the', 'people', 'of', 'the', 'united', 'states', 'in', 'order', 'to', 'form', 'a', 'more', 'perfect', 'union', 'establish', 'justice', 'in', 'sure', 'domestic', 'tranquility', 'provide', 'for', 'the', 'common', 'defence', 'promote', 'the', 'general', 'welfare', 'and', 'secure', 'the', 'blessings', 'of', 'liberty', 'to', 'ourselves', 'and', 'our', 'posterity', 'do', 'ordain', 'and', 'establish', 'this', 'constitution', 'for', 'the', 'united', 'states', 'of', 'america']
```
And scales well.  (This string takes ~7ms to compute.) 

How to Install
--------------

```
pip3 install wordninja
```

Custom Language Models
----------------------
#1 most requested feature!  If you want to do something other than english (or want to specify your own model of english), this is how you do it.

```
>>> lm = wordninja.LanguageModel('my_lang.txt.gz')
>>> lm = wordninja.LanguageModel('my_lang.txt.bz2')  # bzip2 alternative
>>> lm.split('derek')
['der','ek']
```

Language files must be gziped or bziped text files with one word per line in decreasing order of probability.

If you want to make your model the default, set:

```
wordninja.DEFAULT_LANGUAGE_MODEL = wordninja.LanguageModel('my_lang.txt.gz')
wordninja.DEFAULT_LANGUAGE_MODEL = wordninja.LanguageModel('my_lang.txt.bz2')
```
