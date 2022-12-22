from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from django import forms

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Player


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'nationality', 'age')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("ISO-8859-1")
            csv_data = file_data.split("\n")
            

            for x in csv_data[1:]:
                if x == '':
                    continue
                fields = x.split(",")
                
                created = Player.objects.update_or_create(
                    name = fields[0],
                    club = fields[1],
                    nationality = fields[2],
                    position = fields[3],
                    age = fields[4],
                    matches = fields[5],
                    )
                    
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Player, PlayerAdmin)