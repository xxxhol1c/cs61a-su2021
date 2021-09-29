; Question 1
; 
(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

; Question 2
; 
(define (square x) (* x x))

(define (pow base exp) 
  (cond
    ((= 0 exp ) 1 )
    ((= 0 (modulo exp 2))  (pow (square base) (/ exp 2)))
    (else (* base(pow base (- exp 1))))
    )
)

; Question 3
; 
(define (filter-lst func lst) 
 (cond 
  ((null? lst) nil)
  ((func (car lst)) (cons (car lst) (filter-lst func (cdr lst))))
  (else (filter-lst func (cdr lst)))
  )
)

; ;; Tests
(define (even? x) (= (modulo x 2) 0))

(filter-lst even? '(0 1 1 2 3 5 8))

; expect (0 2 8)
; Question 4
; 
(define (accumulate merger start n term)
  (if (<= 1 n)
    (accumulate merger (merger start (term n)) (- n 1) term)
     start))
  



; Question 5
; 
(define (without-duplicates lst) 
  (if (null? lst) lst
    (cons (car lst) (without-duplicates (filter-lst (lambda (x) (not (= (car lst) x))) (cdr lst))))
    
  ))

; Question 7
; 
(define (accumulate-tail merger start n term)
  (if (<= 1 n)
    (accumulate merger (merger start (term n)) (- n 1) term)
    start))

; Optional Question
; 
(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond 
    ((number? expr)
     0)
    ((variable? expr)
     (if (same-variable? expr var)
         1
         0))
    ((sum? expr)
     (derive-sum expr var))
    ((product? expr)
     (derive-product expr var))
    ((exp? expr)
     (derive-exp expr var))
    (else
     'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))

(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eqv? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond 
    ((=number? a1 0)                 a2)
    ((=number? a2 0)                 a1)
    ((and (number? a1) (number? a2)) (+ a1 a2))
    (else                            (list '+ a1 a2))))

(define (sum? x)
  (and (list? x) (eqv? (car x) '+)))

(define (first-operand s) (cadr s))

(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond 
    ((or (=number? m1 0) (=number? m2 0))
     0)
    ((=number? m1 1)
     m2)
    ((=number? m2 1)
     m1)
    ((and (number? m1) (number? m2))
     (* m1 m2))
    (else
     (list '* m1 m2))))

(define (product? x)
  (and (list? x) (eqv? (car x) '*)))

; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))

(define (second-operand p) (caddr p))

(define (derive-sum expr var) 
  (make-sum (derive (first-operand expr) var)
                   (derive (second-operand expr) var))

)

(define (derive-product expr var) 
  (make-sum (make-product (derive (first-operand expr) var) (second-operand expr))
            (make-product (derive (second-operand expr) var) (first-operand expr)))
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent) 
  (cond ((=number? exponent 0) 1)
        ((=number? exponent 1) base)
        ((=number? base 1) 1)
        ((=number? base 0) 0)
        ((and (number? base) (number? exponent)) (expt base exponent))
        (else (list '^ base exponent))))


(define (exp? exp)  
  (and (list? exp) (eqv? (car exp) '^)))

(define x^2 (make-exp 'x 2))

(define x^3 (make-exp 'x 3))

(define (derive-exp exp var) 
  (make-product (second-operand exp)
                (make-exp var (- (second-operand exp) 1)))
)
