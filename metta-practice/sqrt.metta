 ;; Define the square root function with recursive improvement
(: sqrt (-> Number Number))
(= (sqrt $x) (sqrt_recursive $x (/ $x 2.0)))

 ;; Recursive square root approximation
(: sqrt_recursive (-> Number Number Number))
(= (sqrt_recursive $x $guess)
    (if (< (abs (- $guess (improve_sqrt_guess $x $guess))) 0.00001)
        $guess
        (sqrt_recursive $x (improve_sqrt_guess $x $guess))))

 ;; Helper function to improve the current guess
(: improve_sqrt_guess (-> Number Number Number))
(= (improve_sqrt_guess $x $guess)
    (/ (+ $guess (/ $x $guess)) 2.0))

(: abs (-> Number Number))
(= (abs $x)
    ( if (< $x 0)
        (* -1 $x)
        $x
    ))
! (sqrt 16)
