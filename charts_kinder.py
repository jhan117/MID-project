from data_kinder import *

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# === 유치원/원아수 fig1
kinder_fig1 = make_subplots(specs=[[{"secondary_y": True}]])
kinder_fig1.add_trace(
    go.Bar(x=df_stu['연도'], y=df_stu['학생수 총계(만명)'],
           name='원아수', hovertemplate='%{y}만명'),
    secondary_y=False,
)
kinder_fig1.add_trace(
    go.Scatter(
        x=df_sch['연도'], y=df_sch['나이스 학교 코드'], name='유치원', hovertemplate='%{y}개'),
    secondary_y=True,
)
kinder_fig1.update_xaxes(dtick="Y1")
kinder_fig1.update_yaxes(title_text="원아수(만명)", tickmode='linear', tick0=55,
                         dtick=3, range=[55, 79], secondary_y=False)
kinder_fig1.update_yaxes(title_text="유치원(개)", tickmode='linear', tick0=8400, dtick=100,
                         range=[8400, 9200], secondary_y=True)
kinder_fig1.update_layout(hovermode="x unified")

# === 유치원당 원아수 fig2
kinder_fig2 = px.line(df_sch_stu, x='연도', y='학교당 학생수',
                      labels={'학교당 학생수': '유치원당 원아수', '연도': ''}, markers=True, height=720)
kinder_fig2.update_traces(hovertemplate='유치원당 원아수<br>%{y}명')
kinder_fig2.update_xaxes(dtick="Y1")
kinder_fig2.update_layout(hovermode="x unified")

# === 교원/원아수 fig3
kinder_fig3 = make_subplots(specs=[[{"secondary_y": True}]])
kinder_fig3.add_trace(
    go.Bar(x=df_stu['연도'], y=df_stu['학생수 총계(만명)'],
           name='원아', hovertemplate='%{y}만명'),
    secondary_y=False,
)
kinder_fig3.add_trace(
    go.Scatter(
        x=df_teach['연도'], y=df_teach['교원수 총계(천명)'], name='교원', hovertemplate='%{y}천명'),
    secondary_y=True,
)
kinder_fig3.update_xaxes(dtick="Y1")
kinder_fig3.update_yaxes(title_text="원아수(만명)", tickmode='linear', tick0=55,
                         dtick=3, range=[55, 79], secondary_y=False)
kinder_fig3.update_yaxes(title_text="교원수(천명)", tickmode='linear', tick0=39, dtick=3,
                         range=[39, 63], secondary_y=True)
kinder_fig3.update_layout(hovermode="x unified")

# === 교원당 원아수 fig4
kinder_fig4 = px.line(df_teach_stu, x='연도', y='교원1인당 학생수', labels={
                      '교원1인당 학생수': '교원 1인당 원아수', '연도': ''}, markers=True, height=720)
kinder_fig4.update_xaxes(dtick="Y1")
kinder_fig4.update_traces(hovertemplate='교원 1인당 원아수<br>%{y}명')
kinder_fig4.update_layout(hovermode="x unified")

if __name__ == '__main__':
    kinder_fig1.show()
    kinder_fig2.show()
    kinder_fig3.show()
    kinder_fig4.show()
