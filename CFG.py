from collections import defaultdict
import random

def weighted_choice(weights):
	# Trying to select the tuple with the higher weight in order to get various permutations of the different options available in each production rule

	picker = random.random() * sum(weights)

	for i, w in enumerate(weights):
		picker -= w
		if picker < 0:
			return i


class CFG(object):

	def __init__(self):
		self.prod = defaultdict(list)

	def add_prod(self, lhs, rhs):

		prod_rules = rhs.split('|')

		for prod in prod_rules:
			self.prod[lhs].append(tuple(prod.split()))

	def gen_random_sentence(self, symbol, cfactor=0.25, pcount = defaultdict(int)):

		sentence = ''
		weights = []

		for prod in self.prod[symbol]:
			if prod in pcount:

				#Tuples/Prod-Rules are less likely to be selected if they've been selected previously
				weights.append(cfactor ** (pcount[prod]))
			else:

				#Weights initialized to 1.0 in the first run of the function
				weights.append(1.0)

		# This will likely be a production rule with a higher weight
		rand_prod = self.prod[symbol][weighted_choice(weights)]

		pcount[rand_prod] += 1

		# Iterating over a string
		for sym in rand_prod:

			if sym in self.prod:
				sentence += self.gen_random_sentence(sym, cfactor = cfactor, pcount = pcount)
			else:
				sentence += sym + ' '

		pcount[rand_prod] -= 1

		return sentence

