from picozero import DigitalLED
from time import sleep


def allOff():
    p15.off()
    p16.off()
    p17.off()
    p18.off()
    p19.off()
    p20.off()
    p21.off()
    p22.off()
    
#setup output pins
p15 = DigitalLED(15,True,False)
p16 = DigitalLED(16,True,False)
p17 = DigitalLED(17,True,False)
p18 = DigitalLED(18,True,False)
p19 = DigitalLED(19,True,False)
p20 = DigitalLED(20,True,False)
p21 = DigitalLED(21,True,False)
p22 = DigitalLED(22,True,False)

def runString(bString):
    print ("Checking Binary String")
    if bString[0] == 1:
        p15.on()
    if bString[1] == 1:
        p16.on()
    if bString[2] == 1:
        p17.on()
    if bString[3] == 1:
        p18.on()
    if bString[4] == 1:
        p19.on()
    if bString[5] == 1:
        p20.on()
    if bString[6] == 1:
        p21.on()
    if bString[7] == 1:
        p22.on()

def validatebString(bString):
    sleep(1)
    print (len(bString))
    if len(bString) != 8:
        print ("Binary String Failed checks")
        sleep(2)
        if len(bString) < 8:
            print ("String is too short, check again")
        else:
            print ("String is too long, check again")
    else:
        print ("Binary String passed checks")
        

allOff()

def assembly_input():
    mnemonic = input("mnemonic: ")
    chip = input("chip: ")
    addr = input("Address: ")
    print (f"\n{mnemonic} {chip} {addr} \n")
    ic = [0,0,0,0]
    ic = instructionCode(mnemonic)
    
    if chip == "1":
        chipPin = [1]
    else:
        chipPin = [0]
    
    addrPins = [0,0,0]
    
    if addr == "001":
        addrPins = [0,0,1]
    elif addr == "010":
        addrPins = [0,1,0]
    elif addr == "011":
        addrPins = [0,1,1]
    elif addr == "011":
        addrPins = [0,1,1]
    elif addr == "100":
        addrPins = [1,0,0]
    elif addr == "101":
        addrPins = [1,0,1]
    elif addr == "111":
        addrPins = [1,1,1]
    
#     print (ic)
#     print (chipPin)
#     print (addrPins)
    
    bString = ic + chipPin + addrPins
    print (bString)
    runString(bString)

def instructionCode(mnemonic):
    if mnemonic == "NOPO":
        ic = [0,0,0,0]
    elif mnemonic == "NOPF":
        ic = [1,1,1,1]
    elif mnemonic == "LD":
        ic = [0,0,0,1]
    elif mnemonic == "LDC":
        ic = [0,0,1,0]
    elif mnemonic == "AND":
        ic = [0,0,1,1]
    elif mnemonic == "ANDC":
        ic = [0,1,0,0]
    elif mnemonic == "OR":
        ic = [0,1,0,1]
    elif mnemonic == "ORC":
        ic = [0,1,1,0]
    elif mnemonic == "XNOR":
        ic = [0,1,1,1]
    elif mnemonic == "STO":
        ic = [1,0,0,0]
    elif mnemonic == "IEN":
        ic = [1,0,0,1]
    elif mnemonic == "OEN":
        ic = [1,0,1,1]
    elif mnemonic == "JMP":
        ic = [1,1,0,0]
    elif mnemonic == "RTN":
        ic = [1,1,0,1]
    elif mnemonic == "SKZ":
        ic = [1,1,1,0]    
    return ic
        

while True:
    assembly_input()
    var = input("Press Enter once WORD is saved")
    
    
