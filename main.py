import random, time
from Lifelines import fiftyfifty, phone_a_friend, ask_audience, lifeline_choice
import Questions

questions_level1 = Questions.questions_level1
answers_level1 = Questions.answers_level1
correct_answers_level1 = Questions.correct_answers_level1

questions_level2 = Questions.questions_level2
answers_level2 = Questions.answers_level2
correct_answers_level2 = Questions.correct_answers_level2

questions_level3 = Questions.questions_level3
answers_level3 = Questions.answers_level3
correct_answers_level3 = Questions.correct_answers_level3

Lifelines = ['50:50', 'Phone a friend', 'Ask Audience']

prizes = [500, 1000, 2000, 5000, 10000, 20000, 50000, 75000, 150000, 250000, 500000, 1000000]


def draw_question(lst):
    return random.randint(0, len(lst) - 1)


def print_question_nr(x):
    print("-" * 57 + "\n" + " " * (
            20 - (len(str(prizes[x - 1])))) + f"QUESTION No {x} - ${prizes[x - 1]:,}" + "\n" + "-" * 57)


def get_answer():
    while True:
        answer = input("\nYour answer is: ").title().strip()
        if answer not in ['A', 'B', 'C', 'D']:
            print("\n[ERROR] Wrong input! Enter A, B, C or D!")

        else:
            return answer


def main(lvl, no_of_questions, lvl_start_qnumber):
    level = lvl
    if level == 1:
        questions = questions_level1
        answers = answers_level1
        correct_answers = correct_answers_level1

    elif level == 2:
        print(">" * 28 + "O" + "<" * 28 + "\nYou've reached 1st Milestone! Guaranteed prize is $1,000\n"
              + ">" * 28 + "O" + "<" * 28 + "\n")
        questions = questions_level2
        answers = answers_level2
        correct_answers = correct_answers_level2

    else:
        print(">" * 28 + "O" + "<" * 28 + "\n    You've reached 2nd Milestone! Guaranteed prize is:\n"
              + " " * 26 + "$50,000\n" + ">" * 28 + "O" + "<" * 28 + "\n")
        questions = questions_level3
        answers = answers_level3
        correct_answers = correct_answers_level3

    for question_number in range(lvl_start_qnumber, lvl_start_qnumber + no_of_questions):

        print_question_nr(question_number)
        i = draw_question(questions)
        print(questions[i])
        for j in range(len(answers[i])):
            time.sleep(0.3)
            print(f"\t{answers[i][j]}")
        if not Lifelines:
            print("\nYou have no more Liflines available!")
        for LifeLine in range(len(Lifelines)):
            if Lifelines:
                ll_choice = lifeline_choice(Lifelines)
                if ll_choice == '50:50':
                    fiftyfifty(answers, correct_answers, i)
                    lf_idx = Lifelines.index(ll_choice)
                    Lifelines.pop(lf_idx)
                elif ll_choice == 'Phone a friend':
                    phone_a_friend(answers, correct_answers, i, level)
                    lf_idx = Lifelines.index(ll_choice)
                    Lifelines.pop(lf_idx)
                elif ll_choice == 'Ask Audience':
                    ask_audience(answers, correct_answers, i, level)
                    lf_idx = Lifelines.index(ll_choice)
                    Lifelines.pop(lf_idx)
                else:
                    break
        x = 0
        if question_number > 1:
            time.sleep(0.5)
            while True:
                player_decision = input(
                    f"\nWould you like to play further or come back home with:\n${prizes[question_number - 2]:,}"
                    f"\n\nWhat's your decision? Continue or Give Up? (C/G): ").upper().strip()
                if player_decision[0] == 'C':
                    break
                elif player_decision[0] == 'G':
                    print("\n" + "=" * 57 + "\n" +
                          ' ' * (28 - int(
                        len(f'Congratulations! You have won: ${prizes[(question_number - 2)]}') * 0.5)) +
                          f"\x1b[6;10;42mCongratulations! You have won: ${prizes[question_number - 2]:,}\x1b[0m" + "\n" + "=" * 57)
                    return x == 1,

                else:
                    print("\n[ERROR] Wrong input! Input (C)ontinue or (G)ive Up!")

        if x == 1:
            break

        player_answer = get_answer()
        if player_answer == correct_answers[i][0]:
            if question_number < 12:
                print(f"{player_answer} is a right answer! You have ${prizes[question_number - 1]:,}\n")
            else:
                print(
                    "\n" + "*" * 57 + "\n" + " " * 8 + f"\x1b[6;10;42mCONGRATULATIONS! You have won $1,000,000!\x1b[0m\n" + "*" * 57)
        else:
            if question_number == 1:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(
                    len('You have won: $0') * 0.5)) + "\x1b[6;10;41mYou have won: $0\x1b[0m" + "\n" + "=" * 57)

            elif 1 <= question_number < 7:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(
                    len('You have won: $1,000') * 0.5)) + "\x1b[6;10;44mYou have won: $1,000\x1b[0m" + "\n" + "=" * 57)

            elif 7 <= question_number < 12:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(len('You have won: $50,000') * 0.5)) + "\x1b[6;10;44mYou have won: $50,000\x1b[0m" + "\n" + "=" * 57)

            return x == 1

        if x == 1:
            break

        questions.pop(i)
        answers.pop(i)
        correct_answers.pop(i)
        time.sleep(1)
    return 1


print("=" * 55 + "\n" + " " * 4 + f"|m|. WELCOME TO THE ROCK MILLIONAIRES .|m|" +
      "\n\n"
      " You will now see 12 questions checking your knowledge"
      "\n about rock music. Each question brings you closer to:"
      "\n               WINNING 1,000,000 USD!\n")

time.sleep(4)
print("-" * 55 +
      "\nBelow you will find values of the questions:\n")

n = 1
for prize in prizes:
    time.sleep(0.3)
    if n == 12:
        print(f'\x1b[6;10;42mQuestion {n}. - $ {prize:,}\x1b[0m << TOP PRIZE')
    elif n == 2 or n == 7:
        print(f'\x1b[6;10;44mQuestion {n}. - $ {prize:,}\x1b[0m << Milestone')
    else:
        print(f'Question {n}. - $ {prize:,}')
    n += 1

time.sleep(0.5)
print('\nMilestones are capped amounts of your final prize\n')
time.sleep(2)
print('You have 3 Lifelines:')
for Lifeline in Lifelines:
    print(Lifeline, end=", ")
    time.sleep(0.5)
time.sleep(2)
print("\n\n>>>>>> OOOOOOOOOKEEEEEY! SO LET'S ROOOOOOOOOCK!!! <<<<<<\n")

time.sleep(5)

x = main(1, 2, 1)
if x == 1:
    x = main(2, 5, 3)
if x == 1:
    main(3, 5, 8)
