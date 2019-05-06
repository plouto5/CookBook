# Python 2

	first = "eric"

	last = "bower"

	print("hello, %s %s" % (first, last))

# Python >= 2.6

	first = "eric"

	last = "bower"

	print("hello, {} {}".format(first, last))

# Python >= 3.6

	first = "eric"

	last = "bower"

	name = "ERIC BOWER"

	print(f"hello, {first} {last})

	def to_lower(input):

		return input.lower()

	print(f"{to_lower(name)} is now lower case")
