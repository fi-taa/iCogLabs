; put you code here
(= (grade-checker $x)
    (if (>= $x 90)
        A
        (if (>= $x 80)
            B
            (if (>= $x 70)
                C
                F
            )
        )
    )
)

!(grade-checker 44)




(: a A)
(: b B)
(: A Type)

! (get-type a) ; A
! (get-type b) ; B
! (get-type c) ; %Undefined%
! (get-type A) ; Type
! (get-type B) ; %Undefined%