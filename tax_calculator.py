# Tax Calculator created by Jon Erra

def single():
	std = 6350
	exemption = dependants * 4050 + 4050
	
	tax_income = income - std - exemption

	if tax_income <= 9325:
		tax_liability = income * .10
	elif tax_income in range(9326, 37950):
		tax_liability = ((income - 9325) * .15 ) + 932.50
	elif tax_income in range(37951, 91900):
		tax_liability = ((income - 37950) * .25 ) + 5226.25
	elif tax_income in range(91901, 191650):
		tax_liability = ((income - 91900) * .28 ) + 18713.75
	elif tax_income in range(191651, 416700):
		tax_liability = ((income - 191650) * .33 ) + 46643.75
	elif tax_income in range(416701, 418400):
		tax_liability = ((income - 416700) * .35 ) + 120910.25
	else:
		tax_liability = ((income - 418400) * .396 ) + 121505.25
	
	print "You owe $%f in taxes" % (tax_liability)
	print "You income after tax is: $%f" % (income - tax_liability)
	
def mfj():
	std = 12700
	exemption = dependants * 4050 + 8100
	
	tax_income = income - std - exemption
	
	if tax_income <= 18650:
		tax_liability = income * .10
	elif tax_income in range(18651, 75900):
		tax_liability = ((income - 18650) * .15 ) + 1865
	elif tax_income in range(75901, 153100):
		tax_liability = ((income - 75900) * .25 ) + 10452.50
	elif tax_income in range(153101, 233350):
		tax_liability = ((income - 153100) * .28 ) + 29752.50
	elif tax_income in range(233351, 416700):
		tax_liability = ((income - 233350) * .33 ) + 52222.50
	elif tax_income in range(416701, 470700):
		tax_liability = ((income - 416700) * .35 ) + 112728
	else:
		tax_liability = ((income - 470700) * .396 ) + 131628
	
	print "You owe %f in taxes" % (tax_liability)
	print "You income after tax is: $%f" % (income - tax_liability)
	
def mfs():
	std = 6350
	exemption = dependants * 4050 + 4050

	tax_income = income - std - exemption

	if tax_income <= 9325:
		tax_liability = income * .10
	elif tax_income in range(9326, 37950):
		tax_liability = ((income - 9325) * .15 ) + 932.50
	elif tax_income in range(37951, 76550):
		tax_liability = ((income - 37950) * .25 ) + 5226.25
	elif tax_income in range(76551, 116675):
		tax_liability = ((income - 76550) * .28 ) + 14876.25
	elif tax_income in range(116676, 208350):
		tax_liability = ((income - 116675) * .33 ) + 26111.25
	elif tax_income in range(208351, 235350):
		tax_liability = ((income - 208350) * .35 ) + 56364
	else:
		tax_liability = ((income - 235350) * .396 ) + 65814
	
	print "You owe %f in taxes" % (tax_liability)
	print "You income after tax is: $%f" % (income - tax_liability)
	
def hoh():
	std = 9350
	exemption = dependants * 4050 + 4050

	tax_income = income - std - exemption

	if tax_income <= 13350:
		tax_liability = income * .10
	elif tax_income in range(13351, 50800):
		tax_liability = ((income - 13350) * .15 ) + 1335
	elif tax_income in range(50801, 131200):
		tax_liability = ((income - 50800) * .25 ) + 6952.50
	elif tax_income in range(131201, 212500):
		tax_liability = ((income - 131200) * .28 ) + 27052.50
	elif tax_income in range(212501, 416700):
		tax_liability = ((income - 212500) * .33 ) + 49816.50
	elif tax_income in range(416701, 444550):
		tax_liability = ((income - 416700) * .35 ) + 117202.50
	else:
		tax_liability = ((income - 444550) * .396 ) + 126950
	
	print "You owe %f in taxes" % (tax_liability)
	print "You income after tax is: $%f" % (income - tax_liability)
	

status	= raw_input("What is your current filing status? ").lower()
income = int(raw_input("What is your yearly income? "))
dependants = int(raw_input("How many dependents do you have? "))


if status in ["single", "s"]:
	single()
elif status in ["married filing jointly", "qualifying widow", "widow", "mfj"]:
	mfj()
elif status in ["married filing sepearatly", "mfs"]:
	mfs()
elif status in ["hoh", "head of household"]:
	hoh()
else:
	print "Sorry, I didn't get that. Please try again."