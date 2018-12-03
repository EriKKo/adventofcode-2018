(defn count-chars
  [s c]
  (count (filter #(= % c) s)))


(println
  (let [[a b] (reduce
    #(let [counts (into #{} (map (fn [c] (count-chars %2 c)) %2))]
      [(+ (%1 0) (if (contains? counts 2) 1 0))
      (+ (%1 1) (if (contains? counts 3) 1 0))])
    [0 0]
    (line-seq (java.io.BufferedReader. *in*)))]
    (* a b)))
