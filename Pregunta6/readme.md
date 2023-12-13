# EXAMEN 3 - CI3641 - PREGUNTA 6
# Jennifer Gámez 16-10396

## Instrucciones de Ejecución
### Manejador intérprete para un subconjunto del lenguaje Prolog

    - expression.py: Contiene el identificador de expresiones. PARTE A
    - func_def_ask.py: Contiene la implementación de la acción def y la acción ask.
    - main.py: Contiene el main() o la lógica principal de la aplicación
    - test.py: Contiene las pruebas unitarias de expression.py y func_def_ask.py

1. Puede probar el programa, ejecutando la terminal:

    ``` python3 main.py ```

Siga las instrucciones que se indican en el manejador de tablas de métodos virtuales.

2. Para ejercutar las pruebas en Python utilice el marco de prueba

    ``` pytest  ```

3. Para probar la cobertura del programa ejecute

    ``` coverage run -m unittest test.py ``` 

4. y luego

    ``` coverage report -m  ```

## Requisitos del Sistema

Para realizar las pruebas de cobertura, asegúrate de cumplir con los siguientes requisitos:

1. Tener instalado pytest. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install pytest```

2. Tener instalado coverage. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

    ``` pip install coverage```

Asegúrate de que ambas dependencias estén instaladas y configuradas en tu entorno antes de ejecutar las pruebas de cobertura.
