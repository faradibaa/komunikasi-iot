import minimalmodbus
import serial
from apscheduler.schedulers.background import BackgroundScheduler

class Modbus():
	
	PH_REG = 0x6 #1 length
	MOIS_REG = 0x12
	TEMP_REG = 0x13
	COND_REG = 0x15
	NITR_REG = 0x1E
	PHOS_REG = 0x1F
	POTS_REG = 0x20

	def __init__(self):
		self.is_connected = False
		self.instrument = None
		self.connect()
		self.scheduler = BackgroundScheduler(daemon=True)
		self.scheduler.add_job(self.connect, 'interval', seconds=10, id="connect")
		self.scheduler.start()

	def connect(self):
		try:
			if self.is_connected == False or self.instrument == None:
				instrument = minimalmodbus.Instrument('COM3',1,mode=minimalmodbus.MODE_RTU)

				instrument.serial.baudrate              = 9600
				instrument.serial.bytesize              = 8
				instrument.serial.parity                = minimalmodbus.serial.PARITY_EVEN
				instrument.serial.stopbits              = 1
				instrument.serial.timeout               = 1
				instrument.address                      = 1 
				instrument.mode                         = minimalmodbus.MODE_RTU 
				instrument.close_port_after_each_call   = True
				instrument.clear_buffers_before_each_transaction = True
				
				self.instrument = instrument
				self.is_connected = True
		
		except:
			self.is_connected = False
			self.instrument = None

modbus = Modbus()

#contoh membaca nilai ph
addr_reg_ph = modbus.PH_REG
result_ph = modbus.instrument.read_register(addr_reg_ph, 2)

#membaca nilai moisture
addr_reg_moisture = modbus.MOIS_REG
result_moisture = modbus.instrument.read_register(addr_reg_moisture, 2)

#membaca nilai temperature
addr_reg_temp = modbus.TEMP_REG
result_temp = modbus.instrument.read_register(addr_reg_temp, 2)

#membaca nilai conductivity
addr_reg_conductivity = modbus.COND_REG
result_conductivity = modbus.instrument.read_register(addr_reg_conductivity, 2)

#membaca nilai nitrogen
addr_reg_nitrogen = modbus.NITR_REG
result_nitrogen = modbus.instrument.read_register(addr_reg_nitrogen, 2)

#membaca nilai fosfor
addr_reg_phosphorus = modbus.PHOS_REG
result_phosphorus = modbus.instrument.read_register(addr_reg_phosphorus, 2)

#membaca nilai potasium
addr_reg_potassium = modbus.POTS_REG
result_potassium = modbus.instrument.read_register(addr_reg_potassium, 2)

print("Nilai PH: ", result_ph)
print("Nilai kelembaban tanah: ", result_moisture)
print("Nilai suhu: ", result_temp)
print("Nilai konduktivitas: ", result_conductivity)
print("Nilai nitrogen: ", result_nitrogen)
print("Nilai fosfor: ", result_phosphorus)
print("Nilai potassium: ", result_potassium)