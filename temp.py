#!/usr/bin/env python3
'''Records measurments to a given file. Usage example:
$ ./record_measurments.py out.txt'''
import sys
import time
from rplidar import RPLidar


PORT_NAME = 'COM5'


def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME) 
    lidar.disconnect()
    lidar.connect()
    lidar.start_motor()
    lidar.stop_motor()
    lidar.start_motor()
    
    outfile = open(path, 'a')
    base= time.time()
    tiempo_pasado=0
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurment)
            tiempo_pasado= time.time()-base
            line =line + '\t' + 'time\t' + str(tiempo_pasado)
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop_motor()
    lidar.stop()
    lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    
    run("C:\\Users\\PROPIETARIO\\Desktop\\8vo\\Practicas\\prueba4.txt")