# Compiladores e interpretes I S 2018

Tarea #2: Trabajar las imagenes de INCOFER utilizando ```pytesseract```.

## Getting Started

Estas instrucciones le permitirán obtener una copia del proyecto en funcionamiento en su máquina local para fines de desarrollo y prueba.

### Prerequisites

```
sudo apt install python3-pip
pip3 install pillow
pip3 install pytesseract
pip3 install opencv-python
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-spa
```

## Running the tests

Ejemplo de corrida:
'''
	python3 ocr.py --image /home/andres/Desktop/Compiladores/imagen1.jpg
'''
Ejemplo de corrida con preprocess (opcional):
'''
	python3 ocr.py --image /home/andres/Desktop/Compiladores/photo_2018-02-27_22-40-53.jpg --preprocess blur
'''
