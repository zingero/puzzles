import random


def getRandomBalls():
	a = round(random.random())
	b = (a + 1) % 2
	return a, b


red_a, red_b = getRandomBalls()
green_a, green_b = getRandomBalls()
blue_a, blue_b = getRandomBalls()


def checkAnswer(expected_red_a, expected_green_a, expected_blue_a):
	assert red_a == expected_red_a
	assert green_a == expected_green_a
	assert blue_a == expected_blue_a


try:
	if green_a + blue_a == green_b + red_b:
		if blue_a < red_b:
			checkAnswer(0, 1, 0)
		else:
			checkAnswer(1, 0, 1)
	elif green_a + blue_a < green_b + red_b:
		if blue_b == red_b:
			checkAnswer(0, 0, 0)
		elif blue_b < red_b:
			checkAnswer(0, 0, 1)
		else:
			checkAnswer(1, 0, 0)
	else:
		if blue_a == red_a:
			checkAnswer(1, 1, 1)
		elif blue_a < red_a:
			checkAnswer(1, 1, 0)
		else:
			checkAnswer(0, 1, 1)

except Exception as e:
	print("Failed. exception: %s" % e)
	print("Actual Values:")
	print("Red:", red_a, red_b)
	print("Green:", green_a, green_b)
	print("Blue:", blue_a, blue_b)
