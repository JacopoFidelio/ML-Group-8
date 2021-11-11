#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pycaret.regression import load_model, predict_model
from IPython import get_ipython
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


# In[5]:




class StreamlitApp:
    
    def __init__(self):
        self.model = load_model('final_model')

    def predict(self, input_data):
        return predict_model(self.model, data=input_data)
              
    def run(self):
        
        
        add_selectbox = st.sidebar.selectbox('How would you like to predict?', ('Online', 'Batch'))
        st.sidebar.info('This app is created to predict House prices' )
        st.title('House Price Prediction')
        
        
        if add_selectbox == 'Online':
            
            mssubclass = st.selectbox('MSSubClass',['20','30','40','45',
                                                   '50','60','70','75',
                                                   '80','85','90','120',
                                                   '150','160','180','190'] )
            mszoning = st.selectbox('MSZoning',['Agriculture','Commercial',
                                               'Floating Village Residential',
                                               'Industrial','Residential HD',
                                               'Residential LD','Residential LDP',
                                               'Residential MD'])
            lotfrontage = st.number_input('LotFrontage', min_value=0, max_value=150)
            lotarea = st.number_input('LotArea', min_value=1)
            street = st.selectbox('Street', ['Grvl','Pave'])
            alley = st.selectbox('Alley',['Grvl','Pave','NA'])
            lotshape = st.selectbox('LotShape',['Reg','IR1','IR2','IR3'])
            landcontour = st.selectbox('LandContour', ['Lvl','Bnk','HLS','Low'])
            utilities = st.selectbox('Utilities', ['AllPub','NoSewr','NoSeWa','ELO'])
            lotconfig = st.selectbox('LotConfig',['Inside','Corner',
                                                         'CulDSac','FR2','FR3'])
            
            output =''
            input_dict = {'MSSubClass':mssubclass, 'MSZoning':mszoning,'LotFrontage': lotfrontage,
                         'LotArea':lotarea, 'Street':street,'Alley': alley, 'LotShape':lotshape,
                         'LandContour':landcontour,'Utilities':utilities,'LotConfig':lotconfig  } #Output data
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


# In[3]:


#!jupyter nbconvert --to script streamlit_app.ipynb


# In[ ]:




