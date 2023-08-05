import pandas as pd
import numpy as np
import streamlit as st

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

footerText = """
<style>
#MainMenu {
visibility:hidden ;
}

footer {
visibility : hidden ;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>

<div class='footer'>
<p> Copyright @ ycho <a href="mailto:bourbaki10@gmail.com"> bourbaki10@gmail.com </a></p>
</div>
"""

st.markdown(str(footerText), unsafe_allow_html=True)

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
