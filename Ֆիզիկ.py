print(
  '«Ֆիզիկ»-ը ծրագիր է նախատեսված ֆիզիկական խնդիրներ լուծելու համար:Այժմ ծրագիրը կարողանում է հաշվել v-ն,s-ը,t-ն,a-ն,U-ն,R-ը,I-ն,A-ն, և q-ն ինչպես նաև կարողանում է կմ/ժ վերածել մ/վ, կմ-ը մ-ի,կգ-ը գրամների:Ծրագիրը դեռ գտնվում է վերապատրաստման փուլում:'
)
while True:
  import math
  I = 0
  U = 0
  A = 0
  q = 0
  a = 0
  v = 0
  t = 0
  s = 0
  g = 10
  pi=3.141592653589783238

  j = input('Անհայտ')
  if j == ('a'):
    v = eval(input('V'))
    l = input('Միավոր')
    t = eval(input('T'))
    p = input('Միավոր')
    if l == ('կմ/ժ'):
      v = v / 3.6
    if p == ('ժ'):
      t = t * 60
    if v == 0:
      s = input('S')
      v = s / t
    if t == 0:
      s = input('S')
      t = math.sqrt(2 * s / g)
    print('A=', v / t)
  if j == ('s'):
    v = eval(input('V'))
    l = input('Միավոր')
    t = eval(input('T'))
    p = input('Միավոր')
    if l == ('կմ/ժ'):
      v = v / 3.6
    if p == ('ժ'):
      t = t * 60
    if v == 0:
      s = g * t**2 / 2
      print('S=', s)
      continue
    print('S=', v * t)

  
  if j == ('t'):
    v = eval(input('V'))
    l = input('Միավոր')
    s = eval(input('S'))
    k = input('Միավոր')
    if l == ('կմ/ժ'):
      v = v / 3.6
    if k == ('կմ'):
      s = s * 1000
    if s == 0:
      s = g * t**2 / 2
    if v == 0:
      a = input('a')
      v = a * t
    print('T=', s / v)

  if j == ('I'):
    q = eval(input('q'))
    T = eval(input('T'))
    print('I=', q / T)

  if j == ('q'):
    I = eval(input('I'))
    T = eval(input('T'))
    print('q=', I * T)

  if j == ('T'):
    q = eval(input('q'))
    I = eval(input('I'))
    print('T', q / I)

  if j == ('u'):
    A = eval(input('A'))
    q = eval(input('q'))
    if q == 0:
      I = eval(input('I'))
      T = eval(input('T'))
      q = I * T
    print('U=', A / q)

  if j == ('A'):
    U = eval(input('U'))
    q = eval(input('q'))
    if q == 0:
      I = eval(input('I'))
      T = eval(input('T'))
      q = I * T

    print('A=', U * q)

  if j == ('R'):
    U = eval(input('U'))
    I = eval(input('I'))
    print('R=', U / I)

  if j == ('p'):
    m = eval(input('m'))
    v = eval(input('v'))
    if m == 0 or v == 0:
      eval(input('F'))
      eval(input('t'))
      print('p=', f * t)
      continue
    print('p=', m * v)

 # if j == ('v'):
  #  m = eval(input('m'))
   # p = eval(input('p'))
    #print('v=', p / m)

  if j==('E'):
    print('Կինետիկ Էներգիա = E')
    print('Պոտենցիալ Էներգիա = e')
    energia=input('Անհայտ')
    if energia==('E'):
      m = eval(input('m'))
      v = eval(input('v'))
      print('E=',m*v**2/2)
    if energia ==('e'):
      k=eval(input('k'))
      x=eval(input('x'))
      print('E=',k*x**2/2)
      
  if j == ('v'):
    print('Արագությունից=v')
    print('Կինետիկ Էներգիաից=V')
    v=input('Անհայտ')
    if v==('v'):
      s = eval(input('S'))
      k = input('Միավոր(կմ/մ)')
      t = eval(input('T'))
      p = input('Միավոր(Ր/Ժ)')
      if k == ('կմ'):
        s = s * 1000
      if p == ('ժ'):
        t = t * 60
      if t == 0:
        t = math.sqrt(2 * s / g)
      if s == 0:
        s = g * t**2 / 2
      print('V=', s/t)
    if v==('V'):
      E=eval(input('E'))
      m=eval(input('m'))
      print('V=',math.sqrt(2*E/m))
      

    
