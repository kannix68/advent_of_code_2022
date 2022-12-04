#!/usr/bin/env clojure -M 

; Advent of code 2022, AoC day 2.
; This solution (clojure 1.11) by kannix68, @ 2022-12-02.

(require '[clojure.string :as str]) ; clj str ops
(require '[clojure.set]) ; clj str ops
(ns user (:use clojure.pprint))

;** helpers

(defn assert-msg [condit msg]
  "Check condition, fail with message on false, print message otherwise."
  (if (not condit)
    (assert condit (str "assert-ERROR:" msg))
    (println "assert-OK:" msg))
)

(defn assert-eq-msg [expected found msg]
  "Check expected = found, fail with message on false, print message otherwise."
  (let [tst (= expected found)]
    (if (not tst)
      (assert tst (str "assert-ERROR: expected=" expected ", found=" found ": " msg))
      (println "assert-OK: found=expected=" expected ": " msg))
  )
)

; seancorfield gist [map-vals and map-keys](https://gist.github.com/seancorfield/6e8dd10799e9cc7527da5510c739e52f)
;(defn map-vals [f m] (reduce-kv (fn [m k v] (assoc m k (f v))) {} m))
;(defn map-keys [f m] (reduce-kv (fn [m k v] (assoc m (f k) v)) {} m))

; [Is there an equivalent for the Zip function in Clojure Core or Contrib? - Stack Overflow](https://stackoverflow.com/questions/2588227/is-there-an-equivalent-for-the-zip-function-in-clojure-core-or-contrib)
(defn zip [l1 l2]
  "Provide sequence of 2-tuples combined from 2 lists."
  (map vector l1 l2)
)
;(defn zip [& colls]
;  (partition (count colls) (apply interleave colls)))

;** problem solution
(def values {"X"  1, "Y" 2, "Z", 3})

(def outcomes {
  "A" {"X" 3, "Y" 6, "Z" 0},
  "B" {"X" 0, "Y" 3, "Z" 6},
  "C" {"X" 6, "Y" 0, "Z" 3},
})

(defn read-dataset [s]
  "Read/convert data string into list-of-list of integers."
  (let [
    lst (str/split (str/trim s) #"\r?\n") ; split on newlines
    ]
    ;(str/split (str/trim s) #"\r?\n")
    (map #(str/split % #" ") lst)
  )
)

(defn solve-day02-pt1 [s]
  (let [
    lst (read-dataset s)
    mpvals (map #(values (get % 1)) lst)
    mpoutc (map #((outcomes (get % 0)) (get % 1)) lst)
    ]
    (+ (apply + mpvals) (apply + mpoutc))
  )
)

(def outcome_tags {"X"  0, "Y" 3, "Z", 6})

(defn solve-day02-pt2 [s]
  (let [
    outcomes-inv (update-vals outcomes #(clojure.set/map-invert %))  ; invert inner maps
    lst (read-dataset s)  ; read string into data structure
    mpoutc (map #(outcome_tags (get % 1)) lst)
    mpidxs (zip (map #(get % 0) lst) mpoutc)
    mpitems (map #((outcomes-inv (get % 0)) (get % 1)) mpidxs)
    mpvals (map #(get values %) mpitems)
    ]
    (+ (apply + mpvals) (apply + mpoutc))
  )
)

;** test data (as a var(iable))
(def teststr "
A Y
B X
C Z
")

;** MAIN

(assert-eq-msg 15 (solve-day02-pt1 teststr) "day 2 pt 1 test result")

(def datastr (slurp "./in/day02.in"))

(println "day 2 pt 1 result=" (solve-day02-pt1 datastr))

(assert-eq-msg 12 (solve-day02-pt2 teststr) "day 2 pt 2 test result")

(println "day 2 pt 2 result=" (solve-day02-pt2 datastr))
