#!/usr/bin/env clojure -M 

; Advent of code 2022, AoC day 1.
; This solution (clojure 1.11) by kannix68, @ 2022-12-01.

(require '[clojure.string :as str]) ; clj str ops
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

;** problem solution
(defn read-dataset [s]
  "Read/convert data string into list-of-list of integers."
  (let [
    lst (str/split (str/trim s) #"\r?\n\r?\n")  ; outer split on empty lines
    lst2 (map #(str/split % #"\r?\n") lst)  ; inner split on newlines
    ]
    (map #(map read-string %) lst2)  ; map inner string elements (level 2) to int
  )
)

(defn solve-day01-pt1 [s]
  (let [
    lst (read-dataset s)
    lstred (map #(reduce + %) lst)
    ]
    (apply max lstred)
  )
)

(defn solve-day01-pt2 [s]
  (let [
    lst (read-dataset s)
    lstred (map #(reduce + %) lst)  ; inner sums
    lstfin (reverse (sort lstred))  ; sort by values descending
    ]
    (reduce + (take 3 lstfin))  ; sum of largest 3 elements
  )
)

;** test data (as a var(iable))
(def teststr "
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
")

;** MAIN

(assert-eq-msg 24000 (solve-day01-pt1 teststr) "pt 1 test result")

(def datastr (slurp "./in/day01.in"))

(println "day 01 pt 1 result=" (solve-day01-pt1 datastr))

(assert-eq-msg 45000 (solve-day01-pt2 teststr) "pt 2 test result")

(println "day 01 pt 2 result=" (solve-day01-pt2 datastr))
