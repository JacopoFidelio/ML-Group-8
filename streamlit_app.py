#!/usr/bin/env python
# coding: utf-8

# In[9]:


from pycaret.regression import load_model, predict_model
from IPython import get_ipython
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


# In[12]:




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
            alley = st.selectbox('Alley', ['Grvl','Pave','NA'])
            lotshape = st.selectbox('LotShape', ['Reg','IR1','IR2','IR3'])
            landcontour = st.selectbox('LandContour', ['Lvl','Bnk','HLS','Low'])
            utilities = st.selectbox('Utilities', ['AllPub','NoSewr','NoSeWa','ELO'])
            lotconfig = st.selectbox('LotConfig', ['Inside','Corner',
                                                         'CulDSac','FR2','FR3'])
            landslope = st.selectbox('LandSlope', ['Gtl','Mod','Sev'])
            neighborhood = st.selectbox('Neighborhood',
                                        ['Blmngtn','Blueste','BrDale','BrkSide','ClearCr'
                                         ,'CollgCr','Crawfor','Edwards','Gilbert','IDOTRR'
                                         ,'MeadowV','Mitchel','Names','NoRidge','NPkVill'
                                         ,'NridgHt','NWAmes','OldTown','SWISU','Sawyer',
                                         'SawyerW','Somerst','StoneBr','Timber','Veenker'
                                        ])
            condition1 = st.selectbox('Condition1', 
                                      ['Artery','Feedr','Norm','RRNn','RRAn'
                                       ,'PosN','PosA','RRNe','RRAe'])
            condition2 = st.selectbox('Condition2', 
                                      ['Artery','Feedr','Norm','RRNn','RRAn'
                                       ,'PosN','PosA','RRNe','RRAe'])
            bldgtype = st.selectbox('BldgType', ['1Fam', '2FmCon', 'Duplx', 'TwnhsE', 'TwnhsI'])
            housestyle = st.selectbox('HouseStyle', ['1Story', '1.5Fin', '1.5Unf', '2Story',
                                                     '2.5Fin', '2.5Unf', 'SFoyer', 'SLvl'])
            overallqual = st.slider('OverallQual', min_value=1, max_value=10, value=1, step=1)
            overallcond = st.slider('OverallCond', min_value=1, max_value=10, value=1, step=1)
            yearbuilt = st.number_input('YearBuilt', min_value=1800)
            yearremodadd = st.number_input('YearRemodAdd', min_value=1800)
            roofstyle = st.selectbox('RoofStyle', ['ClyTile', 'CompShg', 'Membran', 'Metal',
                                                   'Roll', 'Tar&Grv', 'WdShake', 'WdShngl'])
            roofmatl = st.selectbox('RoofMatl', ['ClyTile', 'CompShg', 'Membran', 'Metal',
                                                 'Roll', 'Tar&Grv', 'WdShake', 'WdShngl'])
            exterior1st = st.selectbox('Exterior1st', ['AsbShng', 'AsphShn', 'BrkComm', 'BrkFace',
                                                 'CBlock', 'CemntBd', 'HdBoard', 'ImStucc',
                                                 'MetalSd', 'Other', 'Plywood', 'PreCast',
                                                 'Stone', 'Stucco', 'VinylSd', 'Wd Sdng',
                                                 'WdShing'])
            exterior2nd = st.selectbox('Exterior2nd', ['AsbShng', 'AsphShn', 'BrkComm', 'BrkFace',
                                                 'CBlock', 'CemntBd', 'HdBoard', 'ImStucc',
                                                 'MetalSd', 'Other', 'Plywood', 'PreCast',
                                                 'Stone', 'Stucco', 'VinylSd', 'Wd Sdng',
                                                 'WdShing'])
            masvnrtype = st.selectbox('MasVnrType', ['BrkCmn', 'BrkFace', 'CBlock', 'None', 'Stone'])
            masvnrarea = st.number_input('MasVnrArea', min_value=0)
            exterqual = st.selectbox('ExterQual', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            extercond = st.selectbox('ExterCond', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            foundation = st.selectbox('Foundation', ['BrkTil', 'CBlock', 'PConc', 'Slab', 'Stone', 'Wood'])
            bsmtqual = st.selectbox('BsmtQual', ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'])
            bsmtcond = st.selectbox('BsmtCond', ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'])
            bsmtexposure = st.selectbox('BsmtExposure', ['Gd', 'Av', 'Mn', 'No', 'NA'])
            bsmtfintype1 = st.selectbox('BsmtFinType1', ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'NA'])
            bsmtfinsf1 = st.number_input('BsmtFinSF1', min_value=0)
            bsmtfintype2 = st.selectbox('BsmtFinType2', ['GLQ', 'ALQ', 'BLQ', 'Rec', 'LwQ', 'Unf', 'NA'])
            bsmtfinsf2 = st.number_input('BsmtFinSF2', min_value=0)
            bsmtunfsf = st.number_input('BsmtUnfSF', min_value=0)
            totalbsmtsf = st.number_input('TotalBsmtSF', min_value=0)
            heating = st.selectbox('Heating', ['Floor', 'GasA', 'GasW', 'GraV', 'OthW', 'Wall'])
            heatingqc = st.selectbox('HeatingQC', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            centralair= st.selectbox('CentralAir',['N','Y'])
            electrical = st.selectbox('Electrical', ['SBrkr', 'FuseA', 'FuseF', 'FuseP', 'Mix'])
            firstflrsf = st.number_input('1stFlrSF', min_value=0)
            secondflrsf = st.number_input('2ndFlrSF', min_value=0)
            lowqualfinsf = st.number_input('LowQualFinSF', min_value=0)
            grlivarea = st.number_input('GrLivArea', min_value=0)
            bsmtfullbath = st.number_input('BsmtFullBath', min_value=0)
            bsmthalfbath = st.number_input('BsmtHalfBath', min_value=0)
            fullbath = st.number_input('FullBath', min_value=0)
            halfbath = st.number_input('HalfBath', min_value=0)
            bedroom = st.number_input('Bedroom', min_value=0)
            kitchen = st.number_input('Kitchen', min_value=0)
            bedroomabvgrg = st.number_input('BedroomAbvGr', min_value=0)
            kitchenabvgrg = st.number_input('KitchenAbvGr', min_value=0)
            kitchenqual = st.selectbox('KitchenQual', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            totrmsabvgrd = st.number_input('TotRmsAbvGrd', min_value=0)
            functional = st.selectbox('TotRmsAbvGrd', ['Typ', 'Min1', 'Min2', 'Mod',
                                                       'Maj1', 'Maj2', 'Sev', 'Sal'])
            fireplaces = st.number_input('Fireplaces', min_value=0)
            fireplacequ = st.selectbox('FireplaceQu', ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
            garagetype = st.selectbox('GarageType', ['2Types', 'Attchd', 'Basment',
                                                     'BuiltIn', 'CarPort', 'Detchd', 'NA'])
            garageyrblt = st.number_input('', min_value=1800)
            garagefinish = st.selectbox('GarageFinish', ['Fin', 'RFn', 'Unf', 'NA'])
            garagecars = st.number_input('GarageCars', min_value=0)
            garagearea = st.number_input('GarageArea', min_value=0)
            garagequal = st.selectbox('GarageQual', ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'])
            garagecond = st.selectbox('GarageCond', ['Ex', 'Gd', 'TA', 'Fa', 'Po', 'NA'])
            paveddrive = st.checkbox('PavedDrive',['Y','P','N'])
            wooddecksf = st.number_input('WoodDeckSf', min_value=0)
            openporchsf = st.number_input('OpenPorchSF', min_value=0)
            enclosedporch = st.number_input('EnclosedPorch', min_value=0)
            thirdssnporch = st.number_input('3SsnPorch', min_value=0)
            screenporch = st.number_input('ScreenPorch', min_value=0)
            poolarea =st.number_input('PoolArea', min_value=0)
            poolqc = st.selectbox('PoolQC', ['Ex', 'Gd', 'TA', 'Fa', 'NA'])
            fence = st.selectbox('Fence', ['GdPrv', 'MnPrv', 'GdWo', 'MnWw', 'NA'])
            miscfeature = st.selectbox('MiscFeature', ['Elev', 'Gar2', 'Othr', 'Shed', 'TenC', 'NA'])
            miscval = st.number_input('MiscVal', min_value=0)
            mosolf = st.slider('MoSold', min_value=1, max_value=12, value=1, step=1)
            yrsold = st.number_input('YrSold', min_value=1900, max_value=2021)
            saletype = st.selectbox('SaleType', ['WD', 'CWD', 'VWD', 'New', 'COD', 'Con',
                                                 'ConLw', 'ConLI', 'ConLD', 'Oth'])
            salecondition = st.selectbox('SaleCondition', ['Normal', 'Abnorml', 'AdjLand',
                                                           'Alloca', 'Family', 'Partial'])
            
            
            
            output =''
            input_dict = {
                          'MSSubClass':mssubclass, 'MSZoning':mszoning,'LotFrontage': lotfrontage,
                          'LotArea':lotarea, 'Street':street,'Alley': alley, 'LotShape':lotshape,
                          'LandContour':landcontour,'Utilities':utilities,'LotConfig':lotconfig,
                          'LandSlope':landslope, 'Neighborhood':neighborhood, 'Condition1':condition1,
                          'Condition2':condition2, 'BldgType':bldgtype, 'HouseStyle':housestyle,
                          'OverallQual':overallqual, 'OverallCond':overallcond, 'YearBuilt':yearbuilt,
                          'YearRemodAdd':yearremodadd, 'RoofStyle':roofstyle, 'RoofMatl':roofmatl,
                          'Exterior1st':exterior1st, 'Exterior2nd':exterior2nd, 'MasVnrType':masvnrtype,
                          'MasVnrArea':masvnrarea, 'ExterQual':exterqual, 'ExterCond':extercond,
                          'Foundation':foundation, 'BsmtQual':bsmtqual, 'BsmtCond':bsmtcond,
                          'BsmtExposure':bsmtexposure, 'BsmtFinType1':bsmtfintype1, 'BsmtFinSF1':bsmtfinsf1,
                          'BsmtFinType2':bsmtfintype2, 'BsmtFinSF2':bsmtfinsf2, 'BsmtUnfSF':bsmtunfsf,
                          'TotalBsmtSF':totalbsmtsf, 'Heating':heating, 'HeatingQC':heatingqc,
                          'CentralAir':centralair, 'Electrical':electrical, '1stFlrSF':firstflrsf,
                          '2ndFlrSF':secondflrsf, 'LowQualFinSF':lowqualfinsf, 'GrLivArea':grlivarea,
                          'BsmtFullBath':bsmtfullbath, 'BsmtHalfBath':bsmthalfbath, 'FullBath':fullbath,
                          'HalfBath':halfbath, 'Bedroom':bedroom, 'Kitchen':kitchen, 'KitchenQual':kitchenqual,
                          'TotRmsAbvGrd':totrmsabvgrd, 'Functional':functional, 'Fireplaces':fireplaces,
                          'FireplaceQu':fireplacequ, 'GarageType':garagetype, 'GarageYrBlt':garageyrblt,
                          'GarageFinish':garagefinish, 'GarageCars':garagecars, 'GarageArea':garagearea,
                          'GarageQual':garagequal, 'GarageCond':garagecond, 'PavedDrive':paveddrive,
                          'WoodDeckSF':wooddecksf, 'OpenPorchSF':openporchsf, 'EnclosedPorch':enclosedporch,
                          '3SsnPorch':thirdssnporch, 'ScreenPorch':screenporch, 'PoolArea':poolarea,
                          'PoolQC':poolqc, 'Fence':fence, 'MiscFeature':miscfeature, 'MiscVal':miscval,
                          'MoSold':mosolf, 'YrSold':yrsold, 'SaleType':saletype, 'SaleCondition':salecondition,
                          'KitchenAbvGr':kitchenabvgrg,'BedroomAbvGr':bedroomabvgrg
                         } #Output data
            input_df = pd.DataFrame(input_dict, index=[0])
            
            if st.button('Predict'):
                output = self.predict(input_df)
                
                output = output['Label'][0]
                
                
            st.success('Predicted output: {}'.format(output))
            
        if add_selectbox == 'Batch':
            fn = st.file_uploader("Upload csv file for predictions")
            if fn is not None:
                input_df = pd.read_csv(fn)
                predictions = self.predict(input_df)
                st.write(predictions)
        
sa = StreamlitApp()
sa.run()               


# In[11]:


#!jupyter nbconvert --to script streamlit_app.ipynb


# In[ ]:




