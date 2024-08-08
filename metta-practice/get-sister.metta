; put you code here
; put you code here
; family tree

; Gender
(Chandler Male)
(Monica Female)
(John Male)
(Pam Female)
(Adam Male)
(Jane Female)
(Bob Male)
(Tim Male)
(Kim Female)
(Eve Female)
(Joey Male)

(Parent Chandler John)
(Parent Chandler Pam)
(Parent Chandler Adam)
(Parent Chandler Jane)
(Parent Monica John)
(Parent Monica Pam)
(Parent Monica Adam)
(Parent Monica Jane)
(Parent John Bob)
(Parent Pam Tim)
(Parent Pam Kim)
(Parent Adam Eve)
(Parent Jane Joey)

; Get the parents of a person
(= (get-parents $x)
    (match &self (Parent $y $x) $y)
)

; Get the mother of a person
(= (get-mother $x)
    (match &self 
    (,
        (Parent $y $x)
        ($y Female)
    )
     $y)
)

; Get the children of a person
(= (get-children $x)
    (match &self (Parent $x $y) $y)
)

(= (eq $x $x) True)
! (eq a b) ; (eq a b)
(= (eq $x $y) (empty))
! (eq a a) ; [True]

; Get the siblings of a person (excluding the person themselves)
(= (get-siblings $x)
    (match &self 
        (,
            (Parent $p $x)
            (Parent $p $s)
        )
        $s)
)

; Get the male siblings (uncles) of a person's parent
(= (get-male-siblings $p)
    (match &self 
        (,
            (Parent $gp $p)
            (Parent $gp $s)
            ($s Male)
        )
        $s)
)

; Get the uncles of a person (ensuring no duplicates)
(= (get-uncles $x)
    (match &self  (Parent $p $x) (get-male-siblings $p) )
)

(= (get-children $x)
    (match &self (Parent $x $y) $y)
)

(= (get-nephews $x)
    (get-children (get-siblings $x))

)

(=(get-pred $x)
    (match &self
    (,
        (Parent $y $x)
        (Parent $z $y)    
    )

    ($y $z)
    )
)

; Test cases
!(get-parents John)
!(get-mother Pam)
!(get-siblings Pam)
!(get-uncles Tim)
!(get-children Pam)
!(get-nephews John)
!(get-pred Bob)