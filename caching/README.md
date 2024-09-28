# Caching Project

## Background Context

In this project, you will learn about different caching algorithms and their applications. Caching is an important aspect of software systems that helps in improving performance and efficiency by storing frequently accessed data. This project focuses on implementing and understanding various cache replacement policies like FIFO, LIFO, LRU, MRU, and LFU.

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without referring to external resources:

### General:

- What a caching system is
- What FIFO (First In, First Out) means
- What LIFO (Last In, First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- What the purpose of a caching system is
- What limits a caching system has

## Resources

For more context and information on these topics, you can review the following resources:

- [Cache replacement policies - FIFO](https://example.com)
- [Cache replacement policies - LIFO](https://example.com)
- [Cache replacement policies - LRU](https://example.com)
- [Cache replacement policies - MRU](https://example.com)
- [Cache replacement policies - LFU](https://example.com)

## Requirements

### Python Scripts:

- All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.9).
- All your files should end with a new line.
- The first line of all your Python scripts should be:
  `#!/usr/bin/env python3`
- You must include a `README.md` file at the root of the project folder.
- Your code should conform to **pycodestyle** (version 2.5) guidelines.
- All your files must be executable.
- The length of your files will be tested using `wc`.

### Documentation:

- All your modules, classes, and functions must have appropriate documentation:
  - For modules: `python3 -c 'print(__import__("my_module").__doc__)'`
  - For classes: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - For functions: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
    and
    `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- The documentation should consist of meaningful sentences explaining the purpose of the module, class, or function. Simple words or vague explanations will not be accepted.

## BaseCaching Class

All your caching classes must inherit from the `BaseCaching` class provided in the `base_caching.py` file. Here’s the basic structure of the class:

```python
#!/usr/bin/python3
"""
BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")
```
