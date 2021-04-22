board = ['1','2','3',
         '4','5','6',
         '7','8','9',]

def show_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')

def take_input(player_xo):
   valid = False
   while not valid:
      player_answer = input("Ваш ход " + player_xo + ' ')
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_xo
            valid = True
         else:
            print("Здесь уже занято")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win():
   win_var= ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_var:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main():
    counter = 0
    win = False
    while not win:
        show_board()
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win()
           if tmp:
              print(tmp, "победил!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    show_board()
main()

input("Нажмите Enter для выхода!")
