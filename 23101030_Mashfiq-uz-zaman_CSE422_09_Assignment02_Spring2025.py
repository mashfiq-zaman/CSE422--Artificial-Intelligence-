
def Fitness_Calculation(capital,choromo,percentage,dict):
  new_cap=capital
  loss=int(choromo[:2])
  profit=int(choromo[2:4])
  trade=int(choromo[4:6])
  for i in percentage:
   if i<(-loss):
     cacl1=round((new_cap*trade)/100,2)
     temp=round((cacl1*-loss)/100,2)
     new_cap+=round(temp,2)
   elif i > profit:
     cacl1=round((new_cap*trade)/100,2)
     temp=round((cacl1*profit)/100,2)
     new_cap+=round(temp,2)
   else:
    cacl1=round((new_cap*trade)/100,2)
    temp=round((cacl1*i)/100,2)
    new_cap+=round(temp,2)
  score= new_cap-capital
  if choromo not in dict1:
    dict1[choromo]=score
  return score
def crossover(parent):
  split=random.randint(1,5)
  split1=random.randint(1,5)
  child1=parent[0][:split] + parent [1][split:]
  child2=parent[1][:split1] + parent [0][split1:]
  #print(child1,child2)
  offspring=mutation(child1,child2)
  return(offspring)

def mutation(child1,child2):
  rate=0.05
  num=[child1[i:i+2] for i in range(0, len(child1), 2)]
  num2=[child2[i:i+2] for i in range(0, len(child2), 2)]
  #(num,num2)
  sp1=random.randint(0,2)
  sp2=random.randint(0,2)
  if random.randint(0,1) <  rate:
      num[sp1]=f"{random.randint(1,99):02d}"
      num2[sp2]=f"{random.randint(1,99):02d}"
      new_num=''.join(num)
      new_num1=''.join(num2)
      temp=Fitness_Calculation(1000,new_num,percentage,dict1)
      temp=Fitness_Calculation(1000,new_num1,percentage,dict1)     
      return temp
dict1={} 
percentage=[-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
store=[]
for k in range(4):
  import random
  random=[random.randint(1,99) for i in range(3)]
  #print(random)
  choromo=''.join(f"{str(random).zfill(2)}" for random in random)
  store.append(choromo)
import random
for i in range(10):
   random_parent=crossover(random.sample(store, k=2))
shorted=dict(sorted(dict1.items(), key=lambda  item : item[1], reverse= True))
new_parent=list(shorted.keys())[:4]

for i in range(10):
  call=crossover(random.sample(new_parent, k=2))
choromo,profit=next(iter(shorted.items()))
#print(choromo[0:2])
#print(new_parent)
print(f"best_strategy:\n stop_loss: {choromo[:2]}, take_profit: {choromo[2:4]}, trade_size: {choromo[4:6]} \n Final_profit: {profit}")



#    PART 2
def crossovertwo(l):
  print(l)
  split1=random.randint(1,7)
  split2=random.randint(split1+1,7)
  child1=l[0][:split1] + l [1][split1:split2]+l[0][split2:]
  child2=l[1][:split1] + l [0][split1:split2]+l[1][split2:]
  print(f"part 2 crossover : {child1,child2}")
store1=[]  
for k in range(4):
  import random
  random=[random.randint(1,99) for i in range(5)]
  choromo=''.join(f"{str(random).zfill(2)}" for random in random)
  store1.append(choromo)
import random
call=crossovertwo(random.sample(store1, k=2))
