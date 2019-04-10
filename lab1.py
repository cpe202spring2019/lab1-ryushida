
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   if int_list is None:
      raise ValueError()
      return None
   elif len(int_list) == 0:
      return None
   else:
      maxvalue = 0
      for num in int_list:
         if num > maxvalue:
            maxvalue = num
      return maxvalue
         
   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   
   if int_list is None:
      raise ValueError()
   else:
      length = len(int_list)
      if length <= 1:
         return int_list
      else:
         tmp = int_list[:length-1]
         #print(tmp)
         first = int_list[length-1]
         return [first] + reverse_rec(tmp)
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   if int_list is None:
      raise ValueError()
   elif high > low:
      # Get index of middle of list (round down)
      middle = int((low + high)/2)
      if target == int_list[middle]:
         return middle
      # If target is larger than the middle item
      elif target > int_list[middle]:
         # Do binary search with 2nd half of list
         return bin_search(target, middle+1, high, int_list)
      else:
         # Do binary search with 1st half of list
         return bin_search(target, low, middle-1, int_list)
   else:
      return None
   pass
