import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(columns=['Population','Case','Rate','LCI','HCI','Info'])

values = st.text_input('Input values')
try:
    valuelist = [int(a) for a in values.split()]
except:
    exit()
    
if len(valuelist) > 1:
    pop  = valuelist[0]
    case = valuelist[1]
    rate = case/pop

    vdict = {'Population':[pop],'Case':[case],'Rate': [f'{rate*100000:.2f}'], 'LCI': [f'{(rate - 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f}'], 'HCI':[f'{(rate + 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f}'], 'Info':[f'{rate*100000:.2f} ({(rate - 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f} to {(rate + 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f})']}

    df0 = pd.DataFrame(vdict)
    
    df = pd.concat([df,df0], ignore_index=True)
    
    st.data_editor(df)

    st.write(f'{rate*100000:.2f} ({(rate - 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f} to {(rate + 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.2f})')
        
    st.write(f'{rate*100000:.3f} ({(rate - 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.3f} to {(rate + 1.96*np.sqrt(rate*(1-rate)/pop))*100000:.3f})')
