from random import randint

# Selects organisms based on their phenotype.
def natural_selection(organisms):
	new_orgs = []
	for org in organisms:
		if org['phenotype'] == "recessive":
			if randint(0, 100) < 10:
				new_orgs.append(org)
		elif org['phenotype'] == "dominant":
			if randint(0, 100) < 90:
				new_orgs.append(org)
	return new_orgs

# Breeds parents - selects random alleles and creates new organism.	
def new_genotype(parents):
	genotype = []
	for parent in parents:
			genotype.append(parent["genotype"][randint(0, 1)])
	return genotype

# Creates phenotype based on a genotype.	
def new_phenotype(genotype):
	allele = genotype[0]
	allele = allele + allele
	dom = allele.upper()
	domrec = allele.title()
	rec = allele.lower()
	alleles = ''.join(genotype)
	if alleles == dom or alleles == domrec:
		return "dominant"
	elif alleles == rec:
		return "recessive"
	else:
		return "dominant"

# Creates a new organism with phenotype and genotype.		
def new_offspring(parents):
	offspring = {}
	offspring['genotype'] = new_genotype(parents)
	offspring['phenotype'] = new_phenotype(offspring['genotype'])
	return offspring

# Selects organisms, then breeds the ones that remain.
def generation(organisms):
	new_gen = natural_selection(organisms)
	next_gen = []
	while len(new_gen) > 1:
		org_1 = new_gen.pop(randint(0, len(new_gen)-1))
		org_2 = new_gen.pop(randint(0, len(new_gen)-1))
		for x in range(0, randint(0,4)):
			offspring = {}
			offspring['genotype'] = new_genotype([org_1, org_2])
			offspring['phenotype'] = new_phenotype(offspring['genotype'])
			next_gen.append(offspring)
	return next_gen

# Checks to see if any recessive alleles are still in the population.	
def check_list(org_list, allele):
	for org in org_list:
		if org['genotype'][0] == allele or org['genotype'][1] == allele:
			return True
			break
	return False

# Runs the generation function until no recessive alleles remain.	
def evolution(organisms):
	gen = 0
	new_orgs = organisms
	while check_list(new_orgs, 's'):
		gen += 1
		new_orgs = generation(new_orgs)
		dom = 0
		rec= 0
		domrec= 0
		for org in new_orgs:
			if org['genotype'] == ['S', 'S']:
				dom += 1
			elif org['genotype'] == ['s', 's']:
				rec += 1
			else:
				domrec += 1
		print gen, dom, domrec, rec

# Creates an array with organisms to be inputted into the evolution function.
def create_organisms(org_list, genotype):
	population = int(input('Number of organisms with genotype %s:' % (genotype)))
	for x in range(0, population):
		org = {}
		org['genotype'] = genotype
		org['phenotype'] = new_phenotype(genotype)
		org_list.append(org)
	return org_list			
			
# Runs code, asking for each population and then running it with evolution.
frogs = []
create_organisms(frogs, ['S', 'S'])
create_organisms(frogs, ['S', 's'])
create_organisms(frogs, ['s', 's'])
	
evolution(frogs)