""" Author = Romain Bervoets"""
def bornes(nombres):
   max = nombres[0]
   min = nombres[0]
   for i in nombres:
       if i > max:
           max = i
       if i < min:
           min = i
   return(min, max)
