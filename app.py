
import plotly.express as px
import streamlit as st

from functions import functions as f
from config.directories import rootDir


# PAGE CONFIGURATOION
st.set_page_config(page_title='ISS Positions',
                   page_icon=':earth_africa:', # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout='wide',
)


df = f.xls_upload(f'{rootDir}\output\\2022-06-02 15-10800.xlsx')

# LANDING PAGE
st.title('ISS Positioning')
st.markdown('##')


fig_flat = px.line_geo(df, lat='latitude', lon='longitude',
                width=1200, height=600
) #try ,line = dict(width = 2, color = 'blue')
fig_flat.update_geos(
    #projection_type="orthographic",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)



fig_oth = px.line_geo(df, lat='latitude', lon='longitude',
                width=1200, height=600
) #try ,line = dict(width = 2, color = 'blue')
fig_oth.update_geos(
    projection_type="orthographic",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)

left_column, right_column = st.columns(2)

with left_column:
    st.plotly_chart(fig_flat,use_container_width=True)

with right_column:
    st.plotly_chart(fig_oth,use_container_width=True)
