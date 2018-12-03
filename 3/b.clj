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

(let [
  fabrics (map parse-line (line-seq (java.io.BufferedReader. *in*)))
  board (fill-board fabrics)]
  (println
    (first
      (map
        (fn [[id]] id)
        (filter
          (fn [[_ x y w h]]
            (every?
              (fn [[r c]] (= ((board r) c) 1))
              (for [r (range x (+ x w)) c (range y (+ y h))] [r c])))
          fabrics)))))
