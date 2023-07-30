import streamlit as st

st.markdown("# Hardware")









st.markdown("## GPU")

col1, col2 = st.columns(2)
with col1:
    st.write("NVIDIA H100 SXM ----------------")
with col2:
    st.write("GPU Memory: 80GB")
    st.write("GPU Memory Bandwidth: 3.35TB/s")
    st.write("Max Flops: 3,958")
    st.write("RAM: ")

st.write("")

col1, col2 = st.columns(2)
with col1:
    st.write("NVIDIA H100 PCIe ---------------")
with col2:
    st.write("GPU Memory: 80GB")
    st.write("GPU Memory Bandwidth: 2TB/s")
    st.write("Max Flops: 3,026")
    st.write("RAM: ")

st.write("")

col1, col2 = st.columns(2)
with col1:
    st.write("NVIDIA A100 80GB PCIe ----------")
with col2:
    st.write("GPU Memory: 80GB")
    st.write("GPU Memory Bandwidth: 1,935 GB/s")
    st.write("Max Flops: 312")
    st.write("RAM: ")

st.write("")

col1, col2 = st.columns(2)
with col1:
    st.write("NVIDIA A100 80GB SXM -----------")
with col2:
    st.write("GPU Memory: 80GB")
    st.write("GPU Memory Bandwidth: 2,039 GB/s")
    st.write("Max Flops: 624")
    st.write("RAM: ")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")









st.markdown("## Rent")

col1, col2 = st.columns(2)
with col1:
    st.write("H100 ---------------------------")
with col2:
    st.write(
        """
        <div style="width:100%">
        <a href="https://www.tensorflow.org/overview" style="float:center">Link</a>
        </div>
        """, 
        unsafe_allow_html=True
        )

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")