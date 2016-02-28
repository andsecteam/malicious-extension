# -*- coding: utf-8 -*-
# se recomienda el uso de ftp simple.
# si este script es usado en sistemas unix (incluiendo OS X) hay que canviar la orden os.system("cls") por os.system("clear")
# si es usado en unix tambien hay que canviar el directorio donde se guarda el archivo log.txt, en el caso de ser linux se tendria que poner: /home/carpeta_usuario
# si es usado en unix tambien hay que borrar la instruccion os.color("ob") ya que hace referencia a un comando de windows y no de unix
# 
#  _____           _          _                 ___ _                     _____  __       _    _     ___________ __ 
# /  __ \         | |        | |               |_  (_)          ___      |____ |/  |     | |  | |   |  _  |  ___/ _|
# | /  \/ ___   __| | ___    | |__  _   _        | |_  ___     ( _ )         / /`| | _ __| | _| |__ | |/' | |_ | |_ 
# | |    / _ \ / _` |/ _ \   | '_ \| | | |       | | |/ _ \    / _ \/\       \ \ | || '__| |/ / '_ \|  /| |  _||  _|
# | \__/\ (_) | (_| |  __/   | |_) | |_| |   /\__/ / | (_) |  | (_>  <   .___/ /_| || |  |   <| | | \ |_/ / |  | |  
#  \____/\___/ \__,_|\___|   |_.__/ \__, |   \____/|_|\___/    \___/\/   \____/ \___/_|  |_|\_\_| |_|\___/\_|  |_|  
#                                    __/ |                                                                          
#                                   |___/                                                                           
 
import os
import shutil
import time
import urllib
import socket
import SocketServer
from ftplib import FTP 
from time import sleep

host = 'localhost'                  # definimos la ip por donde escuchara nuestro servidor
fichero_origen = 'c:\log.txt' 		# Ruta del fichero que vamos a subir
fichero_destino = 'log.txt'			# Nombre que tendrá el fichero en el servidor  												

def menu():
	
	os.system('cls')    		    # funcion que limpia la pantalla
	print ""
	print "#  _____           _          _                 ___ _                     _____  __       _    _     ___________ __  #"
	print "# /  __ \         | |        | |               |_  (_)          ___      |____ |/  |     | |  | |   |  _  |  ___/ _| #"
	print "# | /  \/ ___   __| | ___    | |__  _   _        | |_  ___     ( _ )         / /`| | _ __| | _| |__ | |/' | |_ | |_  #"
	print "# | |    / _ \ / _` |/ _ \   | '_ \| | | |       | | |/ _ \    / _ \/\       \ \ | || '__| |/ / '_ \|  /| |  _||  _| #"
	print "# | \__/\ (_) | (_| |  __/   | |_) | |_| |   /\__/ / | (_) |  | (_>  <   .___/ /_| || |  |   <| | | \ |_/ / |  | |   #"
	print "#  \____/\___/ \__,_|\___|   |_.__/ \__, |   \____/|_|\___/    \___/\/   \____/ \___/_|  |_|\_\_| |_|\___/\_|  |_|   #"
	print "#                                    __/ |                                                                           #"
	print "#                                   |___/                                                                            #"
	print ""
	print ""
	print ""     			
	print ""									
	print "Selecciona una opcion"
	print ""
	print "\t1 - Montar servidor. {Puerto = " + str(port) + "}"
	print "\t2 - Subir archivo log a un FTP. (RECOMENDADO)"
	print "\t3 - Subir archivo log a un FTP seguro. (SOPORTA TLS)"
	print "\t7 - Readme"
	print "\t9 - Salir"	 
	print ""

def subir_ftp():                                                             								# definimos el codigo de la funcion subir archivo log a ftp
	try:
		ftp_server = raw_input("Introduce la direccion del servidor ftp: ")  								#Varibale que coje el servidor ftp
		ftp_user = raw_input("Introduce el usuario del servidor ftp: ")		 								# variable que cojel usuario ftp
		ftp_pass = raw_input("Introduce la contrasena del servidor ftp: ")   								# variable que recoje la password del servidor ftp
		ftp_fitxer = raw_input("Introduce la direccion del archivo a subir (ejemplo c:/log.txt) >> ")       # variable que recoje el archivo origen que subiremos al ftp
		ftp_fitxer_upload = raw_input("Introduce el nombre que cojera el archivo en el servidor ftp: ")     # variable que recoje el nombre que recivira el archivo una vez se haya subido al servidor
		ftp = FTP(ftp_server,ftp_user,ftp_pass)  
		try:
				print ""
				print "Estos son los archivos que tiene en su ftp:"
				print ""
				ftp.retrlines("LIST")                                        								# comando ftp para listar el contenido del servidor ftp
				print ""
				print "Subiendo archivo log....."
				print ""
				s = open(ftp_fitxer, 'rb')                            		 								# declaramos la varibale s que s'encarga de abrir el archivo que subireoms al ftp
				ftp.storbinary('STOR ' + ftp_fitxer_upload, s)               								# funcion que s'encarga de cojer el archivo que declaramos anteriormente en la varibale "s" i lo sube al servidor renombrandolo por la variable "fichero_destino"
				print "Archivo subido con exito!!"
				print ""
				print "Archivos del servidor actualizados con exito!"
				print ""
				ftp.retrlines("LIST")										 								# cierra la conexion ftp
				ftp.quit     
				sleep(7)                                                
		except:
			print "(WARNING!!!) No se ha podido subir el fichero >> " + fichero_origen
			sleep(2)
	except:
		print "(WARNING!!!) No se ha podido conectar con el servidor ftp >> " + ftp_server
		sleep(3)

def subir_ftp_tls():                                                              							# definimos una funcion que recogera las instruccions si se desea usar un servidor con seguridad ssl
	try:
		ftp_server = raw_input("Introduce la direccion del servidor ftp: ")
		ftp_user =  raw_input("Introduce el usuario del servidor ftp: ")
		ftp_pass = raw_input("Introduce la contraseña del servidor ftp: ")
		ftp_fitxer = raw_input("Introduce la direccion del archivo a subir (ejemplo c:/log.txt) >> ")
		ftp_fitxer_upload = raw_input("Introduce el nombre que cojera el archivo en el servidor ftp: ")
		ftp = FTP_TLS(ftp_server,ftp_user,ftp_pass)
		try:
			print ""
			print "Estos son los archivos que tiene en su servidor ftp:"
			print ""
			ftp.retrlines("LIST")
			print ""
			print "Subiendo archivo log....."
			print ""
			s = open(ftp_fitxer, 'rb')
			ftp.storbinary('STOR ' + ftp_fitxer_upload, s)
			print "Archivo subido con exito!!"
			print ""
			print "Archivos sel servidor actualizados con exito!"
			print ""
			ftp.retrlines("LIST")
			ftp.quit
		except:
			print "(WARNING!!!) No se ha podido subir el fichero >> " + ftp_fitxer
			sleep(3)
	except:
		print "(WARNING!!!) Nose ha podido conectar con el servidor ftp >> " + ftp_server	
		sleep(3)		


def connSV(host, port):                                                      								# definimos un simple servidor socket que lo unico que ara sera recivir peticiones

	try:   
	    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
	    sock.bind((host, port))
	    broked = 0
	    sock.listen(1)                                                           							# ponemos a la escucha nuestro servidor
	    print "\nServidor funcionando en", host, ":", port
	    conn, addr = sock.accept()
	    print "\n \nConnected by: ", addr, "\n"
	    while broked == 0:
	        data = conn.recv(1024)                                              						    # establecemos la amplitud del buffer del servidor
	        conn.sendall(data)
	        decrypt_url = urllib.unquote(data).decode('utf8')                   						    # en esta funcion decodificamos la url para que se puedan ver los campos de la peticion en texto plano
	        log_partial(decrypt_url)                                            						    # en este apartado llamamos a la funcion log_partial
	        log_total(decrypt_url)                                              						    # en este apartado llamamos a la funcion log_total  
	        print filtrer(decrypt_url)
	        broked = 1
	except KeyboardInterrupt:
		print ""


                
def filtrer(decrypt_url):                                                    								#Funcion para filtrar un documento por lineas
    x = ''
    linea = []
    shutil.copy2('\\p_log.txt', 
                 '\\~log.txt')                                  	 										#Se crea un archivo temporal (~log.txt) para hacer la filtracion
    decrypt = open('\\~log.txt', 'r')
    for line in decrypt:                                                    							    #Itinera en el archivo linea por linea
        linea.append(line) 
    print linea[0].replace("GET /?data=",''), "\n", linea[1], "\n", linea[2]
    decrypt.close()
    os.remove('\\~log.txt')
    return x
        
        
def log_partial(p_data):                                                     								#Crea un log de las peticiones entrantes
    outfile = open('\\p_log.txt', 'w')                          			 								#a = pone el texto nuevo al final del txt, conservando el antiguo
    outfile.write(p_data)
    outfile.close()
    
def log_total(data):                                                         								#Crea un log de las peticiones entrantes
    outfile = open('\\log.txt', 'a')                  
    outfile.write(data)
    outfile.close()    

def readme():
	os.system("color 0c")
	os.system("cls")
	print ""
	print "#  _____           _          _                 ___ _                     _____  __       _    _     ___________ __  #"
	print "# /  __ \         | |        | |               |_  (_)          ___      |____ |/  |     | |  | |   |  _  |  ___/ _| #"
	print "# | /  \/ ___   __| | ___    | |__  _   _        | |_  ___     ( _ )         / /`| | _ __| | _| |__ | |/' | |_ | |_  #"
	print "# | |    / _ \ / _` |/ _ \   | '_ \| | | |       | | |/ _ \    / _ \/\       \ \ | || '__| |/ / '_ \|  /| |  _||  _| #"
	print "# | \__/\ (_) | (_| |  __/   | |_) | |_| |   /\__/ / | (_) |  | (_>  <   .___/ /_| || |  |   <| | | \ |_/ / |  | |   #"
	print "#  \____/\___/ \__,_|\___|   |_.__/ \__, |   \____/|_|\___/    \___/\/   \____/ \___/_|  |_|\_\_| |_|\___/\_|  |_|   #"
	print "#                                    __/ |                                                                           #"
	print "#                                   |___/                                                                            #"
	print ""
	print ""
	print ""
	sleep(1)
	os.system("color 0a")
	print " se recomienda el uso de ftp simple."
	print ""
	print " si este script es usado en sistemas unix (incluiendo OS X) hay que canviar la orden os.system('cls') por os.system('clear')"
	print ""
	print " si es usado en unix tambien hay que canviar el directorio donde se guarda el archivo log.txt, en el caso de ser linux se tendria que poner: /home/carpeta_usuario"
	print ""
	print " si es usado en unix tambien hay que borrar la instruccion os.color('0b') ya que hace referencia a un comando de windows y no de unix"
	print ""
	print ""
	print ""
	print ""
	print "Sera redireccionado al menu automaticamente en 40 segundos"
	sleep(40)

while True:

	os.system("cls")
	print ""
	print "#  _____           _          _                 ___ _                     _____  __       _    _     ___________ __  #"
	print "# /  __ \         | |        | |               |_  (_)          ___      |____ |/  |     | |  | |   |  _  |  ___/ _| #"
	print "# | /  \/ ___   __| | ___    | |__  _   _        | |_  ___     ( _ )         / /`| | _ __| | _| |__ | |/' | |_ | |_  #"
	print "# | |    / _ \ / _` |/ _ \   | '_ \| | | |       | | |/ _ \    / _ \/\       \ \ | || '__| |/ / '_ \|  /| |  _||  _| #"
	print "# | \__/\ (_) | (_| |  __/   | |_) | |_| |   /\__/ / | (_) |  | (_>  <   .___/ /_| || |  |   <| | | \ |_/ / |  | |   #"
	print "#  \____/\___/ \__,_|\___|   |_.__/ \__, |   \____/|_|\___/    \___/\/   \____/ \___/_|  |_|\_\_| |_|\___/\_|  |_|   #"
	print "#                                    __/ |                                                                           #"
	print "#                                   |___/                                                                            #"
	print ""
	print ""
	print ""
	print ""
	print ""
	os.system("color 07")
	port = int(input("Introduce el puerto por donde escuchara el servidor (ejemplo:8080): "))   		   # definimos el puerto por el cual escuchara nuestro servidor
	print ""
	print "El archivo log.txt sera guardado en c:\code\python\log.txt"
	sleep(3)
	# Mostramos el menu
	menu()
 
	# solicitem una opcio al usuari
	num_menu = raw_input("Inserta un numero >> ")
 
	if(num_menu=="1"):                                                              					   # si hemos seleccionado la opcion 1 del menu lo que ara sera levantar un servidor socket llamando a la funcion connSV
		while 1:
			connSV(host, port)
			sleep(4)

	elif num_menu=="2":                                                                                    # si hemos eleccionado la opcion 2 lo que ara sera subir el archivo log.txt al servidor ftp que nosotros queramos
		subir_ftp()
		menu()																	                           # una vez subido el archivo, se vuelve a mostrar el menu


	elif num_menu=="3":															                           # si hemos sel.leccionado la opcion 2 lo que ara sera subir el archivo mediantu un servidro ftp seguro
		subir_ftp_tls()
		menu()																	                           # una vez subido el archivo se vuelve a mostrar el menu

	elif num_menu=="7":
		readme()
		menu()

	elif num_menu=="9":                                                                                    # si seleccionamos la opcion 9 lo que ara el script sera cerrarse
		break																	                           # se para/cierra nuestro script	
	
	else:
		print ""
		raw_input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar!")