# 🚀 UAS Optimization Methods – Particle Swarm Optimization

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uaspsoprogram2.streamlit.app/) https://uaspsoprogram2.streamlit.app/

Implementasi **Particle Swarm Optimization (PSO)** untuk **Ujian Akhir Semester (UAS) Optimization Methods**.  
Project ini dirancang **sesuai rubrik penilaian** dan terintegrasi penuh antara **Excel, Python, dan Streamlit**.

<img width="1915" height="919" alt="image" src="https://github.com/user-attachments/assets/f1a7a48f-dfb6-4395-8384-dddbec65650d" />


---

## 📋 Deskripsi Project

Project ini bertujuan untuk:
- Memahami konsep **Particle Swarm Optimization (PSO)** secara matematis
- Mengimplementasikan algoritma **PSO secara manual (Excel)** dan **programatis (Python)**
- Menyajikan hasil dalam bentuk **aplikasi web interaktif (Streamlit)**

✅ **diajukan untuk memenuhi penilaian UAS**

---

## 🎯 Fitur Aplikasi Live (Program 2)

- 📊 Visualisasi dataset partikel secara real-time  
- ⚙️ Parameter interaktif:
  - Jumlah Partikel
  - Jumlah Iterasi
  - Inertia Weight (w)
  - Cognitive Coefficient (c1)
  - Social Coefficient (c2)
- 📈 Visualisasi pergerakan partikel menuju solusi optimal
- 🔮 Prediksi posisi terbaik
- 📱 Tampilan web responsif

🌐 **Live App:**  
👉 [PSO Simulation: Interactive Particle Swarm Optimization](https://uaspsoprogram2.streamlit.app/)

---

## 📁 Struktur Folder

```
UAS_OptimizationMethods/
├── pso_interactive.py   # ✨ Streamlit App
├── requirements.txt     # Dependency
└── README.md            # Dokumentasi project
```

---

# 🌟 Particle Swarm Optimization (PSO) Interactive Simulation

A Python-based interactive application built with **Streamlit** to simulate and visualize the Particle Swarm Optimization (PSO) algorithm in real-time.

## 📖 Algorithm Overview

**Particle Swarm Optimization (PSO)** is a heuristic optimization algorithm inspired by the social behavior of birds flocking or fish schooling. It is used to find the best solution to an optimization problem by iteratively moving particles in the search space.

### PSO Steps:
1.  **Initialize**: Particles are generated with random positions and velocities.
2.  **Evaluate**: Each particle tracks its personal best position (`P_best`), and the swarm tracks the global best position (`G_best`).
3.  **Update**: At each iteration, velocity and position are updated based on `P_best`, `G_best`, and random factors.
4.  **Repeat**: The process repeats for a defined number of iterations to find the optimal solution.

---

## 🚀 How to Run the Application

Follow these steps to get the application running on your local machine:

1.  **Clone or download** this repository.
2.  **Install the required packages** by running the following command in your terminal:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Save the Python script** (ensure your main file is named `pso_interactive.py`).
4.  **Run the Streamlit app**:
    ```bash
    streamlit run pso_interactive.py
    ```
5.  The app will automatically open in your default web browser!

---

## 📝 How to Use the Application

### 1. Enter Initial Positions
In the **"Initial Positions"** input field, define the starting coordinates for each particle.
* **Format:** `x,y; x,y; ...`
* **Example (for 2 particles):** `3,7; 2,5`

### 2. Adjust PSO Parameters
Use the **sidebar** menu to tweak the simulation settings:
* Number of Particles
* Number of Iterations
* Inertia Weight
* Cognitive Coefficient
* Social Coefficient

### 3. Click "ctrl+enter" 
After setting up, Click "ctrl+enter". The simulation will start, and particles will move toward the optimal solution.

### 4. View Results
Analyze the final output, including the **Final Best Position** and the **Distance to Target**.

---

## 🎨 Visuals & 📈 Example Output

The application provides real-time graphical visualization of the swarm's behavior:

* **2D Space Plot**: Shows particle movement dynamically.
* 🔴 **Target Position**: Marked in red.
* 🟢 **Best Position**: The optimal solution found is marked in green.
* **Metrics**: Displays the best position and distance to the target for each iteration.

---

## 📂 Project Structure

```text
.
├── pso_interactive.py  # Main Streamlit app file
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```

---

## 👤 Author

**Suci Fransisca Sisilia**
