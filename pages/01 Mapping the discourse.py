import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tableau", page_icon=":world_map:", layout="wide")

st.title ("Web use around the world")
st.markdown("*With Tableau*")
def main():
    html_temp='''<div class='tableauPlaceholder' id='viz1704296468276' style='position: relative'><noscript><a href='#'><img alt='Story 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HeatMaps_17015178444210&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='HeatMaps_17015178444210&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;He&#47;HeatMaps_17015178444210&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1704296468276');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1040px';vizElement.style.height='827px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
    components.html(html_temp, width=1000, height=600)
if __name__ == '__main__':
    main()

