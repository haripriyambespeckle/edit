from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dashboard.models import ClusterInfo,DashboardResult,InvoiceDetails
from json import loads
from django.core.serializers import serialize
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from django.db import connection
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from.models import InvoiceDetails
# from dashboard.views import invoice_report


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        try:
            page = paginator.page(page_number)
        except Exception as exc:
            # Handle invalid page numbers
            return None

        self.page = page
        self.request = request
        return list(page)

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })














# www.example.com/api/invoice_report

# Create your views here.
class Dashboard(APIView):
    def get(self,request):
        return Response(
            {"beneficariesCovered": "1053902",
             "investigationsCovered": "1091806",
             "emergencyCases": "41761",
             "emergencyCasesReported": "41758",
             "tatMet %": "98.54",
             "totalNumberOfDistrictsUnderPPP": "48",
             "totalnumberOfFunctionalUnitsUnderPPP" :"44"}
        )

class functn(APIView):
    def get(self,request):
        return Response(
            [
                {
                    "slNo":"1",
                    "district":"LakhimpurKheri",
                    "category":"Category 1",
                    "commencementDate":"Nov. 23, 2017",
                    "instituteName":"Old CMO office, District Hospital (Male) - LakhimpurKheri (U.P.) 262701",
                    "scans":"28228	",
                    "patients":"27720"
                },
                {
                    "slNo":"2",
                    "district":"Pilibhit",
                    "category":"Category 1",
                    "commencementDate":"Dec. 9, 2017",
                    "instituteName":"District Hospital (Male) - Tanakpur Road, Pilibhit (U.P.) 262001",
                    "scans":"21123",
                    "patients":"20711"
                },
                {
                    "slNo":"3",
                    "district":"Chandauli",
                    "category":"Category 1",
                    "commencementDate":"Dec. 8, 2017",
                    "instituteName":"Pt. Kamlapati District Hospital (Combined), Gautam Nagar - Chandauli (U.P.) 232104",
                    "scans":"35815",
                    "patients":"33797"
                },



                {
                    "slNo": "4",
                    "district": "Deoria",
                    "category": "Category 1",
                    "commencementDate": "ec. 16, 2017",
                    "instituteName": "Diagnostic Centre Building, District Hospital (Male) - Deoria (U.P.) 274001",
                    "scans": "66469",
                    "patients": "64755"
                },


                {
                    "slNo": "5",
                    "district": "	Mathura",
                    "category": "Category 1",
                    "commencementDate": "Dec. 23, 2017",
                    "instituteName": "Maharishi dayanad District Hospital - Mathura",
                    "scans": "25783",
                    "patients": "22930"
                },



                {
                    "slNo": "6",
                    "district": "Farrukhabad",
                    "category": "Category 1",
                    "commencementDate": "	Dec. 30, 2017",
                    "instituteName": "Ram Manohar Lohia Combined District Hospital - Farrukhabad	",
                    "scans": "21853",
                    "patients": "2"
                },



                {
                    "slNo": "7",
                    "district": "Hathras",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "Bagla District Hospital - Hathras",
                    "scans": "32186",
                    "patients": "31037"
                },


                {
                    "slNo": "8",
                    "district": "SantKabir Nagar",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "District Hospital (Combined) , Khalilabad - SantKabir Nagar",
                    "scans": "23964",
                    "patients": "22374"
                },


                {
                    "slNo": "9",
                    "district": "Kaushambi",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "District Hospital (Combined) Manjhanpur - Kaushambi",
                    "scans": "35785",
                    "patients": "35481"
                },



                {
                    "slNo": "10",
                    "district": " Sitapur",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "District Hospital (Male) - Sitapur",
                    "scans": "23997",
                    "patients": "23480"
                },

                {
                    "slNo": "11",
                    "district": "Aligarh ",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "DeenDayalUpadhyay District Hospital - Aligarh",
                    "scans": "30229",
                    "patients": "29212"
                },

                {
                    "slNo": "12",
                    "district": "Shahjahanpur ",
                    "category": "Category 1",
                    "commencementDate": "Jan. 24, 2018",
                    "instituteName": "	Pt. Ram Prasad Bismil District hospital (Combined) Azizganj - Shajahanpur (U.P.) 242226",
                    "scans": "47017",
                    "patients": "46552"
                },

                {
                    "slNo": "13",
                    "district": "	Chitrakoot ",
                    "category": "Category 1",
                    "commencementDate": "Feb. 26, 2018",
                    "instituteName": "	District Hospital (Combined) - KarwiMafi (U.P.) 210205",
                    "scans": "19007",
                    "patients": "18652"
                },

                {
                    "slNo": "14",
                    "district": "Ambedkar Nagar ",
                    "category": "Category 1",
                    "commencementDate": "March 2, 2018",
                    "instituteName": "MJPC District Hospital Akbarpur (Ambaedkar Nagar) UP 224122	",
                    "scans": "45201",
                    "patients": "45156"
                },

                {
                    "slNo": "15",
                    "district": " Mahoba",
                    "category": "Category 1",
                    "commencementDate": "March 20, 2018",
                    "instituteName": "District Hospital (Male) - Mahoba",
                    "scans": "21355",
                    "patients": "21098"
                },

                {
                    "slNo": "16",
                    "district": "Siddharthnagar ",
                    "category": "Category 1",
                    "commencementDate": "April 17, 2018",
                    "instituteName": "District Hospital - Siddharth Nagar",
                    "scans": "36539",
                    "patients": "35923"
                },

                {
                    "slNo": "17",
                    "district": "Hamirpur ",
                    "category": "Category 1",
                    "commencementDate": "April 16, 2018",
                    "instituteName": "District Hospital (Male) - Hamirpur",
                    "scans": "12889",
                    "patients": "12520"
                },

                {
                    "slNo": "18",
                    "district": "Balrampur ",
                    "category": "Category 1",
                    "commencementDate": "May 3, 2018",
                    "instituteName": "District Hospital - SH 26, Balrampur",
                    "scans": "24555",
                    "patients": "24036"
                },

                {
                    "slNo": "19",
                    "district": "	Mau ",
                    "category": "Category 1",
                    "commencementDate": "June 13, 2018",
                    "instituteName": "District Hospital - Mau",
                    "scans": "41627",
                    "patients": "40125"
                },

                {
                    "slNo": "20",
                    "district": " Auraiya",
                    "category": "Category 1",
                    "commencementDate": "May 4, 2018",
                    "instituteName": "District Hospital - Auraiya",
                    "scans": "14812	",
                    "patients": "14507"
                },

                {
                    "slNo": "21",
                    "district": " Shravasti",
                    "category": "Category 1",
                    "commencementDate": "May 7, 2018",
                    "instituteName": "Combined District Hospital, Bhinga - Shravasti",
                    "scans": "34085",
                    "patients": "33495"
                },

                {
                    "slNo": "22",
                    "district": "Ghazipur	 ",
                    "category": "Category 1",
                    "commencementDate": "July 11, 2018	",
                    "instituteName": "District Hospital (Male) – Gaura Bazar - Ghazipur (UP) 233001	",
                    "scans": "66265",
                    "patients": "66252"
                },

                {
                    "slNo": "23",
                    "district": "Lucknow ",
                    "category": "Category 2",
                    "commencementDate": "July 26, 2018	",
                    "instituteName": "Dr. Ram Manohar Lohia Hospital, Vibhuti Khand Lucknow (UP)-226010",
                    "scans": "42674",
                    "patients": "41184"
                },

                {
                    "slNo": "24",
                    "district": "Kasganj ",
                    "category": "Category 1",
                    "commencementDate": "	March 6, 2019",
                    "instituteName": "District Hospital - Kasganj",
                    "scans": "16273",
                    "patients": "15436"
                },

                {
                    "slNo": "25",
                    "district": "Hardoi ",
                    "category": "Category 2",
                    "commencementDate": "Sept. 11, 2019",
                    "instituteName": "District Hospital - Hardoi (UP)-241001",
                    "scans": "35494",
                    "patients": "34332"
                },

                {
                    "slNo": "26",
                    "district": " Kanpur ",
                    "category": "Category 2",
                    "commencementDate": "March 26, 2019",
                    "instituteName": "Manyavar Kanshiram Combined Hospital(Male) - Kanpur(UP) - 284403 ",
                    "scans": "12005",
                    "patients": "11024"
                },

                {
                    "slNo": "27",
                    "district": "Lalitpur ",
                    "category": "Category 2",
                    "commencementDate": "June 29, 2020",
                    "instituteName": "Manyavar Kanshiram Combined Hospital (Male) - Lalitpur (UP)-284403",
                    "scans": "13887",
                    "patients": "12937"
                },

                {
                    "slNo": "28",
                    "district": "Amethi ",
                    "category": "Category 1",
                    "commencementDate": "Jan. 4, 2019	",
                    "instituteName": "District Hospital - Amethi",
                    "scans": "41559",
                    "patients": "40858"
                },

                {
                    "slNo": "29",
                    "district": "Kushinagar ",
                    "category": "Category 1",
                    "commencementDate": "May 30, 2019	",
                    "instituteName": "District Hospital - KushiNagar",
                    "scans": "27421",
                    "patients": "27142"
                },

                {
                    "slNo": "30",
                    "district": "Banda ",
                    "category": "Category 2",
                    "commencementDate": "June 20, 2019",
                    "instituteName": "District Hospital Banda (UP) - 210001",
                    "scans": "41093",
                    "patients": "39711"
                },

                {
                    "slNo": "31",
                    "district": "Basti ",
                    "category": "Category 2",
                    "commencementDate": "Aug. 12, 2019",
                    "instituteName": "District Hospital Basti (UP) - 272001	",
                    "scans": "14890",
                    "patients": "14492"
                },

                {
                    "slNo": "32",
                    "district": "Barabanki ",
                    "category": "Category 2",
                    "commencementDate": "Sept. 9, 2019",
                    "instituteName": "District Hospital Barabanki (UP) - 225001	",
                    "scans": "14141",
                    "patients": "13380"
                },


                {
                    "slNo": "33",
                    "district": " Fatehpur",
                    "category": "Category 2",
                    "commencementDate": "Aug. 8, 2019",
                    "instituteName": "District Hospital (Male) - Fatehpur (UP) - 212601	",
                    "scans": "21903",
                    "patients": "20795"
                },

                {
                    "slNo": "34",
                    "district": "Unnao ",
                    "category": "Category 2",
                    "commencementDate": "Aug. 14, 2019",
                    "instituteName": "District Hospital Unnao (UP) - 209801	",
                    "scans": "20099",
                    "patients": "19593"
                },



                {
                    "slNo": "35",
                    "district": "Jalaun ",
                    "category": "Category 1",
                    "commencementDate": "Aug. 27, 2019	",
                    "instituteName": "District Hospitall Orai (Jalaon ) (UP) - 285001	",
                    "scans": "21087",
                    "patients": "20798"
                },



                {
                    "slNo": "36",
                    "district": " Kannauj",
                    "category": "Category 2",
                    "commencementDate": "	Oct. 22, 2019",
                    "instituteName": "District Hospital - Kannauj (UP) 209801	",
                    "scans": "9752",
                    "patients": "9667"
                },

                {
                    "slNo": "37",
                    "district": "Ayodhya ",
                    "category": "Category 2",
                    "commencementDate": "July 15, 2020",
                    "instituteName": "100 BED Hospital, Darshan Nagar - Faizabad (UP) 224123	",
                    "scans": "17821",
                    "patients": "16921"
                },

                {
                    "slNo": "38",
                    "district": "Maharajganj ",
                    "category": "Category 1",
                    "commencementDate": "	Jan. 25, 2022",
                    "instituteName": "District Hospital (Combined) – Maharajganj (UP) -273303	",
                    "scans": "12546",
                    "patients": "11997"
                },

                {
                    "slNo": "39",
                    "district": "Prayagraj ",
                    "category": "Category 1",
                    "commencementDate": "Feb. 25, 2022",
                    "instituteName": "T.B. Sapru Hospital - Stanley Rd	",
                    "scans": "6530	",
                    "patients": "6126"
                },

                {
                    "slNo": "40",
                    "district": "Varanasi ",
                    "category": "Category 1",
                    "commencementDate": "Nov. 5, 2021",
                    "instituteName": "SSPG Divisional District Hospital		",
                    "scans": "15089	",
                    "patients": "9266"
                },

                {
                    "slNo": "41",
                    "district": " Shamli",
                    "category": "Category 3",
                    "commencementDate": "	Feb. 1, 2023",
                    "instituteName": "District Combined Hospital, Near Canal Road (Village Mundet),"
                                     " Shamli - PIN Code 24336, Uttar Pradesh		",
                    "scans": "0	",
                    "patients": "0"
                },

                {
                    "slNo": "42",
                    "district": "Ghaziabad ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "MMG Hospital, Grand Trunk Rd, nr. Ghanta Ghar, Bihari Pura, Sarai Nagar, Naya Ganj, Ghaziabad, Pin Code 201001,"
                                     " Uttar Pradesh		",
                    "scans": "0	",
                    "patients": "0"
                },

                {
                    "slNo": "43",
                    "district": "Sambhal ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023	",
                    "instituteName": "District Hospital, Chaman Sarai - Sambhal - Pin code 244302, Uttar Pradesh		",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "44",
                    "district": " Amroha",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "District Combined Hospital, Hasanpur - Amroha Rd, near SP Office, Amroha - Pin code 244221, Uttar Pradesh		",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "45",
                    "district": "Bareilly",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "Maharana Pratap Combined District Hospital,Civil Lines, Bareilly - Pin code 243003, Uttar Pradesh		",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "46",
                    "district": "Mainpuri ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "District Hospital, Kachahri Road, Mainpuri - Pin code 205001, Uttar Pradesh		",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "47",
                    "district": "Etah ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "	District Hospital, Police Line, Etah - Pin code 207001, Uttar Pradesh	",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "48",
                    "district": "Jhansi ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 1, 2023",
                    "instituteName": "District Hospital (Male), Nehru Marg, Manik Chowk, Jhansi -Pin codeÿ 284002, Uttar Pradesh		",
                    "scans": "0",
                    "patients": "0"
                },

                {
                    "slNo": "49",
                    "district": "Gorakhpur ",
                    "category": "Category 3",
                    "commencementDate": "Feb. 20, 2023",
                    "instituteName": "AIIMS GorakhPur, PIN -273001, Uttar Pradesh		",
                    "scans": "1",
                    "patients": "1"
                },


            ]
        )
class non_functn(APIView):
    def get(self,request):
        return Response(
            [
                {
                    "slNo":"1",
                    "district":"LakhimpurKheri",
                    "category":"Category 1",
                    "commencementDate":"Nov. 23, 2017",
                    "instituteName":"Old CMO office, District Hospital (Male) - LakhimpurKheri (U.P.) 262701",
                    "scans":"28228",
                    "patients":"27720"
                },
                {
                    "slNo":"2",
                    "district":"Pilibhit",
                    "category":"Category 1",
                    "commencementDate":"Dec. 9, 2017",
                    "instituteName":"District Hospital (Male) - Tanakpur Road, Pilibhit (U.P.) 262001",
                    "scans":"21133",
                    "patients":"21133"
                },
                {
                    "slNo":"3",
                    "district":"Chandauli",
                    "category":"Category 1",
                    "commencementDate":"	Dec. 8, 2017",
                    "instituteName":"Pt. Kamlapati District Hospital (Combined), Gautam Nagar - Chandauli (U.P.) 232104",
                    "scans":"35815",
                    "patients":"33797"
                }

            ]
        )





# class ClusterInfo():
#     pass
class district_code(APIView):
    def get(self, request):
            data = ClusterInfo.objects.distinct().values('district_code', 'district')
            return Response(
                {
                    "districts":data
                })
class functional_centres(APIView):
    def get(self, request):
            cursor = connection.cursor()
            query = """SELECT district,institute,categoryId,commencement_date,
                    case when scanres.patientcount is null then 0 else scanres.patientcount end as patientcount,
                    case when scanres.totalscans is null then 0 else scanres.totalscans end as totalscans
                    from cluster_info ci 
                    left join (SELECT sum(patientCount) as patientcount,sum(totalScans) as totalscans, centerId  from 
                    dashboard_result dr  group by centerId ) as scanres on scanres.centerId = ci.centerId where centerStatus='active'"""
            cursor.execute(query)
            data = cursor.fetchall()
            data = [{
                 "district":l[0],
                 "instituteName":l[1],
                 "category":l[2],
                 "commencementDate":l[3],
                 "patients":l[4],
                 "scans":l[5]
            } for l in data]
            return JsonResponse(data, safe=False)
    
class non_functional_centres(APIView):
    def get(self,request):
        cursor = connection.cursor()
        query = """SELECT district,institute,categoryId,commencement_date,
                case when scanres.patientcount is null then 0 else scanres.patientcount end as patientcount,
                case when scanres.totalscans is null then 0 else scanres.totalscans end as totalscans
                from cluster_info ci 
                left join (SELECT sum(patientCount) as patientcount,sum(totalScans) as totalscans, centerId  from 
                dashboard_result dr  group by centerId ) as scanres on scanres.centerId = ci.centerId where centerStatus='inactive'"""
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{
                "district":l[0],
                "instituteName":l[1],
                "category":l[2],
                "commencementDate":l[3],
                "patients":l[4],
                "scans":l[5]
        } for l in data]
        return JsonResponse(data, safe=False)
    
class district_scan_count(APIView):
    def get(self, request):
        cursor = connection.cursor()
        query = """select ci.district ,sum(scanres.patientcount) as patientcount ,sum(scanres.totalscans) as totalscans from cluster_info ci
                left join (SELECT sum(patientCount) as patientcount,sum(totalScans) as totalscans, centerId  from 
                dashboard_result dr  group by centerId ) as scanres  on scanres.centerId = ci.centerId group by district"""
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{
            "district":l[0],
            "patientcount":l[1],
            "totalscans":l[2]
        } for l in data]
        return JsonResponse({"data":data}, safe=False)
    
class count(APIView):
    def get(self, request):
        cursor = connection.cursor()
        query = """SELECT SUM(patientCount), SUM(ctscan), SUM(otherscan), SUM(reportedStudy), SUM(reportedCTStudy), SUM(reportedOtherStudy),
                SUM(unReportedStudy), SUM(unReportedCTStudy), SUM(unReportedOtherStudy), SUM(emergencyCase), SUM(emergencyCaseReported),
                SUM(groupId), SUM(totalScans), SUM(category), SUM(allCentersTATMetPercentage)
                FROM dashboard_group_result;"""
        cursor.execute(query)
        data = cursor.fetchall()
        data = [{
            "patientcount":l[0],
            "ctscan":l[1],
            "otherscan":l[2],
            "reportedstudy":l[3],
            "reportedctstudy":l[4],
            "reportedotherstudy":l[5],
            "unreportedstudy":l[6],
            "unreportedctscan":l[7],
            "unreportedotherstudy":l[8],
            "emergencycase":l[9],
            "emergencycasereported":l[10],
            "groupid":l[11],
            "totalscans":l[12],
            "category":l[13],
            "allcenterstatmetpercentage_count":l[14]
        } for l in data]
        return JsonResponse({"data":data}, safe=False)


class dashboard_result(APIView):
    def get(self,request):
        data = DashboardResult.objects.distinct().values('id','patientcount','ctscan','otherscan','reportedstudy',
                                                         'reportedctstudy','reportedotherstudy','unreportedstudy',
                                                         'unreportedctstudy','unreportedotherstudy',
                                                         'emergencycase','emergencycasereported','centerid',
                                                         'groupid','totalscans','institute',
                                                         'category','ordercount','patientscandonecount','tatmetpercentage')

        return Response(
            {
                "dashboardResult": data,
            })

class scan_category1(APIView):
     def get(self, request):
        cursor = connection.cursor()
        query ="select ci.district,ci.institute,scanres.totalscans from cluster_info ci left join (SELECT sum(totalScans) as totalscans, centerId  from dashboard_result dr  group by centerId ) as scanres on scanres.centerId = ci.centerId WHERE ci.categoryId = 'category 1'"
        cursor.execute(query)
        data = cursor.fetchall()
        data=[{"Type":"District Hospital",
               "district":l[0],
               "institute":l[1],
               "totalscans":l[2]
        }for l in data]
        return JsonResponse({"data":data}, safe=False)


class scan_category2(APIView):
     def get(self, request):
        cursor = connection.cursor()
        query ="select ci.district,ci.institute,scanres.totalscans from cluster_info ci left join (SELECT sum(totalScans) as totalscans, centerId  from dashboard_result dr  group by centerId ) as scanres on scanres.centerId = ci.centerId  where ci.categoryId = 'category 2' "
        cursor.execute(query)
        data = cursor.fetchall()
        data=[{"Type":"District Hospital",
               "district":l[0],
               "institute":l[1],
               "totalscans":l[2]
        }for l in data]
        return JsonResponse({"data":data}, safe=False)

class scan_category3(APIView):
     def get(self, request):
        cursor = connection.cursor()
        query ="select ci.district,ci.institute,scanres.totalscans from cluster_info ci left join (SELECT sum(totalScans) as totalscans, centerId  from dashboard_result dr  group by centerId ) as scanres on scanres.centerId = ci.centerId WHERE ci.categoryId = 'category 3' "
        cursor.execute(query)
        data = cursor.fetchall()
        data=[{"Type":"District Hospital",
               "district":l[0],
               "institute":l[1],
               "totalscans":l[2]
        }for l in data]
        return JsonResponse({"data":data}, safe=False)

class totalcount_highest_lowest_district(APIView):
    def get(self, request):
        cursor = connection.cursor()
        query = """select sum(pd.todayStudyCount) as totalscans from pie_data pd"""
        cursor.execute(query)
        data = cursor.fetchall()
        data=[{"totalscans":l[0]
              }for l in data]
        return JsonResponse({"data": data},safe=False)



class emergencycase(APIView):
    def get(self, request):
        cursor = connection.cursor()
        query ="""select sum(patientCount) as patientCount ,sum(dr.reportedCTStudy) as reportedCTStudy ,
                  sum(dr.unReportedCTStudy) as unReportedCTStudy ,sum(dr.emergencyCase) as emergencyCase ,
                  sum(emergencyCaseReported) emergencyCaseReported 
                  from dashboard_result dr"""
        cursor.execute(query)
        data = cursor.fetchall()
        data=[{"patientCount":l[0],
               "reportedCTStudy":l[1],
               "unReportedCTStudy":l[2],
               "emergencyCaseReported":l[3]
        }for l in data]
        return JsonResponse({"data":data}, safe=False)

class district_code_count(APIView):
    def post(self, request):
        district_code = request.data['district_code']
        if district_code:
            cursor = connection.cursor()
            query = """SELECT SUM(patientCount) AS patientCount,
                            SUM(totalScans) AS totalScans,
                            SUM(emergencyCase) AS emergencyCase,
                            SUM(emergencyCaseReported) AS emergencyCaseReported,
                            AVG(tatMetPercentage) AS tatMetPercentage 
                        FROM dashboard_result dr 
                        LEFT JOIN cluster_info ci ON dr.centerId = ci.centerId
                        WHERE ci.district_code = %s"""
            cursor.execute(query, [district_code])
            data = cursor.fetchall()
            data = [{"patientCount": l[0],
                    "totalScans": l[1],
                    "emergencyCase": l[2],
                    "emergencyCaseReported": l[3],
                    "tatMetPercentage": l[4]} for l in data]
            return JsonResponse({"data": data}, safe=False)
        else:
            return JsonResponse({"error": "district_code parameter is required"}, status=400)

class patient_category_count(APIView):
    def get(self,request):
            cursor = connection.cursor()
            query = """select sum(patientcount),categoryId from(
            select scanres.patientcount,ci.categoryId ,ci.centerId  from cluster_info ci 
            left join (SELECT sum(patientCount) as patientcount,centerId  from 
            dashboard_result dr  group by centerId ) as scanres 
            on scanres.centerId = ci.centerId  GROUP by ci.centerId,ci.categoryId  ) 
            as datart group by datart.categoryId"""
            cursor.execute(query)
            data = cursor.fetchall()
            data = [{"patientCount": l[0],
                    "category": l[1]
                    } for l in data]
            return JsonResponse(data, safe=False)

class invoice_report(APIView):
    pagination_class = CustomPagination
    def get(self ,request):
        invoice_details = InvoiceDetails.objects.all()
        print('________________________')
        print(invoice_details)
        json_data = serialize('json', invoice_details)
        return JsonResponse(json_data, safe=False)

    def post(self, request):
        data = [{
             "fromdate" :l[0],
             "todate":l[1],
             "category":l[3],
             "center":l[4]
        } for l in data]
        return JsonResponse({"data":data},safe=False)

class invoice_report_summary(APIView):
    pagination_class = CustomPagination
    def post(self,request):
        data=[{
            "fromdate": l[0],
            "todate": l[1],
            "category": l[3],
            "center": l[4]


        }for l in data]
        return JsonResponse({"data":data},safe=False)



class sales_report(APIView):
    pagination_class = CustomPagination
    def post(self, request):
        data = [{
            "fromdate": l[0],
            "todate": l[1],
            "category": l[3],
            "center": l[4]
        } for l in data]
        return JsonResponse({"data": data}, safe=False)


class TAT_report(APIView):
    pagination_class = CustomPagination
    def post(self, request):
        data = [{
            "fromdate": l[0],
            "todate": l[1],
            "category": l[3],
            "center": l[4]
        } for l in data]
        return JsonResponse({"data": data}, safe=False)

class study_billing_report(APIView):
    pagination_class = CustomPagination
    def post(self, request):
        data = [{
            "fromdate": l[0],
            "todate": l[1],
            "category": l[3],
            "center": l[4]
        } for l in data]
        return JsonResponse({"data": data}, safe=False)












