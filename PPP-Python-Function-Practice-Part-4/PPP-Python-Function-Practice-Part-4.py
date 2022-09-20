def max_num(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
        
    if(num2 > num1 and num2 > num3):
        return num2

    if(num3 > num1 and num3 > num2):
        return num3

#print(max_num(9,8,7))



def mult_list(number_list):
    print(number_list)
    result = 1
    for i in number_list:
        result = result * i
    
    return result

#print(mult_list([1,5,5,5]))



def rev_string(string):
    return string[::-1]

#print(rev_string("functest"))



def num_within(num, start, stop):
    result = False
    for i in range(start, stop):
        print(i, start, stop)
        if (i == num):
            result = True

    return result

#print(num_within(50,2,90))



triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate numbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)


pascal(5)