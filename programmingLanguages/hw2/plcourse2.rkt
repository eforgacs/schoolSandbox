(define (members elem lis)
      (cond
         ((null? lis) #f)
         ((= elem (car lis)) lis)
         (else (members elem (cdr lis)))))

(members 5 '(1 4 6 7))

(define (factorial n) 
        (if (= n 0) 
               1 
               (* n (factorial (- n 1)))))
(factorial 5)