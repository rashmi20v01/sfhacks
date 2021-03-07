from django.shortcuts import render

# Create your views here.
def home(request):
  context={}
  if request.method=='POST':
    if(request.POST.get('ch203',False)):
      course1='Transport Phenomena'
      context['ch203']=course1
    if(request.POST.get('ch201',False)):
      course2='Particle Technology'
      context['ch201']=course2
    if(request.POST.get('oc',False)):
      course3='Organic Chem'
      context['oc']=course3
    if(request.POST.get('ma207',False)):
      course4='Numerical Methods'
      context['ma207']=course4
    if(request.POST.get('ch202',False)):
      course5='Thermodynamics'
      context['ch202']=course5
    if(request.POST.get('ma207',False) and request.POST.get('ch203',False)):
      return render(request,'error.html')
    return render(request,'create.html',context)
  return render(request,'home.html')
