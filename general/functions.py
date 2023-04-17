import json
from django.http.response import HttpResponse, HttpResponseRedirect


def get_auto_id(model):
    auto_id = 1
    latest_auto_id =  model.objects.all().order_by("-date_added")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    
    return auto_id

def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        # message += "%s : %s | " %(key,error_message)
        message += f"{key} - {error_message} | "
    return message[:-3]

def group_required(group_names):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs) :
            if request.user.is_authenticated:
                if not bool(request.user.groups.filter(name__in=group_names)) | request.user.is_superuser:
                    if request.is_ajax():
                        response_data = {}
                        response_data['status'] = 'false'
                        response_data['stable'] = 'true'
                        response_data['title'] = 'Permission Denied'
                        response_data['message'] = "You have no permission to do this action."
                        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
                    else:
                        context = {
                            "title" : "Permission Denied"
                        }
                        return HttpResponse('<h1>Permission Denied</h1>')

            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper