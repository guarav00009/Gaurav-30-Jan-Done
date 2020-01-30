from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps import apps
from setting.models import Vehicle
from django.contrib import messages
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_vehicle_list(request):
    vendor_id = request.POST.get('vendor_id')
    draw = int(request.GET.get("draw", 0))
    start = int(request.GET.get("start", 0))
    length = int(request.GET.get("length", 7))

    all_objects = Vehicle.objects.filter(vendor_id = vendor_id)
    filtered_count = all_objects.count()
    total_count = Vehicle.objects.count()
    data = serializers.serialize('json', all_objects)

    json_objects = json.loads(data)
    list_objects = []
    for index in range(len(json_objects)):
        json_objects[index]['fields']['id'] = all_objects[index].id
        result = json_objects[index]['fields']['status']
        if(result == 1):
            json_objects[index]['fields']['status'] = 'Active'
        elif(result == 2):
            json_objects[index]['fields']['status'] = 'Inactive'
        elif(result == 3):
            json_objects[index]['fields']['status'] = 'Booked'
        else:
            json_objects[index]['fields']['status'] = 'Booked'
        list_objects.append(json_objects[index]['fields'])
    print(json.dumps(list_objects))
    return HttpResponse(json.dumps(list_objects), content_type='application/json;charset=utf-8')
