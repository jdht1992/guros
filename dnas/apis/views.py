from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dnas.models import Organism
from .serializers import OrganismModelSerializer
from dnas.mutation import Mutation


class StatsAPIView(APIView):

    def get(self, request):
        mutations, no_mutations, ratio = self._get_stats()
        data = {
            "count_mutations": mutations,
            "count_no_mutation": no_mutations,
            "ratio": ratio
        }                                      
        return Response(data)

    def _get_stats(self):
        positive_mutations, negative_mutations = self._get_mutations_amount()
        ratio = self._get_ratio(positive_mutations, negative_mutations)
        return positive_mutations, negative_mutations, ratio

    def _get_mutations_amount(self):
        positive_mutations = Organism.objects.filter(mutation=True).count()
        negative_mutations = Organism.objects.filter(mutation=False).count()
        return positive_mutations, negative_mutations

    def _get_ratio(self, positive_mutations, negative_mutations):
        if not negative_mutations:
            return 0.0
        return float(f"{positive_mutations / negative_mutations:.1f}")


class MutationAPIView(APIView):
    def post(self, request, format=None):
        serializer = OrganismModelSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.mutation = self._get_mutation(instance.dna)
            instance.save()
            if instance.mutation:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def _get_mutation(self, data):
        dna_sequence = [list(dna) for dna in data]
        return self._has_mutation(dna_sequence)

    def _has_mutation(self, dna_sequence):
        return Mutation.validate_genetic_difference(dna_sequence)
