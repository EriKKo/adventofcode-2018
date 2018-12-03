(def SIZE 1000)

(defn fill-board
  [fabrics]
  (reduce
    (fn [board [_ x y w h]]
      (reduce
        (fn [b [r c]] (assoc b r (assoc (b r) c (+ ((b r) c) 1))))
        board
        (for [i (range x (+ x w)) j (range y (+ y h))] [i j])))
    (into [] (repeat SIZE (into [] (repeat SIZE 0))))
    fabrics))

(defn parse-line
  [line]
  (map #(. Integer parseInt %) (re-seq #"\d+" line)))

(defn count-overlap
  [board]
  (reduce
    (fn [cnt row] (+ cnt (count (filter #(> % 1) row))))
    0
    board))

(println 
  (count-overlap 
    (fill-board 
      (map
        parse-line
        (line-seq (java.io.BufferedReader. *in*))))))
