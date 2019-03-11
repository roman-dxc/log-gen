
# +---------------+-----------------+
# |     Level     |   Num. value    |
# +---------------+-----------------+
# | NONSET        |        0        |
# | DEBUG         |       10        |
# | INFO          |       20        |
# | WARNING       |       30* <- DEF|
# | ERROR         |       40*       |
# | CRITICAL      |       50*       |
# +---------------+-----------------+

# se almacenan en el log a partir del 30 valor. Configurado a 10

import logging
import random
from time import sleep

LOG_PATH = "/log-gen/ejemplo2.log" 
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
	filename = LOG_PATH, 
	level = LOG_LEVEL,
	format = LOG_FORMAT
)

def insertar_en_log(logger, txt):
	
	nivel_log = (int(random.uniform(0,100)) % 6) * 10
	
	if nivel_log<=10:
		logger.debug(txt)
	elif nivel_log==20:
		logger.info(txt)
	elif nivel_log==30:
		logger.warning(txt)
	elif nivel_log==40:
		logger.error(txt)
	else:
		logger.critical(txt)
		
	


logger = logging.getLogger()

for x in range(0, 5):
	cad = " Memoria cache llena, el rendimiento no es optimo (" + str(x) + ")"
	
	insertar_en_log(logger, cad)
	
	sleep(2) # segundos
