
def property_tax():
	user_value = float(input("Enter the actual value: "))
	assessment_percent = float(.6)

	assessment_value = user_value * assessment_percent

	print("Assessed value: $" + "{:,.2f}".format(float(assessment_value),'.2f'))

	assessment_value = float(assessment_value)
	amount_taxed = assessment_value // 100
	total_tax = amount_taxed * .72
	total_tax = format(total_tax, '.2f')

	print("Property tax: $" + "{:,.2f}".format(float(total_tax),'.2f'))

def future_value():
	user_pv = float(input("Enter the present value of the account in dollars: "))
	user_monthly_int = float(input("Enter the monthly interest rate as a  percentage: "))
	user_months = int(input("Enter the number of months: "))

	converted_monthly_int = user_monthly_int / 100

	future_value = user_pv * (1 + converted_monthly_int)**user_months

	print("The information for your account is:")
	print("Present value: $" + "{:,.2f}".format(float(user_pv),'.2f'))
	print("Interest Rate: %" + "{:,.2f}".format(float(user_monthly_int),'.2f'))
	print("After " + str(user_months) + " months, the value of your account will be $" + "{:,.2f}".format(float(future_value),'.2f'))

def genz_search():

	with open("GirlNames.txt", "r") as girl_names:
		content_girls = girl_names.readlines()

	content_girls = [x.strip('\n') for x in content_girls]

	with open("BoyNames.txt", "r") as boy_names:
		content_boys = boy_names.readlines()

	content_boys = [x.strip('\n') for x in content_boys]

	user_boy = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
	user_girl = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

	if user_boy == "N" or user_boy == "n":
		print("You chose not to enter a boy's name.")
	else:
		if user_boy in content_boys:
			print(user_boy + " is one of the most popular boy's names.")
		elif user_boy not in content_boys:
			print(user_boy + " is not one of the most popular boy's names.")

	if user_girl == 'N' or user_girl == 'n':
		print("You chose not to enter a girl's name.")
	else:
		if user_girl in content_girls:
			print(user_girl + " is one of the most popular girl's names.")
		elif user_girl not in content_girls:
			print(user_girl + " is not one of the most popular girl's names.")


def prime_gen():

	user_number = int(input("Enter an integer greater than 1: "))

	number_list = []

	for i in range(2,user_number + 1):
		number_list.append(i)
	
	# print(number_list)

	for i in number_list:
		num = 0
		for j in range(2,i):
			if i % j == 0:
				num = 1
		if num == 0:
			print(str(i) + " is prime")
		if num == 1:
			print(str(i) + " is composite")


# The get_word_dict function returns a dictionary containing
# the words from line_list as keys, and their line numbers
# as values.
def get_word_dict(line_list):
	
	word_dict = {}

	for e in line_list:
		words = e.split(' ')
		for w in words:
			if w in word_dict:
				word_dict[w] += 1
			else:
				word_dict[w] = 1

	return(word_dict)

def write_index_file(word_dict):
	outputfile = open('index_j.txt', 'w')
	sorted_list = sorted(word_dict)
	for key in sorted_list:
		outputfile.write(key + " " + str(word_dict[key]))			
		outputfile.write('\n')
	outputfile.close()
	


def master():
	# Open the file.
	inputfile = open('tirole_nobel.txt', 'r')

	# Read the file's contents into a list.
	line_list = inputfile.readlines()

	# Close the file.
	inputfile.close()

	# Strip the newline from each list element.
	for i in range(len(line_list)):
		line_list[i] = line_list[i].rstrip('\n')

	# Get a dictionary holding the words and their line numbers.
	word_dict = get_word_dict(line_list)

	# Write the index file.
	write_index_file(word_dict)

def pow_recursive(x,number):
	if number == 0:
		return(1)
	else:
		return(x * pow_recursive(x,number-1))

x = float(input("Enter a number: "))
number = int(input("Enter a positive whole number between 1 and 100: "))
print(format(x,'.1f') + " raised to the power of " + str(number) + " is " "{:,.2f}".format(float(pow_recursive(x,number)),'.2f'))



def main():
	property_tax()
	future_value()
	genz_search()
	prime_gen()
	master()

if __name__ == '__main__':
	main()




