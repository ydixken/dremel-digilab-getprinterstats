#!/usr/bin/env python3
import requests
import json
import threading

url = "http://10.42.0.102:80/command"
#data = {'':'getprinterstatus'}
data = 'getprinterstatus'

import threading

def getprinterstatus():
    threading.Timer(3.0, getprinterstatus).start()
    # get data and parse it
    r = requests.post(url=url, data=data) 
    resp = r.text
    json_string = r.text
    encoded = json.loads(json_string)
    jobname = encoded['jobname']
    progress = str(encoded['progress'])
    remaining_seconds = str(int(encoded['remaining']))
    elapsed_seconds = str(int(encoded['elaspedtime']))
    filament_type = encoded['filament_type ']
    plate_target_temp = str(encoded['buildPlate_target_temperature'])
    plate_temp = str(encoded['platform_temperature'])
    nozzle_target_temp = str(encoded['extruder_target_temperature'])
    nozzle_temp = str(encoded['temperature'])
    layer = str(encoded['layer'])
    chamber_temp = str(encoded['chamber_temperature'])
    # write to file
    f = open("printer.txt", "w")
    f.write('Current Job: ' + jobname + '\n')
    f.write('Progress: ' + progress + '%' + '\n')
    f.write('Time Remaining: ' + remaining_seconds + 's' + '\n')
    f.write('Time Elapsed: ' + elapsed_seconds + 's' + '\n')
    f.write('Filament: ' + filament_type + '\n')
    f.write('Nozzle Temp: ' + nozzle_temp + '°C (current) ' + '/ ' + nozzle_target_temp + '°C (target)' + '\n')
    f.write('Plate Temp: ' + plate_temp + '°C (current) ' + '/ ' + plate_target_temp + '°C (target)' + '\n')
    f.write('Chamber Temp: ' + chamber_temp + '°C (current)' + '\n')
    f.close()

getprinterstatus()