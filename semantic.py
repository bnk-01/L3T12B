import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.

print('''
QUESTION 1
from what I can see from the output of the program, Money and cat 
are both animals so they have high similarities. same with apple and banana because
because they both fruits. 
WHILE
Cats does not have any high similarity with any fruits because they are not naturally 
associated with any fruits. never heard a cat eat banana or apples. unlike monkey that has 
high similarity with banana because everyone knows monkey eats banana
''')

# Run the example file with the simpler language model ‘en_core_web_sm’ and write a note on
# what you notice is different from the model 'en_core_web_md'.

print(''' QUESTION 2
when I run the program with a simpler model ‘en_core_web_sm’ the similarity output
came out lower than 'en_core_web_md' this means that the accuracy rate is low because the model
may not be able to recognize more complex patterns and entities in text. The simpler model ‘en_core_web_sm’
should be used on simpler task or with smaller datasets. 
''')