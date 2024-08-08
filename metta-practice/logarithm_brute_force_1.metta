 ;; NOTICE : This logarithmic function implementation works
 ;;          only for numbers which are multiple of their log base.
 ;;          i.e. logb(n) ; n have to be multiple of b

 ;; Define the brute-force logarithm function
(: log_brute_force (-> Number Number Number))
(= (log_brute_force $b $n) (log_recursive $b $n 1))

 ;; Recursive function to check powers of b
(: log_recursive (-> Number Number Number Number))
(= (log_recursive $b $n $p)
    (if (== (pow $b $p) $n)
        $p
        (if (> (pow $b $p) $n)
            (undefined)
            (log_recursive $b $n (+ $p 1)))))

 ;; Helper function to calculate power
(: pow (-> Number Number Number))
(= (pow $b $p)
    (if (== $p 0)
        1
        (* $b (pow $b (- $p 1)))))

 ;; Example usage
! (log_brute_force 2 5) ;; Should return 3, because 2^3 = 8
