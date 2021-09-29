(define-macro (def func args body)
  `(define ,func (lambda ,args ,body)))

(define (tail-replicate x n) 
  (define (replicate-helper x n res)
        (if (zero? n)
            res
            (replicate-helper x (- n 1) (cons x res))))
  (replicate-helper x n nil))

(define (exp b n) 
  (define (exp-helper b n res)
      (if (zero? n)
          res
          (exp-helper b (- n 1) (* b res))))
  (exp-helper b n 1))


