signature MLPQUEUE =
sig

exception Overflow
exception Empty
exception LevelNoExist
exception NotFound

val maxlevel : int
type 'a mlqueue
val empty : 'a mlqueue
val enqueue : 'a mlqueue -> int -> int -> 'a -> 'a mlqueue
val dequeue : 'a mlqueue -> 'a * 'a mlqueue
val move : ('a -> bool) -> 'a mlqueue -> 'a mlqueue
val atlevel : 'a mlqueue -> int -> (int * 'a) list
val lookup :  ('a -> bool) -> 'a mlqueue -> int * int
val isempty : 'a mlqueue -> bool
val flatten :  'a mlqueue -> 'a list
end;

signature SIG =
sig
val maxlevel :int
end;

functor MakeQ (im : SIG
		): MLPQUEUE =
struct
exception Overflow
exception Empty
exception LevelNoExist
exception NotFound
val maxlevel = im.maxlevel
datatype 'a mlqueue = N | Q of (int * int * 'a) list;
val empty = (Q[ ])
fun enqueue (Q[]) l p v = if (l > im.maxlevel) then raise LevelNoExist else Q[(l,p,v)]
    | enqueue (Q((x,y,z)::xs)) l p v  = if (x>l) then (Q((l,p,v)::(x,y,z)::xs))
                                        else if (l=x andalso p<y) then Q((l,p,v)::(x,y,z)::xs)
                                        else
                                        let
                                           val Q (L) = enqueue (Q xs)  l p v ;
                                           in
                                           Q ((x,y,z)::L)
                                                    end;
fun dequeue (Q []) = raise Empty
        | dequeue (Q((l,p,v)::xs)) = (v, Q xs);
fun move pred (Q elems) =
        let fun enq ((l,p,v), q) = enqueue q (if pred v then l+1 else l) p v
        in foldl enq (Q []) elems end;
fun atlevel  (Q []) level = if level > im.maxlevel then raise LevelNoExist else []
        | atlevel (Q((l,p,v)::xs)) level = if (level=l) then (p,v) :: atlevel (Q xs) level
                                                else atlevel (Q xs ) level;
fun lookup pred (Q []) = raise NotFound
        | lookup pred (Q((l,p,v)::xs)) = if pred (v) then (l,p) else  lookup pred (Q xs);
fun isempty (Q[]) = true
        | isempty (Q(s::xs)) = false;
fun flatten (Q []) = raise Empty
        | flatten (Q((l,p,v)::[])) = [v]
        | flatten (Q((l,p,v)::xs)) =
                v :: flatten (Q xs);
end;
