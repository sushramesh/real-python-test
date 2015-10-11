# -*- coding: utf-8 -*-

from random import choice

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
vowels = "aeiou"

# Poem structure:
# “{A/An} {adjective1} {noun1}
#
# {A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {preposition2} a {adjective3} {noun3}”
#
# Excerpt From: Fletcher Heisler. “Real Python Part 1: Introduction to Python.” iBooks.

def get_3_random(words):
	n1 = choice(words)
	n2 = choice(words)
	n3 = choice(words)
	while n1 == n2 and n1 == n3 and n2 == n3:
		n2 = choice(words)
		n3 = choice(words)
	x = [n1, n2, n3]
	return x

def make_poem():
	noun_3 = get_3_random(nouns)
	verb_3 = get_3_random(verbs)
	adj_3 = get_3_random(adjectives)
	prepo_3 = get_3_random(prepositions)
	adverb_3 = get_3_random(adverbs)

	if vowels.find(adj_3[0][0]) != -1:
		print "An {adjective1} {noun1}".format(adjective1=adj_3[0], noun1 = noun_3[0])
	else:
		print "A {adjective1} {noun1}".format(adjective1=adj_3[0], noun1 = noun_3[0])

	if vowels.find(adj_3[0][0]) != -1:
		print "An {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}"\
		.format(adjective1=adj_3[0], noun1=noun_3[0], verb1=verb_3[0], preposition1=prepo_3[0], \
		adjective2=adj_3[1], noun2=noun_3[1])
	else:
		print "A {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}"\
		.format(adjective1=adj_3[0], noun1=noun_3[0], verb1=verb_3[0], preposition1=prepo_3[0], \
		adjective2=adj_3[1], noun2=noun_3[1])

	print "{adverb1}, the {noun1} {verb2}".format(adverb1=adverb_3[0], noun1=noun_3[0], verb2=verb_3[1])
	print "the {noun2} {verb3} {preposition2} a {adjective3} {noun3}".format(noun2=noun_3[1], verb3=verb_3[2],\
	preposition2=prepo_3[1], adjective3=adj_3[2], noun3=noun_3[2])
	print "\n"

for i in range(0,4):
	make_poem()
