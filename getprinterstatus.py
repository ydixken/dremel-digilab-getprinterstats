#!/usr/bin/env python3
import requests
import json
import threading

url = "http://10.42.0.102:80/command"
#data = {'':'getprinterstatus'}
data = 'getprinterstatus'

debug = False

def getprinterstats():
    threading.Timer(3.0, getprinterstats).start()
    # get data and parse it
    r = requests.post(url=url, data=data) 
    resp = r.text
    json_string = r.text
    encoded = json.loads(json_string)
    jobname = encoded['jobname'].strip('.gcode')
    progress = str(encoded['progress'])
    remaining_seconds = int(encoded['remaining'])
    elapsed_seconds = int(encoded['elaspedtime'])
    filament_type = encoded['filament_type ']
    plate_target_temp = str(encoded['buildPlate_target_temperature'])
    plate_temp = str(encoded['platform_temperature'])
    nozzle_target_temp = str(encoded['extruder_target_temperature'])
    nozzle_temp = str(encoded['temperature'])
    layer = str(encoded['layer'])
    chamber_temp = str(encoded['chamber_temperature'])

    # write to file
    if not debug:
        f = open("printer.txt", "w")
        f.write('Current Job: ' + jobname + '\n')
        f.write('Progress: ' + progress + '%' + '\n')
        if remaining_seconds > 0:
            remaining_seconds = str(remaining_seconds)
            f.write('Time Remaining: ' + remaining_seconds + 's' + '\n')
        else:
            pass
        elapsed_seconds = str(elapsed_seconds)
        f.write('Time Elapsed: ' + elapsed_seconds + 's' + '\n')
        f.write('Filament: ' + filament_type + '\n')
        f.write('Nozzle Temp: ' + nozzle_temp + '°C (current) ' + '/ ' + nozzle_target_temp + '°C (target)' + '\n')
        f.write('Plate Temp: ' + plate_temp + '°C (current) ' + '/ ' + plate_target_temp + '°C (target)' + '\n')
        f.write('Chamber Temp: ' + chamber_temp + '°C (current)' + '\n')
        f.close()
    else: 
        print(encoded)
        print('Current Job: ' + jobname + '\n')
        print('Progress: ' + progress + '%' + '\n')
        if remaining_seconds > 0:
            remaining_seconds = str(remaining_seconds)
            print('Time Remaining: ' + remaining_seconds + 's' + '\n')
        else:
            pass
        elapsed_seconds = str(elapsed_seconds)
        print('Time Elapsed: ' + elapsed_seconds + 's' + '\n')
        print('Filament: ' + filament_type + '\n')
        print('Nozzle Temp: ' + nozzle_temp + '°C (current) ' + '/ ' + nozzle_target_temp + '°C (target)' + '\n')
        print('Plate Temp: ' + plate_temp + '°C (current) ' + '/ ' + plate_target_temp + '°C (target)' + '\n')
        print('Chamber Temp: ' + chamber_temp + '°C (current)' + '\n')

getprinterstats()
