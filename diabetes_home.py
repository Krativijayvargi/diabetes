# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    #st.set_page_config(page_title='Early diabetes prediction Web App',page_icon=':random:',layout='centered',intial_sidebar_state='auto') 
    # Provide a brief description for the web app.
    st.write('''Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
    There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
    This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.''')

    # Add the 'beta_expander' to view full dataset 
    with st.beta_expander("View Dataset"):
       st.table(diabetes_df)
    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    st.subheader('Columns Description:')
    col1,col2,col3 = st.beta_columns(3)

    with col1:
      if st.checkbox('View all column names'):
        st.table(list(diabetes_df.columns))
    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with col2:
      if st.checkbox('View Column data-type'):
        st.table(list(diabetes_df.dtypes))
    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with col3:
      if st.checkbox('View column data'):
        column_data = st.selectbox('Select Column',('Pregnancies','Glucose','Blood_Pressure','Skin_Thickness','Insulin','BMI','Pedigree_Function','Age','Outcome'))
        st.write(diabetes_df[column_data])
    if st.checkbox('Show summary'):
      st.table(diabetes_df.describe())