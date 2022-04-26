import streamlit as st
import pandas as pd
import requests
url = 'https://dsci551-project-data3-default-rtdb.firebaseio.com/.json'
response = requests.get(url)
response1 = response.json()
#df1 = pd.DataFrame.from_dict(response1)
cols = ['Position Name','Hourly Pay','Location','Course Related','Description','Requirement']
final = []
for key,value in response1.items():
    each_row = ['','','','','','']
    each_row[0] = key
    dict1 = response1[key]
    for key1,value1 in dict1.items():
        if key1 in cols:
            each_row[cols.index(key1)] = value1
    final.append(each_row)
df1 = pd.DataFrame(final)
df1.columns = cols
df1_result_search = pd.DataFrame()
searchcheckbox_Name = st.checkbox("Position Name",value = False,key=1)
if searchcheckbox_Name:   
    name_search = st.text_input("Position Name")
if st.button("search"):
    df1_result_search = df1[df1['Position Name'].str.contains(name_search,case=False, na=False)]
#st.dataframe(data=None, width=None, height=None)
st.title('Job List Data')
st.dataframe(df1)
st.write('This is what you searched!')
st.dataframe(df1_result_search)
url = "https://empowerusc.netlify.app/job_listing.html"
st.write("Link back [link](%s)" % url)
url2 = 'https://empowerusc.netlify.app/application.html'
st.write("Link to apply [link](%s)" % url2)
