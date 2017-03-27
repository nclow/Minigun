import rest_framework_mongoengine.serializers as serializers
from minigunapp.models import Email

class EmailSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Email
        fields = '__all__'
