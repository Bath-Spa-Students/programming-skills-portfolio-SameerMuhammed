# Original glossary dictionary
programming_glossary = {
    'variable': 'A named storage location that holds data.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.',
    'list': 'An ordered, mutable collection of elements.',
    'dictionary': 'An unordered, mutable collection of key-value pairs.'
}

# Print each word and its meaning with a newline between pairs
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")

# Adding five more Python terms to the glossary
programming_glossary['tuple'] = 'An ordered, immutable collection of elements.'
programming_glossary['module'] = 'A file containing Python definitions and statements.'
programming_glossary['exception'] = 'An event that occurs during the execution of a program, causing the program to terminate.'
programming_glossary['boolean'] = 'A data type that can have only two values: True or False.'
programming_glossary['method'] = 'A function associated with an object, acting on it or returning a value.'

# Print the updated glossary
print("\nUpdated Glossary:")
for word, meaning in programming_glossary.items():
    print(f"{word}:\n{meaning}\n")
  
