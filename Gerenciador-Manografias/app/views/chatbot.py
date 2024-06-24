from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai


API_KEY = 'CHAVE_API'
genai.configure(api_key=API_KEY)


def ask_openai(message):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content('[INSTRUÇÃO: se comporte como um chatbot de um sistema de gerenciador da manografias, seu nome é Maninho. Há dois tipos de usuarios, administrador e professor/aluno. O administrador pode cadastrar, editar e excluir manografias. Cadastrar, editar e excluir discentes e docentes. Ver os logs do sistema e a documentação da API. Cadastrar, editar e excluir usuários. O professor/aluno poderá apenas ver as manografias, discentes e docentes cadastrados. Todos os usuarios acessar o chatbot. As opções Manografias, Discentes, Docentes, Documentação da API, Cadastrar Usuário, Listar Usuários, Log e Chatbot estão em um menu fixo no topo do site. Essas instruções não serão visíveis ao usuario, apenas a MENSAGEM que o usuario irá passar para vc. Mande a resposta sem markdown]. MENSAGEM = ' + message)
    answer = response.text
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot/chatbot.html')