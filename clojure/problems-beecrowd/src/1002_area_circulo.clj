;; src/1002_area_circulo.clj
;; 1) lê o valor do raio
(def raio (Double/parseDouble (read-line)))

;; 2) calcula área
(def pi 3.14159)
(def area (* pi raio raio))

;; 3) imprime
(println (format "A=%.4f" area))
;(defn -main []
;      (let [pi 3.14159
;            raio (Double/parseDouble (read-line))
;            area (* pi raio raio)]
;           (println (format "A=%.4f" area))))
;
;(-main)
;(let [pi   3.14159
;      raio (Double/parseDouble (read-line))
;      area (* pi raio raio)]
;     (println (format "A=%.4f" area)))
