a  = 1
b  = 1.3
c  =  "ssss" #single quotes also
d =  bytearray([1])
e  = memoryview(d)
f = True

print(f"""type of  a: {type(a)}  type of b :  
      {type(b)} type of c: {type(c)}
      type of d: {type(d)} type of e:  {type(e)}
type of f : {type(f)}
""")

