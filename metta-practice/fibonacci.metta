(= (fib $x)
    (if 
        (<= $x 1)
        1
        (+ 
            (fib (- $x 1)) 
            (fib (- $x 2))
        )
    )
)

!(fib 3)