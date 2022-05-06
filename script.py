
import sys; # importamos el modulo para argumentos de entrada
# es el principal sys.argv[1] -> 2
# es el secundario sys.argv[2] -> 19
import os; # importamos el modulo os para sentencias en terminal

#creo la carpeta
os.mkdir("sub_directorio_"+sys.argv[1]+"."+sys.argv[2]);
#ubico en subdirectorio
os.chdir("sub_directorio_"+sys.argv[1]+"."+sys.argv[2]);

patch = ["9","8","7","6","5","4","3","2","1","0"]# suponemos que pueden exisistir estas ultimas versiones
for p in patch:
    os.system("curl -LO https://github.com/pre-commit/pre-commit/archive/refs/tags/v"+sys.argv[1]+"."+sys.argv[2]+"."+p+".zip");#descargo el archivo
    os.system("unzip v"+sys.argv[1]+"."+sys.argv[2]+"."+p+".zip");#descomprimo el archivo
    os.system("rm v"+sys.argv[1]+"."+sys.argv[2]+"."+p+".zip");#elimino el zip
    if(os.path.exists("pre-commit-"+sys.argv[1]+"."+sys.argv[2]+"."+p)): #si existe el contenido, salir del loop
        break;
    
#Lo ideal seria validar la url, para no tener que descargar todos y chequear que esten vacios.
#Pero no encontre comandos que validen correctamente la url, me tiran un status http/302 sea correcta o no la url.