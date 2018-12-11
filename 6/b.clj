(def MAX-DIST 10000)

(defn count-points
  [points]
  (let
    [minX (apply min (map first points))
    maxX (apply max (map first points))
    minY (apply min (map second points))
    maxY (apply max (map second points))]
    (count (filter
      #(< % MAX-DIST)
      (for [x (range minX (+ maxX 1)) y (range minY (+ maxY))]
        (reduce + (map
          (fn [[px py]] (+ (Math/abs (- x px)) (Math/abs (- y py))))
          points)))))))

(let
  [points (map
    (fn [line] (map #(. Integer parseInt %) (clojure.string/split line #", ")))
    (line-seq (java.io.BufferedReader. *in*)))]
  (println (count-points points)))
