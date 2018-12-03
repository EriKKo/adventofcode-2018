(defn common
  [a b]
  (map #(a %) (filter #(= (a %) (b %)) (range (count a)))))

(println (filter (complement nil?) (let [ids (into [] (line-seq (java.io.BufferedReader. *in*)))]
  (for [i (range (count ids)) j (range (count ids))]
    (let [base (common (into [] (ids i)) (into [] (ids j)))]
      (if (= (count base) (- (count (ids i)) 1)) (clojure.string/join base)))))))
