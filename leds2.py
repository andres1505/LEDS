from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

leda=pin(2, pin.OUT)
ledb=pin(15, pin.OUT)
ledc=pin(16, pin.OUT)
ledd=pin(17, pin.OUT)
lede=pin(5, pin.OUT)
ledf=pin(18, pin.OUT)
ledg=pin(19, pin.OUT)
ledh=pin(3, pin.OUT)
ledi=pin(1, pin.OUT)
ledj=pin(22, pin.OUT)

def print_led(a,b,c,d,e,f,g,h,i,j):
  leda.value(a)
  ledb.value(b)
  ledc.value(c)
  ledd.value(d)
  lede.value(e)
  ledf.value(f)
  ledg.value(g)
  ledh.value(h)
  ledi.value(i)
  ledj.value(j) 
  pausam(200)
while True:
  print_led(0,0,0,0,0,0,0,0,0,0)
  print_led(0,0,0,0,0,0,0,0,0,1)
  print_led(0,0,0,0,0,0,0,0,1,0)
  print_led(0,0,0,0,0,0,0,1,0,0)
  print_led(0,0,0,0,0,0,1,0,0,0)
  print_led(0,0,0,0,0,1,0,0,0,0)
  print_led(0,0,0,0,1,0,0,0,0,0)
  print_led(0,0,0,1,0,0,0,0,0,0)
  print_led(0,0,1,0,0,0,0,0,0,0)
  print_led(0,1,0,0,0,0,0,0,0,0)
  print_led(1,0,0,0,0,0,0,0,0,0)