# try..except
try : 
  a = int(input('masukan nilai a: '))
  b = int(input('masukan nilai b: '))
  c = a / b
  print(f"{a} / {b} = {c}")

except ZeroDivisionError as e :
  print('Error : Tidak boleh bagi 0')

# try..except..finally
f = ''

try :
  f = open('contoh.txt', 'r')
  lines = f.readlines()
  for line in lines :
      print(line, end = '\n')
  
except IOError as e :
  print('Error : File Not Found Mate!')

finally :
  if f :
    f.close()