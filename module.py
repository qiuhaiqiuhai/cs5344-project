import numpy as  np
#import networkx as nx
'''
comm=[[1,2,3],[4,5,6],...]
G=nx.Graph()
'''
def read_edge(filename):
    file = open(filename, 'r')
    edge = []
    degree = {}

    for line in file:
        words = line.split(' ')
        src = int(words[0].strip())
        dst = int(words[1].strip())
        if(src>dst):
            src,dst = dst,src
        if((src,dst) not in edge):
            edge.append((src,dst))
            if(src not in degree):
                degree[src] = 1
            else:
                degree[src]+=1

            if (dst not in degree):
                degree[dst] = 1
            else:
                degree[dst] += 1


    file.close()
    return edge, degree

import re
def read_com(filename):
    file = open(filename, 'r')
    com = []

    for line in file:
        com.append([int(x) for x in re.findall(r'\d+', line)])

    return com


def Q1(comm,edges,du):
   m=len(edges)
   #print'm',m
   #print 'du',du
   ret=0.0
   for c in comm:
       for x in c:
           for y in c:
               if x<=y:
                   if (x,y) in edges:
                       aij=1.0
                   else:
                       aij=0.0
               else:
                   if (y,x) in edges:
                       aij=1.0
                   else:
                       aij=0
               #print x,' ',y,' ',aij
               tmp=aij-du[x]*du[y]*1.0/(2*m)
               #print du[x],' ',du[y]
               #print tmp
               ret=ret+tmp
               #print ret
               #print ' '
               
   ret=ret*1.0/(2*m)
   print 'ret ',ret
   return ret
   

def Q2(comm,edges,du):

   m=len(edges)
   #print 'm',m


   #print 'du',du

   ret2=0.0
   for c in comm:
       bian=0
       for x in c:
           for y in c:
               if x<=y:
                   if (x,y) in edges:
                       bian=bian+1
               else:
                   if (y,x) in edges:
                       bian=bian+1
       duHe=0
       for x in c:
           duHe=duHe+du[x]
       tmp=bian*1.0/(2*m)-(duHe*1.0/(2*m))*(duHe*1.0/(2*m))
       #print 'bian',bian,'tmp',tmp
       ret2=ret2+tmp
   print 'ret2 ', ret2
   return ret2
   
   
def Q3(comm,edges,du):
   k=len(comm)

   m=len(edges)
   print 'm',m

   e=np.zeros((k,k),np.float)
   for i in range(k):
       for j in range(k):
           bian=0
           for x in comm[i]:
               for y in comm[j]:
                   if x<y:
                       if (x,y) in edges:
                           bian=bian+1
                   else:
                       if (y,x) in edges:
                           bian=bian+1
           if i==j:
               bian=bian/2
           if i==j:
               e[i,j]=bian*1.0/m
           else:
               e[i,j]=bian*0.5/m
           #e[i,j]=bian
       #endforj
   #endfori
   print e

   a=np.zeros(k,np.float)
   for i in range(k):
       he=0
       for j in range(k):
           he=he+e[i,j]
       a[i]=he
   #
   print a
   QValue=0
   for i in range(k):
       QValue=QValue+e[i,i]-a[i]*a[i]
   #
   print 'QValue ', QValue
   return QValue

import sys
if __name__ == "__main__":
    edges, degree = read_edge(sys.argv[1])
    com = read_com(sys.argv[2])
    Q1(com, edges, degree)
    Q2(com, edges, degree)
    Q3(com, edges, degree)