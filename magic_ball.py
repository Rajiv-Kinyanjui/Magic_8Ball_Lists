import random

print("Ask a question")
question = input()

answers = ["It is certain.", "As I see it yes.", "Reply hazy, try again.", "Don`t count on it.", "It is decidedly so.", "Most likely.", "Ask again later.", "My reply is no.", "Without a doubt.", "Outlook good.", "Better not tell you now.", "My sources say no.", "Yes definitely.", "yes,", "Cannot predict now", "Outlook not so good.", "You may rely on it.", "Signs point to yes.", "Concentrate and ask again.", "Very doubtful."]

print_answer = random.choice(answers)
print(print_answer)