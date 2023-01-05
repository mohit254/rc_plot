import streamlit as st
from RamachanDraw import fetch, phi_psi, plot
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Ramachandran Plot Generator", page_icon=":heart:")


st.text('This webapp is designed to help researchers and scientists obtain Ramachandran Plot through the protein database id (PDB id)')

st.title("Ramachandran Plot Generator")

st.markdown('''
A Ramachandran plot is a graphical representation of the conformations of peptides and proteins based on the values of their phi and psi angles. Phi and psi are dihedral angles that describe the conformation of a protein's main chain.

The phi angle is defined as the angle between the plane formed by the atoms N-C alpha-C and the plane formed by the atoms C alpha-N-C. The psi angle is defined as the angle between the plane formed by the atoms C alpha-N and the plane formed by the atoms N-C alpha-C.

Ramachandran plots are often used to analyze the conformational flexibility of proteins and to identify regions of a protein that are prone to structural perturbations. They are also used to identify structural anomalies and to predict the conformations of protein loops.

Ramachandran plots are typically generated by plotting the phi angles on the x-axis and the psi angles on the y-axis. The resulting plot is divided into regions, with each region corresponding to a different type of protein conformation. The most common 
''')


# PDB id to be downloaded
PDB_id = st.text_input("Enter the protein id(pdb id): ","1FAT")
if PDB_id:
  # Fetch the PDB file for the given ID
  pdb_file = fetch(PDB_id)

  # Generate the plot using Matplotlib
  plt.figure()
  plot(pdb_file)

  # Display the plot in the Streamlit app using st.pyplot
  # st.markkdown("##### Ramachandran PLot of given Protein: ")
  st.pyplot()
  st.write("[Special Thanks to Python Project RamachanDraw]('https://pypi.org/project/RamachanDraw/')") 
  
 # --- HERO SECTION ---
st.markdown("## Developed By: ")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://mohit254-portfolio-cv-t4bwqw.streamlit.app/~/+/media/511fd1351113b1b2f0acc6c65d463c50c4155c521ee6fce285af2566.png", width=230)

with col2:
    st.title("Mohit Poudel")
    st.write(""" Bioinformatics & population genetics enthusiast, self-taught python programmer """)
    st.markdown(" ### Agriculture and Forestry Univeresity")
    st.markdown(" #### Chitwan, Nepal")

# st.markdown("# Mohit Poudel")
# st.markdown("### Research Intern at the Centre for Biotechnology, Agriculture and Forestry University,Nepal")
# st.markdown("#### Please email for feedback and criticism to: poudelmohit59@gmail.com ")
st.markdown("##### [Know more about the developer !!](https://mohit254-portfolio-cv-t4bwqw.streamlit.app/#mohit-poudel)")

