def mdc(a,b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a
class Fracao:
  denominador = 1
  numerador = 1

  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador

  def add(self, fracao):
    
    num = (fracao.denominador*self.numerador) \
+ (self.denominador*fracao.numerador)
    den = self.denominador * fracao.denominador
    return Fracao(num, den)

  def sub(self,fracao):
    num = (fracao.denominador*self.numerador) \
- (self.denominador*fracao.numerador)
    den = self.denominador * fracao.denominador
    return Fracao(num, den)

  def mul(self,fracao):
    num = (self.numerador * fracao.numerador)
    den = (self.denominador * fracao.denominador)
    return Fracao(num, den)
    
    
  def solve(self):
    return self.numerador/self.denominador
    
  def __str__(self ):
    return f"{self.numerador}/{self.denominador}"
    
  def simplify(self):
    if self.numerador == 0:
      return f"{int(self.numerador)}/{int(self.denominador)}"
    elif self.denominador == 0:
      return f"{self.numerador}"
    else:
      d = mdc(self.numerador,self.denominador)
      return f"{int(self.numerador//d)}/{int(self.denominador//d)}"
  
fracao1 = Fracao(10,5)
fracao2 = Fracao(9,7)
fracaoAdd = fracao1.add(fracao2)
fracaoSub = fracao1.sub(fracao2)
fracaoMul = fracao1.mul(fracao2)

print(f"fracao1 : {fracao1.simplify()}")
print(f"fracao2 : {fracao2.simplify()}")
print(f"Adição : {fracaoAdd.simplify()}")
print(f"Subtração : {fracaoSub.simplify()}")
print(f"Multiplicação : {fracaoMul.simplify()}")
