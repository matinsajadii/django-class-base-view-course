from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView, ListView, FormView, DetailView, UpdateView, MonthArchiveView
from .models import Car
from django.views.generic.detail import DetailView
from .forms import CarCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_views
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CarSerializer

# class HomeView(TemplateView):
#     # http_method_names = ["post", "options"]

#     template_name = "home/home.html"

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["cars"] = Car.objects.all()
#         return context
    
    # def options(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     response = super().options(request, *args, **kwargs)
    #     response.headers["host"] = "localhost"
    #     response.headers["user"] = request.user
    #     return response
    
    # def http_method_not_allowed(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     super().http_method_not_allowed(request, *args, **kwargs)
    #     return render(request, "method_not_allowed.html")
    

class HomeView(ListView):
    template_name = "home/home.html"
    context_object_name = "cars"

    def get_queryset(self) -> QuerySet[Any]:
        # return Car.objects.filter(year__gte=1400)
        return Car.objects.all()

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["username"] = "matin"
        return context 
    

# class Two(RedirectView):
#     pattern_name = "home:home"
#     query_string = True


#     def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
#         print("="*90)
#         print("processing your request...")
#         print(kwargs["id"])
#         print(kwargs["name"])
#         return super().get_redirect_url(*args, **kwargs)
    
# class CarDetail(DetailView):
#     template_name = "home/detail.html"
#     slug_field = "name"
#     slug_url_kwarg = "my_slug"

#     def get_queryset(self) -> QuerySet[Any]:
#         if self.request.user.is_authenticated:
#             return Car.objects.filter(name=self.kwargs["my_slug"])
#         else:
#             return Car.objects.none()


# class CarCreateView(FormView):
#     template_name = "home/create.html"
#     form_class = CarCreateForm
#     success_url = reverse_lazy("home:home")

#     def form_valid(self, form) -> HttpResponse:
#         self._create_car(form.cleaned_data)
#         messages.success(self.request, "created car successfully", extra_tags="success")
#         return super().form_valid(form)

#     def _create_car(self, data):
#         Car.objects.create(
#             name=data["name"], 
#             owner=data["owner"],
#             year=data["year"],
#         )


# class CarDelete(DetailView):
#     model = Car
#     success_url = reverse_lazy("home:home")
#     template_name = "home/delete.html"

# class CarUpdate(UpdateView):
#     model = Car
#     fields = ["name", "year"]
#     success_url = reverse_lazy("home:home")
#     template_name = "home/update.html"


# class UserLogin(auth_views.LoginView):
#     template_name = "home/login.html"
#     next_page = reverse_lazy("home:home")


# class UserLogout(auth_views.LogoutView):
#     next_page = reverse_lazy("home:home")


# class MonthCar(MonthArchiveView):
#     template_name = "home/home.html"
#     model = Car
#     date_field = "created"
#     allow_future = True
#     context_object_name = "cars"
#     month_format = "%m"


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class SingleCar(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()