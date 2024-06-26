import streamlit as st
import pandas as pd
import plotly.express as px
import base64 
import csv
import matplotlib.pyplot as plt
from io import StringIO, BytesIO
import math
import os
from itertools import zip_longest

hide_st_style="""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)

st.title('Placement 📈')
st.subheader('Feed me with your Excel file')

#file upload
uploaded_file = st.file_uploader('Choose a CSV file', type='CSV')
if uploaded_file:
  st.markdown("---")
  df=pd.read_csv(uploaded_file)
  st.dataframe(df)
  dep=["Post Graduate","Job","No Studies & Job"]
  #filename
  select_dep=st.selectbox('Select the department',dep)
  title = st.text_input(
        "Enter File Name 👇" )
  st.write('Your File Name is:',title)

  #post
  if (select_dep=="Post Graduate"):
    df=df.dropna(subset=["Higher Studies Roll Number"])
    a = df["Name"].dropna().tolist()
    b= df["Address"].dropna().tolist()
    c = df["Contact Number"].dropna().tolist()
    d= df["Higher Studies Roll Number"].dropna().tolist()
    e = df["Name of the Higher Studies College"].dropna().tolist()
    f = df['Course of Higher Studies'].dropna().tolist()
    folder_input = 'D:/streamlit/placement/Backup/'
    file_input =title+'.csv'
    f=[a,b,c,d,e,f] 
    export_data = zip_longest(*f, fillvalue = '')
    with open( os.path.join(folder_input, file_input), 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('Name', 'Address','Contact Number','Higher Studies Roll Number','Name of the Higher Studies College','Course of Higher Studies'))
      wr.writerows(export_data)
    myfile.close()

  #job
  elif(select_dep=="Job"):
    df=df.dropna(subset=["Job Role"])
    a = df["Name"].dropna().tolist()
    b= df["Address"].dropna().tolist()
    c = df["Contact Number"].dropna().tolist()
    d = df["Job Role"].dropna().tolist()
    e= df["Campus"].dropna().tolist()
    f= df["Salary"].dropna().tolist()
      #write 
    folder_input = 'D:/streamlit/placement/Backup/'
    file_input =title+'.csv'
    f=[a,b,c,d,e,f] 
    export_data = zip_longest(*f, fillvalue = '')
    with open( os.path.join(folder_input, file_input), 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('Name', 'Address','Contact Number','Job Role','Campus','Salary'))
      wr.writerows(export_data)
    myfile.close()
  
  elif(select_dep=="No Studies & Job"):
    df=df.dropna(subset=["No Higher Studies and No Salary"])
    a = df["Name"].dropna().tolist()
    b= df["Address"].dropna().tolist()
    c = df["Contact Number"].dropna().tolist()
    d= df["No Higher Studies and No Salary"].dropna().tolist()
    e= df["Reason"].dropna().tolist()
      #write 
    folder_input = 'D:/streamlit/placement/Backup/'
    file_input =title+'.csv'
    f=[a,b,c,d,e] 
    export_data = zip_longest(*f, fillvalue = '')
    with open( os.path.join(folder_input, file_input), 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('Name', 'Address','Contact Number','No Higher Studies and No Salary','Reason'))
      wr.writerows(export_data)
    myfile.close()
     
  
  #sumbit
  if st.button("Submit"): 

    def main():
    #display
       col1, col2= st.columns([2,3])
       with col1:
         st.subheader('Data')
         data=pd.read_csv(r'D:/streamlit/placement/Backup/'+title+'.csv')
         st.dataframe(data, width = 400,height=300)
         def generate_csv():
            df = pd.DataFrame(data)
            return df
         df = generate_csv()
         csv_data = df.to_csv(index=False)
         st.download_button(label="Download CSV", data=csv_data, file_name=title+'.csv', mime='text/csv')
    if __name__ == '__main__':
                  main()     
