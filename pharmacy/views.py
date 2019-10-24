import json

import telepot
from django.conf import settings
from django.http import HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework import generics, status
from rest_framework.response import Response

from pharmacy.models import Organization, Branch, Medicament, MedicamentInBranch, Category
from pharmacy.serializers import OrganizationSerializer, BranchSerializer, MedicamentSerializer, \
    MedicamentInBranchSerializer, CategorySerializer


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BranchView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class MedicamentView(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query:
            medicaments = self.queryset.filter(name__contains=query)
        else:
            medicaments = self.queryset.all()
        serializer = self.serializer_class(medicaments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MedicamentInBranchView(generics.ListCreateAPIView):
    queryset = MedicamentInBranch.objects.all()
    serializer_class = MedicamentInBranchSerializer

    def get(self, request, pk=None, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.filter(branch_id=pk), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def find_drugs(request):
    items = MedicamentInBranch.objects.filter(medicament__name=request)
    return render_to_string('feed.md', {'items': items})

token = settings.TELEGRAM_BOT_TOKEN
TelegramBot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
TelegramBot.setWebhook('https://intense-lowlands-30460.herokuapp.com/api/bot/{token}/'.format(token=token))


class CommandReceiveView(View):
    def post(self, request, bot_token):
        if bot_token != settings.TELEGRAM_BOT_TOKEN:
            return HttpResponseForbidden('Invalid Token')
        raw = request.body.decode('utf8')
        jsn = json.loads(raw, strict=False)
        commands = {
            jsn['message']['text']: find_drugs(jsn['message']['text'])
        }
        try:
            payload = json.loads(raw, strict=False)
        except ValueError:
            return HttpResponseRedirect('Invalid Request Body')
        else:
            chat_id = payload['message']['chat']['id']
            cmd = payload['message'].get('text')
            func = commands.get(cmd.split()[0].lower())

            if func:
                TelegramBot.sendMessage(chat_id, func, parse_mode='Markdown')
            else:
                TelegramBot.sendMessage(chat_id, 'I dont no')
        return JsonResponse({"message":"OK"}, status=status.HTTP_200_OK)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)
