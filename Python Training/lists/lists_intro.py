# # create a list

# #first_list = ['0', '1', '2', '3', '4', '5']
# first_list = [0,1,2,3,4,5]

# # access second element
# print(first_list[1])
# # access last element using negative variable
# print(first_list[-1])

# # sublisting using slicing
# print(first_list[1:4])
# print(len(first_list))
# print(sum(first_list))

# for i in first_list:
#     print(i)

# second_list = [i ** 2 for i in range(6)]

# print(second_list)

def logging_decorator(original_function):
  def wrapper(*args, **kwargs):
    print(f"[LOG] Calling {original_function.__name__} with args={args}, kwargs={kwargs}")
    result = original_function(*args, **kwargs)
    print(f"[LOG] {original_function.__name__} returned {result}")
    return result
  return wrapper

@logging_decorator
def my_function(a, b):
  return a + b

# Usage
my_function(11, 13)
