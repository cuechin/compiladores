from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re

#####################################
#   Tarea #2                        #
#   Andrés Mora Miranda 2013241401  #
#   Daniela Quesada 2014009760      #
#####################################

def main():

	'''
	Ejemplo de corrida: python3 ocr.py --image /home/andres/Desktop/Compiladores/photo_2018-02-27_22-40-53.jpg
	Ejemplo de corrida con preprocess (opcional): python3 ocr.py --image /home/andres/Desktop/Compiladores/photo_2018-02-27_22-40-53.jpg --preprocess blur
	'''

	filename = 'ocr.txt' # nombre del archivo.
	pattern = '([0-1]?\d|2[0-3]):?([0-5]\d)(\s?[apAP].[mM].)?' # expresión regular.

	'''
	 Construcción y análisis del argumento.
	 --image: El camino a la imagen que estamos enviando a través del sistema OCR.
	 --preprocess: El método de preprocesamiento, thresh (umbral) o blur (desenfoque).
	'''

	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="path to input image to be OCR'd")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh",
		help="type of preprocessing to be done")
	args = vars(ap.parse_args())

	image = cv2.imread(args["image"]) #Cargamos la imagen de disco a memoria.
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convierte en escala de grises.

	# Si "thresh" o "blur", aplicar umbrales para preprocesar la imagen.
	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	# escribe la imagen en escala de grises en el disco como un archivo temporal.
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# cargar la imagen como una imagen PIL / Pillow para luego aplicar OCR.
	text = pytesseract.image_to_string(Image.open(filename))

	# Creamos el archivo con el nombre del atributo 'filename'.
	f = open(filename,'w')
	f.write(text)
	f.close()
	print ("Resultado al aplicar OCR a la imagen: " + '\n')
	print(text)

	#Abrir el archivo
	ff = open(filename, 'r')
	lines = ff.readlines()

	print ("Resultado de la expresión regular: " + '\n')
	for line in lines:
	    match = re.search(pattern, line)
	    if match:
	        new_line = match.group() + '\n'
	        print (new_line)

	ff.close()

	#muestra las imagenes de salida
	#cv2.imshow("Image", image)
	#cv2.imshow("Output", gray)
	#cv2.waitKey(0)

if __name__ == "__main__":
   main()
