import random
o=1
z=0
trailing=True
def print3x3(board,trailing = True):
    print(" ", board[0], "|", board[1], "|", board[2])
    print(" ---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print(" ---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])

if trailing:
    print()
    
board= 9*[""]
ring1="small"
ring2="medium"
ring3="large"
#plithos kenwn tetragwnwn
blank=9
#h metavliti pou deixnei an symplhrothike o arithmos daktyliwn orizontia katheta h diagwnia
inarow=False

if o<100:
 if blank>0 and not inarow :
    print3x3(board)
    print3x3(range(9))
    position=(random.randrange(0,8))
    z=z+1
    if board[position]!=ring1 :
      if board[position]==ring2:
            board[position]=ring3
    if board[position]!=ring2:
            board[position]=ring2
            if board[position]=="":
             board[position]=ring1

blank-=1

if board[0] == board[1] == board[2] == ring1 :
            inarow = True
elif board[3] == board[4] == board[5] == ring1 :
            inarow = True
elif board[6] == board[7] == board[8] == ring1 :
            inarow = True
elif board[0] == board[3] == board[6] == ring1:
            inarow = True
elif board[1] == board[4] == board[7] == ring1:
            inarow = True
elif board[2] == board[5] == board[8] == ring1:
            inarow = True
elif board[0] == board[4] == board[8] == ring1:
            inarow = True
elif board[2] == board[4] == board[6] == ring1:
            inarow = True

if board[0] == board[1] == board[2] == ring2 :
            inarow = True
elif board[3] == board[4] == board[5] == ring2 :
            inarow = True
elif board[6] == board[7] == board[8] == ring2 :
            inarow = True
elif board[0] == board[3] == board[6] == ring2:
            inarow = True
elif board[1] == board[4] == board[7] == ring2:
            inarow = True
elif board[2] == board[5] == board[8] == ring2:
            inarow = True
elif board[0] == board[4] == board[8] == ring2:
            inarow = True
elif board[2] == board[4] == board[6] == ring2:
            inarow = True
            o==o+1

if board[0] == board[1] == board[2] == ring3 :
            inarow = True
elif board[3] == board[4] == board[5] == ring3 :
            inarow = True
            o==o+1
elif board[6] == board[7] == board[8] == ring3 :
            inarow = True
elif board[0] == board[3] == board[6] == ring3:
            inarow = True
elif board[1] == board[4] == board[7] == ring3:
            inarow = True
elif board[2] == board[5] == board[8] == ring3:
            inarow = True
elif board[0] == board[4] == board[8] == ring3:
            inarow = True
elif board[2] == board[4] == board[6] == ring3:
            inarow = True

#emfanish telikou pinaka
print3x3(board)

#emfanish apotelesmatos
if inarow:
    print("WIN!")
    o==o+1
else:
    print("GAME OVER")
    o==o+1


if o==100:
    x=z/100
print (x)