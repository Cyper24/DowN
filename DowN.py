import requests
import streamlit as st 

st.set_page_config(
    page_title="-----| DowN |-----",
    )

st.title("-----| DowN |-----")
cari = st.text_input('Paste link below ', ' ')
url = "https://ssyoutube.com/api/convert"
querystring = {"url":"{}".format(cari)}
headers = {
    "Content-Type": "application/json",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

if st.button('LetsGo'):
    try:
        response = requests.request("POST", url, headers=headers, params=querystring)
        r = response.json()
        x = len(r["url"])
        name = r["meta"]["title"]
        try :
            duration = r["meta"]["duration"]
        except:
            duration = " "
        thumb = r["thumb"]
        source = r["meta"]["source"]
        colz, colx, colc = st.columns(3)
        with colx:
            st.image(thumb,width=300)
        st.header(name + " - "+duration)
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            st.text("| Download |")
        with col2:
            st.text("| Format |")
        with col3:
            st.text("| Quality |")
        with col4:
            st.text("| Audio |")

        for xx in range(0,x):
            link = r["url"][xx]["url"]
            ext = r["url"][xx]["ext"]   
            try:
                quality = r["url"][xx]["quality"]
                audio = r["url"][xx]["no_audio"]
                if audio == False:
                    audio = "✓"
                else:
                    audio = "☓"
            except:
                audio = " "
                quality = " "
            col1, col2, col3,col4 = st.columns(4)
            with col1:
                st.markdown(f'''
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                    <button><i class="fa fa-cloud-download"></i>
                    <a href="{link}">Download
                    </a></button>
                        ''',unsafe_allow_html=True)
            with col2:
                st.text(ext)
            with col3:
                st.text(quality) 
            with col4:
                st.text(audio)
    except:
        False

st.text('$/$ Made with ❤ By Cyper24 $/$')