
# 🎮 Predicción de Ventas de Videojuegos / Video Game Sales Prediction

## 🧠 Problema / Problem

**ES:**  
Queremos predecir las ventas de videojuegos en América del Norte (`NA_Sales`) usando variables como año, plataforma, género y ventas en otras regiones.  
**EN:**  
We aim to predict video game sales in North America (`NA_Sales`) using features such as year, platform, genre, and regional sales.

## 📊 Dataset

- Fuente / Source: Kaggle – Video Game Sales
- Tamaño / Size: 16,000 rows × 11 columns
- Target: `NA_Sales`

## 📁 Estructura del Repositorio / Repository Structure

```
src/
├── data_sample/         # Dataset reducido
├── img/                 # Imágenes del análisis
├── models/              # Script de modelado
├── notebooks/           # Notebooks de prueba
├── results_notebook/    # Notebook final
└── utils/               # Funciones auxiliares

README.md                # Este archivo, bilingüe
```

## 🛠️ Modelos / Models

- Regresión Lineal / Linear Regression  
- K-Nearest Neighbors  
- Árboles de Decisión / Decision Tree  
- Stacking con Gradient Boosting

## 📈 Métricas / Metrics

- R² Score
- Mean Squared Error (MSE)

## ✅ Resultados / Results

Modelo final (`Stacking + GradientBoosting`):  
- Entrenamiento: R² ~ 0.92  
- Test: R² ~ 0.88  

## 📌 Conclusiones / Conclusions

- El stacking mejora significativamente frente a modelos simples.
- El proyecto demuestra una aplicación práctica de ML en marketing.

## 📦 Requisitos / Requirements

```bash
pip install -r requirements.txt
```
