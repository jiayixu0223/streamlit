import streamlit as st
import pandas as pd
import requests
url = 'https://dsci551-project-data2-default-rtdb.firebaseio.com/.json'
response = requests.get(url)
response1 = response.json()
#df1 = pd.DataFrame.from_dict(response1)
cols = ['Filename','Text','Linkedin Links','Organizations','Skills','Location','Name',
       'Number of Organizations','Number of Skills','Positions','Number of Positions']
final = []
for key,value in response1.items():
    each_row = ['','','','','','','','','','','']
    each_row[0] = key
    dict1 = response1[key]
    for key1,value1 in dict1.items():
        if key1 in cols:
            each_row[cols.index(key1)] = value1
    final.append(each_row)
df1 = pd.DataFrame(final)
df1.columns = cols
df1_result_search = pd.DataFrame()
searchcheckbox_Name = st.checkbox("Filename",value = False,key=1)
if searchcheckbox_Name:   
    name_search = st.text_input("Filename")
if st.button("search"):
    df1_result_search = df1[df1['Filename'].str.contains(name_search,case=False, na=False)]
#st.dataframe(data=None, width=None, height=None)
st.title('Resume Data')
st.dataframe(df1)
st.write('This is what you searched!')
st.dataframe(df1_result_search)
url = "https://empowerusc.netlify.app/"
st.write("Link back to home page [link](%s)" % url)
