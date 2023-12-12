-- PREGUNTA 5

------------------
-- Parte c.ii.
------------------

sospechosa arbolito (genA 1)
=
sospechosa arbolito Rama 1 
                         (genA (2)) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (Rama 2 (genA (3)) (genA (4))) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (Rama 3 (genA (4)) (genA (6))) 
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
.
.
.
Evaluacion recursiva infinita de genA. 