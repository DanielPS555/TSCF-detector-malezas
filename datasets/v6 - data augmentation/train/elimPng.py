import os 


dir_name = 'labels/'
arch = os.listdir(dir_name)


cont = 0
for name in arch:
	if '_fake' in name and '.png.txt' in name:
		partes_png = name.split('.png')
		os.rename(dir_name  + name, dir_name + partes_png[0] + partes_png[1])
		
		
        

