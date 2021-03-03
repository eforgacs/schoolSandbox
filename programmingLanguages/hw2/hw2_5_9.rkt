;; compute integer log, base 2
;; (number of bits in binary representation)
;; works only for positive integers

(define (int_lg x y)
  (define (in_lg_bs_2 x y r)
    (if (zero? y) r
        (in_lg_bs_2 (* x x)
                    (find_quo y 2)
                    (if (odd? y) (* r x) r))))
  (in_lg_bs_2 x y 1))


; or

(define (log2_tail n)
  (let log2 ((n n) (res 0))
    (if (= n 1)
        res
        (log2 (quotient n 2)
              (+ 1 res)))))


(define (minimum l)
  (min-helper list #f))

(define (min-helper l el_min)
  (if (null? l)
      el_min
      (let ((m (car l)))
        (if (eq? el_min #f)
            (set! el_min m))
        (if (< m el_min)
            (min-helper (cdr l) m)
            (min-helper (cdr l) el_min)))))




