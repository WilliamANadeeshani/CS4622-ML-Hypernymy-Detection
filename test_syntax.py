import spacy
from spacy.en import English
from nltk import Tree
from collections import defaultdict


nlp = English()

doc = nlp(u'Is it safe for female traveller to go alone to Cape Town?')


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]

satellites = defaultdict(list)
# [satellites[(x, y)].extend([sat_path for path in paths[(x, y)] for sat_path in get_satellite_links(path)
#                             if sat_path is not None]) for (x, y) in paths.keys()]
token = doc[5]
print(token)
print token.idx
print(token.tag_ )
print(token.dep_)

