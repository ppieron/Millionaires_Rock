import random, time

questions = ['Który klub piłkarski wygrał Ligę Mistrzów w sezonie 21/22: ',
             'W którym filmie nie wystąpił Dwane Johnson:',
             'Trik polegający na złapaniu deski za tylną krawędź w trakcie skoku to:',
             'Który język programowania nie jest językiem backendowym: ',
             'W którym roku rozegrała się bitwa pod Grundwaldem: ',
             'Który aktor wcielił się w rolę Jamesa Bonda jako pierwszy: ',
             'Którego dzieła autorem nie był Michał Anioł: ',
             'Jak nazywa się najnowszy album grupy AC/DC: ',
             "Który utwór nie jest utworem Ozzy'ego Osobourne'a: ",
             'Wzór na pole koła to: '
             ]

answers = [['A. Real Madryt', 'B. Manchester City', 'C. PSG', 'D. Liverpool FC'],
           ['A. Jumanji', 'B. Black Adam', 'C. Za szybcy, za wścieki', 'D. Baywatch' ],
           ['A. Tail Grab', 'B. Nose Grab', 'C. Method', 'D. 3.6'],
           ['A. Python', 'B. C#', 'C. Java', 'D. Java Script'],
           ['A. 966', 'B. 1140', 'C. 1410', 'D. 1520'],
           ['A. Roger Moore', 'B. Sean Connery', 'C. Pierce Brosnan', 'D. George Lazenby'],
           ['A. Dama z gronostajem', 'B. Fresk w Kaplicy Sykstyńskiej', 'C. Stworzenie Adama', 'D. Rzeźba Dawida'],
           ['A. Back in Black', "B. Power Up", 'C. Highway to Hell', 'D. High Voltage'],
           ['A. Paranoid', 'B. Iron Man', 'C. T.N.T.', 'D. Crazy Train'],
           ['A. π * r**2', 'B. π * 2r', 'C. π * r / 2', 'D. π**2 + 2r']
           ]

correct_answers = ['A', 'C', 'C', 'D', 'C', 'B', 'A', 'B', 'C', 'A']


def draw_question(lst):
    return random.randint(0, len(lst) - 1)


def print_question(x):
    print(f"---------------------------------------------------------"
          f"\n" + " " * 21 + f"PYTANIE NR {x}"
          f"\n---------------------------------------------------------")


def check_prize(score):
    prizes = ['lot w kosmos z Elonem Muskiem', 'wycieczkę', 'pralkę']
    if score == 10:
        prize = prizes[0]
    elif score == 9:
        prize = prizes[1]
    else:
        prize = prizes[2]

    print(f"\n========================================================="
          f"\n    GRATULACJE! Wygrałeś {prize}!"
          f"\n=========================================================")


def get_answer():
    while True:
        answer = input("\nTwoja odpowiedź to: ").title().strip()
        if answer not in ['A', 'B', 'C', 'D']:
            print("\n[BŁĄD] Wprowadzono błędne dane! Wpisz A, B, C lub D!")

        else:
            return answer

print(f"========================================================="
      f"\n" + " " * 15 + f"WITAJ W GRZE MILIONERZY!"
      f"\n     Odpowiedz na pytania i wygraj cenne nagrody!"
      f"\n=========================================================")

time.sleep(1)
player_score = 0
tries = 3
for question_number in range(1, len(questions) + 1):
    if tries == 0:
        print(f"\n========================================================="
              f"\n     KONIEC GRY. Odpowiedziałeś błędnie na 3 pytania!"
              f"\n=========================================================")
        break

    print_question(question_number)
    i = draw_question(questions)
    print(questions[i])
    for j in range(len(answers[i])):
        time.sleep(0.3)
        print(f"\t{answers[i][j]}")
    answer = get_answer()
    if answer == correct_answers[i]:
        print(f"{answer} to dobra odpowiedź. Gratulacje!")
        player_score += 1
    else:
        print(f"{answer} to zła odpowiedź.\nWłaściwa odpowiedź to: {correct_answers[i]}")
        tries -= 1

    questions.pop(i)
    answers.pop(i)
    correct_answers.pop(i)
    time.sleep(1)

check_prize(player_score)