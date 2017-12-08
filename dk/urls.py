from django.urls import path
from dk import views
from django.urls import register_converter


class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return (value)

    # def to_url(self, value):
    #     return '%04d' % value


register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('<yyyy:year>/', views.pr),
    path('', views.pp),
    path('s', views.dd),
]
