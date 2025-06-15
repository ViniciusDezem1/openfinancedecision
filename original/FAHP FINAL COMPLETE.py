# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:20:24 2023

@author: vinic
"""

# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset

print ("integration juddgment")
dataset = list([
    [ ( 1,   1,   1), ( 1/1,   1/2,   1/3)], #g1
    [ ( 1,   2,   3), ( 1,   1,   1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
# Costs of technological solutions judgment 


# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset

print ("costs x flexible solutions juddgment")
dataset = list([
    [ ( 1,   1,   1), ( 1/1,   1/2,   1/3)], #g1
    [ ( 1,   2,   3), ( 1,   1,   1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
  
  
# Relationship subdimensions judgment 



print ("Relationship subdimensions judgment")

# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset

print ("Institutional image x Perfomance x Customer at the centre juddgments")
dataset = list([
    [ ( 1, 1, 1), ( 2, 3, 4), (1/3, 1/4, 1/5)], #g1
    [ ( 1/2, 1/3, 1/4), ( 1, 1, 1), (1/4, 1/5, 1/6)], #g2
    [ ( 3, 4, 5), ( 4, 5, 6), ( 1, 1, 1)],#g3
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')


# Institutional Image Judgments

print ("Institutional Image Judgments")


# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ ( 1,   1,   1), ( 2, 3, 4)], #g1
    [ ( 1/2, 1/3, 1/4), ( 1, 1, 1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
  
# Performance Judgments

print ("Performance  Image Judgments")



# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ ( 1,   1,   1), ( 2, 3, 4)], #g1
    [ ( 1/2, 1/3, 1/4), ( 1, 1, 1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
  
  # Customer at the centre
  

  print ("Customer at the centre")
  
# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset
dataset = list([
    [ (  1,   1,   1),   (  1,   2,   3), (  2,   3,   4), (  2,   3,   4),  ( 1/2, 1/3, 1/4), (  2,   3,   4), (  1/2, 1/3, 1/4), (  2,   3,   4) ], #g1
    [ (  1/1, 1/2, 1/3), (  1,   1,   1), ( 1/2, 1/3, 1/4),( 1/1, 1/2, 1/3), ( 1/2, 1/3, 1/4), (  2,   3,   4), (  1/2, 1/3, 1/4), (  2,   3,   4) ], #g2
    [ (  1/2, 1/3, 1/4), (  2,   3,   4), (  1,   1,   1), ( 1/1, 1/2, 1/3), ( 1/2, 1/3, 1/4), (  2,   3,   4), (  1/3, 1/4, 1/5), (  2,   3,   4) ], #g3
    [ (  1/2, 1/3, 1/4), (  1,   2,   3), (  1,   2,   3), (  1,   1,   1),  ( 1/2, 1/3, 1/4), (  2,   3,   4), (  1/2, 1/3, 1/4), (  2,   3,   4) ], #g4
    [ (  2,   3,   4),   (  2,   3,   4), (  2,   3,   4), (  2,   3,   4),  (  1,   1,   1),  (  2,   3,   4), (  1/1, 1/2, 1/3), (  3,   4,   5) ], #G5
    [ (  1/2, 1/3, 1/4), ( 1/2, 1/3, 1/4),( 1/2, 1/3, 1/4),( 1/2, 1/3, 1/4), ( 1/2, 1/3, 1/4), (  1,   1,   1), (  1/2, 1/3, 1/4), (  2,   3,   4) ], #G6
    [ (  1,   2,   3),   (  2,   3,   4), (  3,   4,   5), (  2,   3,   4),  (  1,   2,   3),  (  2,   3,   4), (  1,   1,   1),   (  3,   4,   5) ], #G7
    [ (  1/2, 1/3, 1/4), ( 1/2, 1/3, 1/4),( 1/2, 1/3, 1/4),( 1/2, 1/3, 1/4), (1/3, 1/4, 1/5),  (1/3, 1/4, 1/5), (  1/3, 1/4, 1/5), (  1,   1,   1) ], #G8
    ],)
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
# Marketplace subdimensions judgment 



print ("Marketplace judgment")

# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset

print ("Available x Personalization x Products distributor juddgments")
dataset = list([
    [ ( 1,   1,   1), ( 1/2, 1/3, 1/4),(1/3, 1/4, 1/5)], #g1
    [ ( 2,   3,   4), ( 1,   1,   1),  (1/3, 1/4, 1/5)], #g2
    [ ( 3,   4,   5), ( 3,   4,   5),  ( 1,   1,   1)],#g3
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')

  

# Data sub dimensions Judgments

print ("Data sub dimensions Image Judgments")



# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ ( 1,   1,   1), (  1/2, 1/3, 1/4)], #g1
    [ ( 2, 3, 4), ( 1, 1, 1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  
  
  # Exploration judgment 



  print ("Exploration judgment")

  # Required Libraries
  import numpy as np

  # Fuzzy AHP 
  from pyDecision.algorithm import fuzzy_ahp_method
  # Fuzzy AHP

  # Dataset

  print ("Transactional data x Non transactional data x Data collection juddgments")
  dataset = list([
      [ ( 1,   1,   1), ( 1/2, 1/3, 1/4),( 1/2, 1/3, 1/4)], #g1
      [ ( 2,   3,   4), ( 1,   1,   1),  ( 1/2, 1/3, 1/4)], #g2
      [ ( 2,   3,   4), ( 2,   3,   4),  ( 1,   1,   1)], #g3
      ])
  # Call Fuzzy AHP Function        
  fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

  for i in range(0, len(fuzzy_weights)):
    print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
    # Crisp Weigths
  for i in range(0, len(defuzzified_weights)):
    print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
    
  for i in range(0, len(normalized_weights)):
    print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
    # Consistency Ratio
  print('RC: ' + str(round(rc, 2)))
  if (rc > 0.10):
    print('The solution is inconsistent, the pairwise comparisons must be reviewed')
  else:
    print('The solution is consistent')


# Regulatory Judgments

print ("Regulatory Judgments")



# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ ( 1,   1,   1), (  1/2, 1/3, 1/4)], #g1
    [ ( 2, 3, 4), ( 1, 1, 1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
 
  
  # Ecossystem Judgments


  print ("Ecossystem Judgments")


  # Required Libraries
  import numpy as np

  # Fuzzy AHP 
  from pyDecision.algorithm import fuzzy_ahp_method
  # Fuzzy AHP

  # Dataset


  dataset = list([
      [ ( 1,   1,   1), ( 1/2, 1/3, 1/4)], #g2
      [ ( 2, 3, 4), ( 1, 1, 1)], #g1
      ])
  # Call Fuzzy AHP Function        
  fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

  for i in range(0, len(fuzzy_weights)):
    print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
    # Crisp Weigths
  for i in range(0, len(defuzzified_weights)):
    print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
    
  for i in range(0, len(normalized_weights)):
    print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
    # Consistency Ratio
  print('RC: ' + str(round(rc, 2)))
  if (rc > 0.10):
    print('The solution is inconsistent, the pairwise comparisons must be reviewed')
  else:
    print('The solution is consistent')
    
    
  
   
# Performance Judgments

print ("Product subdimensions Judgments")



# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ ( 1,   1,   1), ( 2, 3, 4)], #g1
    [ ( 1/2, 1/3, 1/4), ( 1, 1, 1)], #g2
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  


# Variety Judgments

print ("Variety Judgments")



# Required Libraries
import numpy as np

# Fuzzy AHP 
from pyDecision.algorithm import fuzzy_ahp_method
# Fuzzy AHP

# Dataset


dataset = list([
    [ (   1,   1,   1), (  2,  3,  4), (  3,  4,  5), (  1,   2,   3)],#g1
    [ ( 1/2, 1/3, 1/4), (  1,  1,  1), (  1,  2,  3), (1/2, 1/3, 1/4)],#g2
    [ ( 1/3, 1/4, 1/5), (1/1,1/2,1/3), (  1,  1,  1), (  2,   3,   4)],#g3
    [ ( 1/2, 1/3, 1/4), (  2,  3,  4), (1/2,1/3,1/4), (  1,   1,   1)],#g4
    ])
# Call Fuzzy AHP Function        
fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

for i in range(0, len(fuzzy_weights)):
  print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
  # Crisp Weigths
for i in range(0, len(defuzzified_weights)):
  print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
  
for i in range(0, len(normalized_weights)):
  print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
  # Consistency Ratio
print('RC: ' + str(round(rc, 2)))
if (rc > 0.10):
  print('The solution is inconsistent, the pairwise comparisons must be reviewed')
else:
  print('The solution is consistent')
  
  # Prices Policy Judgments


  print ("Prices Policy Judgments")


  # Required Libraries
  import numpy as np

  # Fuzzy AHP 
  from pyDecision.algorithm import fuzzy_ahp_method
  # Fuzzy AHP

  # Dataset


  dataset = list([
      [ ( 1,   1,   1), ( 1/2, 1/3, 1/4)], #g2
      [ ( 2, 3, 4), ( 1, 1, 1)], #g1
      ])
  # Call Fuzzy AHP Function        
  fuzzy_weights, defuzzified_weights, normalized_weights, rc = fuzzy_ahp_method(dataset)

  for i in range(0, len(fuzzy_weights)):
    print('g'+str(i+1)+': ', np.around(fuzzy_weights[i], 3))
    # Crisp Weigths
  for i in range(0, len(defuzzified_weights)):
    print('g'+str(i+1)+': ', round(defuzzified_weights[i], 3))
    
  for i in range(0, len(normalized_weights)):
    print('g'+str(i+1)+': ', round(normalized_weights[i], 3))
    # Consistency Ratio
  print('RC: ' + str(round(rc, 2)))
  if (rc > 0.10):
    print('The solution is inconsistent, the pairwise comparisons must be reviewed')
  else:
    print('The solution is consistent')
    