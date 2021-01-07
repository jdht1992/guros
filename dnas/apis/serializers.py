from rest_framework import serializers
from dnas.models import Organism


class OrganismModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organism
        fields = ['dna']