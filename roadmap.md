## 0.1 operator support ##

- multiplication `(a * b != b * a)`
- division `([a / b == a * b ^ -1] != [b / a == b * a ^ -1])`
- addition `(a + b == b + a)`
- subtraction `(a - b != b - a)`
- scaling
	- `(a * s == s * a)`
	- `(s / a == s * a ^ -1)`

## 0.2 rewrite tests to use test generators ##
- Might make `nose` a dependency
- Allows multiple checks for things like `test_add` to register as inidivudal tests


## 0.3 Cement API ##
- naming conventions
- package layout and imports
- quaternion internals
- quaternion - specific methods and functions

## 0.4 Arithmetic Functions ##
- `add`
- `sub`
- `mul`
- `div`
- `scale`

## 0.4 Quaternion Python Properties ##
- `magnitude`
- `conjugate`
- `inverse`
- `normalized`

## 0.5 Quaternion Functions ##
Functions that produce the same results as
- `magnitude`
- `conjugate`
- `inverse`
- `normalized`

## 0.6 Inplace Quaternion Functions ##
- imagnitude
- iconjugate
- iinverse
- inormalized

## 0.6 Coercion ##
	- `int`
	- `long`
	- `float`
	- `complex`

## 0.7 ##
## 1.0 Pure python implementation ##
## 2.0 Numpy implementation ##
## 3.0 Cython implementation ##
## 4.0 Expression implementation ##
support for parsing a + bi + cj + dk
