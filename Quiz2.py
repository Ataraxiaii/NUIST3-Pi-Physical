# Author: Xuanru Guo
# Date: 2/4/2025

import RPi.GPIO as GPIO
import time

# set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
GREEN_LED = 17
RED_LED = 18

# Set up the GPIO pins as outputs
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Turn off the LEDs initially
GPIO.output(GREEN_LED, GPIO.LOW)
GPIO.output(RED_LED, GPIO.LOW)

# Quiz questions and answers
questions = [
	{
		"question": "Which of the following is NOT a python data type?",
		"options": ["A. int", "B. float", "C. rational", "D. string", "E. bool"],
		"answer": "C"
	},
	{ 
                "question": "Which of the following is NOT a built-in operation in Python?",
                "options": ["A. +", "B. %", "C. abs()", "D. sqrt()"],
                "answer": "D"
        },
	{ 
                "question": "In a mixed-type expression involving ints and floats, Python will convert:",
                "options": ["A. floats to ints", "B. ints to strings", "C. floats and ints to strings", "D. ints to floats"],
                "answer": "D"
        },
	{ 
                "question": "The best structure for implementing a multi-way decision in Python is:",
                "options": ["A. if", "B. if-else", "C. if-elif-else", "D. try"],
                "answer": "C"
        },
	{ 
                "question": "What statement can be executed in the body of a loop to cause it to terminate?",
                "options": ["A. if", "B. exit", "C. continue", "D. break"],
                "answer": "D"
        }
]

def flash_led(led_pin, duration = 1):
	GPIO.output(led_pin, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(led_pin, GPIO.LOW)

# Run the quiz
def run_quiz():
	print("Welcome to the Interactive Quiz!")
	print("Answer each question by entering the letterof your choice.\n")
	score = 0
	for i,q in enumerate(questions, 1):
		print(f"Question {i}: {q['question']}")
		for option in q['options']:
			print(option)
		while True:
			user_answer = input("Your answer is: ").upper()
			if user_answer in ['A', 'B', 'C', 'D', 'E']:
				break
			print("Invalid answer.")
		# Judge the answer
		if user_answer == q['answer']:
			print("Correct!\n")
			flash_led(GREEN_LED)
			score += 1
		else:
			print(f"Incorrect! The answer is {q['answer']}.\n")
			flash_led(RED_LED)

	# Finish the quiz
	print(f"Quiz Complete! Your final score is: {score}/{len(questions)}")

run_quiz()
