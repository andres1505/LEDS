from machine import Pin as Pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[2,15,16,17,5,18,19,3,1,22]

toditicos=[]
for i in puerto:
 
  toditicos.append (Pin(i,Pin.OUT))  

print (toditicos)
inicial=1
final=5
def derecha(inicio,fin):
  for i in toditicos[inicio:fin]:
    for j in range (2):
      i.value(not i.value())
    pausam(150)
def izquierda(inicio,fin):
  for i in reversed (toditicos[inicio:fin]):
    for j in range(2):
      i.value(not i.value())
    pausam(150)
inicial-=1
print (final)
while True:
  derecha(inicial,final)
  izquierda(inicial,final)