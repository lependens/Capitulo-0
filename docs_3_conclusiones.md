En el estudio presentado, se evalúa la aplicación de diferentes **modelos de redes neuronales artificiales (ANN)** para estimar la evapotranspiración de referencia ($ET_0$) en las Islas Baleares. Estos modelos se comparan con ecuaciones empíricas (Hargreaves, Hargreaves y Samani, y Valiantzas) que utilizan los mismos datos de entrada. El análisis se enfoca en el rendimiento de los modelos y en la fiabilidad de la metodología de validación.

---

### Conclusiones Principales del Estudio

* **Rendimiento de los Modelos**: Los modelos de redes neuronales demostraron ser consistentemente superiores a las fórmulas empíricas en la estimación de la $ET_0$, logrando un error menor. La mejor combinación de datos de entrada para la red neuronal, según el indicador AARE (Error Relativo Absoluto Medio), fue la que incluyó la temperatura máxima, mínima, media, la radiación extraterrestre y la humedad relativa.
* **Importancia de la Metodología de Validación**: El estudio resalta la crucial importancia de utilizar una técnica de validación por partes, como el **k-fold**. Esta metodología evita que los resultados y las conclusiones sean sesgados por la selección de un único conjunto de datos de prueba, como ocurre en el método "hold-out". Se demostró que un conjunto de datos no representativo, como el de la estación de Ciutadella con pocos registros, puede distorsionar significativamente los resultados globales, lo que subraya la necesidad de una validación exhaustiva.

---

### Resumen Global

En resumen, este estudio valida la eficacia de las redes neuronales artificiales como una herramienta precisa para estimar la $ET_0$, superando a los métodos empíricos tradicionales. La clave para obtener resultados fiables y robustos es la aplicación de una metodología de validación rigurosa, como el k-fold, que asegura que la evaluación del modelo se base en un rendimiento consistente a través de múltiples subconjuntos de datos, en lugar de depender de un único conjunto de prueba. Esto garantiza que las conclusiones sobre la capacidad de los modelos sean fiables.