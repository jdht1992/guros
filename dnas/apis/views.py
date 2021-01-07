from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dnas.models import Organism
from .serializers import OrganismModelSerializer
from dnas.mutation import Mutation


class StatsAPIView(APIView):

    def get(self, request, format=None):
        mutations = Organism.objects.filter(mutation=True).count()
        no_mutations = Organism.objects.filter(mutation=False).count()
        ratio = 0
        if no_mutations > 0:
            ratio = mutations / no_mutations
        data = {
            "count_mutations": mutations,
            "count_no_mutation": no_mutations,
            "ratio": f"{ratio:.1f}"
        }                                      
        return Response(data)


class MutationAPIView(APIView):
    def post(self, request, format=None):
        serializer = OrganismModelSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.initial_data.get("dna") 
            mutations = self.has_mutation([list(dna) for dna in data])
            serializer.save(mutation=mutations)  # instance = serializer.save()   instance.mutation = self._get_mutation()   instance.save()
            if mutations:
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def _get_mutation(self):
        # Y aqui generaria la instancia a la clase Mutation y lo que tienes en has mutation iria aqui 
        return is_mutation

    """

    def has_mutation(self, data):
        """
        return any([mutation.horizontal(data), mutation.vertical(data)])
        """
        if Mutation.horizontal(data):
            return True  
        if Mutation.vertical(data):
            return True
        else:
            return False
