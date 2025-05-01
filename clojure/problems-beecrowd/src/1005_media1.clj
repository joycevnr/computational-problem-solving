(def A (Double/parseDouble (read-line)))
(def B (Double/parseDouble (read-line)))
(def media (/ (+ (* A 3.5) (* B 7.5)) 11.0))

(println (format "MEDIA = %.5f" media))
;;para rodar:  "echo -e "5.0\n7.1" | clojur
;e -M src/1005_media1.clj" ou sem o echo
;
;(let [A (Double/parseDouble (read-line))
;      B (Double/parseDouble (read-line))
;      media (/ (+ (* A 3.5) (* B 7.5)) 11.0)]
;     (println (format "MEDIA = %.5f" media)))
;
;
;(let [entrada (clojure.string/split (read-line) #" ")
;      A (Double/parseDouble (nth entrada 0))
;      B (Double/parseDouble (nth entrada 1))
;      media (/ (+ (* A 3.5) (* B 7.5)) 11.0)]
;     (println (format "MEDIA = %.5f" media)))

;;read-line: lê uma linha de entrada como "5.0 7.1"
;;clojure.string/split ... #" ": separa a linha em ["5.0" "7.1"]
;;nth entrada 0 e nth entrada 1: pega os valores separadamente
;;Double/parseDouble: converte as strings para números