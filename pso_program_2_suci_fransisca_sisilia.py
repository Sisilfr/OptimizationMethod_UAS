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
st.title('PSO Simulation: Interactive Particle Swarm Optimization')

# Upload file Excel
uploaded_file = st.file_uploader("Upload Excel file with particle positions", type=["xlsx"])

if uploaded_file is not None:
    # Membaca file Excel yang diunggah
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')  # Pastikan menggunakan openpyxl untuk membaca Excel

        # Menampilkan data yang ada di Excel (Posisi X dan Posisi Y)
        st.write("Initial Particle Positions from Excel:")
        st.dataframe(df)

        # Mengambil data posisi dan kecepatan dari Excel
        positions_input = df[['Posisi X', 'Posisi Y']].values  # Mengambil posisi X dan Y
        velocities = np.random.uniform(-0.5, 0.5, positions_input.shape)  # Kecepatan acak

        # Target position (fixed as 10, 10)
        target_position = np.array([10, 10])

        # Initial P_best and G_best
        p_best_positions = positions_input.copy()
        p_best_values = np.linalg.norm(positions_input - target_position, axis=1)
        g_best_position = positions_input[np.argmin(p_best_values)]
        g_best_value = np.min(p_best_values)

        # Input untuk jumlah partikel dan iterasi
        num_particles = len(positions_input)
        num_iterations = 10  # Iterasi yang tetap

        # Run PSO simulation
        for iteration in range(num_iterations):
            for i in range(num_particles):
                # Calculate distance to target for each particle
                distance = calculate_distance(positions_input[i], target_position)
                
                # Update P_best if found better position
                if distance < p_best_values[i]:
                    p_best_positions[i] = positions_input[i]
                    p_best_values[i] = distance
            
            # Update G_best
            best_particle_index = np.argmin(p_best_values)
            g_best_position = p_best_positions[best_particle_index]
            g_best_value = p_best_values[best_particle_index]
            
            # Update positions and velocities
            positions_input, velocities = update_velocity_and_position(positions_input, velocities, p_best_positions, g_best_position)

            # Visualization
            fig, ax = plt.subplots()
            ax.set_xlim(0, 12)
            ax.set_ylim(0, 12)
            ax.scatter(positions_input[:, 0], positions_input[:, 1], color='blue', label="Particles")
            ax.scatter(target_position[0], target_position[1], color='red', label="Target")
            ax.scatter(g_best_position[0], g_best_position[1], color='green', label="Best Position")

            ax.set_title(f"Iteration {iteration + 1}")
            ax.set_xlabel("X")
            ax.set_ylabel("Y")
            ax.legend()

            # Display plot in Streamlit
            canvas = FigureCanvas(fig)
            canvas.draw()
            st.pyplot(fig)

            # Show text explanation
            st.write(f"Iteration {iteration + 1}: Best Position = {g_best_position}, Distance = {g_best_value:.4f}")

        # Final Results
        st.write(f"Final Best Position: {g_best_position}")
        st.write(f"Final Best Distance to Target: {g_best_value:.4f}")

    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
        st.stop()
