
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
   length = len(int_list)
   
   if None in int_list:
      raise ValueError()
   elif length <= 1:
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
   pass
