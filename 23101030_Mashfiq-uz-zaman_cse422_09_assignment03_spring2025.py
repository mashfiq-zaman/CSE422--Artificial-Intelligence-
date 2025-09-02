import random
import math
class chess:
    def __init__(self,leafv=None,child=None):
        self.leafv=leafv
        if child is not None:
            self.child=child
        else:
            self.child=[]
def game_tree(depth,maxv,minv):
        if depth==0:
             value=utility(maxv,minv)
             return chess(leafv=value)
        childnode=[game_tree(depth-1,maxv,minv),game_tree(depth-1,maxv,minv)]
        return chess(child=childnode)
def power(m):
     temp=math.log2(m+1)+(m/10)
     return temp
     
def utility(maxv,minv):
    i=random.randint(0,1)
    u_value=(power(maxv)-power(minv)+(-1)**i)*(((random.randint(1,10)))/10)
    return u_value
def minimax(game_board ,depth,alpha,beta,flag):
     if depth==0 or game_board.child==[]:
          return game_board.leafv
     if flag:
      v=float('-inf')
      for child in game_board.child:
          v2=minimax(child,depth-1,alpha,beta,flag=False)
          if v2>v:
               v=v2
          if v2>alpha:
               alpha=v
          if v >= beta:
                break
      return v
     
     if flag==False:
      v=float('inf')
      for child in game_board.child:
          v2=minimax(child,depth-1,alpha,beta,flag=True)
          if v2<v:
               v=v2
          if v2<beta:
               beta=v
          if v <= alpha:
                break
      return v    
    
player=int(input("choose your player (0 for Carlsen, 1 for Caruana) : "))
max1=int(input("insert your dominance(maxV): "))
min1=int(input("just give a value(minV): "))
players=["Carlsen","Caruana"]
value=[max1,min1]
carua=0
carl=0
draw=0
for i in range(1,5):
    max_p=players[(player+i)%2]
    min_p=players[(player+i+1)%2]
    maxv=value[(player+i)%2]
    minv=value[(player+i+1)%2]
    #if player==1: 
       # max_p=players[(i+1)%2]
        #min_p=players[i%2]
        #maxv=value[(i+1)%2]
       # minv=value[i%2]
    game_board=game_tree(5,maxv,minv)
    #print(tree)
    winner=minimax(game_board , 5, alpha=float('-inf'),beta=float('inf'),flag=True)
    #print(winner)
    if winner > 0:
        print(f"Game {i} Winner: {max_p} (Max) (Utility value: {winner:.3f}")
        if max_p=="Caruana":
            carua+=1
        else:
            carl+=1
    if winner < 0:
        print(f"Game {i} Winner: {min_p} (min) (Utility value: {winner:.3f}")
        if min_p=="Caruana":
            carua+=1
        else:
            carl+=1
    if winner == 0:
        print(f"game is draw")
        draw+=1
if carua>carl:
    print(f"Overall Results: Fabiano Caruana Wins:{carua}\n Magnus Carlsen Wins: {carl}\n Draws: {draw} \nOverall Winner: Fabiano Caruana")
if carua<carl:
    print(f"Overall Results: Magnus Carlsen Wins:{carl} \nFabiano Caruana Wins: {carua}\n Draws: {draw}\nOverall Winner: Magnus Carlsen")
if carua==carl:
    print(f"Overall Results: Magnus Carlsen Wins:{carl}\nFabiano Caruana Wins: {carua}\n Draws: {draw}\nOverall Winner: draw")



#####part 2
def maxmax(game_board ,depth,alpha,beta):
     if depth==0 or game_board.child==[]:
          return game_board.leafv
     else:
      v=float('-inf')
      for child in game_board.child:
          v2=maxmax(child,depth-1,alpha,beta)
          if v2>v:
               v=v2
          if v2>alpha:
               alpha=v
          if v >= beta:
                break
      return v
p=["Light","L"]
player1=int(input("Enter who goes first (0 for Light, 1 for L): "))
cost=float(input("Enter the cost of using Mind Control: "))
base1=int(input("Enter base strength for Light: "))
base2=int(input("Enter base strength for L: "))

mind_control_without=minimax(game_tree(5, base1, base2), 5, alpha=float('-inf'), beta=float('inf'), flag=True)

mind_control_with=maxmax(game_tree(5, base1, base2), 5, alpha=float('-inf'), beta=float('inf'))

Mind_Control_after_incurring_the_cost=(mind_control_with-cost)

print(f"Minimax value without Mind Control:{mind_control_without:.2f}")
print(f"Minimax value with Mind Control:{mind_control_with:.2f}")
print(f"Minimax value with Mind Control after incurring the cost:{Mind_Control_after_incurring_the_cost:.2f}")
if mind_control_with>mind_control_without:
    print(f"{p[player1]} should use Mind Control!")
else:
    print(f"{p[player1]} should NOT use Mind Control as the position is already winning.")
