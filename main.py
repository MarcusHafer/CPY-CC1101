from cpc.cpc import *

# CircuitPython specific
#myspi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
#cs = DigitalInOut(board.D9)
#gdo0 = DigitalInOut(board.D10)



# CC1101(spi, cs, gdo0, baudrate, frequency, syncword, offset=0) #optional frequency offset in Hz

# SPI channel @ 80MHz
# CP: SPIDevice(spi, chip_select=None, *, baudrate=100000, polarity=0, phase=0, extra_clocks=0)
# MP: SPI.init(id, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))
sck = Pin(14) 	# serial clock
mosi = Pin(13)	# SPI data out (Master Out Slave In)
miso = Pin(14)	# SPI data in (Master In Slave Out)
gdo0 = Pin(10)	# GPIO Digital Out 0
cs = Pin(9)		# Chip Select

baudrate = 50000
frequency = 434400000
syncword = "666A"

myspi = SPI(1, baudrate=50000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso) # HSPI

# CC1101(spi, cs, gdo0, baudrate, frequency, syncword, offset=0)
#rx = CC1101(myspi, cs, gdo0, 50000, 434400000, "666A")
rx = CC1101(myspi, cs, gdo0, baudrate, frequency, syncword)

rx.setupRX()

while True:
	rx.receiveData(0x19)
