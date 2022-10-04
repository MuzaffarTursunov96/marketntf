from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'avatar', 'biograph')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            avatar=validated_data['avatar'],
            biograph=validated_data['biograph'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # implement your logic here
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['avatar'] = str(self.user.avatar)
        data['biograph'] = self.user.biograph
        return data

class AssetSerializer(serializers.ModelSerializer):
  creator = serializers.SerializerMethodField('get_creator') 
  history = serializers.SerializerMethodField('get_history') 
  # image = serializers.SerializerMethodField('get_image') 
  # time_left = serializers.SerializerMethodField('get_time_left')
  class Meta:
        model = Projects
        fields =["id","slug","liked","likes","name","image","description","price","time_left","updated_at","creator","collection","history"]
        depth = 1
  
  def get_creator(self,project):
    name =project.creator.username
    avatar =str(project.creator.avatar)
    return {'name':name,'avatar':avatar}

  def get_history(self,project):
    histories =History.objects.filter(project=project)
    total = len(histories)
    data = []
    for history in histories:
      data.append({'date':history.date,'price':history.price})
    return{"total":total,'data':data}

  

class AssetsAllSerializer(serializers.ModelSerializer):
  # image = serializers.SerializerMethodField('get_image') 
  # time_left = serializers.SerializerMethodField('get_time_left')
  class Meta:
    model = Projects
    fields =["id","name","liked","likes","slug","image","price","time_left","biddings"]

class CollectionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collection
    fields ="__all__"  

class CreateAssetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ["name","slug","image","price","time_left","collection","creator"]
