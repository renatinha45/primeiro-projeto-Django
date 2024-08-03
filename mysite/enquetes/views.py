from django.shortcuts import render, get_object_or_404
from. models import Pergunta, Escolha
from django.urls import reverse
from django.http import HttpResponse, Http404


def index(request):
    ultimas_perguntas = Pergunta.objects.order_by("-data_publicacao")[:5]
    contexto = {'ultimas_perguntas': ultimas_perguntas}
    return render(request,'enquetes/index.html',contexto) 

def detalhes(request,pergunta_id):
    try:
        pergunta = pergunta.objects.get(pk=pergunta_id)
    except:
        raise "Http404"("A pergunta nao existe!")
    return render(request,'enquetes/detalhes.html',{'pergunta':pergunta})              


def detalhes(resquest, pergunta_id):
    return "HttpResponse(f"( "Você está acessando a questão) {pergunta_id}")


def resultados(request, pergunta_id):
    Pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/resultados.html" , {"pergunta": "pergunta"})
    
    
def votos(request, pergunta_id):
    Perguntas = get_object_or_404 (Perguntas, pk = pergunta_id)
    try:
        escolha_selecionada = pergunta.escolha_set.get (pk = request.POST ["escolha"])
    except (KeyError, Escolha.DoesNotExist):
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "question": Pergunta,
                "error_message" : "você não seçecionou uma escolha"

            }
        )
    else:
        escolha_selecionada.votos = F("votos") + 1
        escolha_selecionada.save()
    return HttpResponse(f'Você esetá votando na questão {pergunta_id}')