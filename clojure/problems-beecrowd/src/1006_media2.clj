(let [A (Double/parseDouble (read-line))
      B (Double/parseDouble (read-line))
      C (Double/parseDouble (read-line))
      media (/ (+ (* A 2) (* B 3) (* C 5)) 10.0)]
     (println (format "MEDIA = %.1f" media)))
