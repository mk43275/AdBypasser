
import random
import streamlit as st
from PyBypass.main import BypasserNotFoundError, UnableToBypassError, UrlConnectionError
import PyBypass as bypasser

st.set_page_config(page_title="URL Bypasser", page_icon='🧊',
                   layout="centered", initial_sidebar_state="auto",    menu_items={
                       'Get Help': 'https://telegram.me/',
                       'Report a bug': "https://telegram.me/",
                       'About': "This is URL Bypasser for ADLINKFLY based website. Made by [Kevin](https://github.com/)"
                   })


def random_celeb():
    return random.choice([st.balloons()])
  
st.markdown(f' <iframe src="//www.profitabledisplaynetwork.com/watchnew?key=f274454d04b18b3c2e76a5be61a28a33" width="728" height="90" frameborder="0" scrolling="no"></iframe>', unsafe_allow_html=True)
st.markdown(f' <script type="text/javascript" src="//pl18705436.highrevenuegate.com/19/b7/81/19b781bc5fb6b75f2f7a76d24c5c6461.js"></script>', unsafe_allow_html=True)


    
    
st.title("URL Bypasser")
tab1, tab2 = st.tabs(["Bypass", "Available Websites", ])

__avl_website__ = ['try2link.com', ' adf.ly', ' bit.ly', ' ouo.io', ' ouo.press', ' shareus.in', ' shortly.xyz', ' tinyurl.com', ' thinfi.com', ' hypershort.com ', 'safeurl.sirigan.my.id', ' gtlinks.me', ' loan.kinemaster.cc', ' theforyou.in', ' linkvertise.com', ' shorte.st', ' earn4link.in', ' tekcrypt.in', ' link.short2url.in', ' go.rocklinks.net', ' rocklinks.net', ' earn.moneykamalo.com', ' m.easysky.in', ' indianshortner.in', ' open.crazyblog.in', ' link.tnvalue.in',' shortingly.me', ' open2get.in', ' dulink.in', ' bindaaslinks.com', ' za.uy', ' pdiskshortener.com', ' mdiskshortner.link', ' go.earnl.xyz', ' g.rewayatcafe.com', ' ser2.crazyblog.in', ' bitshorten.com', ' rocklink.in', ' droplink.co', ' tnlink.in', ' ez4short.com', ' xpshort.com', ' vearnl.in', ' adrinolinks.in', ' techymozo.com', ' linkbnao.com', ' linksxyz.in', ' short-jambo.com', ' ads.droplink.co.in', ' linkpays.in', ' pi-l.ink', ' link.tnlink.in ', ' pkin.me']

with tab1:
    show_alert = False
    url = st.text_input(label="Paste your URL")
    if st.button("Submit"):
        if url:
            try:

                with st.spinner("Loading..."):
                    bypassed_link = bypasser.bypass(url)
                    st.success(bypassed_link)

                random_celeb()

                with st.expander("Copy"):
                    st.code(bypassed_link)

            except (UnableToBypassError, BypasserNotFoundError, UrlConnectionError) as e:
                if show_alert := True:
                    st.error(e)

            if st.button("Dismiss"):
                show_alert = False

        elif show_alert := True:
            st.error("No URLS found")

with tab2:
    st.subheader("Available Websites")
    st.table(__avl_website__)
    
    st.markdown(f' <a href="https://www.highrevenuegate.com/pk4vvag9?key=878bd8d1a906a45f10db7fd41c9cb857">Clain your free gift here!</a>', unsafe_allow_html=True)


