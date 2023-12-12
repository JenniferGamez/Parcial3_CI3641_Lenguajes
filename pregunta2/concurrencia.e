-- Programa ¡Hola, mundo! en Euphoria

printf(1, "¡Hola, mundo!\n")

-- Ejemplo de ejecución de un proceso externo en Euphoria
-- Este código ejecutará el comando 'ls' en el sistema operativo

include process.e

-- Ejecutar el comando 'ls'
system("ls")

-- Ejemplo simple de "concurrente" en Euphoria usando una simulación básica de alternancia de tareas

include std/io.e

procedure task1()
    ? "Tarea 1 ejecutándose..."
end procedure

procedure task2()
    ? "Tarea 2 ejecutándose..."
end procedure

-- Simulación básica de concurrencia alternando tareas
for i = 1 to 5 do
    task1()
    task2()
end for
