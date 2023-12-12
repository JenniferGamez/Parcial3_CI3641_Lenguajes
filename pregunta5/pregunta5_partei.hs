-- PREGUNTA 5

------------------
-- Parte c.i.
------------------

sospechosa arbolito (genA 1)
=
foldA whatTF (const Hoja) arbolito (genA 1)
=
foldA whatTF (const Hoja) (Rama 'a' 
                                   (Rama 'b' 
                                        Hoja 
                                        (Rama 'c' Hoja Hoja)
                                   ) 
                                   Hoja
                              ) (genA 1)
=
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'
                                             Hoja
                                             (Rama 'c' 
                                                       Hoja 
                                                       Hoja
                                             )
                                        )
          ) 
          (foldA whatTF (const Hoja) Hoja) 
          (genA 1)
=
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'                     
                                             Hoja                   
                                             (Rama 'c' Hoja Hoja)
                                        )
           )                                                       
           (foldA whatTF (const Hoja) Hoja)                         
           (Rama 1   
                (genA (1 + 1))
                (genA (1 * 2))
           )
= 
Rama ('a', 1) 
     ((foldA whatTF (const Hoja) (Rama 'b'
                                        Hoja
                                        (Rama 'c' Hoja Hoja)
                                 )
      )
      (genA (1 + 1))
     ) 
     ((foldA whatTF (const Hoja) Hoja)
      (genA (1 * 2))
     )
=
Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA (1 + 1))) 
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
= 
Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (Rama 2 
                                                                                                         (genA (2 + 1))
                                                                                                         (genA (2 * 2))
                                                                                                   )
     )                                                                                           
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           ((foldA whatTF (const Hoja) Hoja)                (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           ((const Hoja) (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (Rama 4
                                                                                               (genA(4+1))
                                                                                               (genA(4*2))
                                                                                          ) 
           )
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((foldA whatTF (const Hoja) Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((const Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((const Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((const Hoja) (genA (1 * 2)))
=
Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     Hoja