#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:46:49 2021

@author: james
"""

#VOTING SIMULATION (PARADOX DETECTION)
import numpy as np
from random import seed
from random import gauss


counter = 0
fpp_counter = 0
conwin = 0
labwin = 0
ldwin = 0
greenwin = 0
z = input('[PROGRAMME 1] Number of runs to complete = ')
for i in range(int(z)): 
    seed(seed(3*i))




    A = np.empty(17)
    
    P0 = abs(gauss(0.5, 1)) #GO OVER STANDRAD DEVIATIONS
    P1 = abs(gauss(1.5, 3))
    P2 = abs(gauss(1, 1))
    P3 = abs(gauss(6, 6))
    P4 = abs(gauss(14, 14))
    P5 = abs(gauss(12, 12))
    P6 = abs(gauss(16, 16))
    P7 = abs(gauss(10, 10))
    P8 = abs(gauss(5, 5))
    P9 = abs(gauss(5, 5))
    P10 = abs(gauss(8, 8))
    P11 = abs(gauss(8, 8))
    P12 = abs(gauss(2, 2))
    P13 = abs(gauss(1, 2))    
    P14 = abs(gauss(3, 3))
    P15 = abs(gauss(3, 3))
    P16 = abs(gauss(4, 4))
    A[0] = P0
    A[1] = P1
    A[2] = P2
    A[3] = P3
    A[4] = P4
    A[5] = P5
    A[6] = P6
    A[7] = P7
    A[8] = P8
    A[9] = P9
    A[10] = P10
    A[11] = P11
    A[12] = P12
    A[13] = P13
    A[14] = P14
    A[15] = P15
    A[16] = P16
    
    
    B = np.empty(17)
    
    for i in range(17):
        B[i] = (A[i]/sum(A))*100
   # print(A)    
   # print(sum(A))
    #print(B)
    #print(sum(B))
    
    for i in range(len(B)):
        if B[i] == max(B):
            if i == 0 or i == 1 or i == 2:
                winner = 'Green'
                greenwin += 1
                #print('The Green Party win using first past the post.')
            if i == 3 or i == 4 or i == 5 or i == 6:
                winner = 'Con'
                conwin += 1
                #print('The Tories win using first past the post.')
            if i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
                winner = 'Lab'
                labwin += 1
                #print('The Labour Party win using first past the post.')
            if i == 12 or i == 13 or i == 14 or i == 15 or i == 16:
                winner = 'LD'
                ldwin += 1
                #print('The Lib Dems win using first past the post.')
    C = np.zeros(12)
    
    g_to_l = B[0] + B[1] + B[3] + B[5] + B[13]
    C[0] = g_to_l
    g_to_ld = B[0] + B[1] + B[2] + B[3] + B[7] + B[8]
    C[1] = g_to_ld
    c_to_l = B[3] + B[4] + B[5] + B[6] + B[9]
    C[2] = c_to_l 
    c_to_ld = B[0] + B[3] + B[4] + B[5] + B[6] + B[8] + B[9]
    C[3] = c_to_ld
    c_to_g = B[3] + B[4] + B[5] + B[6] + B[8] + B[9] + B[11] + B[13] + B[14] + B[16]
    C[4] = c_to_g
    l_to_g = B[3] + B[4] + B[6] + B[7] + B[8] + B[9] + B[10] + B[11] + B[14] + B[15] + B[16]
    C[5] = l_to_g
    l_to_c = B[0] + B[1] + B[2] + B[7] + B[8] + B[9] + B[10] + B[11] + B[12] + B[15] + B[16]
    C[6] = l_to_c
    l_to_ld = B[0] + B[1] + B[3] + B[4] + B[7] + B[8] + B[9] + B[10] + B[11] 
    C[7] = l_to_ld
    ld_to_g = B[4] + B[5] + B[6] + B[9]+ B[10] + B[11] + B[12] + B[13] + B[14] + B[15] + B[16]
    C[8] = ld_to_g
    ld_to_c = B[1] + B[2] + B[7] + B[10] +B[11] + B[12] + B[13] + B[14] + B[15] + B[16]
    C[9] = ld_to_c 
    ld_to_l = B[5] + B[6] + B[12] + B[13] + B[14] + B[15] + B[16]
    C[10] = ld_to_l
    g_to_c = B[0] + B[1] + B[2] + B[7] + B[10] + B[12] + B[15]
    C[11] = g_to_c
    
    
    
    
    #print(C)
    
    
    #for i in range(11):
           # if C[i] > 50.0:
               # counter += 1
              #  print('The majority was the', i, 'th member of the list')
             
            #GREEN LABOUR LIB DEM
            
    if C[0] > 50.0 and C[7] > 50.0 and C[8] > 50.0:
                #print('There was a condorcet cycle of length 3 where green was preferred to labour, labour was preferred')
                #print('to lib dems and lib dems were preferred to green')
                counter += 1
                if winner == 'Green' or winner == 'Lab' or winner == "LD":
                    fpp_counter += 1
                    
            #GREEN LIB DEM CON
            
    if C[1] > 50.0 and C[9] > 50.0 and C[4] > 50.0:
                #print('Condorcet of cycle length 3, green is preferred to lib dems, lib dems are preferred to con and con preferred to green')
                counter += 1
                if winner == 'Green' or winner == 'Con' or winner == "LD":
                    fpp_counter += 1
            #GREEN LABOUR CON
            
    if C[0] > 50.0 and C[6] > 50.0 and C[4] > 50.0:
                #print('Condorcet cycle of length 3: green preferred to labour, labour preferred to con, con preferred to green')
                counter += 1
                if winner == 'Green' or winner == 'Lab' or winner == "Con":
                    fpp_counter += 1
            #GREEN LIB DEM LABOUR
            
    if C[1] > 50.0 and C[10] > 50.0 and C[5] > 50.0:
                #print('Condorcet cycle of length 3: green preferred to lib dem, lib dem to labour and labour preferred to green' )
                counter += 1
                if winner == 'Green' or winner == 'Lab' or winner == "LD":
                    fpp_counter += 1
            #GREEN CON LIB DEM
            
    if C[11] > 50.0 and C[3] > 50.0 and C[8] > 50.0:
                #print('Condorcet cycle of length 3: green is preferred to con, con to lib dem, lib dem to green')
                counter += 1
                if winner == 'Green' or winner == 'Con' or winner == "LD":
                    fpp_counter += 1
            #GREEN CON LABOUR 
            
    if C[11] > 50.0 and C[2] > 50.0 and C[5] > 50.0:
                #print('Condorcet cycle of length 3: green is preferred to con, con to labour and labour to green' )
                counter += 1
                if winner == 'Green' or winner == 'Con' or winner == "Lab":
                    fpp_counter += 1
            #LABOUR GREEN CON
            
    #if C[5] > 50.0 and C[11] > 50.0 and C[2] > 50.0:
               # print('Condorcet cycle of length 3: labour is preferred to green, green to con and con to labour')
            
            #LABOUR CON GREEN
            
    #if C[6] > 50.0 and C[4] > 50.0 and C[0] > 50.0:
                #print('Condorcet cycle of length 3: labour preferred to con, con to green and green to labour')
            
            #LABOUR LIB DEM CON
            
    if C[7] > 50.0 and C[9] > 50.0 and C[2] > 50.0:
                #print('Condorcet cycle of length 3: labour preferred to lib dem, lib dem preferred to con, con to labour')
                counter += 1
                if winner == 'Con' or winner == 'Lab' or winner == "LD":
                    fpp_counter += 1
            #LABOUR  LIB DEM GREEN
            
    #if C[7] > 50.0 and C[8] > 50.0 and C[0] > 50.0:
                #print('Condorcet cycle of length 3: labour preferred to lib dem, lib dem preferred to green and green to labour' )
            
            #LABOUR CON LIB DEM
            
    if C[6] > 50.0 and C[3] > 50.0 and C[10] > 50.0:
                #print('Condorcet cycle of length 3: labour preferred to con, con to lib dem, lib dem to labour')
                counter += 1
                if winner == 'Con' or winner == 'Lab' or winner == "LD":
                    fpp_counter += 1
            #LABOUR GREEN LIB DEM
            
    #if C[5] > 50.0 and C[1] > 50.0 and C[10] > 50.0:
               # print('Condorcet cycle of length 3: labour preferred to green, green to lib dem, lib dem to labour')
                
            #CON LABOUR LIB DEM
            
    #if C[2] > 50.0 and C[7] > 50.0 and C[9] > 50.0:
               # print('Condorcet cycle of length 3: con preferred to lab, lab to lib dem, lib dem to con')
            
            #CON LABOUR GREEN
            
    #if C[2] > 50.0 and C[5] > 50.0 and C[11] > 50.0:
               # print('Condorcet cycle of length 3: con preferred to lab, lab to green, green to con')
                
            #CON GREEN LABOUR
            
    #if C[4] > 50.0 and C[0] > 50.0 and C[6] > 50.0:
                #print('Condorcet cycle of length 3: con preferred to green, green to lab, lab to con')
                
            #CON GREEN LIB DEM
            
    #if C[4] > 50.0 and C[1] > 50.0 and C[9] > 50.0:
                #print('COndorcet cycle of length 3: con to green, green to lib dem, lib dem to con')
                
            #CON LIB DEM LABOUR
            
    #if C[3] > 50.0 and C[10] > 50.0 and C[6] > 50.0:
                #print('Condorcet cycle of length 3: con to lib dem, lib dem to lab, lab to con')
                
            #CON LIB DEM GREEN
            
    #if C[3] > 50.0 and C[8] > 50.0 and C[11] > 50.0:
                #print('Condorcet cycle of length 3: con preferred to lib dems, lib dems to green, green to con')
            
            #LIB DEM GREEN CON
            
    #if C[8] > 50.0 and C[11] > 50.0 and C[3] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to green, green to con, con to lib dem')
                
            #LIB DEM GREEN LABOUR
            
    #if C[8] > 50.0 and C[0] > 50.0 and C[7] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to green, green to lab, lab to lib dem')
                
            #LIB DEM LABOUR CON
            
    #if C[10] > 50.0 and C[6] > 50.0 and C[3] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to labour, labour to con, con to lib dem')
                
            #LIB DEM LABOUR GREEN
            
    #if C[10] > 50.0 and C[5] > 50.0 and C[1] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to labour, labour to green, green to lib dems')
                
            #LIB DEM CON GREEN
            
    #if C[9] > 50.0 and C[4] > 50.0 and C[1] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to con, con preferred to green, green preferred to lib dem')
                
            #LIB DEM CON LABOUR
            
    #if C[9] > 50.0 and C[2] > 50.0 and C[7] > 50.0:
                #print('Condorcet cycle of length 3: lib dem preferred to con, con to lab, lab to lib dem')
                
                
print('[PROGRAMME 1] The number of condorcet cycles of length 3 from', str(z) , 'runs through =', counter) 
print('[PROGRAMME 1] Hence the probability of a condorcet cycle of length 3 is =', ((100*counter)/int(z)), '%')     
print('[PROGRAMME 1] Out of', str(counter), 'Condorcet cycles, there were', fpp_counter, 'cycles containing the winner of the election')         
print('[PROGRAMME 1] Hence the probability of a condorcet cycle of length 3 containing the leader is=', ((100*fpp_counter)/int(z)), '%')                
print('Con win =', str((conwin/int(z))), ', Lab win=', str((labwin/int(z))), ', Green win=', str((greenwin/int(z))), ', Lib dems win=', str((ldwin/int(z))))               
                
                
                
    #if counter > 2:
    #   print('There is a condorcet cycle')   




###NOW WE TRY TO DO THE ALTERNATE VOTE

#D = np.zeros(17)

#for i in range(17):
   # D[i] = (B[i] * z)
    
#for i in range(len(D)):
        #if (D[i]/sum(D)) > 0.5:
         #   if i == 0 or i == 1 or i == 2:
           #     winner = 'Green'
                #print('The Green Party win using first past the post.')
          #  if i == 3 or i == 4 or i == 5 or i == 6:
           #     winner = 'Con'
           #     #print('The Tories win using first past the post.')
           # if i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
             #   winner = 'Lab'
            #    #print('The Labour Party win using first past the post.')
           # if i == 12 or i == 13 or i == 14 or i == 15 or i == 16:
           #     winner = 'LD'
                
       # else: 
         #   for i in range(17):
           #     if D[i] = min(D):
             #       storage = D[i]
            #        D[i] = 0
                    
                   # if i == 0 or i == 1 or i == 2:
                        
                        #print('The Green Party win using first past the post.')
                  #  if i == 3 or i == 4 or i == 5 or i == 6:
                  #      winner = 'Con'
                    #print('The Tories win using first past the post.')
                  #  if i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
                      #  winner = 'Lab'
                    #print('The Labour Party win using first past the post.')
                  #  if i == 12 or i == 13 or i == 14 or i == 15 or i == 16:
                   #     winner = 'LD'
                    
                

                 
            
    
    
    
    
    
    
    
