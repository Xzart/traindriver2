import os

#Open and check do railroad roilling stock files exist
rs_folder = os.listdir('./presets/')
rs_passenger = './presets/tabor_pasazerski.txt'
rs_freight = './presets/tabor_towarowy.txt'

if os.path.exists(rs_passenger):
    rs_file_passenger = open('./presets/tabor_pasazerski.txt')
    rs_content_passenger = rs_file_passenger.read()
    print('Tabor pasażerski...OK')
    rs_file_passenger.close()
else:
    print('Brakuje pliku tabor_pasazerski.txt')
    rs_content_passenger = ''
    
if os.path.exists(rs_freight):
    rs_file_freight = open('./presets/tabor_towarowy.txt')
    rs_content_freight = rs_file_freight.read()
    print('Tabor towarowy...OK\n')
    rs_file_freight.close()
else:
    print('Brakuje pliku tabor_towarowy.txt')
    rs_content_freight = ''

print('Test zawartości pliku:\n', rs_content_passenger, rs_content_freight)

#Railroad rolling stock list
rs_passenger_list = []
with open('./presets/tabor_pasazerski.txt') as inputfile:
    for line in inputfile:
        rs_passenger_list.extend(line.rstrip().split(';'))
rs_freight_list = []
with open('./presets/tabor_towarowy.txt') as inputfile:
    for line in inputfile:
        rs_freight_list.extend(line.rstrip().split(';'))

print('\nTest zawartości tablicy:\n',rs_passenger_list,rs_freight_list)

#Random railroad cars
#def randomCars():
