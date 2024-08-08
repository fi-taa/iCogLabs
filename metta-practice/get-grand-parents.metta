; put you code here

(Parent Tom Bob)
(Parent Pam Bob)
(Parent Tom Liz)
(Parent Bob Ann)
(Parent Bob Pat)
(Parent Pat Jim)

(= (get-parents $x)
   (match &self (Parent $y $x) $y))
(= (get-grand-parents $x)
   (match &self (Parent $p $x)
          (match &self (Parent $gp $p) $gp)))

(= (get-grand-parents-2 $x)
   ((get-parents (get-parents $x))))

!(get-grand-parents-2 Pat)