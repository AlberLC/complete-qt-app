import os
import subprocess
import pathlib


def reemplazar(string):
    return string.replace('self.', 'self.w.').replace('Form"', 'self.w.centralWidget"').replace('Form.', 'self.w.centralWidget.').replace('Form)', 'self.w.centralWidget)').replace('"', "'")


try:
    url_archivo = input('Archivo: ').strip().strip('"').strip("'")
    nombre, extension = os.path.splitext(os.path.basename(url_archivo))
    nombre_clase = nombre.title().replace('_', '')

    if extension == '.ui':
        # Creo el codigo python a partir del .ui
        url_archivo_py = pathlib.Path(url_archivo).with_suffix('.py')
        subprocess.Popen(f'pyside2-uic {url_archivo} -o {url_archivo_py}', shell=True, stdout=subprocess.PIPE).wait()

    # ---------- Comenzamos el formateo del archivo .py ----------
    lineas_resultado = []

    # Leo las lineas del archivo
    with open(url_archivo_py) as file:
        lineas = file.readlines()

    i = 0
    # Ignoramos los comentarios del principio
    while 'from PySide2 import' not in lineas[i]:
        i += 1

    # Empezamos con la clase
    while 'class' not in lineas[i]:
        lineas_resultado.append(reemplazar(lineas[i]))
        i += 1

    lineas_resultado.append("\n")
    lineas_resultado.append(f"class {nombre_clase}:\n")
    lineas_resultado.append(f"    def __init__(self, window):\n")
    lineas_resultado.append(f"        self.w = window\n")
    lineas_resultado.append("\n")
    lineas_resultado.append(f"        self.setup_gui()\n")
    lineas_resultado.append("\n")
    lineas_resultado.append(f"    def setup_gui(self):\n")
    lineas_resultado.append(f"        self.w.centralWidget = QtWidgets.QWidget(self.w)\n")
    lineas_resultado.append(f"        self.w.centralWidget.setObjectName('centralWidget')\n")

    # Ignoramos las 3 lineas siguientes (def, Form.set, Form.resize) y avanzamos a la siguiente
    i += 4

    # Copiamos hasta linea en blanco
    while lineas[i] != '\n':
        lineas_resultado.append(reemplazar(lineas[i]))
        i += 1

    # Anadimos el widget a la vista
    lineas_resultado.append('        self.w.setCentralWidget(self.w.centralWidget)\n')

    # Copiamos la linea en blanco
    lineas_resultado.append(reemplazar(lineas[i]))

    # Ignoramos hasta los setText()
    while 'Form.' not in lineas[i]:
        i += 1

    # Nos saltamos el Form.setWindowTitle()
    i += 1

    # Transformamos las lineas de los setText()
    for linea in lineas[i:]:
        lineas_resultado.append(reemplazar(
            linea.replace('QtWidgets.QApplication.translate("Form", ', '').replace(', None, -1)', '')))

    lineas_resultado.append('    def connect_signals(self, controller):\n')
    lineas_resultado.append('        pass\n')

    # Sobreescribo el archivo .py
    with open(url_archivo_py, 'w', encoding='utf-8') as file:
        file.writelines(lineas_resultado)

except Exception as e:
    os.remove(url_archivo_py)
    print(f'{e.__class__.__name__}: {e}')
    input('Presione una tecla para continuar...')
