# Alexander Hill | 1.24.18 | Dight 360
# This is for my project on nominalizations

import re

print('\n')
print('From the wiki article on the history of Python.\n')

mystr = """Features and philosophy[edit]
Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including by metaprogramming[41] and metaobjects (magic methods)).[42] Many other paradigms are supported via extensions, including design by contract[43][44] and logic programming.[45]

Python uses dynamic typing, and a combination of reference counting and a cycle-detecting garbage collector for memory management. It also features dynamic name resolution (late binding), which binds method and variable names during program execution.

Python's design offers some support for functional programming in the Lisp tradition. It has filter(), map(), and reduce() functions; list comprehensions, dictionaries, and sets; and generator expressions.[46] The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.[47]

The language's core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:[48]

Beautiful is better than ugly

Explicit is better than implicit

Simple is better than complex

Complex is better than complicated

Readability counts

Rather than having all of its functionality built into its core, Python was designed to be highly extensible. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.[30]

While offering choice in coding methodology, the Python philosophy rejects exuberant syntax (such as that of Perl) in favor of a simpler, less-cluttered grammar. As Alex Martelli put it: "To describe something as 'clever' is not considered a compliment in the Python culture."[49] Python's philosophy rejects the Perl "there is more than one way to do it" approach to language design in favor of "there should be one—and preferably only one—obvious way to do it".[48]

Python's developers strive to avoid premature optimization, and reject patches to non-critical parts of CPython that would offer marginal increases in speed at the cost of clarity.[50] When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

An important goal of Python's developers is keeping it fun to use. This is reflected in the language's name—a tribute to the British comedy group Monty Python[51]—and in occasionally playful approaches to tutorials and reference materials, such as examples that refer to spam and eggs (from a famous Monty Python sketch) instead of the standard foo and bar.[52][53]

A common neologism in the Python community is pythonic, which can have a wide range of meanings related to program style. To say that code is pythonic is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it conforms with Python's minimalist philosophy and emphasis on readability. In contrast, code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.

Users and admirers of Python, especially those considered knowledgeable or experienced, are often referred to as Pythonists, Pythonistas, and Pythoneers."""

myre1 = r'\b\w{2,}ing\b'
myre2 = r'\b\w{2,}or\b'
myre3 = r'\b\w{2,}ee\b'
myre4 = r'\b\w{2,}tion\b'
myre5 = r'\b\w{2,}sion\b'
myre6 = r'\b\w{2,}ment\b'
myre7 = r'\b\w{2,}ence\b'
myre8 = r'\b\w{2,}ance\b'
myre9 = r'\b\w{2,}er\b'
myre10 = r'\b\w{2,}al\b'
myre11 = r'\b\w{2,}ure\b'

result1 = re.findall(myre1, mystr)
result2 = re.findall(myre2, mystr)
result3 = re.findall(myre3, mystr)
result4 = re.findall(myre4, mystr)
result5 = re.findall(myre5, mystr)
result6 = re.findall(myre6, mystr)
result7 = re.findall(myre7, mystr)
result8 = re.findall(myre8, mystr)
result9 = re.findall(myre9, mystr)
result10 = re.findall(myre10, mystr)
result11 = re.findall(myre11, mystr)

count1 = len(result1)
count2 = len(result2)
count3 = len(result3)
count4 = len(result4)
count5 = len(result5)
count6 = len(result6)
count7 = len(result7)
count8 = len(result8)
count9 = len(result9)
count10 = len(result10)
count11 = len(result11)

count12 = count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11

print('The number of nominalized verbs with "ing" is ', count1, '.\n')
print(result1, '\n')

print('The number of nominalized verbs with "or" is ', count2, '.\n')
print(result2, '\n')

print('The number of nominalized verbs with "ee" is ', count3, '.\n')
print(result3, '\n')

print('The number of nominalized verbs with suffixes (tion, sion, ent, ence, ance, er) is ', count12, '.\n')
print(result4, result5, result6, result7, result8, result9, result10, result11, '\n')

print('There are real issues when it comes to finding nominalized verbs with Regular Expressions. The gerrunds are more frequently correct than other suffix nominalizations but there are still issues where they pull out words that have these suffixes but which are not nominalized verbs. Regular Expressions probably isn\'t the best way to go about looking for nominalized verbs.')

