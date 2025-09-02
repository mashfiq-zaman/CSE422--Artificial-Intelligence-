import copy
def create_graph(graph,parent, child, main_cost):
  if parent not in graph:
        graph[parent] = {}  
  graph[parent][child] = main_cost
  #print(graph)

def cheap_path(graph,dict1,start,goal):
   if start==goal:
      return "Dude you are at the same city"
   sum=0
   data=(graph[start[0]])
   for k,v in data.items():
    data[k]=v+ dict1[k]         #this adds hiuristic and main cost value
   sorted_data=dict(sorted(data.items(), key=lambda x: x[1])) #this sorts the dictionary like priority queue
   #print(sorted_data)
   i=0
   for k,v in sorted_data.items():
    if i==1:
        break
    i+=1
    visited=start
    return recurrive(graph,k,visited,goal)
   
def recurrive(graph,k,visited,goal):     
  visited.append(k)
  #print(k)
  if k == goal[0]:
     return visited
  a= dict(graph.get(k, {}))
  #print(a)#gives all child
  sorted_data=dict(sorted(a.items(), key=lambda x: x[1])) #sort the child
  #print(sorted_data)
  s=next(iter(sorted_data))  
  if  s in visited and len(sorted_data)<=1: 
     return "NO PATH FOUND"
  if s in visited and len(sorted_data)>=1:  
    s=list(sorted_data.keys())[1]                 #gives you the 2nd key
    return recurrive(graph,s,visited,goal)
  else:
     return recurrive(graph,s,visited,goal,)

with open("input.txt","r") as file:
 dict1={} #HIURISTIC VALUE
 graph={}
 for i in range (20):
    place=[elem for elem in file.readline().split()]
    key=place[0][0]
    value=int(place[1])
    if key not in dict1:    
      dict1[key]=value
    dict2={}
    for i in range(2,len(place),2):
        dict2[place[i]]=int(place[i+1])  #Temporary path cost store
    #print(dict2)
    for k,v in dict2.items():
     create_graph(graph,place[0][0],k[0],v) # with dict2 and graph it creates the main added graph
c=copy.deepcopy(graph) 
start=([input("Please enter which city you are at in capital   ")])
goal=([input("plase enter where you wanna go  ")]) # this is set for bucBucharest
a=cheap_path(graph,dict1,start,goal)
with open('output.txt', 'w') as out:
 if a=="Dude you are at the same city" or a== "NO PATH FOUND":
  out.writelines(f' {a} ')
 else:
  sum=0
  for i in range(len(a)):
    if i==len(a)-1:
      break
    temp=c[a[i]]
    sum+=temp[a[i+1]]
  new= " -> ".join(a)
  out.writelines(f'Path : {new}\n')
  out.writelines(f'Total distance: {sum} km')
 
   






         