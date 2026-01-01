import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Fungsi untuk menghitung jarak ke target
def calculate_distance(position, target_position):
    return np.linalg.norm(position - target_position)

# Fungsi untuk memperbarui kecepatan dan posisi partikel
def update_velocity_and_position(positions, velocities, p_best_positions, g_best_position, w=0.8, c1=1.5, c2=1.5):
    r1 = np.random.random(positions.shape)
    r2 = np.random.random(positions.shape)
    
    # Update kecepatan
    velocities = (w * velocities
                  + c1 * r1 * (p_best_positions - positions)
                  + c2 * r2 * (g_best_position - positions))
    
    # Update posisi
    positions = positions + velocities
    return positions, velocities

# Streamlit Interface
st.set_page_config(page_title="PSO Simulation - Particle Swarm Optimization", layout="wide")
st.title('🚀 PSO Simulation: Interactive Particle Swarm Optimization')

# Sidebar untuk parameter input
st.sidebar.header("⚙️ Parameter PSO")
num_particles = st.sidebar.number_input("Number of Particles:", min_value=2, max_value=100, value=5)
num_iterations = st.sidebar.number_input("Number of Iterations:", min_value=1, max_value=100, value=10)
w = st.sidebar.slider("Inertia Weight (w)", 0.0, 1.0, 0.8)
c1 = st.sidebar.slider("Cognitive Coefficient (c1)", 0.0, 2.0, 1.5)
c2 = st.sidebar.slider("Social Coefficient (c2)", 0.0, 2.0, 1.5)

# Input untuk posisi awal partikel (bisa diisi manual oleh pengguna)
positions_input = st.text_area("Initial Positions (x, y) of particles (comma separated, e.g., 3,7;2,5;...):")

# Mengolah input posisi partikel yang dimasukkan oleh pengguna
def process_positions_input(positions_input):
    positions_list = []
    try:
        # Mengolah input menjadi tuple (x, y)
        positions = positions_input.split(';')  # Memisahkan partikel
        for pos in positions:
            x, y = pos.split(',')  # Memisahkan x dan y
            positions_list.append((int(x.strip()), int(y.strip())))  # Mengubah menjadi tuple dan menghapus spasi
        return positions_list
    except Exception as e:
        st.error(f"Error processing input: {e}")
        return []

positions_list = process_positions_input(positions_input)

# Jika format input salah, hentikan eksekusi
if not positions_list:
    st.stop()

positions = np.array(positions_list)
velocities = np.random.uniform(-0.5, 0.5, positions.shape)

# Target position (fixed as 10, 10)
target_position = np.array([10, 10])

# Initial P_best and G_best
p_best_positions = positions.copy()
p_best_values = np.linalg.norm(positions - target_position, axis=1)
g_best_position = positions[np.argmin(p_best_values)]
g_best_value = np.min(p_best_values)

# Run PSO simulation
for iteration in range(num_iterations):
    for i in range(num_particles):
        # Calculate distance to target for each particle
        distance = calculate_distance(positions[i], target_position)
        
        # Update P_best if found better position
        if distance < p_best_values[i]:
            p_best_positions[i] = positions[i]
            p_best_values[i] = distance
    
    # Update G_best
    best_particle_index = np.argmin(p_best_values)
    g_best_position = p_best_positions[best_particle_index]
    g_best_value = p_best_values[best_particle_index]
    
    # Update positions and velocities
    positions, velocities = update_velocity_and_position(positions, velocities, p_best_positions, g_best_position)

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.scatter(positions[:, 0], positions[:, 1], color='blue', label="Particles", s=60)
    ax.scatter(target_position[0], target_position[1], color='red', label="Target", s=100)
    ax.scatter(g_best_position[0], g_best_position[1], color='green', label="Best Position", s=150, marker="X")

    ax.set_title(f"Iteration {iteration + 1}", fontsize=16)
    ax.set_xlabel("X", fontsize=14)
    ax.set_ylabel("Y", fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Display plot in Streamlit
    canvas = FigureCanvas(fig)
    canvas.draw()
    st.pyplot(fig)

    # Show text explanation
    st.write(f"Iteration {iteration + 1}: Best Position = {g_best_position}, Distance = {g_best_value:.4f}")

# Final Results
st.write(f"### Final Best Position: {g_best_position}")
st.write(f"### Final Best Distance to Target: {g_best_value:.4f}")
