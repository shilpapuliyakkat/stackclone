from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from api.serializers import UserSerializer,ProfileSerializer,QuestionSerializer,AnswersSerializer
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import authentication,permissions
from stack.models import UserProfile,Questions,Answers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import serializers

# Create your views here.

# class UsersView(ViewSet):
#     def create(self,request,*args,**kwargs):

#         serializer_class=UserSerializer
#         serializer=UserSerializer(data=serializer.data)
#         if serializer.is_valid(): 
#            serializer.save()
#            return Response(data=request.data)
#         else:
#             return Response(data=serializer.errors)

class UsersView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
class ProfileView(ModelViewSet):
    serializer_class=ProfileSerializer
    queryset=UserProfile.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


    # def get_queryset(self):
    #     return UserProfile.objects.filter(user=self.request.user)

    def destroy(self,request,*args,**kwargs):
        prof=self.get_object()
        if prof.user!=request.user:
            raise serializers.ValidationError("not allowed to perform")
        else:
            return super().destroy(request,*args,**kwargs)




class QuestionView(ModelViewSet):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def destroy(self,request,*args,**kwargs):
        ans=self.get_object()
        if ans.user!=request.user:
            raise serializers.ValidationError("not allowed to perform")
        else:
            return super().destroy(request,*args,**kwargs)    

    # def get_queryset(self):
    #     return Questions.objects.all().order_by("-created_date")
    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        serializer=AnswersSerializer(data=request.data)
        quest=self.get_object()
        user=request.user
        if serializer.is_valid():
          serializer.save(question=quest,user=user)
          return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class AnswersView(ModelViewSet):
    serializer_class=AnswersSerializer
    queryset=Answers.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    # permission_classes=[permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method not allowed")
    
    def destroy(self,request,*args,**kwargs):
        ans=self.get_object()
        if ans.user!=request.user:
            raise serializers.ValidationError("not allowed to perform")
        else:
            return super().destroy(request,*args,**kwargs)
    


    
    @action(methods=["post"],detail=True)
    def add_up_vote(self,request,*args,**kwargs):
        answer=self.get_object()
        answer.up_vote.add(request.user)
        answer.save()
        return Response(data="upvoted")
    
    @action(methods=["post"],detail=True)
    def down_up_vote(self,request,*args,**kwargs):
        answer=self.get_object()
        answer.up_vote.remove(request.user)
        answer.save()
        return Response(data="upvote Removed")


