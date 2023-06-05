from django.shortcuts import render
from .models import Student,Marks
from rest_framework import viewsets,generics
from .serializer import StudentSerializer,MarkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class StuView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class MarkView(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
    lookup_field = 'id'

class ReportView(APIView):
    def get(self, request, format=None):
        Mark = Marks.objects.all()
        sgrade = agrade = bgrade= cgrade = dgrade = egrade = fgrade = 0
        tot_marks = 0

        for student in Mark:
            if student.mark >= 91:
                sgrade += 1
            elif student.mark >= 81:
                agrade += 1
            elif student.mark >= 71:
                bgrade += 1
            elif student.mark >= 61:
                cgrade += 1
            elif student.mark >= 51:
                dgrade += 1
            elif student.mark >= 50:
                egrade += 1
            else:
                fgrade += 1

            tot_marks += student.mark

        pass_percentage = ((len(Mark) - fgrade) / len(Mark)) * 100

        report = {
            "S Grade": sgrade,
            "A Grade": agrade,
            "B Grade": bgrade,
            "C Grade": cgrade,
            "D Grade": dgrade,
            "E Grade": egrade,
            "F Grade": fgrade,
            "Pass Percentage": pass_percentage
        }

        return Response(report)