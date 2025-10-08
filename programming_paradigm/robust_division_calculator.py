def safe_divide(numerator, denominator):
	try:
		num = float(numerator)
		denom = float(denominator)
		try:
			result = num / denom
			return result
		except ZeroDivisionError:
			return "Error: Cannot divide by zero."
	except ValueError:
		return "Error: Both inputs must be numeric."

