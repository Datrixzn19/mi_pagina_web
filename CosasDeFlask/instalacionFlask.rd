Esta carpeta se crea para documentar instalacion, pruebas y etc de flask

COSAS A TOMAR EN CUENTA DE FLASK 
en la raiz del proyecto=> py -3 -m venv .venv        en .venv crea una carpeta invisible pero si no ponemos el punto es visibble, recomendado dejarlo asi 
activar env .\.venv\Scripts\activate  => en un inicio da error porque algo lo bloquea entonces hacer....:
desde vscode selecionar el interprete el que dice algo de .ven scripts pyhonexe

PS C:\Users\PERSONAL\Desktop\repos\mi_pagina_web> .venv\Scripts\Activate.ps1        si esto da error ejecutar:
PS C:\Users\PERSONAL\Desktop\repos\mi_pagina_web> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
y luego volver a ejecutar 
PS C:\Users\PERSONAL\Desktop\repos\mi_pagina_web> .venv\Scripts\Activate.ps1
(.venv) PS C:\Users\PERSONAL\Desktop\repos\mi_pagina_web> y listo debe salir .venv al inicio 