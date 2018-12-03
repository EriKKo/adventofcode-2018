(println 
  (loop [
    value 0
    index 0
    nums (into [] (map #(. Integer parseInt %) (line-seq (java.io.BufferedReader. *in*))))
    mem {}]
    (if (mem value)
      value
      (recur
        (+ value (nums index))
        (if (= (+ index 1) (count nums)) 0 (+ index 1))
        nums
        (assoc mem value 1)))))
