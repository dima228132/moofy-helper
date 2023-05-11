import os, time
from main import menu

pages = ["""                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |1. open some app             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |2. open some tool|for linux  |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |3. maybe start some song?    |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |4. stop me                   |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                                WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |5. stop some app             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |6. open some site            |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |7. turn off my computer      |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |8. ssh connect               |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |9. lock my computer          |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |10. destroy my comp|dangerous|MooFyMooFyMooFyMooFyMooFyMooFy| VERY DANGEROUS
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |11. fill in card details     |MooFyMooFyMooFyMooFyMooFyMooFy| (CREDIT CARD) NOT AVALIBALE AT THE MOMENT
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |12.do a call by available app|MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------""", """                               WHAT YOUR COMMAND WILL DO?
                 ______________________________________________________________
                 |13. connect with alisa stance|MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |14. connect with some stuff  |MooFyMooFyMooFyMooFyMooFyMooFy| it may be a smart desk or maybe 
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |15. smth3                    |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |16. kit of available options |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | return - return to menu     |MooFyMooFyMooFyMooFyMooFyMooFy|
                 |                             |MooFyMooFyMooFyMooFyMooFyMooFy|
                 | next - next page of commands|MooFyMooFyMooFyMooFyMooFyMooFy|
                 --------------------------------------------------------------"""]


def sleep(long):
    time.sleep(long)

def clear():
    os.system('clear')


def next_page(page):


def log_new_command():
    page = 0
    print(pages[page])
    n = input('what do you want?\n>>>')

    while n == 'next' or n == 'return':
        clear()
        if n == 'return':
            return('menu')
        print(pages[page + 1])
        page += 1
        n = input()

    while True:
        try:
            n = int(n)
            if n < 17 and n > 0:
                return (n)
            else:
                print('only digit 1-16')
        except:
            print('seems like you put not digit here, try it again')
            n = input('>>>')




def more_similar_os(user_os):
    list_of_len_sim = []
    list_of_able_os = ['macos, windows, linux']
    for i in list_of_able_os:
        count = 0
        for j in range(len(user_os)):
            if user_os[j] == i[j]:
                count += 1
        list_of_len_sim.append(count)

    if max(list_of_len_sim) <= 2:
        return(False)
    else:
        return(list_of_able_os[list_of_len_sim.index(max(list_of_len_sim))])


def find_more_similar_command(cmd):
    list_of_len_sim = []
    list_of_commads = take_from_database('list_of_commands')
    for i in list_of_commads:
        count = 0
        for j in range(len(cmd)):
            if cmd[j] == i[j]:
                count += 1
        list_of_len_sim.append(count)

    return(list_of_commads[count.index(max(count))])


def start():
    while True:
        command = find_more_similar_command(input_vocie_command())
        if take_from_database(2) in command:
            try:
                do_command(command)
            except:
                say('smth went wrong, sorry, try it again')
def stop():
    exit(0)

def do_it(choice):
    if choice == 1:
        what_is_new_command = log_new_command()
        if what_is_new_command != 'menu':
            add_to_list_of_commands(what_is_new_command)
        clear()
        menu()

    elif choice == 2:
        print("i just kidding. i don't need to reg your voice")
    elif choice == 3:
        clear()
        start()