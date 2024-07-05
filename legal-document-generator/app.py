import streamlit as st
from document_generator import generate_doc, generate_pdf
import tempfile
import json
# Title displayed on the Streamlit Web App
st.set_page_config(page_title="Document Generator", page_icon=":tada", layout="wide")

# Header and Subheader dsiplayed in the Web App
with st.container():
    # setting the header of the application
    st.header("Contract Generation Assistant")
    # adding some spacing between headers
    st.subheader("")
    # setting the larger description of the application
    st.title("Add details about the document you want to create")

# Setup
with st.container():
    # configuring the first section to input the details you want the document to be generated based on
    st.write("---")
    st.write("")
    # the actual user input box where users can input the details for their document
    user_input = st.text_area("Document Details")

# Saving LLM response as variable
temp_llm_response = ""

# Create Buttons and start document generation workflow upon "Submit"
result = st.button("Generate Document")
# if a result is created by the LLM...
if result:
    # save the response as the llm_response
    llm_response = generate_doc(user_input)
    # write the LLM response to the front end so the user can see the first iteration
    st.markdown(llm_response['content'][0]['text'])
    # store the LLM response as the temporary llm response as this will be used to refine later
    temp_llm_response = llm_response
    
    # try:
    # Load and parse JSON input
    print('start pdf create')
        
    # print(llm_response)

    # Generate PDF
    pdf = generate_pdf(llm_response['content'][0]['text'])

    pdf_output = 'Consultancy_Services_Agreement.pdf'
    pdf.output(pdf_output)

    # Provide download link
    with open(pdf_output, 'rb') as f:
        st.download_button('Download PDF', f, file_name=pdf_output)

    # except Exception as e:
    #     st.error(f'Error generating PDF: {e}')    


# add a line of spacing in the front end app
st.write("---")

