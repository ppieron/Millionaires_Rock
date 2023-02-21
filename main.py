import random, time

questions_level1 = ['Who is a frontman of a legendary rock band - The Rolling Stones:',
                    'Slash is a famous:',
                    'Curt Cobain was a frontman of:',
                    '"Highway to Hell" is a signature song of:',
                    'Which rock band has a lighting sign in its logo:',
                    'The Beatles were an rock band from:'
                    ]

answers_level1 = [['A. Bon Scott', 'B. Mick Jagger', 'C. Axl Rose', 'D. Ozzy Osbourne'],
                  ['A. Singer', 'B. Drummer', 'C. Guitarist', 'D. Pianist'],
                  ['A. Nirvana', 'B. Aerosmith', 'C. Black Sabbath', 'D. ACDC'],
                  ['A. Guns n Roses', 'B. Marylin Mason', 'C. ACDC', 'D. The Rolling Stones'],
                  ['A. ACDC', 'B. The Offspring', 'C. Disturbed', 'D. Korn'],
                  ['A. USA', 'B. France', 'C. Scotland', 'D. England']
                  ]

correct_answers_level1 = ["B. Mick Jagger", "C. Guitarist", "A. Nirvana", "C. ACDC", "A. ACDC", "D. England"]

questions_level2 = ["What's the name of the latest album of ACDC:",
                    'Ozzy Osbourne is not an author of:',
                    'Who is the frontman of Korn:',
                    'Which song performed by Marylin Manson is a cover: ',
                    'In clip for which song members of Queen are dressed like women: ',
                    'Father of an actress Liv Tyler is a frontman of which rock band: ',
                    'The famous scene in which Axl rose gets married comes from the clip to:',
                    '"Californication" is a title of TV series with David Duchovny and a song of:',
                    'The famous rock ballad "Nothing Else Matters" is written by:',
                    'Who is the frontman of Iron Maiden'
                    ]

answers_level2 = [['A. Back in Black', "B. Power Up", 'C. Highway to Hell', 'D. High Voltage'],
                  ['A. Paranoid', 'B. Iron Man', 'C. T.N.T.', 'D. Crazy Train'],
                  ['A. Jonathan Davis', 'B. James Hetfield', 'C. Brian Johnson', 'D. Lenny Kravitz'],
                  ['A. Beautiful People', 'B. mObscene', 'C. Antichrist Superstar', 'D. Tainted Love'],
                  ['A. We Will Rock You', 'B. Bohemian Rhapsody', 'C. I Want to Break Free', 'D. Hammer to Fall'],
                  ['A. Guns n Roses', 'B. Red Hot Chilli Peppers', 'C. Metallica', 'D. Aerosmith'],
                  ['A. Paradise City', "B. Yesterdays", 'C. November Rain', 'D. You Could Be Mine'],
                  ['A. The Offspring', 'B. Red Hot Chilli Peppers', 'C. Ozzy Osbourne', 'D. The Rolling Stones'],
                  ['A. The Rolling Stones', 'B. Black Sabbath', 'C. Rammstein', 'D. Metallica'],
                  ['A. Bruce Dickinson', 'D. Brian Johnson', 'C. Mick Jagger', 'D. Ozzy Osbourne']
                  ]

correct_answers_level2 = ["B. Power Up", 'C. T.N.T.', 'A. Jonathan Davis', 'D. Tainted Love', 'C. I Want to Break Free',
                          'D. Aerosmith', 'C. November Rain', 'B. Red Hot Chilli Peppers', 'D. Metallica', 'A. Bruce Dickinson']

questions_level3 = ["Who was a vocalist on ACDC's album 'Back in Black': ",
                    'Who was the first lead vocalist of Nightwish:',
                    "Which Ozzy Osbourne's guitarist died in a plane crash:",
                    "What fairy tale does the music video for the Rammstein's song 'Sonne' refer to",
                    'In which TV series Marlyin Manson appeared as himself:',
                    'Which song by Korn was first: ',
                    'Axl Rose was a frontman of Guns n Roses and: ',
                    'Which rock band covered "The Sound of Silence":',
                    'Take me down to the Paradise City, where: ',
                    'Greta van Fleet is often compared to:',
                    ]

answers_level3 = [['A. Bon Scott', 'B. Brian Johnson', 'C. Axl Rose', 'D. Peter Clack'],
                  ['A. Anette Olzon', 'B. Floor Jansen', 'C. Tarja Turunen', 'D. Alissa White-Gluz'],
                  ['A. Randy Rhoads', 'B. Zakk Wydle', 'C. Steve Vai', 'D. Lemmy Kilmister'],
                  ['A. Cindirella', 'B. Snow White', 'C. Hänsel und Gretel', 'D. The Little Match Girl'],
                  ['A. Sons of Anarchy', 'B. Callifornication', 'C. The Office', 'D. House of Cards'],
                  ['A. Falling Away from Me', 'B. Coming Undone', 'C. Freak On a Leash', 'D. Here to Stay'],
                  ['A. The Rolling Stones', 'B. Iron Maiden', 'C. Aerosmith', 'D. ACDC'],
                  ['A. Marylin Manson', 'B. Guns n Roses', 'C. Disturbed', 'D. Motorhead'],
                  ['A. The grass is green and the girls are pretty.', "B. The love is free and the life's not shitty.",
                   "C. The sky is blue and and girls are pretty.", 'D. The drugs are free and they make us witty'],
                  ['A. Guns n Roses', 'B. Led Zeppelin', 'C. Deep Purple', 'D. Pink FLoyd'],
                  ]

correct_answers_level3 = ['B. Brian Johnson', 'C. Tarja Turunen', 'A. Randy Rhoads', 'B. Snow White',
                          'B. Callifornication', 'C. Freak On a Leash', 'D. ACDC', 'C. Disturbed', 'A. The grass is green and the girls are pretty.', 'B. Led Zeppelin']

Lifelines = ['50:50', 'Phone a friend', 'Ask Audience']

prizes = [500, 1000, 2000, 5000, 10000, 20000, 50000, 75000, 150000, 250000, 500000, 1000000]


def draw_question(lst):
    return random.randint(0, len(lst) - 1)


def print_question_nr(x):
    print("-" * 57 + "\n" + " " * (
            20 - (len(str(prizes[x - 1])))) + f"QUESTION No {x} - ${prizes[x - 1]:,}" + "\n" + "-" * 57)


def fiftyfifty(alst, calst, i):
    ranswr = calst[i]
    ranswr_idx = alst[i].index(ranswr)
    answr_choice_idx = random.randint(0, 3)
    if answr_choice_idx == ranswr_idx:
        return fiftyfifty(alst, calst, i)
    else:
        if answr_choice_idx < ranswr_idx:
            print(
                f"\nHere are the answers:\n\t{alst[i][answr_choice_idx]}\n\t{alst[i][ranswr_idx]}"
            )
            blst = [alst[i][ranswr_idx], alst[i][answr_choice_idx]]
            alst[i].clear()
            alst[i].append(blst[1])
            alst[i].append(blst[0])
        else:
            print(
                f"\nHere are the answers:\n\t{alst[i][ranswr_idx]}\n\t{alst[i][answr_choice_idx]}"
            )
            blst = [alst[i][ranswr_idx], alst[i][answr_choice_idx]]
            alst[i].clear()
            alst[i].append(blst[0])
            alst[i].append(blst[1])


def phone_a_friend(alst, calst, i, lvl):
    frnd_answer = []
    ranswr = calst[i]
    ranswr_idx = alst[i].index(ranswr)
    if len(alst[i]) == 2:
        for _ in range(5 - lvl):
            frnd_answer.append(ranswr_idx)
        r_choice = random.randint(0, 1)
        frnd_answer.append(r_choice)
        frnd_choice = random.choice(frnd_answer)
        print(f"\nYour friend says it's: {alst[i][frnd_choice]}")
    else:
        for _ in range(4 - lvl):
            frnd_answer.append(ranswr_idx)
        r_choice = random.randint(0, 3)
        frnd_answer.append(r_choice)
        frnd_choice = random.choice(frnd_answer)
        print(f"\nYour friend says it's: {alst[i][frnd_choice]}")


def ask_audience(alst, calst, i, lvl):
    ranswr = calst[i]  # B
    ranswr_idx = alst[i].index(ranswr)

    if len(alst[i]) == 4:
        if lvl == 1:
            ranswr_prcnt = round((random.uniform(0.45, 1)), 2)

        elif lvl == 2:
            ranswr_prcnt = round((random.uniform(0.4, 0.7)), 2)

        else:
            ranswr_prcnt = round((random.uniform(0.3, 0.6)), 2)

        wanswr1 = round(random.uniform(0, (1 - ranswr_prcnt)), 2)
        wanswr2 = round(random.uniform(0, (1 - ranswr_prcnt - wanswr1)), 2)
        if wanswr2 < 0:
            wanswr2 = 0
        wanswr3 = round((1 - ranswr_prcnt - wanswr1 - wanswr2), 2)
        if wanswr3 < 0:
            wanswr3 = 0

        wanswr_lst = [wanswr1, wanswr2, wanswr3]

        print("\nThe Audience poll results:")

        if ranswr_idx == 0:
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][2]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        elif ranswr_idx == 1:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][2]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        elif ranswr_idx == 2:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        else:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][2]} - {wanswr_lst[0]:.0%}')
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')

    else:
        if lvl == 1:
            ranswr_prcnt = round((random.uniform(0.45, 1)), 2)

        elif lvl == 2:
            ranswr_prcnt = round((random.uniform(0.4, 0.7)), 2)

        else:
            ranswr_prcnt = round((random.uniform(0.3, 0.6)), 2)

        wanswr = round(1 - ranswr_prcnt, 2)

        print("\nThe Audience poll results:")

        if ranswr_idx == 0:
            print(f'\t{alst[i][0]} - {ranswr_prcnt:.0%}')
            print(f'\t{alst[i][1]} - {wanswr:.0%}')

        elif ranswr_idx == 1:
            print(f'\t{alst[i][0]} - {wanswr:.0%}')
            print(f'\t{alst[i][1]} - {ranswr_prcnt:.0%}')


def lifeline_choice(lflst):
    decision = input("\nWould you like to use a Lifeline? (Y/N): ").upper().strip()
    if decision[0] == 'Y':
        print("\nYour available Lifelines:")
        for i in lflst:
            print(i, end=", ")
        lfchoice = input(f"\n\nWhich one do you choose? ").upper().strip()
        if lfchoice[0] == '5':
            print(f'Your choice is: "50:50"')
            return '50:50'
        elif lfchoice[0] == 'P':
            print(f'Your choice is: "Phone a friend"')
            return 'Phone a friend'
        elif lfchoice[0] == 'A':
            print(f'Your choice is: "Ask Audience:')
            return 'Ask Audience'

    else:
        return False


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
        if Lifelines == []:
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
                player_decision = input(f"\nWould you like to play further or come back home with:\n${prizes[question_number - 2]:,}"
                                        f"\n\nWhat's your decision? Continue or Give Up?: ").upper().strip()
                if player_decision[0] == 'C':
                    break
                elif player_decision[0] == 'G':
                    print("\n" + "=" * 57 + "\n" +
                          ' ' * (28 - int(len(f'Congratulations! You have won: ${prizes[(question_number - 2)]}') * 0.5)) +
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
                print("\n" + "*" * 57 + "\n" + " " * 8 + f"\x1b[6;10;42mCONGRATULATIONS! You have won $1,000,000!\x1b[0m\n" + "*" * 57)
        else:
            if question_number == 1:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(len('You have won: $0') * 0.5)) + "\x1b[6;10;41mYou have won: $0\x1b[0m" + "\n" + "=" * 57)

            elif 1 <= question_number < 7:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(len('You have won: $1,000') * 0.5)) + "\x1b[6;10;44mYou have won: $1,000\x1b[0m" + "\n" + "=" * 57)

            elif 7 <= question_number < 12:
                print(f"{player_answer} is a wrong answer." +
                      f"\nCorrect answer: {correct_answers[i]}" + "\n" + "=" * 57 + "\n" +
                      ' ' * (28 - int(len('You have won: $50,000') * 0.5)) + "You have won: $50,000" + "\n" + "=" * 57)

            return x == 1

        if x == 1:
            break

        questions.pop(i)
        answers.pop(i)
        correct_answers.pop(i)
        time.sleep(1)
    return 1


print("=" * 55 + "\n" + " " * 8 + f"|m|. WLECOME TO ROCK MILLIONAIRES .|m|" +
      "\n\n"
      " You will now see 12 questions checking your knowledge"
      "\n about rock music. Each question brings you closer to:"
      "\n               WINNING 1,000,000 USD!\n")

time.sleep(2)
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
print('\nMilestones are capped amounts of your final prize\n'
      'You have 3 Lifelines:\n'
      '\t50:50\n\tPhone a friend\n\tAsk Audience\n'
      "\n>>>>>> OOOOOOOOOKEEEEEY! SO LET'S ROOOOOOOOOCK!!! <<<<<<")

time.sleep(1)

x = main(1, 2, 1)
if x == 1:
    x = main(2, 5, 3)
if x == 1:
    main(3, 5, 8)
