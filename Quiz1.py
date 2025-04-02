# NUIST Quiz Game in Python
# Author: Xuanru Guo
# Date: 2025/4/2
# Student Number: 20109677
def quiz():
	print("Welcome to the Animal Quiz!")
	print("Answer the following questions:")
	# Qustions and Answers
	questions = [
		"1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
		"2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird",
		"3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin"
	]
	answers = ["blue whale","hummingbird","bat"]
	score = 0
	
	# Ask questions
	for i in range(len(questions)):
		user_answer = input(questions[i]).strip().lower()
		# Judge the answer
		if user_answer == answers[i]:
			print("Correct!")
			score += 1
		else:
			print("Incorrect!")
	
	# Provide final score
	print("\nQuiz completed!")
	print(f"You got {score}/{len(questions)} questions correct.")

# Run the quiz function
quiz()

