(* Example code from recitation *)

fun filt p lst =
  case lst of
  [] => []
  | hd :: tl => if p hd then hd :: (filt p tl) else filt p tl

val gt5lst = filt (fn elem => elem > 5) [1,5,6,2,3,4,7,8];

(* Two functions that seem useful *)

fun head(xs) =
	case xs of
		[] => raise List.Empty
	  | (x::_) => x

fun tail(xs) =
	case xs of
		[] => raise List.Empty
	  | (_::xs') => xs'

(* 1. Implement reverse = fn : ’a list -> ’a list using the Standard Basis Library function
foldl. Do not use recursion directly.
Example:
- reverse [1,2,3];
val it = [3,2,1] : int list *)


(* uses foldl *)

fun reverse list = foldl op:: [] list;

(* reverse needs to be implemented without using recursion directly *)

fun reverse2 nil = nil | reverse2 (x::xs) = (reverse2 xs) @ [x];

(* does not use foldl *)

(* fun reverse3(xs) =
	let
		fun aux(xs, acc) =
			case xs of
				[] => acc
			  | (x::xs') => aux(xs', x :: acc)
	in
		aux(xs, [])
	end *)

(* 2. Write a function composelist = ’a -> (’a -> ’a) list -> ’a which, given an initial value v
and a list of unary functions f1, . . . , fn, computes fn(. . . (f2(f1(v)))).
Example:
composelist 5 [ fn x => x+1, fn x => x*2, fn x => x-3 ];
val it = 9 : int
composelist "Hello" [ fn x => x ^ " World!", fn x => x ^ " I love", fn x => x ^ " PL!"];
val it = "Hello World! I love PL!" : string *)

fun composelist v nil = v
  | composelist v (x::xs) = composelist (x v) xs


(* 3. Write a function scan_left : (’a -> ’b -> ’a) -> ’a -> ’b list -> ’a list that returns
a list of each value taken by the accumulator during the processing of a fold.
For example:
scan_left (fn x => fn y => x+y) 0 [1, 2, 3]; would return [0, 1, 3, 6].

Hint: try starting with this curried definition of foldl:
fun myfoldl f y [] = y
| myfoldl f y (x::xs) = myfoldl f (f x y) xs; *)

(* this seems to be working even without the curried definition of foldl... *)

fun scan_left plus x (hd::tl) = x::(scan_left plus (plus x hd) tl)
	| scan_left plus x [] = [x];

(* 4. Write a function zip: ’a list * b list -> (’a * ’b) list that takes a pair of lists (of equal
length) and returns the equivalent list of pairs. Raise the exception Mismatch if the lengths don’t
match. Example:

- zip ([1,2,3,4,5], ["a","b","c","d","e"]);
val it = [(1,"a"),(2,"b"),(3,"c"),(4,"d"),(5,"e")] : (int * string) list*)

exception Mismatch
fun zip ([],    [])    = []
  | zip (x::xs, y::ys) = (x,y) :: zip (xs,ys)
  | zip _              = raise Mismatch;

 (* 5. Write a function unzip : (’a * ’b) list -> ’a list * ’b list that turns a list of pairs (such
as generated with zip above) into a pair of lists. Example:
- unzip [(1,"a"),(5,"c"),(3,"e")];
val it = ([1,5,3],["a","c","e"]) : int list * string list *)

fun unzip [] = ([], [])
  | unzip ((x,y)::xys)  =
      let val (xs,ys) = unzip xys in (x::xs,y::ys) end;

(* 6. Write a function bind = fn : ’a option -> ’b option -> (’a -> ’b -> ’c) -> ’c option
which, given two option arguments x and y, evaluates to f x y on the two arguments, provided
neither x nor y are NONE. Otherwise, the function should evaluate to NONE. Examples:
(* Define a method that operates on ordinary int arguments
We choose add purely for the sake of example. *)
fun add x y = x + y;
val add = fn : int -> int -> int
bind (SOME 4) (SOME 3) add;
val it = SOME 7 : int option
bind (SOME 4) NONE add;
val it = NONE : int option *)

(* this is here just so I don't have to define it every time *)
fun add x y = x + y;

(* fun bind (NONE)          (NONE)          f = NONE
  | bind (SOME option_1) (NONE)          f = NONE
  | bind (NONE)          (SOME option_2) f = NONE
  | bind (SOME option_1) (SOME option_2) f = (f option_1 option_2) *)

fun bind (SOME x) (SOME y) f = SOME(f x y)
  | bind (NONE) (SOME y) f = NONE
  | bind (SOME x) (NONE) f = NONE
  | bind (NONE) (NONE) f = NONE

(* 7. Write a function getitem = fn :int -> ’a list -> ’a option which, given an integer n and a
list, evaluates to the nth item in the list, assuming the first item in the list is at position 1. If the
value v exists then it evaluates to SOME v, or otherwise evaluates to NONE. Examples:
getitem 2 [1,2,3,4];
val it = SOME 2 : int option
getitem 5 [1,2,3,4];
val it = NONE : int option *)

fun getitem _ nil = NONE
  | getitem n (h::t) = if n < 0 then NONE
  else if n=0 then SOME h else getitem (n-1) t


(* 8. Write a function getitem2 = fn : int option -> ’a list -> ’a option. This is similar to
above, but instead of accepting an int as the first argument, it accepts int option. The function
should evaluate to NONE if NONE is passed as an argument, and behave as above otherwise. Examples:
getitem2 (SOME 2) [1,2,3,4];
val it = SOME 2 : int option
getitem2 (SOME 5) [1,2,3,4];
val it = NONE : int option
getitem2 NONE [1,2,3];
val it = NONE : int option
getitem2 (SOME 5) [];
stdIn:251.1-251.20 Warning: type vars not generalized because of
value restriction are instantiated to dummy types (X1,X2,...)
val it = NONE : ?.X1 option
(* Oops. Let’s try this instead *)
getitem2 (SOME 5) ([] : int list);
val it = NONE : int option
Hint: this should follow the same idea as the bind function, but should fix the underlying routine
as getitem.
*)

fun getitem2 (SOME _) nil = NONE
  | getitem2 NONE nil = NONE
  | getitem2 NONE (h::t) = NONE
  | getitem2 (SOME n) (h::t) = if n < 0 then NONE
  else if n=1 then SOME h else getitem2 ((SOME (n-1))) t
