import random
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

name = "Joe"
question = ""
answer = ""

question = input("Ask a question: ")

if not question:
    print("Please ask a question.")
else:
    try:
        random_number = random.randint(1, 9)
        assert 1 <= random_number <= 9, "Random number out of range: {}".format(random_number)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
        print("An error occurred. Please try again.")
    else:
        if random_number == 1:
            answer = "Yes - definitely"
        elif random_number == 2:
            answer = "It is decidedly so"
        elif random_number == 3:
            answer = "Without a doubt"
        elif random_number == 4:
            answer = "Reply hazy, try again"
        elif random_number == 5:
            answer = "Ask again later"
        elif random_number == 6:
            answer = "Better not tell you now"
        elif random_number == 7:
            answer = "My sources say no"
        elif random_number == 8:
            answer = "Outlook not so good"
        elif random_number == 9:
            answer = "Very doubtful"

        if not name:
            print("Magic 8 Ball's answer: " + answer)
        else:
            print(name + " asks: " + question)
            print("Magic 8 Ball's answer: " + answer)
