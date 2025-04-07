## 📌 Descripción del Problema

Breve descripción del problema de negocio y objetivo del proyecto.  
Ejemplo: Predecir las ventas de videojuegos en América del Norte a partir de datos históricos.

## 📊 Dataset

- **Nombre:** Video Game Sales
- **Fuente:** Kaggle
- **Tamaño original:** 16k filas, 11 columnas
- **Muestra incluida:** `src/data_sample/vgsales_sample.csv` (limitada a 5MB)

## 🧠 Solución Adoptada

- Modelos probados: Regresión Lineal, KNN, Árboles de Decisión, Stacking
- Mejor rendimiento: Stacking con Gradient Boosting como meta-modelo
- Métricas: R² y MSE
- Visualización de rendimiento incluida en el notebook final
