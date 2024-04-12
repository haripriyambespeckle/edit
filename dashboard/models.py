{'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': 'radspeed', 'USER': 'root', 'PASSWORD': '', 'HOST': 'localhost', 'PORT': '3306'}}
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClusterInfo(models.Model):
    objects = None

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    clusterid = models.CharField(db_column='clusterId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(max_length=100, blank=True, null=True)
    institute = models.CharField(max_length=200, blank=True, null=True)
    categoryid = models.CharField(db_column='categoryId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(blank=True, null=True)
    modalityavailable = models.TextField(db_column='modalityAvailable', blank=True, null=True)  # Field name made lowercase.
    centerstatus = models.CharField(db_column='centerStatus', max_length=20)  # Field name made lowercase.
    commencement_date = models.DateField(blank=True, null=True)
    district_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cluster_info'


class CollectedAmount(models.Model):
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    monthyear = models.CharField(db_column='monthYear', max_length=64, blank=True, null=True)  # Field name made lowercase.
    collectedamount = models.FloatField(db_column='collectedAmount', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='modifiedBy', max_length=64, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'collected_amount'


class Corruptedmessages(models.Model):
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(blank=True, null=True)
    eventtype = models.CharField(db_column='eventType', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corruptedmessages'


class DashboardGroupResult(models.Model):
    patientcount = models.BigIntegerField(db_column='patientCount', blank=True, null=True)  # Field name made lowercase.
    ctscan = models.BigIntegerField(db_column='ctScan', blank=True, null=True)  # Field name made lowercase.
    otherscan = models.BigIntegerField(db_column='otherScan', blank=True, null=True)  # Field name made lowercase.
    reportedstudy = models.BigIntegerField(db_column='reportedStudy', blank=True, null=True)  # Field name made lowercase.
    reportedctstudy = models.BigIntegerField(db_column='reportedCTStudy', blank=True, null=True)  # Field name made lowercase.
    reportedotherstudy = models.BigIntegerField(db_column='reportedOtherStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedstudy = models.BigIntegerField(db_column='unReportedStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedctstudy = models.BigIntegerField(db_column='unReportedCTStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedotherstudy = models.BigIntegerField(db_column='unReportedOtherStudy', blank=True, null=True)  # Field name made lowercase.
    emergencycase = models.BigIntegerField(db_column='emergencyCase', blank=True, null=True)  # Field name made lowercase.
    emergencycasereported = models.BigIntegerField(db_column='emergencyCaseReported', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    totalscans = models.BigIntegerField(db_column='totalScans', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=64, blank=True, null=True)
    allcenterstatmetpercentage = models.FloatField(db_column='allCentersTATMetPercentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_group_result'


class DashboardResult(models.Model):

    patientcount = models.BigIntegerField(db_column='patientCount', blank=True, null=True)  # Field name made lowercase.
    ctscan = models.BigIntegerField(db_column='ctScan', blank=True, null=True)  # Field name made lowercase.
    otherscan = models.BigIntegerField(db_column='otherScan', blank=True, null=True)  # Field name made lowercase.
    reportedstudy = models.BigIntegerField(db_column='reportedStudy', blank=True, null=True)  # Field name made lowercase.
    reportedctstudy = models.BigIntegerField(db_column='reportedCTStudy', blank=True, null=True)  # Field name made lowercase.
    reportedotherstudy = models.BigIntegerField(db_column='reportedOtherStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedstudy = models.BigIntegerField(db_column='unReportedStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedctstudy = models.BigIntegerField(db_column='unReportedCTStudy', blank=True, null=True)  # Field name made lowercase.
    unreportedotherstudy = models.BigIntegerField(db_column='unReportedOtherStudy', blank=True, null=True)  # Field name made lowercase.
    emergencycase = models.BigIntegerField(db_column='emergencyCase', blank=True, null=True)  # Field name made lowercase.
    emergencycasereported = models.BigIntegerField(db_column='emergencyCaseReported', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    totalscans = models.BigIntegerField(db_column='totalScans', blank=True, null=True)  # Field name made lowercase.
    institute = models.CharField(max_length=100)
    category = models.CharField(max_length=64, blank=True, null=True)
    ordercount = models.BigIntegerField(db_column='orderCount', blank=True, null=True)  # Field name made lowercase.
    patientscandonecount = models.BigIntegerField(db_column='patientScanDoneCount')  # Field name made lowercase.
    tatmetpercentage = models.FloatField(db_column='tatMetPercentage', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dashboard_result'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DoctorsDetails(models.Model):
    placeofposting = models.CharField(db_column='placeOfPosting', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    medicalcouncilno = models.CharField(db_column='medicalCouncilNo', max_length=64, blank=True, null=True)  # Field name made lowercase.
    highestqualification = models.CharField(db_column='highestQualification', max_length=64, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(max_length=64, blank=True, null=True)
    dateofjoining = models.DateField(db_column='dateOfJoining', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doctors_details'


class EquipmentDetails(models.Model):
    centername = models.CharField(db_column='centerName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dateofoperational = models.DateField(db_column='dateOfOperational', blank=True, null=True)  # Field name made lowercase.
    servicesprovided = models.CharField(db_column='servicesProvided', max_length=64, blank=True, null=True)  # Field name made lowercase.
    nameofthemodel = models.CharField(db_column='nameOfTheModel', max_length=64, blank=True, null=True)  # Field name made lowercase.
    operationalstatus = models.CharField(db_column='operationalStatus', max_length=20)  # Field name made lowercase.
    reasonforinactive = models.CharField(db_column='reasonForInactive', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipment_details'


class GroupStudyCount(models.Model):
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    todaystudycount = models.BigIntegerField(db_column='todayStudyCount', blank=True, null=True)  # Field name made lowercase.
    highestdistrict = models.CharField(db_column='highestDistrict', max_length=20)  # Field name made lowercase.
    lowestdistrict = models.IntegerField(db_column='lowestDistrict', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_study_count'


class InventoryStockConsumption(models.Model):
    dbid = models.IntegerField(db_column='dBId')  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    institutename = models.CharField(db_column='instituteName', max_length=100)  # Field name made lowercase.
    usagetype = models.CharField(db_column='usageType', max_length=64)  # Field name made lowercase.
    entityname = models.CharField(db_column='entityName', max_length=64)  # Field name made lowercase.
    batchid = models.CharField(db_column='batchId', max_length=64)  # Field name made lowercase.
    unitprice = models.CharField(db_column='unitPrice', max_length=10)  # Field name made lowercase.
    cost = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    pilferage = models.CharField(max_length=10)
    stockflow = models.CharField(db_column='stockFlow', max_length=10)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=64)  # Field name made lowercase.
    userrole = models.CharField(db_column='userRole', max_length=64)  # Field name made lowercase.
    patientid = models.CharField(db_column='patientId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    entrytime = models.DateTimeField(db_column='entryTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory_stock_consumption'


class InventoryStockDetails(models.Model):
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    institutename = models.CharField(db_column='instituteName', max_length=100)  # Field name made lowercase.
    usagetype = models.CharField(db_column='usageType', max_length=64)  # Field name made lowercase.
    entityname = models.CharField(db_column='entityName', max_length=64)  # Field name made lowercase.
    batchid = models.CharField(db_column='batchId', max_length=64)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='unitPrice')  # Field name made lowercase.
    qtyonhand = models.IntegerField(db_column='qtyOnHand')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory_stock_details'


class InvoiceDetails(models.Model):
    documentname = models.CharField(db_column='documentName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    centername = models.CharField(db_column='centerName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_details'


class ManpowerDetails(models.Model):
    placeofposting = models.CharField(db_column='placeOfPosting', max_length=64, blank=True, null=True)  # Field name made lowercase.
    employeecode = models.CharField(db_column='employeeCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    designation = models.CharField(max_length=64, blank=True, null=True)
    department = models.CharField(max_length=64, blank=True, null=True)
    dateofjoining = models.DateField(db_column='dateOfJoining', blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manpower_details'


class ModalityTat(models.Model):
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(max_length=64, blank=True, null=True)
    maxtattime = models.TimeField(db_column='maxTATTime', blank=True, null=True)  # Field name made lowercase.
    mintattime = models.TimeField(db_column='minTATTime', blank=True, null=True)  # Field name made lowercase.
    emgmaxtattime = models.TimeField(db_column='emgMaxTATTime', blank=True, null=True)  # Field name made lowercase.
    emgmintattime = models.TimeField(db_column='emgMinTATTime', blank=True, null=True)  # Field name made lowercase.
    asapmaxtattime = models.TimeField(db_column='asapMaxTATTime', blank=True, null=True)  # Field name made lowercase.
    asapmintattime = models.TimeField(db_column='asapMinTATTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modality_tat'


class PieData(models.Model):
    studycount = models.BigIntegerField(db_column='studyCount', blank=True, null=True)  # Field name made lowercase.
    todaystudycount = models.BigIntegerField(db_column='todayStudyCount', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    institute = models.CharField(max_length=100)
    category = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pie_data'


class RatelistDetails(models.Model):
    modality = models.CharField(max_length=64, blank=True, null=True)
    testname = models.TextField(db_column='testName', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratelist_details'


class RisData(models.Model):
    dbid = models.IntegerField(db_column='dBId')  # Field name made lowercase.
    patientid = models.CharField(db_column='patientId', max_length=64)  # Field name made lowercase.
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=8)
    studyinstanceuid = models.CharField(db_column='studyInstanceUID', max_length=70)  # Field name made lowercase.
    studydate = models.DateField(db_column='studyDate', blank=True, null=True)  # Field name made lowercase.
    reportstatus = models.CharField(db_column='reportStatus', max_length=4)  # Field name made lowercase.
    isemergencycase = models.CharField(db_column='isEmergencyCase', max_length=4)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    modality = models.CharField(max_length=64, blank=True, null=True)
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    accessionno = models.CharField(db_column='accessionNo', max_length=20)  # Field name made lowercase.
    his_status = models.CharField(db_column='HIS_Status', max_length=35)  # Field name made lowercase.
    studytime = models.TimeField(db_column='studyTime', blank=True, null=True)  # Field name made lowercase.
    billingprocedure = models.CharField(db_column='billingProcedure', max_length=64, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    institute = models.CharField(max_length=100)
    reportdispatchtime = models.CharField(db_column='reportDispatchTime', max_length=30)  # Field name made lowercase.
    tat = models.CharField(max_length=30)
    trfno = models.CharField(db_column='trfNo', max_length=30)  # Field name made lowercase.
    penaltyprice = models.FloatField(db_column='penaltyPrice', blank=True, null=True)  # Field name made lowercase.
    claimedamount = models.FloatField(db_column='claimedAmount')  # Field name made lowercase.
    delaytime = models.CharField(db_column='delayTime', max_length=30)  # Field name made lowercase.
    description = models.CharField(max_length=100)
    examinationprice = models.FloatField(db_column='examinationPrice')  # Field name made lowercase.
    ordercreationdatetime = models.DateTimeField(db_column='orderCreationDateTime', blank=True, null=True)  # Field name made lowercase.
    firstandlastimagetimediff = models.CharField(db_column='firstAndLastImageTimeDiff', max_length=64, blank=True, null=True)  # Field name made lowercase.
    isdifferencegreater = models.CharField(db_column='isDifferenceGreater', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dicomlogin = models.CharField(db_column='dicomLogin', max_length=64, blank=True, null=True)  # Field name made lowercase.
    dicompswd = models.CharField(db_column='dicomPswd', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rvucost = models.IntegerField(db_column='RVUCost', blank=True, null=True)  # Field name made lowercase.
    physicianid = models.CharField(db_column='physicianId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    radiologist = models.CharField(max_length=255, blank=True, null=True)
    recordverified = models.IntegerField(db_column='recordVerified', blank=True, null=True)  # Field name made lowercase.
    patientcategory = models.CharField(db_column='patientCategory', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patienttype = models.CharField(db_column='patientType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    refphysician = models.CharField(db_column='refPhysician', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patientwaitingtat = models.CharField(db_column='patientWaitingTAT', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patientidprooftype = models.CharField(db_column='patientIdProofType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patientidproofno = models.CharField(db_column='patientIdProofNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_data'


class RisDirectorsReport(models.Model):
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    orderdbid = models.BigIntegerField(db_column='orderdBId', blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(max_length=64, blank=True, null=True)
    ordercreationdatetime = models.DateTimeField(db_column='orderCreationDateTime', blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.TextField(blank=True, null=True)
    patientname = models.CharField(db_column='patientName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='patientId', max_length=64)  # Field name made lowercase.
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=8)
    totalitemcost = models.FloatField(db_column='totalItemCost', blank=True, null=True)  # Field name made lowercase.
    totaldiscount = models.FloatField(db_column='totalDiscount', blank=True, null=True)  # Field name made lowercase.
    totalroundoffamount = models.FloatField(db_column='totalRoundOffAmount', blank=True, null=True)  # Field name made lowercase.
    netpaid = models.FloatField(db_column='netPaid', blank=True, null=True)  # Field name made lowercase.
    balanceamount = models.FloatField(db_column='balanceAmount', blank=True, null=True)  # Field name made lowercase.
    invoicedbid = models.BigIntegerField(db_column='invoicedBId', blank=True, null=True)  # Field name made lowercase.
    categorydiscount = models.FloatField(db_column='categoryDiscount', blank=True, null=True)  # Field name made lowercase.
    additionaldiscount = models.FloatField(db_column='additionalDiscount', blank=True, null=True)  # Field name made lowercase.
    totalconsumablecost = models.FloatField(db_column='totalConsumableCost', blank=True, null=True)  # Field name made lowercase.
    additionaldiscountper = models.FloatField(db_column='additionalDiscountPer', blank=True, null=True)  # Field name made lowercase.
    patientcategory = models.CharField(db_column='patientCategory', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patienttype = models.CharField(db_column='patientType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    refphysician = models.CharField(db_column='refPhysician', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_directors_report'


class RisDirectorsSummary(models.Model):
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(max_length=64, blank=True, null=True)
    noofpatients = models.IntegerField(db_column='noOfPatients', blank=True, null=True)  # Field name made lowercase.
    expectedrevenue = models.FloatField(db_column='expectedRevenue', blank=True, null=True)  # Field name made lowercase.
    revenuegenerated = models.FloatField(db_column='revenueGenerated', blank=True, null=True)  # Field name made lowercase.
    billtohospital = models.FloatField(db_column='billToHospital', blank=True, null=True)  # Field name made lowercase.
    discount = models.FloatField(blank=True, null=True)
    pendingamount = models.FloatField(db_column='pendingAmount', blank=True, null=True)  # Field name made lowercase.
    nooforders = models.IntegerField(db_column='noOfOrders', blank=True, null=True)  # Field name made lowercase.
    aplnoofpatients = models.IntegerField(db_column='aplNoOfPatients', blank=True, null=True)  # Field name made lowercase.
    aplcashamount = models.FloatField(db_column='aplCashAmount', blank=True, null=True)  # Field name made lowercase.
    bplnoofpatients = models.IntegerField(db_column='bplNoOfPatients', blank=True, null=True)  # Field name made lowercase.
    bplbilltohospital = models.FloatField(db_column='bplBillToHospital', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.FloatField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_directors_summary'


class RisFoundation(models.Model):
    dbid = models.IntegerField(db_column='dBId', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    foundationname = models.CharField(db_column='foundationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ris_foundation'


class RisOrder(models.Model):
    dbid = models.IntegerField(db_column='dBId')  # Field name made lowercase.
    trfnumber = models.CharField(db_column='TRFNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    patient_dbid = models.IntegerField(db_column='patient_dbId', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    ordernumber = models.CharField(db_column='orderNumber', max_length=50)  # Field name made lowercase.
    creationdatetime = models.DateTimeField(db_column='creationDateTime', blank=True, null=True)  # Field name made lowercase.
    directorsreportcomputed = models.IntegerField(db_column='directorsReportComputed', blank=True, null=True)  # Field name made lowercase.
    patientcategory = models.CharField(db_column='patientCategory', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_order'


class RisOrderAdditionalDetails(models.Model):
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    additionaldiscount = models.FloatField(db_column='additionalDiscount', blank=True, null=True)  # Field name made lowercase.
    additionaldiscountper = models.FloatField(db_column='additionalDiscountPer', blank=True, null=True)  # Field name made lowercase.
    patientcategorydiscount = models.FloatField(db_column='patientCategoryDiscount', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.FloatField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_order_additional_details'


class RisOrderInvoice(models.Model):
    dbid = models.BigIntegerField(db_column='dBId', blank=True, null=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.FloatField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.
    totalamountreceived = models.FloatField(db_column='totalAmountReceived', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    additionaldiscount = models.FloatField(db_column='additionalDiscount', blank=True, null=True)  # Field name made lowercase.
    finalamount = models.FloatField(db_column='finalAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_order_invoice'


class RisOrderInvoiceItems(models.Model):
    dbid = models.BigIntegerField(db_column='dBId', blank=True, null=True)  # Field name made lowercase.
    orderinvoiceid = models.BigIntegerField(db_column='orderInvoiceId', blank=True, null=True)  # Field name made lowercase.
    itemcost = models.FloatField(db_column='itemCost', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)
    itemtype = models.CharField(db_column='itemType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    itemcode = models.CharField(db_column='itemCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orderitemdbid = models.IntegerField(db_column='orderItemDbId', blank=True, null=True)  # Field name made lowercase.
    hospitalbillingcodediscount = models.FloatField(db_column='hospitalBillingCodeDiscount', blank=True, null=True)  # Field name made lowercase.
    premium = models.FloatField(blank=True, null=True)
    messageentrytime = models.DateTimeField(db_column='messageEntryTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_order_invoice_items'


class RisOrderItems(models.Model):
    accessionno = models.CharField(db_column='accessionNo', max_length=50)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderId', blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(db_column='itemCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    itemcost = models.IntegerField(db_column='itemCost', blank=True, null=True)  # Field name made lowercase.
    itemdesc = models.CharField(db_column='itemDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    premium = models.FloatField(blank=True, null=True)
    hospitalbillingcodediscount = models.FloatField(db_column='hospitalBillingCodeDiscount', blank=True, null=True)  # Field name made lowercase.
    modality = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    modalityalias = models.CharField(db_column='modalityAlias', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dbid = models.IntegerField(db_column='dBId', blank=True, null=True)  # Field name made lowercase.
    addedconsumablecost = models.IntegerField(db_column='addedConsumableCost', blank=True, null=True)  # Field name made lowercase.
    refphysician = models.CharField(db_column='refPhysician', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_order_items'


class RisPatient(models.Model):
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dbid = models.BigIntegerField(db_column='dBId', blank=True, null=True)  # Field name made lowercase.
    patientfirstname = models.CharField(db_column='patientFirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    patientsearchablename = models.CharField(db_column='patientSearchableName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=25, blank=True, null=True)
    sex = models.CharField(max_length=8, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    patientcategory = models.CharField(db_column='patientCategory', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patienttype = models.CharField(db_column='patientType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.CharField(db_column='hospitalId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patientidprooftype = models.CharField(db_column='patientIdProofType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    patientidproofno = models.CharField(db_column='patientIdProofNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobileno = models.CharField(db_column='mobileNo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_patient'


class RisPaymentDetails(models.Model):
    centerid = models.IntegerField(db_column='centerId', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6, blank=True, null=True)  # Field name made lowercase.
    orderinvoicedbid = models.IntegerField(db_column='orderInvoicedBId', blank=True, null=True)  # Field name made lowercase.
    amountrcv = models.FloatField(db_column='amountRcv', blank=True, null=True)  # Field name made lowercase.
    paymentdatetime = models.DateTimeField(db_column='paymentDateTime', blank=True, null=True)  # Field name made lowercase.
    paymentmode = models.CharField(db_column='paymentMode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='paymentType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dbid = models.CharField(db_column='dBId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    foundationid = models.IntegerField(db_column='foundationId', blank=True, null=True)  # Field name made lowercase.
    orderiteminvoiceid = models.IntegerField(db_column='orderItemInvoiceId', blank=True, null=True)  # Field name made lowercase.
    dirpaymentprocessed = models.IntegerField(db_column='dirPaymentProcessed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ris_payment_details'


class RisReport(models.Model):
    reportid = models.IntegerField(db_column='reportId')  # Field name made lowercase.
    patientdbid = models.IntegerField(db_column='patientdbId')  # Field name made lowercase.
    studyinstanceuid = models.CharField(db_column='studyInstanceUID', max_length=70)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    accessionno = models.CharField(db_column='accessionNo', max_length=30)  # Field name made lowercase.
    studydate = models.DateField(db_column='studyDate', blank=True, null=True)  # Field name made lowercase.
    studytime = models.TimeField(db_column='studyTime', blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='lastUpdateTime', blank=True, null=True)  # Field name made lowercase.
    reportdate = models.DateField(db_column='reportDate')  # Field name made lowercase.
    reporttime = models.TimeField(db_column='reportTime', blank=True, null=True)  # Field name made lowercase.
    reportstatus = models.IntegerField(db_column='reportStatus')  # Field name made lowercase.
    emergencycase = models.CharField(db_column='emergencyCase', max_length=4)  # Field name made lowercase.
    delayedreport = models.BigIntegerField(db_column='delayedReport', blank=True, null=True)  # Field name made lowercase.
    rvucost = models.IntegerField(db_column='RVUCost', blank=True, null=True)  # Field name made lowercase.
    physicianid = models.CharField(db_column='physicianId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    radiologist = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ris_report'


class SiteConfig(models.Model):
    sitename = models.CharField(db_column='siteName', max_length=64)  # Field name made lowercase.
    coloraccent = models.CharField(db_column='colorAccent', max_length=64, blank=True, null=True)  # Field name made lowercase.
    invoicereport = models.IntegerField(db_column='invoiceReport', blank=True, null=True)  # Field name made lowercase.
    directorsreport = models.IntegerField(db_column='directorsReport', blank=True, null=True)  # Field name made lowercase.
    summaryinvoicereport = models.IntegerField(db_column='summaryInvoiceReport', blank=True, null=True)  # Field name made lowercase.
    salesreport = models.IntegerField(db_column='salesReport', blank=True, null=True)  # Field name made lowercase.
    tatreport = models.IntegerField(db_column='tatReport', blank=True, null=True)  # Field name made lowercase.
    studybillingreport = models.IntegerField(db_column='studyBillingReport', blank=True, null=True)  # Field name made lowercase.
    radiologistreport = models.IntegerField(db_column='radiologistReport', blank=True, null=True)  # Field name made lowercase.
    centerreport = models.IntegerField(db_column='centerReport', blank=True, null=True)  # Field name made lowercase.
    physicianreport = models.IntegerField(db_column='physicianReport', blank=True, null=True)  # Field name made lowercase.
    inventoryreport = models.IntegerField(db_column='inventoryReport', blank=True, null=True)  # Field name made lowercase.
    modalitywisesalereport = models.IntegerField(db_column='modalityWiseSaleReport', blank=True, null=True)  # Field name made lowercase.
    negativetimereport = models.IntegerField(db_column='negativeTimeReport', blank=True, null=True)  # Field name made lowercase.
    homepageloginrequired = models.IntegerField(db_column='homePageLoginRequired', blank=True, null=True)  # Field name made lowercase.
    summarypageloginrequired = models.IntegerField(db_column='summaryPageLoginRequired', blank=True, null=True)  # Field name made lowercase.
    facilitystatuspage = models.IntegerField(db_column='facilityStatusPage', blank=True, null=True)  # Field name made lowercase.
    restrictiononcenters = models.IntegerField(db_column='restrictionOnCenters', blank=True, null=True)  # Field name made lowercase.
    detailedandscanned = models.IntegerField(db_column='detailedAndScanned', blank=True, null=True)  # Field name made lowercase.
    govdataverification = models.IntegerField(db_column='govDataVerification', blank=True, null=True)  # Field name made lowercase.
    summarypagemodalityfilter = models.IntegerField(db_column='summaryPageModalityFilter', blank=True, null=True)  # Field name made lowercase.
    combineddirectorsreport = models.IntegerField(db_column='combinedDirectorsReport', blank=True, null=True)  # Field name made lowercase.
    logo1 = models.IntegerField(blank=True, null=True)
    logo2 = models.IntegerField(blank=True, null=True)
    logo3 = models.IntegerField(blank=True, null=True)
    logo4 = models.IntegerField(blank=True, null=True)
    backgroundimg = models.IntegerField(db_column='backgroundImg', blank=True, null=True)  # Field name made lowercase.
    hllcustomhomepage = models.IntegerField(db_column='hllCustomHomePage', blank=True, null=True)  # Field name made lowercase.
    tatdetailsreport = models.IntegerField(db_column='tatDetailsReport', blank=True, null=True)  # Field name made lowercase.
    paymenttransactionreport = models.IntegerField(db_column='paymentTransactionReport', blank=True, null=True)  # Field name made lowercase.
    healthmapgovtusersfeature = models.IntegerField(db_column='healthMapGovtUsersFeature', blank=True, null=True)  # Field name made lowercase.
    healthmapadditionalpagefeature = models.IntegerField(db_column='healthMapAdditionalPageFeature', blank=True, null=True)  # Field name made lowercase.
    hllcollectedamountentryfeature = models.IntegerField(db_column='hllCollectedAmountEntryFeature', blank=True, null=True)  # Field name made lowercase.
    salesreportorderbased = models.IntegerField(db_column='salesReportOrderBased', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_config'


class SummaryCenterResult(models.Model):
    mondaypatientcount = models.BigIntegerField(db_column='mondaypatientCount', blank=True, null=True)  # Field name made lowercase.
    mondayreportedstudy = models.BigIntegerField(db_column='mondayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    mondayunreportedstudy = models.BigIntegerField(db_column='mondayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    tuedaypatientcount = models.BigIntegerField(db_column='tuedaypatientCount', blank=True, null=True)  # Field name made lowercase.
    tuedayreportedstudy = models.BigIntegerField(db_column='tuedayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    tuedayunreportedstudy = models.BigIntegerField(db_column='tuedayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    wednesdaypatientcount = models.BigIntegerField(db_column='wednesdaypatientCount', blank=True, null=True)  # Field name made lowercase.
    wednesdayreportedstudy = models.BigIntegerField(db_column='wednesdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    wednesdayunreportedstudy = models.BigIntegerField(db_column='wednesdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    thursdaypatientcount = models.BigIntegerField(db_column='thursdaypatientCount', blank=True, null=True)  # Field name made lowercase.
    thursdayreportedstudy = models.BigIntegerField(db_column='thursdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    thursdayunreportedstudy = models.BigIntegerField(db_column='thursdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    fridaypatientcount = models.BigIntegerField(db_column='fridaypatientCount', blank=True, null=True)  # Field name made lowercase.
    fridayreportedstudy = models.BigIntegerField(db_column='fridayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    fridayunreportedstudy = models.BigIntegerField(db_column='fridayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    saturdaydaypatientcount = models.BigIntegerField(db_column='saturdaydaypatientCount', blank=True, null=True)  # Field name made lowercase.
    saturdayreportedstudy = models.BigIntegerField(db_column='saturdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    saturdayunreportedstudy = models.BigIntegerField(db_column='saturdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    sundaypatientcount = models.BigIntegerField(db_column='sundaypatientCount', blank=True, null=True)  # Field name made lowercase.
    sundayreportedstudy = models.BigIntegerField(db_column='sundayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    sundayunreportedstudy = models.BigIntegerField(db_column='sundayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    centerid = models.IntegerField(db_column='centerId')  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'summary_center_result'


class SummaryGroupResult(models.Model):
    mondaypatientcount = models.BigIntegerField(db_column='mondaypatientCount', blank=True, null=True)  # Field name made lowercase.
    mondayreportedstudy = models.BigIntegerField(db_column='mondayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    mondayunreportedstudy = models.BigIntegerField(db_column='mondayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    tuedaypatientcount = models.BigIntegerField(db_column='tuedaypatientCount', blank=True, null=True)  # Field name made lowercase.
    tuedayreportedstudy = models.BigIntegerField(db_column='tuedayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    tuedayunreportedstudy = models.BigIntegerField(db_column='tuedayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    wednesdaypatientcount = models.BigIntegerField(db_column='wednesdaypatientCount', blank=True, null=True)  # Field name made lowercase.
    wednesdayreportedstudy = models.BigIntegerField(db_column='wednesdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    wednesdayunreportedstudy = models.BigIntegerField(db_column='wednesdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    thursdaypatientcount = models.BigIntegerField(db_column='thursdaypatientCount', blank=True, null=True)  # Field name made lowercase.
    thursdayreportedstudy = models.BigIntegerField(db_column='thursdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    thursdayunreportedstudy = models.BigIntegerField(db_column='thursdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    fridaypatientcount = models.BigIntegerField(db_column='fridaypatientCount', blank=True, null=True)  # Field name made lowercase.
    fridayreportedstudy = models.BigIntegerField(db_column='fridayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    fridayunreportedstudy = models.BigIntegerField(db_column='fridayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    saturdaydaypatientcount = models.BigIntegerField(db_column='saturdaydaypatientCount', blank=True, null=True)  # Field name made lowercase.
    saturdayreportedstudy = models.BigIntegerField(db_column='saturdayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    saturdayunreportedstudy = models.BigIntegerField(db_column='saturdayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    sundaypatientcount = models.BigIntegerField(db_column='sundaypatientCount', blank=True, null=True)  # Field name made lowercase.
    sundayreportedstudy = models.BigIntegerField(db_column='sundayreportedStudy', blank=True, null=True)  # Field name made lowercase.
    sundayunreportedstudy = models.BigIntegerField(db_column='sundayunReportedStudy', blank=True, null=True)  # Field name made lowercase.
    groupid = models.CharField(db_column='groupId', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'summary_group_result'
