from ..models import Manografia_models
from ..serializers import ManografiaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated


@swagger_auto_schema(
    methods=['GET'],
    operation_summary="Obtém uma lista de todas as manografias.",
    tags=['manografia'],
    responses={200: openapi.Response(
        "Lista de manografias", ManografiaSerializer(many=True))},
    security=[{"Bearer": []}]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manografia_get(request):
    manografias = Manografia_models.objects.all()
    serializer = ManografiaSerializer(manografias, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    methods=['GET'],
    operation_summary="Obtém detalhes de uma manografia pelo seu ID.",
    tags=['manografia'],
    responses={200: openapi.Response(
        "Detalhes da manografia", ManografiaSerializer)},
)
@api_view(['GET'])
def manografia_get_id(request, pk):
    try:
        manografia = Manografia_models.objects.get(pk=pk)
    except Manografia_models.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ManografiaSerializer(manografia)
    return Response(serializer.data)


@swagger_auto_schema(
    methods=['POST'],
    operation_summary="Cria uma nova manografia.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'titulo': openapi.Schema(type=openapi.TYPE_STRING),
            'autor': openapi.Schema(type=openapi.TYPE_INTEGER),
            'orientador': openapi.Schema(type=openapi.TYPE_INTEGER),
            'coorientador': openapi.Schema(type=openapi.TYPE_INTEGER),
            'resumo': openapi.Schema(type=openapi.TYPE_STRING),
            'palavras_chave': openapi.Schema(type=openapi.TYPE_STRING),
            'data_entrega': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            'banca_examinadora': openapi.Schema(type=openapi.TYPE_STRING),
            'nota_final': openapi.Schema(type=openapi.TYPE_INTEGER),
            'area_concentracao': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['titulo', 'autor_id', 'orientador_id', 'coorientador_id', 'resumo',
                'palavras_chave', 'data_entrega', 'banca_examinadora', 'nota_final', 'area_concentracao']
    ),
    tags=['manografia'],
    responses={201: openapi.Response(
        "Manografia criada com sucesso", ManografiaSerializer)},
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def manografia_post(request):
    serializer = ManografiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['PUT'],
    operation_summary="Atualiza uma manografia existente pelo seu ID. Não é necessário enviar todos os campos no corpo da solicitação, apenas o(s) que deseja atualizar.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'titulo': openapi.Schema(type=openapi.TYPE_STRING),
            'autor': openapi.Schema(type=openapi.TYPE_INTEGER),
            'orientador': openapi.Schema(type=openapi.TYPE_INTEGER),
            'coorientador': openapi.Schema(type=openapi.TYPE_INTEGER),
            'resumo': openapi.Schema(type=openapi.TYPE_STRING),
            'palavras_chave': openapi.Schema(type=openapi.TYPE_STRING),
            'data_entrega': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE),
            'banca_examinadora': openapi.Schema(type=openapi.TYPE_STRING),
            'nota_final': openapi.Schema(type=openapi.TYPE_INTEGER),
            'area_concentracao': openapi.Schema(type=openapi.TYPE_STRING),
        },
    ),
    tags=['manografia'],
    responses={200: openapi.Response(
        "Manografia atualizada com sucesso", ManografiaSerializer)},
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def manografia_put(request, pk):
    try:
        manografia = Manografia_models.objects.get(pk=pk)
    except Manografia_models.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ManografiaSerializer(manografia, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['DELETE'],
    operation_summary="Exclui uma manografia existente pelo seu ID.",
    responses={204: "Manografia excluída com sucesso"},
    tags=['manografia'],
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def manografia_delete(request, pk):
    try:
        manografia = Manografia_models.objects.get(pk=pk)
    except Manografia_models.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    manografia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)