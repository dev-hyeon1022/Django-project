from django.urls import path

from mypage import views
from mypage.views import MyProfileView, MyLessonView, MyLessonReviewView, MyHelpersView, MyEventView, MyMessageListView, \
    MyMessageDetailView, MyMessageWriteView, MyPayView, MyEventDeleteView, MyHelpersDeleteView

app_name = 'mypage'

urlpatterns = [
    # 프로필
    path('profile/', MyProfileView.as_view(), name='myprofile'),
    # 과외 매칭
    path('lesson/', MyLessonView.as_view(), name='mylesson'),
    path('lesson/<int:page>/', MyLessonView.as_view(), name='mylesson'),
    path('lesson-review/', MyLessonReviewView.as_view(), name='mylesson-review'),
    # 헬퍼스
    path('helpers/', MyHelpersView.as_view(), name='myhelpers_init'),
    path('helpers/<int:page>/', MyHelpersView.as_view(), name='myhelpers_page'),
    path('helpers/<str:keyword>/', MyHelpersView.as_view(), name='myhelpers_find'),
    path('helpers/delete/<int:helpers_id>/', MyHelpersDeleteView.as_view(), name='myhelpers_delete'),
    path('helpers/<str:keyword>/<int:page>/', MyHelpersView.as_view(), name='myhelpers_list'),
    # 이벤트
    path('event/', MyEventView.as_view(), name='myevent_init'),
    path('event/<int:page>/', MyEventView.as_view(), name='myevent_page'),
    path('event/<str:keyword>/', MyEventView.as_view(), name='myevent_find'),
    path('event/delete/<int:event_id>/', MyEventDeleteView.as_view(), name='myevent_delete'),
    path('event/<str:keyword>/<int:page>/', MyEventView.as_view(), name='myevent_list'),
    # 쪽지
    path('message-list/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<int:page>', MyMessageListView.as_view(), name='message-list'),
    path('message-detail/', MyMessageDetailView.as_view(), name='message-detail'),
    path('message-write/', MyMessageWriteView.as_view(), name='message-write'),
# 테스트
    path('message-list/', MyMessageListView.as_view(), name='message-list-init'),
    path('message-list/<str:keyword>/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<str:keyword>/<int:page>', MyMessageListView.as_view(), name='message-list-page'),
    # 결제
    path('pay/', MyPayView.as_view(), name='mypay'),
]
