include std/concurrency.e

-- Función para calcular el producto punto entre dos vectores
function producto_punto_concurrente(vector1, vector2)
    sequence resultados = repeat(0, length(vector1))  -- Inicializa un vector de resultados parciales
    
    -- Función para realizar el cálculo del producto punto de una sección de los vectores
    function producto_prunto(inicio, fin)
        local suma = 0
        for i = inicio to fin do
            resultados[i] = vector1[i] * vector2[i]
            suma += resultados[i]
        end for
        return suma
    end function
    
    integer chunk_size = floor(length(vector1) / number_of_cpus())  -- Tamaño del fragmento para cada tarea
    
    atom tasks[number_of_cpus()]
    for i = 1 to number_of_cpus() do
        integer start = (i - 1) * chunk_size + 1
        integer finish = i * chunk_size
        if i = number_of_cpus() then
            finish = length(vector1)
        end if
        
        tasks[i] = create_thread(:producto_prunto, {start, finish})
    end for
    
    sync_threads(tasks)  -- Espera a que todas las tareas terminen
    
    return sum(resultados)  -- Suma los resultados parciales para obtener el producto punto
end function

-- Ejemplo de uso
sequence vec1 = {1, 2, 3, 4, 5}
sequence vec2 = {5, 4, 3, 2, 1}

atom resultado = producto_punto_concurrente(vec1, vec2)
? resultado
