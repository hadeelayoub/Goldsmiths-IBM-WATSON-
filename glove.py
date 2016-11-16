from gpiozero import MCP3008
pot = MCP3008(0)
pot1 = MCP3008(1)
pot2 = MCP3008(2)
pot3 = MCP3008(3)
pot4 = MCP3008(4)

while True:
    print(pot.value, pot1.value, pot2.value, pot3.value, pot4.value)
    
    
