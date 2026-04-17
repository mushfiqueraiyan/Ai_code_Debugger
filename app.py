import streamlit as st
from PIL import Image
from api_calling import debugCode


st.title("Your AI Code Debugger")
st.write("Solve your code error by sending screenshots!")

with st.sidebar:
    st.header("Dashboard")

    images = st.file_uploader("Upload your error image",
                              type=['jpg','jpeg', 'png'],
                              accept_multiple_files=True)
    
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)


    if pil_images:
         if len(pil_images) > 3:
            st.error("You can able to add only 3 images of error")
         else:
            col = st.columns(len(pil_images))

            for i, image in enumerate(images):
                with col[i]:
                    st.image(img)       

    options = st.selectbox("Select a Option", ("Hint", "Full Code"))

    pressed = st.button("Start Debugging", type="primary")


if pressed:
    if not images:
        st.error("Please at least one image")
    else:
       with st.container(border=True):
          with st.spinner("Your code is Cooking"):  
            st.subheader("Your Resolved code")
            solvedCode = debugCode(pil_images,options)     
            st.markdown(solvedCode)   

