import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FormTemplate
# from .validators import detect_field_type
from .db import get_form_templates, add_form_template, remove_all_templates
import re

@csrf_exempt
def get_form(request):
    if request.method == 'POST':
        form_data = request.POST.dict()
        templates = get_form_templates()
        matched_template = None

        for template in templates:
            match = True
            for field_name, field_type in template['fields'].items():
                if field_name not in form_data:
                    print(f"Field {field_name} not found in form data")
                    match = False
                    break
                detected_type = detect_field_type(form_data[field_name])
                if detected_type != field_type:
                    print(f"Field type mismatch for {field_name}: expected {field_type}, got {detected_type}")
                    match = False
                    break
            if match:
                matched_template = template
                break

        if matched_template:
            print(f"Matched template: {matched_template['name']}")
            return JsonResponse({"template_name": matched_template['name']})
        else:
            detected_fields = {key: detect_field_type(value) for key, value in form_data.items()}
            return JsonResponse(detected_fields)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=400)

def detect_field_type(value):
    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value) or re.match(r"^\d{4}-\d{2}-\d{2}$", value):
        return 'date'
    elif re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value):
        return 'phone'
    elif re.match(r"[^@]+@[^@]+\.[^@]+", value):
        return 'email'
    else:
        return 'text'
    
@csrf_exempt
def add_template(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            fields = data['fields']
            add_form_template(name, fields)
            return JsonResponse({'status': 'Template added successfully'}, status=201)
        except (KeyError, json.JSONDecodeError) as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

@csrf_exempt
def clear_templates(request):
    if request.method == 'POST':
        remove_all_templates()
        return JsonResponse({'status': 'All templates removed successfully'}, status=200)
    
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

