#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pycaret.regression import load_model, predict_model
from IPython import get_ipython
import pandas as pd
import numpy as np
import streamlit as st


# In[22]:




class StreamlitApp:
    
    def __init__(self):
        self.model = load_model('final_model')

    def predict(self, input_data):
        return predict_model(self.model, data=input_data)
    
    def store_prediction(self, output_df):
        if os.path.exists(self.save_fn):
            save_df = pd.read.csv(self.save_fn)
            save_df = save_df.append(output_df, ignore_index=True)
            save_df.to_csv(self.save_fn, index=False)
            
        else:
            output_df.to_csv(self.save_fn, index=False)
            
            
    def run(self):
        #image = Image.open('..assets/human-heart.jpg')
        #st.image(image, use_column_width=False)
        
        
        add_selectbox = st.sidebar.selectbox('How would you like to predict?', ('Online', 'Batch'))
        st.sidebar.info('This app is created to predict House prices' )
        st.sidebar.success('DAT158')
        st.title('House Price Prediction')
        
        
        if add_selectbox == 'Online':
            
            #Code here for input of values
            
            output =''
            input_dict = {} #Output data
            input_df = pd.DataFrame(input_dict, index=[0])
            
            if st.button('Predict'):
                output = self.predict(input_df)
                self.store_prediction(output)
                
                output = 'House Value prediction: ' # + predicted value of house
                
                
            st.success('Predicted output: {}'.format(output))
            
        if add_selectbox == 'Batch':
            fn = st.file_uploader("Upload csv file for predictions")
            if fn is not None:
                input_df = pd.read_csv(fn)
                predictions = self.predict(input_df)
                st.write(predictions)
        
sa = StreamlitApp()
sa.run()               


# In[21]:


#!jupyter nbconvert --to script Deployment_to_heroku.ipynb


# In[ ]:




