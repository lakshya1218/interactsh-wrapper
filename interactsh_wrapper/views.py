from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import pandas as pd
import subprocess
import re
from .helper_functions import read_and_store_data, query_data, empty_file

interaction_data = {}
url_file_path = 'url.txt'
output_file_path = 'output.txt'


class GetURLView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        try:
            empty_file(url_file_path)
            read_and_store_data(output_file_path, interaction_data)

            command = "(./interactsh-client | tee " + output_file_path + ") 3>&1 1>&2 2>&3 | tee " + url_file_path

            subprocess.Popen(command, shell=True, text=True)

            content = ''
            oast_link_regex = re.compile(r'.*oast.*')

            while len(content) == 0:
                with open(url_file_path, 'r') as file:
                    content = file.read()
                    content = oast_link_regex.findall(content)

            link = content[0].split()[1]

            df = pd.DataFrame(columns=['datetime', 'value'])
            interaction_data[link.split('.')[0]] = df

            return JsonResponse({'url': link})

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)


class GetInteractionsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        try:
            read_and_store_data(output_file_path, interaction_data)

            link = request.GET.get('link').split('.')[0]

            if 'startDateTime' in request.GET:
                start_datetime = pd.to_datetime(request.GET.get('startDateTime'))
            else:
                start_datetime = pd.to_datetime('1970-01-01 00:00:00')

            if 'endDateTime' in request.GET:
                end_datetime = pd.to_datetime(request.GET.get('endDateTime'))
            else:
                end_datetime = pd.Timestamp.now()

            df = interaction_data[link]
            df = query_data(start_datetime, end_datetime, df)

            data_in_dict = df.to_dict()
            data_in_list = []

            for key, value in data_in_dict['value'].items():
                data_in_list.append(value)

            return JsonResponse({'interactions': data_in_list})

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
