from django.urls import path
from .views import homepage, create, particularData, contacts, deleteData, updateData

app_name = "crud"
urlpatterns = [
    path("", homepage, name="home"),
    path("create/", create, name="create"),
    path("<int:id>/", particularData, name="particular"),
    path("contacts/", contacts, name="contacts"),
    path("delete/<int:id>", deleteData, name="deletedata"),
    path("update/<int:id>", updateData, name="updatedata"),



]
