## Calculating 401(k) vs Roth

print("Please input salary:")
salary = int(input())

salary_growth = 1.04
investment_seed_percentage = 0.05
investment_growth = 1.07
years_working = 37

def calculate_tax_rate(salary):
	if salary > 38700 and salary <= 82500:
		tax_rate = 0.22
	elif salary > 82500 and salary <= 157500:
		tax_rate = 0.24
	elif salary > 157500 and salary <= 200000:
		tax_rate = 0.32
	elif salary > 200000 and salary <= 500000:
		tax_rate = 0.35
	else:
		tax_rate = 0.37
	return tax_rate

def calculate_tax_paid(salary):
	salary += 25000 # Social Security estimate
	if salary <= 38700:
		tax_rate = 952.5 + 0.12*(salary-9525)
	elif salary > 38700 and salary <= 82500:
		tax_rate = 4453.5 + 0.22*(salary-38700)
	elif salary > 82500 and salary <= 157500:
		tax_rate = 14089.5 + 0.24*(salary-82500)
	elif salary > 157500 and salary <= 200000:
		tax_rate = 32089.5 + 0.32*(salary-157500)
	elif salary > 200000 and salary <= 500000:
		tax_rate = 45689.5 + 0.35*(salary-200000)
	else:
		tax_rate = 150689.5 + 0.37*(salary-500000)
	return tax_rate - 2809.5 # taxes already paid on social security

def calculate_roth_total(salary, salary_growth, investment_seed_percentage, investment_growth):
	total_fund = 0

	for x in range(0,years_working):
		current_tax_rate = calculate_tax_rate(salary)
		this_year_contribution = salary*(investment_seed_percentage+x/1000)*(1-current_tax_rate)
		total_fund += this_year_contribution
		total_fund = total_fund*investment_growth
		salary = salary*salary_growth

	print("Roth Total: " + str(total_fund))

	yearly_payout = total_fund*0.05

	print("Roth Payout: " + str(yearly_payout))

def calculate_traditional_total(salary, salary_growth, investment_seed_percentage, investment_growth):
	total_fund = 0

	for x in range(0,years_working):
		this_year_contribution = salary*(investment_seed_percentage+x/1000)
		total_fund += this_year_contribution
		total_fund = total_fund*investment_growth
		salary = salary*salary_growth

	print("Traditional Total: " + str(total_fund))

	yearly_payout = total_fund*0.05

	print("Traditional Payout: " + str(yearly_payout - calculate_tax_paid(yearly_payout)))

calculate_traditional_total(salary, salary_growth, investment_seed_percentage, investment_growth)
calculate_roth_total(salary, salary_growth, investment_seed_percentage, investment_growth)