# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:40:27 2022

@author: Dom
"""
import numpy as np
import random


def matrixgraph_from_edges(filename):

  
  graph={}
  file = open(filename, "r") 
  for line in file:  
     w = line.split()
     
    
     if w[0] not in graph:
        graph[w[0]] = []
     if w[1] not in graph:
        graph[w[1]]= []
     if w[1] not in graph[w[0]]:
        graph[w[0]].append(w[1])
     if w[0] not in graph[w[1]]:
        graph[w[1]].append(w[0])
   
  file.close()

  n = len(graph)
  matrixgraph = np.zeros((n,n))
  vertices = []
  for v in graph.keys():
     vertices.append(v)
  verticesdict = {vertices[i]: i for i in range(n)}

  for v in graph.keys():   
     for u in graph[v]:
        matrixgraph[verticesdict[v],verticesdict[u]]=1
        
  
    
  return  graph, matrixgraph, vertices


class Scientists:
    def __init__(self, graph, matrix, vertices):
        self.graph = graph 
        self.matrix = matrix
        self.vertices = vertices
        
        
class PerfectTeam:
    def __init__(self, scientists, l_losowan):
       n = len(scientists.vertices) 
       self.team = []        
       for i in range(l_losowan):
           first = scientists.vertices[random.randint(0,n-1)]
           while len(scientists.graph[first]) >= 7:
              first = scientists.vertices[random.randint(0,n-1)]
          
           verts = scientists.vertices[:]
           team = []
           team.append(first)
           verts.remove(first)
           for v in scientists.graph[first]:
              if v in verts:
                 verts.remove(v)
           while verts:
              m = len(verts)
              w = verts[random.randint(0,m-1)]
              verts.remove(w)
              for v in scientists.graph[w]:
                 if v in verts:
                    verts.remove(v)
              team.append(w)
           if len(team)>len(self.team):
               self.team = team
               self.possiblevertices = verts
      

    def mutate(self, scientists, ind):
        self.previousteam = self.team
        n = len(self.team)
        verts = self.possiblevertices[:]
        w = self.team[ind]
        self.team.remove(w)
        coauthors = False
        for v in scientists.graph[w]:
              ind_v = scientists.vertices.index(v)
              for i in range(len(self.team)):            
                  ind_i = scientists.vertices.index(self.team[i])
                  if scientists.matrix[ind_v][ind_i]==1:
                     coauthors = True
                     break
              if coauthors == False:
                 verts.append(w)
        while verts:
           n = len(verts)
           w = verts[random.randint(0,n-1)]
           self.team.append(w)
           verts.remove(w)
           for v in scientists.graph[w]:
               if v in verts:
                  verts.remove(v)
        
               
           
             
    def reverse_mutation(self):
         self.team = self.previousteam
         
         
    def ILS(self, scientists, N, m):
        
        war_stop = 1000
        
        while war_stop >= m:
           iterations = 0
           before_value = len(self.team)
           current_value = len(self.team)
          
           while(iterations<N):
              iterations = iterations + 1
              inds = [i for i in range(len(self.team))]
              r = random.choice(inds)
              self.mutate(scientists,r)
              new_value = len(self.team)
              if(new_value >= current_value):
                 current_value = new_value
              else:
                 self.reverse_mutation()
               
           war_stop = current_value - before_value   
               
        
        
        
        
for i in range(1):        
  G, M, vertices = matrixgraph_from_edges('naukowcy.txt')     
  S = Scientists(G, M, vertices) 
  Rozw = PerfectTeam(S, 80)
  Rozw.ILS(S, 30, 1)
  print(len(Rozw.team))
        
    
        
        
        
        
  


