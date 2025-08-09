import time
import datetime as dt

COMM_TXT = 'reviews-due-checker.txt'

def get_data():
    with open(COMM_TXT, 'r') as f:
        cards = f.readlines()
        return cards

def get_due_cards(list_of_cards):
    time_now = dt.datetime.now()

    due_cards = []
    for card in list_of_cards:
        card = card.split(',')
        card_datetime = dt.datetime.strptime(card[5].strip(), '%Y-%m-%d %H:%M:%S.%f')
        if card_datetime <= time_now:
            due_cards.append(card)
    return (due_cards)

def send_data(data):
    with open(COMM_TXT, 'w') as f:
        for item in data:
            f.write(','.join(item))

def clear_txt():
    with open(COMM_TXT, 'w') as f:
        f.write('')

if __name__ == '__main__':
    while True:
        data = get_data()
        if data == [] or data == '':
            continue
        else:
            due_cards = get_due_cards(data)
            send_data(due_cards)

            time.sleep(10)
            clear_txt()
        time.sleep(3)
