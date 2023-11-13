import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def calculate_power_triangle(voltage, current, phase_angle):
    # Calculate real, reactive, and apparent power
    real_power = voltage * current * np.cos(np.radians(phase_angle))
    reactive_power = voltage * current * np.sin(np.radians(phase_angle))
    apparent_power = voltage * current

    return real_power, reactive_power, apparent_power

def calculate_impedance_triangle(voltage, current, phase_angle):
    # Calculate real, reactive, and apparent power
    resistance = (voltage / current) * np.cos(np.radians(phase_angle))
    reactance = (voltage / current) * np.sin(np.radians(phase_angle))
    impedance = np.sqrt(resistance**2 + reactance**2)

    return resistance, reactance, impedance

def plot_power_triangle(real_power, reactive_power, apparent_power):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, apparent_power + 5)
    ax.set_ylim(0, apparent_power + 5)

    # Vertices of the power triangle
    vertices = [(0, 0), (real_power, 0), (real_power, reactive_power)]

    triangle = Polygon(vertices, closed=True, edgecolor='black', linewidth=2, fill=None)
    ax.add_patch(triangle)

    # Add labels
    ax.text(real_power / 2, -1, f'Real Power: {real_power:.2f}', ha='center')
    ax.text(real_power + 1, reactive_power / 2, f'Reactive Power: {reactive_power:.2f}', va='center', rotation=90)
    ax.text(real_power / 2, reactive_power / 2, f'Apparent Power: {apparent_power:.2f}', ha='center', va='center', rotation=30)

    ax.set_xlabel('Real Power')
    ax.set_ylabel('Reactive Power')

    st.pyplot(fig)

def plot_impedance_triangle(resistance, reactance, impedance):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, impedance + 5)
    ax.set_ylim(0, impedance + 5)

    # Vertices of the power triangle
    vertices = [(0, 0), (resistance, 0), (resistance, reactance)]

    triangle = Polygon(vertices, closed=True, edgecolor='black', linewidth=2, fill=None)
    ax.add_patch(triangle)

    # Add labels
    ax.text(resistance / 2, -1, f'Resistance: {resistance:.2f}', ha='center')
    ax.text(resistance + 1, reactance / 2, f'Reactance: {reactance:.2f}', va='center', rotation=90)
    ax.text(resistance / 2, reactance / 2, f'Impedance: {impedance:.2f}', ha='center', va='center', rotation=30)

    ax.set_xlabel('Resistance')
    ax.set_ylabel('Reactance')

    st.pyplot(fig)


def main():

    st.sidebar.markdown("Types of triangle : ")
    triangle_type = st.sidebar.radio('Select',['Power Triangle', 'Impedance Triangle'])

    if triangle_type == 'Power Triangle':
        st.subheader('Select the type of triangle in the sidebar : Impedance / Power')
        st.title('Power Triangle Calculator')
    # Input sliders for voltage, current, and phase angle
        voltage = st.slider('Voltage', min_value=0, max_value=100, value=50)
        current = st.slider('Current', min_value=0, max_value=100, value=25)
        phase_angle = st.slider('Phase Angle', min_value=-180, max_value=180, value=30)

        real_power, reactive_power, apparent_power = calculate_power_triangle(voltage, current, phase_angle)

        st.subheader('Power Triangle')
        plot_power_triangle(real_power, reactive_power, apparent_power)

    elif triangle_type == 'Impedance Triangle':
        st.subheader('Select the type of triangle in the sidebar : Impedance / Power')
        st.title('Impedance Triangle Calculator')
    # Input sliders for voltage, current, and phase angle
        voltage = st.slider('Voltage', min_value=0, max_value=100, value=10)
        current = st.slider('Current', min_value=0, max_value=100, value=5)
        phase_angle = st.slider('Phase Angle', min_value=-180, max_value=180, value=0)

        resistance, reactance, impedance = calculate_impedance_triangle(voltage, current, phase_angle)

        st.subheader('Impedance Triangle')
        plot_impedance_triangle(resistance, reactance, impedance)

if __name__ == '__main__':
    main()


# Copyright text at the bottom
st.sidebar.markdown(
    '<div style="text-align:center; margin-top: 370px">'
    '<a href = "https://pranavsuriya-sr.github.io/personalPortfolio/" style = "text-decoration: none;" ><p style="font-size: 10px;">PranavSuriya Devs © 2023 Project Hack Community.</a></p>'
    '<p style="font-size: 10px;">Open Source rights reserved.</p>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown(
        '<div style="text-align:center; margin-top: 42px">'
        '<a href = "https://pranavsuriya-sr.github.io/personalPortfolio/" style = "text-decoration: none;" ><p style="font-size: 10px;">PranavSuriya Devs © 2023 Project Hack Community.</a></p>'
        '<p style="font-size: 10px;">Open Source rights reserved.</p>'
        '</div>',
        unsafe_allow_html=True
    )