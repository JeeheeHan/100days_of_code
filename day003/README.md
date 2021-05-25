# Day 3 learnings:
Good to knows: 
- Learned a neat list comprehension for checking out all method in a desired class:
- method_list = [func for func in dir(Foo) if callable(getattr(Foo, func)) and not func.startswith("__")]
- Tried out three methods to solve one problem today, test shows runtimes were very close:
```
Testing for decoder_enumerate

Ran100 times
.Testing for decoder_using_range

Ran100 times
.Testing for decoder_while

Ran100 times
.decoder_enumerate:1.0 ms
decoder_using_range:1.2 ms
decoder_while:1.0 ms
.
----------------------------------------------------------------------
Ran 4 tests in 0.023s

OK
```

All runtimes are big O(n)



