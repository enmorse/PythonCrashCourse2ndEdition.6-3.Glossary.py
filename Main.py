# A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let's call it
# a glossary.
# Think of five programming words that you have
# learned about in the previous chapters. Use these
# words as the keys in your glossary, and store their
# meanings as values.
# Print each word and its meaning as neatly formatted
# output. You might print the word followed by a colon
# and then its meaning, or print the word on one line
# and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line
# between each word-meaning pair in your output.

glossary = {
    "Class": "Python is a language that supports the "
             "\n\tObject Oriented Programming paradigm. "
             "\n\tLike other OOP languages, Python has "
             "\n\tclasses which are defined wireframes of "
             "\n\tobjects.",
    "Dictionaries": "Dictionaries are Python's built-in"
                    "\n\tassociative data type. A dictionary is"
                    "\n\tmade of key-value pairs where each "
                    "\n\tkey corresponds to a value.",
    "Functions": "Python functions can be used to"
                 "\n\tabstract pieces of code to use elsewhere.",
    "Function Objects": "Python functions are first-class"
                        "\n\tobjects, which means that they can "
                        "\n\tbe stored in variables and lists and "
                        "\n\tcan even be returned by other "
                        "\n\tfunctions.",
    "len()": "Using len(some_object) returns the number"
             "\n\tof top-level items contained in the object"
             "\n\tqueried.",
}

for key, value in glossary.items():
    print(f"\nKey: {key}")
    print(f"\tValue: {value}")
