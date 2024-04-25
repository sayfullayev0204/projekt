# from rest_framework import generics,status
# from .models import Tuman, Maktab, Shaxs
# from .serializers import TumanSerializer, MaktabSerializer, ShaxsSerializer
# from rest_framework.response import Response
# class TumanAPIView(generics.ListAPIView):
#     queryset = Tuman.objects.all()
#     serializer_class = TumanSerializer

# class MaktabAPIView(generics.ListCreateAPIView):
#     serializer_class = MaktabSerializer

#     def get_queryset(self):
#         tuman_id = self.kwargs['tuman_id']
#         return Maktab.objects.filter(tuman_id=tuman_id)

# class ShaxsAPIView(generics.ListCreateAPIView):
#     serializer_class = ShaxsSerializer

#     def get_queryset(self):
#         maktab_id = self.kwargs['maktab_id']
#         return Shaxs.objects.filter(maktab_id=maktab_id)

#     def perform_create(self, serializer):
#         maktab_id = self.kwargs['maktab_id']
#         serializer.save(maktab_id=maktab_id)

# class ShaxSoni(generics.RetrieveAPIView):
#     serializer_class = MaktabSerializer

#     def get(self, request, *args, **kwargs):
#         maktab_id = self.kwargs['maktab_id']
#         shaxs_soni = Shaxs.objects.filter(maktab_id=maktab_id).count()
#         return Response({'shaxs_soni':shaxs_soni}, status=status.HTTP_200_OK)


from django.shortcuts import render, redirect, get_object_or_404
from .models import Tuman, Maktab, Shaxs
from .forms import ShaxsForm
from django.db.models import Count
from django.views.generic import DetailView
def tuman_list(request):
    tumandagi_oquvchilar = {}
    tumans = Tuman.objects.all()
    for tuman in tumans:
        tumandagi_oquvchilar[tuman] = Shaxs.objects.filter(maktab__tuman=tuman).count()
    sorted_tumandagi_oquvchilar = dict(sorted(tumandagi_oquvchilar.items(), key=lambda item: item[1], reverse=True))
    return render(request, 'tuman_list.html', {'tumandagi_oquvchilar': sorted_tumandagi_oquvchilar, 'tumans':tumans})


from django.db.models import Count

def maktab_list(request, tuman_id):
    tuman = get_object_or_404(Tuman, pk=tuman_id)
    maktablar = tuman.maktab_set.annotate(oquvchi_soni=Count('shaxs')).order_by('-oquvchi_soni')
    return render(request, 'maktab_list.html', {'tuman': tuman, 'maktablar': maktablar})

def oquvchi_list(request, maktab_id):
    maktab = get_object_or_404(Maktab, pk=maktab_id)
    oquvchilar = maktab.shaxs_set.all()
    oquvchi_soni = oquvchilar.count()
    return render(request, 'oquvchi_list.html', {'maktab': maktab, 'oquvchilar': oquvchilar, 'oquvchi_soni': oquvchi_soni})

def oquvchi_qoshish(request, maktab_id):
    maktab = Maktab.objects.get(id=maktab_id)
    
    if request.method == 'POST':
        form = ShaxsForm(request.POST)
        if form.is_valid():
            oquvchi = form.save(commit=False)
            oquvchi.maktab = maktab
            oquvchi.save()
            return redirect('oquvchi_list', maktab_id=maktab.id)
    else:
        form = ShaxsForm()
    
    return render(request, 'oquvchi_qoshish.html', {'form': form})


def oquvchi_tahrirlash(request, oquvchi_id):
    oquvchi = Shaxs.objects.get(id=oquvchi_id)
    if request.method == 'POST':
        form = ShaxsForm(request.POST, instance=oquvchi)
        if form.is_valid():
            form.save()
            return redirect('oquvchi_list', maktab_id=oquvchi.maktab.id)
    else:
        form = ShaxsForm(instance=oquvchi)
    return render(request, 'oquvchi_tahrirlash.html', {'form': form})

def oquvchi_detail(request, oquvchi_id):
    oquvchi = get_object_or_404(Shaxs, pk=oquvchi_id)
    return render(request, 'oquvchi_detail.html', {'oquvchi': oquvchi})

def students_per_district(request):
    tumans = Tuman.objects.all()
    data = []
    for tuman in tumans:
        students = Shaxs.objects.filter(tuman=tuman)
        language_counts = {}
        proficiency_counts = {}
        status_counts = {}
        
        for student in students:
            language = student.Biladigan_tili
            language_counts[language] = language_counts.get(language, 0) + 1
            
            proficiency = student.Til_bilish_darajasi
            proficiency_counts.setdefault(language, {}).setdefault(proficiency, 0)
            proficiency_counts[language][proficiency] += 1
            
            status = student.Holati
            status_counts.setdefault(language, {}).setdefault(status, 0)
            status_counts[language][status] += 1
        
        data.append({
            'tuman': tuman,
            'language_counts': language_counts,
            'proficiency_counts': proficiency_counts,
            'status_counts': status_counts,
        })
    return render(request, 'list.html', {'data': data})


