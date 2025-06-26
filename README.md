# 📘 README.md - Simulador de Bonificaciones

## 🎯 Descripción del Proyecto
Esta aplicación full stack permite simular la asignación de bonificaciones para pedidos que incluyen productos del grupo **"JUGOS"**. Por cada **10 unidades compradas** de productos de este grupo, se otorgan **2 unidades de bonificación**, distribuidas proporcionalmente.

Se ha desarrollado bajo principios **SOLID** y siguiendo una estructura de **Clean Architecture** para una separación clara de responsabilidades.

---

## ⚙️ Tecnologías Utilizadas

- **Backend:** Python 3.10+, Flask, Flask-CORS
- **Frontend:** HTML5, CSS3, JavaScript vanilla
- **Pruebas:** unittest

---

## 🧪 Lógica de Bonificación

1. Se filtran los productos del grupo `"JUGOS"`.
2. Por cada 10 unidades, se otorgan 2 unidades de bonificación.
3. Las bonificaciones se distribuyen proporcionalmente entre los productos del grupo.
4. El total siempre se redondea y respeta el total máximo de bonificaciones.

Ejemplo:
```json
Entrada:
[
  { "codigo": "PROD_A", "grupo": "JUGOS", "cantidad": 12 },
  { "codigo": "PROD_B", "grupo": "JUGOS", "cantidad": 8 },
  { "codigo": "PROD_C", "grupo": "AGUA", "cantidad": 5 }
]

Salida:
[
  { "codigo": "PROD_A", "bonificacion": 2 },
  { "codigo": "PROD_B", "bonificacion": 2 }
]
```

---

## 🚀 Instalación desde Cero

### 1. ✅ Instalar Python

Descargar Python desde: https://www.python.org/downloads/

Verifica la instalación:
```bash
python --version
```

### 2. ✅ Clonar o copiar el proyecto

```bash
cd proyecto_bonificaciones
```

### 3. ✅ Crear entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# o
source venv/bin/activate  # macOS/Linux
```

### 4. ✅ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. ✅ Ejecutar el servidor
```bash
python app.py
```

---

## 🧪 Probar el Backend (Postman / curl)

### Endpoint
```
POST http://127.0.0.1:5000/simular
```

### Body (JSON):
```json
[
  { "codigo": "A", "grupo": "JUGOS", "cantidad": 12 },
  { "codigo": "B", "grupo": "JUGOS", "cantidad": 8 }
]
```

### Respuesta esperada:
```json
[
  { "codigo": "A", "bonificacion": 2 },
  { "codigo": "B", "bonificacion": 2 }
]
```

---

## 🖥️ Probar el Frontend

1. Ejecuta el backend (`python app.py`)
2. Abre el archivo:
```
frontend/index.html
```
3. Agrega productos, haz clic en **Simular** y observa el resultado.

---

## ✅ Ejecutar pruebas

```bash
python -m unittest discover tests
```

---

## 🧱 Estructura del Proyecto (Clean Architecture)
```
proyecto_bonificaciones/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── frontend/
│   └── index.html
├── main/
│   ├── adapters/
│   │   └── controllers.py
│   ├── domain/
│   │   ├── entities.py
│   │   └── services.py
│   └── use_cases/
│       └── simulate.py
└── tests/
    └── test_services.py
```

---

## 👨‍💻 Autor
**Christian Ruiz** — Prueba Técnica Full Stack – Bonificaciones 2025
