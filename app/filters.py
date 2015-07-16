import django-filters

class NameFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = ['name']

class DirectorFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = ['director']

class GenreFilter(django_filters.FilterSet):
    class Meta:
        model = Movies
        fields = ['title']