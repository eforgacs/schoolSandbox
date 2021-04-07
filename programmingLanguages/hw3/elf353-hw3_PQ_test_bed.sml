(*Question 1: Use the functor above to instantiate a structure with maximum level set to 2 (i.e., 0, 1, 2) and
int as the underlying type.
*)
structure RegInt = struct val maxlevel = 2 end;
(* structure RegInt : sig
  val maxlevel : int
end *)

structure maxLevel2PQueue = MakeQ(RegInt);
(* structure maxLevel2PQueue : MLPQUEUE *)

val i = maxLevel2PQueue.maxlevel;
(* val i = 2 : int *)

(*
Question 2: Enqueue the following elements (in the given sequence) in the queue (where q is the queue).
The queue resulting from any given enqueue call should be passed to the next expression
so that the operations are cumulative. For this example we assume your structure is named
maxLevel2PQueue:
(a) maxLevel2PQueue.enqueue q 1 1 2
(b) maxLevel2PQueue.enqueue q 0 0 3
(c) maxLevel2PQueue.enqueue q 2 0 5
(d) maxLevel2PQueue.enqueue q 2 2 1
(e) maxLevel2PQueue.enqueue q 1 0 4
(f) maxLevel2PQueue.enqueue q 2 1 6
*)
val q = maxLevel2PQueue.empty;
(* val q = Q [] : 'a maxLevel2PQueue.mlqueue *)

(*2a*)
val q = maxLevel2PQueue.enqueue q 1 1 2;
(* val q = Q [(1,1,2)] : int maxLevel2PQueue.mlqueue *)

(*2b*)
val q = maxLevel2PQueue.enqueue q 0 0 3;
(* val q = Q [(0,0,3),(1,1,2)] : int maxLevel2PQueue.mlqueue *)

(*2c*)
val q = maxLevel2PQueue.enqueue q 2 0 5;
(* val q = Q [(0,0,3),(1,1,2),(2,0,5)] : int maxLevel2PQueue.mlqueue *)

(*2d*)
val q = maxLevel2PQueue.enqueue q 2 2 1;
(*val q = Q [(0,0,3),(1,1,2),(2,0,5),(2,2,1)] : int maxLevel2PQueue.mlqueue*)

(*2e*)
val q = maxLevel2PQueue.enqueue q 1 0 4;
(* val q = Q [(0,0,3),(1,0,4),(1,1,2),(2,0,5)] : int maxLevel2PQueue.mlqueue *)

(*2f*)
val q = maxLevel2PQueue.enqueue q 2 1 6;
(* val q = Q [(0,0,3),(1,0,4),(1,1,2),(2,0,5),(2,1,6)] :
  int maxLevel2PQueue.mlqueue *)

(*
Question 3: Raise an exception when element is enqueued at a level exceeding the maxlevel of the queue.
*)
val q = maxLevel2PQueue.enqueue q 3 1 4;
(* uncaught exception LevelNoExist
  raised at: elf353-hw3_PQ2.sml:36.59-36.71 *)


(*
Question 4: Move all the elements which are greater than 3 to the next lower level.
*)
val q = maxLevel2PQueue.move (fn v => v>3) q;
(*
uncaught exception LevelNoExist
  raised at: elf353-hw3_PQ2.sml:36.59-36.71
*)

(*
Question 5: Dequeue two elements from the queue.
*)
val (d,q) = maxLevel2PQueue.dequeue q;
(*
val d = 3 : int
val q = Q [(1,0,4),(1,1,2),(2,0,5),(2,1,6)] : int maxLevel2PQueue.mlqueue
*)

val (d,q) = maxLevel2PQueue.dequeue q;
(*
val d = 4 : int
val q = Q [(1,1,2),(2,0,5),(2,1,6)] : int maxLevel2PQueue.mlqueue
*)

(*
Question 6: Query the priority queue for level 1.
*)
val z = maxLevel2PQueue.atlevel q 1;
(* val z = [(1,2)] : (int * int) list *)

(*
Question 7: Find the first element whose value is less than 5.
*)
val l = maxLevel2PQueue.lookup (fn v => v<5) q;
(* val l = (1,1) : int * int *)
