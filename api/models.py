from django.db import models


# Create your models here.

class Student(models.Model):
    username=models.TextField(max_length=50, default="",null=False,unique=True)
    password=models.TextField(max_length=40,null=True,unique=False)
    encryptedpassword=models.TextField(max_length=500,null=True,blank=True)
    StudentName=models.CharField(max_length=50,default="",blank=True,null=True,unique=False)
    StudentNameHindi=models.CharField(max_length=50,default="",null=True,blank=True,unique=False)
    photo=models.ImageField(upload_to="api/images",default="",null=True,blank=True)
    DateOfBirth=models.DateField(null=True,blank=True,default="")
    Contact=models.TextField(default=0,null=True,blank=True)
    AlternateContact=models.TextField(default=0,null=True,blank=True)
    Branch=models.TextField(default='',null=True,blank=True)
    Programme=models.TextField(default='',null=True,blank=True)
    Category=models.TextField(default='',null=True,blank=True)
    SubCategory=models.TextField(default='',null=True,blank=True)
    SeatCategory=models.TextField(default='',null=True,blank=True)
    IdentificationMark=models.TextField(default='',null=True,blank=True)
    FeeWaiver=models.TextField(default='',null=True,blank=True)
    EntranceExam=models.TextField(default='',null=True,blank=True)
    Year=models.TextField(default='',null=True,blank=True)
    ApplicationNo=models.TextField(default='',null=True,blank=True)
    AIRRank=models.TextField(default='',null=True,blank=True)
    CategoryRank=models.TextField(default='',null=True,blank=True)
    Gender=models.TextField(default='',null=True,blank=True)
    UniversityRollNo=models.TextField(default=1,null=True,blank=True)
    EnrollmentNumber=models.CharField(max_length=20,default='',null=True,blank=True)
    AdmissionSource=models.CharField(max_length=15,default="JEE MAINS",null=True,blank=True)
    Nationality=models.CharField(max_length=10,default="",null=True,blank=True)
    Religion=models.CharField(max_length=10,default='',null=True,blank=True)
    Hostel=models.TextField(default='True',null=True,blank=True)
    ModeOfTransport=models.CharField(max_length=10,default='',null=True,blank=True)
    PersonalEmail=models.EmailField(default='',null=True,blank=True)
    HBTUEmail=models.EmailField(default='',null=True,blank=True)
    BloodGroup=models.CharField(max_length=10,default='',null=True,blank=True)
    AadhaarCard=models.TextField(default=1,null=True,blank=True)
    FatherName=models.CharField(max_length=50,default='',null=True,blank=True)
    MotherName=models.CharField(max_length=50,default='',null=True,blank=True)
    FatherContact=models.TextField(default=1,null=True,blank=True)
    Landline=models.TextField(null=True,default="",blank=True)
    ParentEmail=models.EmailField(default='',null=True,blank=True)
    CurrentSemester=models.TextField(default='',null=True,blank=True)
    CGPA=models.DecimalField(default=0.0,max_digits=7,decimal_places=4,null=True,blank=True)
    CurAddress=models.TextField(default="",blank=True,null=True)
    CurAddress1=models.TextField(default="",blank=True,null=True)
    CurAddress2=models.TextField(default="",blank=True,null=True)
    CurCity=models.TextField(default="",blank=True,null=True)
    CurZipCode=models.TextField(default="",blank=True,null=True)
    CurState=models.TextField(default="",blank=True,null=True)
    CurCountry=models.TextField(default="",blank=True,null=True)
    PerAddress=models.TextField(default="",blank=True,null=True)
    PerAddress1=models.TextField(default="",blank=True,null=True)
    PerAddress2=models.TextField(default="",blank=True,null=True)
    PerCity=models.TextField(default="",blank=True,null=True)
    PerZipCode=models.TextField(default="",blank=True,null=True)
    PerState=models.TextField(default="",blank=True,null=True)
    PerCountry=models.TextField(default="",blank=True,null=True)

    HighSchoolBoard=models.TextField(default="",blank=True,null=True)
    HighSchoolRollNo=models.TextField(default="",blank=True,null=True)
    HighSchoolYear=models.TextField(default="",blank=True,null=True)
    HighSchoolInstitution=models.TextField(default="",blank=True,null=True)
    HighSchoolDivision=models.TextField(default="",blank=True,null=True)
    HighSchoolSubjects=models.TextField(default="",blank=True,null=True)

    IntermediateBoard=models.TextField(default="",blank=True,null=True)
    IntermediateRollNo=models.TextField(default="",blank=True,null=True)
    IntermediateYear=models.TextField(default="",blank=True,null=True)
    IntermediateInstitution=models.TextField(default="",blank=True,null=True)
    IntermediateDivision=models.TextField(default="",blank=True,null=True)
    IntermediateSubjects=models.TextField(default="",blank=True,null=True)

    BtechBoard=models.TextField(default="",blank=True,null=True)
    BtechRollNo=models.TextField(default="",blank=True,null=True)
    BtechYear=models.TextField(default="",blank=True,null=True)
    BtechInstitution=models.TextField(default="",blank=True,null=True)
    BtechDivision=models.TextField(default="",blank=True,null=True)
    BtechSubjects=models.TextField(default="",blank=True,null=True)

    MtechBoard=models.TextField(default="",blank=True,null=True)
    MtechRollNo=models.TextField(default="",blank=True,null=True)
    MtechSubjects=models.TextField(default="",blank=True,null=True)
    MtechDivision=models.TextField(default="",blank=True,null=True)
    MtechYear=models.TextField(default="",blank=True,null=True)
    MtechInstitution=models.TextField(default="",blank=True,null=True)

    MCABoard=models.TextField(default="",blank=True,null=True)
    MCAInstitution=models.TextField(default="",blank=True,null=True)
    MCASubjects=models.TextField(default="",blank=True,null=True)
    MCARollNo=models.TextField(default="",blank=True,null=True)
    MCAYear=models.TextField(default="",blank=True,null=True)
    MCADivision=models.TextField(default="",blank=True,null=True)

    BCADivision=models.TextField(default="",blank=True,null=True)
    BCABoard=models.TextField(default="",blank=True,null=True)
    BCASubjects=models.TextField(default="",blank=True,null=True)
    BCARollNo=models.TextField(default="",blank=True,null=True)
    BCAYear=models.TextField(default="",blank=True,null=True)
    BCAInstitution=models.TextField(default="",blank=True,null=True)

    MSCInstitution=models.TextField(default="",blank=True,null=True)
    MSCBoard=models.TextField(default="",blank=True,null=True)
    MSCYear=models.TextField(default="",blank=True,null=True)
    MSCRollNo=models.TextField(default="",blank=True,null=True)
    MSCDivision=models.TextField(default="",blank=True,null=True)
    MSCSubjects=models.TextField(default="",blank=True,null=True)

    BSCSubjects=models.TextField(default="",blank=True,null=True)
    BSCBoard=models.TextField(default="",blank=True,null=True)
    BSCDivision=models.TextField(default="",blank=True,null=True)
    BSCYear=models.TextField(default="",blank=True,null=True)
    BSCRollNo=models.TextField(default="",blank=True,null=True)
    BSCInstitution=models.TextField(default="",blank=True,null=True)

    Member1Name=models.TextField(default="",blank=True,null=True)
    Member1Relationship=models.TextField(default="",blank=True,null=True)
    Member1Age=models.TextField(default="",blank=True,null=True)
    Member1Address=models.TextField(default="",blank=True,null=True)
    Member1EduQualification=models.TextField(default="",blank=True,null=True)
    Member1ProQualification=models.TextField(default="",blank=True,null=True)
    Member1Organization=models.TextField(default="",blank=True,null=True)
    Member1Occupation=models.TextField(default="",blank=True,null=True)
    Member1Income=models.TextField(default="",blank=True,null=True)
    Member1EarningStatus=models.TextField(default="",blank=True,null=True)

    Member2Name=models.TextField(default="",blank=True,null=True)
    Member2Relationship=models.TextField(default="",blank=True,null=True)
    Member2Age=models.TextField(default="",blank=True,null=True)
    Member2Address=models.TextField(default="",blank=True,null=True)
    Member2EduQualification=models.TextField(default="",blank=True,null=True)
    Member2ProQualification=models.TextField(default="",blank=True,null=True)
    Member2Organization=models.TextField(default="",blank=True,null=True)
    Member2Occupation=models.TextField(default="",blank=True,null=True)
    Member2Income=models.TextField(default="",blank=True,null=True)
    Member2EarningStatus=models.TextField(default="",blank=True,null=True)

    Member3Name=models.TextField(default="",blank=True,null=True)
    Member3Relationship=models.TextField(default="",blank=True,null=True)
    Member3Age=models.TextField(default="",blank=True,null=True)
    Member3Address=models.TextField(default="",blank=True,null=True)
    Member3EduQualification=models.TextField(default="",blank=True,null=True)
    Member3ProQualification=models.TextField(default="",blank=True,null=True)
    Member3Organization=models.TextField(default="",blank=True,null=True)
    Member3Occupation=models.TextField(default="",blank=True,null=True)
    Member3Income=models.TextField(default="",blank=True,null=True)
    Member3EarningStatus=models.TextField(default="",blank=True,null=True)

    Member4Name=models.TextField(default="",blank=True,null=True)
    Member4Relationship=models.TextField(default="",blank=True,null=True)
    Member4Age=models.TextField(default="",blank=True,null=True)
    Member4Address=models.TextField(default="",blank=True,null=True)
    Member4EduQualification=models.TextField(default="",blank=True,null=True)
    Member4ProQualification=models.TextField(default="",blank=True,null=True)
    Member4Organization=models.TextField(default="",blank=True,null=True)
    Member4Occupation=models.TextField(default="",blank=True,null=True)
    Member4Income=models.TextField(default="",blank=True,null=True)
    Member4EarningStatus=models.TextField(default="",blank=True,null=True)

    Member5Name=models.TextField(default="",blank=True,null=True)
    Member5Relationship=models.TextField(default="",blank=True,null=True)
    Member5Age=models.TextField(default="",blank=True,null=True)
    Member5Address=models.TextField(default="",blank=True,null=True)
    Member5EduQualification=models.TextField(default="",blank=True,null=True)
    Member5ProQualification=models.TextField(default="",blank=True,null=True)
    Member5Organization=models.TextField(default="",blank=True,null=True)
    Member5Occupation=models.TextField(default="",blank=True,null=True)
    Member5Income=models.TextField(default="",blank=True,null=True)
    Member5EarningStatus=models.TextField(default="",blank=True,null=True)

    PhyMarks=models.TextField(default="",blank=True,null=True)
    ChemMarks=models.TextField(default="",blank=True,null=True)
    MathMarks=models.TextField(default="",blank=True,null=True)
    Percentage=models.TextField(default="",blank=True,null=True)

    IsformSaved=models.TextField(blank=True,null=True,default="False")
    IsformSubmitted=models.TextField(blank=True,null=True,default="False")
    Image=models.TextField(blank=True,null=True,default="")



    def __str__(self):
        return self.username

class StoredSessions(models.Model):
    key = models.CharField(unique=True,max_length=50,null=False,default="")
    username = models.TextField(max_length=50, default="",null=False)
