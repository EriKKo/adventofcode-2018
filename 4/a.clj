(defn date
  [line]
  (re-find #"\[.*\]" line))

(defn guard-id
  [line]
  (re-find #"#\d+" line))

(defn minute
  [line]
  (. Integer parseInt (subs (re-find #":\d+" line) 1)))

(defn asleep
  [line]
  (boolean (re-find #"asleep" line)))

(defn wakes
  [line]
  (boolean (re-find #"wakes" line)))

(defn apply-sleep
  [counts id start end]
  (assoc counts id (reduce
    (fn [c m] (assoc c m (+ (c m) 1)))
    (if (counts id) (counts id) (into [] (repeat 60 0)))
    (range start end))))

(defn create-summary
  [log]
  (loop [index 0 id "" m 0 counts {}]
    (if (= index (count log))
      counts
      (let [line (log index) newId (guard-id line)]
        (if newId
          (recur (+ index 1) newId m counts)
          (if (asleep line)
            (recur (+ index 1) id (minute line) counts)
            (recur (+ index 1) id m (apply-sleep counts id m (minute line)))))))))
  
(println (let [summary (create-summary (into [] (sort-by date (line-seq (java.io.BufferedReader. *in*)))))
  best-guy (apply max-key #(reduce + (summary %)) (keys summary))
  best-minute (apply max-key #((summary best-guy) %) (range (count (summary best-guy))))]
  (* (. Integer parseInt (subs best-guy 1)) best-minute)))
