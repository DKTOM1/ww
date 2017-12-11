from django.urls import path
from dk import views
from django.urls import register_converter


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return (value)

    def to_url(self, value):
        return '%04d' % value


register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('arr/20155', views.dd),
    path('<yyyy:year>/', views.pr),
    # path('arr/<yyyy:year>/', views.pr, name='news-year-archive'),
    path('', views.pp),
    path('s', views.dd),

]
