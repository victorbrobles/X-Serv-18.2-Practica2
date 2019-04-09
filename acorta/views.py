from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Urls
from django.views.decorators.csrf import csrf_exempt

formulario = """
	<form action="" method="POST">
		URL:<br>
		<input type="text" name="url"><br><br>
		<input type="submit" value="Enviar">
	</form>
"""


@csrf_exempt


def bar (request):

	try:
		Urls.objects.get(short="localhost:1234/0")
		i=0
		for x in Urls.objects.all():
			i = i + 1
		
	except Urls.DoesNotExist:
		i=0

	if request.method == "GET":
		urls = Urls.objects.all()
		response = ""
		for url in urls:
			response += url.original + "	->	" + url.short + " " + "<br>"
		return HttpResponse (formulario + response)
	elif request.method == "POST":
		url = request.POST['url']
		if url == "":
			return HttpResponseNotFound ("Error, url vacia")
		url = url.replace("%3A", ":")
		url = url.replace("%2F", "/")

		if url.startswith('http://') or url.startswith('https://'):
			urlReal = url
		else:
			urlReal = str("http://" + url)

		try:
			url = Urls.objects.get(original=urlReal)
			link = str("<a href=" + str(url.short) + ">" + str(url.short) + "</a>")
			return HttpResponse("Url ya existente: " + link)

		except Urls.DoesNotExist:
			urlAcortada = str("localhost:1234/" + str(i))
			i = i + 1
			url = Urls (original=urlReal, short=urlAcortada)
			url.save()
			link1 = str("<a href=" + urlReal + ">" + urlReal + "</a>")
			link2 = str("<a href=" + urlAcortada + ">" + urlAcortada + "</a>")
			return HttpResponse(link1 + "	-->	" + link2)


def comprobar_url (request, numero):
	
	url = str("localhost:1234/" + str(numero))
	try:
		url = Urls.objects.get(short=url)
		return HttpResponseRedirect (str(url.original))
	except Urls.DoesNotExist:
		return HttpResponseNotFound ("No existe la url asociada a localhost:1234/" + str(numero))


def error (request, cadena):

	return HttpResponseNotFound ("Recurso " + cadena + " not found.")
			
									
			
			

		
