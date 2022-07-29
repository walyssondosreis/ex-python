
import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = r"D:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("ex_bandeiras.py", base=base,icon=r".\images\flag.ico")]
 # esse r na frente dos paths é para que uma junção \x não seja detectada como comando de string
cx_Freeze.setup(
    name = "bandeira",
    options = {"build_exe":
                   {"packages":["tkinter"],
                    "include_files": [
                r"D:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll",
                 r"D:\Users\walyssondosreis\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                    r".\images\flag.ico"],
                    "include_msvcr":True, # O msvcr faz com que seja anexado todas as dlls necessarias para o programa rodar em outro pc
                    }
               },

    version = "1.0",
    description = "Bandeiras Nacionais",
    executables = executables
    )

#CORRIGINDO ERRO DO TK
# http://stackoverflow.com/questions/35533803/keyerror-tcl-library-when-i-use-cx-freeze
# CORRIGINDO ERRO DAS DLL DO TK
# http://stackoverflow.com/questions/42077990/cx-freeze-dll-load-error-with-tkinter
# DLLS JUNTO COM EXECUTAVEL
# http://fernandofreitasalves.com/como-criar-um-executavel-com-instalador-msi-em-python-e-com-cx_freeze/
# TUTORIAL CX-FREEZE COM TK
#https://pythonprogramming.net/converting-tkinter-to-exe-with-cx-freeze/