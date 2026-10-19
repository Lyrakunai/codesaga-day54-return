# Codesaga Day 54 — Practice
# Topic: Return Statement & Function Output Flow


# 1. Basic return
def add(a, b):
    return a + b


result = add(10, 20)
print(result)


# 2. Multiple return values
def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference


total, difference = calculate(30, 10)

print(total)
print(difference)


# 3. Return with conditional flow
def check_number(number):
    if number > 0:
        return "Positive"
    return "Zero or Negative"


print(check_number(15))
print(check_number(-5))


# 4. Return value used in an expression
def square(number):
    return number * number


answer = square(6) + 10
print(answer)


# 5. None behavior
def display_message():
    print("Hello")


value = display_message()
print(value)