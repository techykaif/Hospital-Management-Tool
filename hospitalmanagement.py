from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x830+100+0")

        self.NameofTablet=StringVar()
        self.RefNO=StringVar()
        self.NoofDoses=StringVar()
        self.NumberOfTablets=StringVar()
        self.IssueDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurInfo=StringVar()
        self.BP=StringVar()
        self.Storage=StringVar()
        self.PName=StringVar()
        self.PID=StringVar()
        self.DOb=StringVar()
        self.Address=StringVar()
        self.record_id=None

        ##Here goes the Heading
        lbtitle=Label(self.root,bd=10,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)

        #here goes the Dataframe
        Dataframe=Frame(self.root,bd=10,padx=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1240,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=5,padx=20,relief=GROOVE,font=("times new roman",18,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=790,height=350)

        #Datframe Left Components
        ##First Column of Left Side Dataframe
        lblNameTablet=Label(DataframeLeft,text="Name of The Tablet : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lblNameTablet.grid(row=0,column=0)
        comNameTablet=ttk.Combobox(DataframeLeft,state="readonly",textvariable=self.NameofTablet,font=("arial",13,"bold"),width=24)
        comNameTablet["values"]=("Nice","Corona Vaccine","Paracetamol","Aderall","Amidopine","Aspirin")
        comNameTablet.grid(row=0,column=1)

        lbRefrenceNumber=Label(DataframeLeft,text="Reference No : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbRefrenceNumber.grid(row=1,column=0,sticky=W)
        txtReferenceNumber=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.RefNO)
        txtReferenceNumber.grid(row=1,column=1)

        lbDoses=Label(DataframeLeft,text="No. of Doses : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbDoses.grid(row=2,column=0,sticky=W)
        txtDoses=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.NoofDoses)
        txtDoses.grid(row=2,column=1)
        
        lbNoTablets=Label(DataframeLeft,text="Number of Tablets : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbNoTablets.grid(row=3,column=0,sticky=W)
        txtNoTablets=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.NumberOfTablets)
        txtNoTablets.grid(row=3,column=1)

        lbIssueDate=Label(DataframeLeft,text="Issue Date : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbIssueDate.grid(row=4,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.IssueDate)
        txtIssueDate.grid(row=4,column=1)

        lbDailyDose=Label(DataframeLeft,text="Daily Dose : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbDailyDose.grid(row=5,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.DailyDose)
        txtDailyDose.grid(row=5,column=1)

        lbSideEffect=Label(DataframeLeft,text="Side Effect : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbSideEffect.grid(row=6,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.SideEffect)
        txtSideEffect.grid(row=6,column=1)


        ##Second Column of Left Side Dataframe
        lbFurInfo=Label(DataframeLeft,text="Further Information : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbFurInfo.grid(row=0,column=3,sticky=W)
        txtFurInfo=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.FurInfo)
        txtFurInfo.grid(row=0,column=4)

        lbBloodPres=Label(DataframeLeft,text="Blood Pressure : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbBloodPres.grid(row=1,column=3,sticky=W)
        txtBloodPres=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.BP)
        txtBloodPres.grid(row=1,column=4)

        lbStorage=Label(DataframeLeft,text="Storage Advice : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbStorage.grid(row=2,column=3,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.Storage)
        txtStorage.grid(row=2,column=4)

        lbPName=Label(DataframeLeft,text="Patient Name : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbPName.grid(row=3,column=3,sticky=W)
        txtPname=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.PName)
        txtPname.grid(row=3,column=4)

        lbPID=Label(DataframeLeft,text="Patient ID : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbPID.grid(row=4,column=3,sticky=W)
        txtPID=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.PID)
        txtPID.grid(row=4,column=4)

        lbPDOB=Label(DataframeLeft,text="Date of Birth : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbPDOB.grid(row=5,column=3,sticky=W)
        txtPDOB=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.DOb)
        txtPDOB.grid(row=5,column=4)

        lbAddress=Label(DataframeLeft,text="Address : ",font=("times new roman",16,"bold"),padx=2,pady=10)
        lbAddress.grid(row=6,column=3,sticky=W)
        txtAddress=Entry(DataframeLeft,font=("arial",13,"bold"),width=25,textvariable=self.Address)
        txtAddress.grid(row=6,column=4)

        #Dataframe Right begins here    
        DataframeRight=LabelFrame(Dataframe,bd=5,padx=20,relief=GROOVE,font=("times new roman",18,"bold"),text="Prescription")
        DataframeRight.place(x=800,y=5,width=370,height=350)

        #dataframe right Content
        self.txtPresciptionText=Text(DataframeRight,font=("arial",14,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtPresciptionText.grid(row=0,column=0)

        #here goes the button frame

        ButtonFrame=Frame(self.root,padx=20,relief=GROOVE)
        ButtonFrame.place(x=20,y=540,width=1190,height=70)

        btnPrescription=Button(ButtonFrame,fg="green",text="Prescription",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.show_data)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(ButtonFrame,fg="green",text="Submit",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.iPrescription)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(ButtonFrame,fg="green",text="Update",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.update_data)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(ButtonFrame,fg="green",text="Delete",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.delete_data)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(ButtonFrame,fg="green",text="Clear",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.clear_application)
        btnClear.grid(row=0,column=4)

        btnExit=Button(ButtonFrame,fg="green",text="Exit",font=("arial",16,"bold"),padx=2,pady=10,width=17,command=self.exit_application)
        btnExit.grid(row=0,column=5)



        #here goes the Detail Frame

        DetailFrame=Frame(self.root,bd=10,padx=20,relief=RIDGE)
        DetailFrame.place(x=0,y=620,width=1240,height=190)

        ##Scrollbar

        scroll_x=ttk.Scrollbar(DetailFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailFrame,columns=("nameoftablet","ref","doses","nooftablets","issuedate","dailydose","sideeffect","furinfo","bp","storage","pname","pid","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("doses",text="Doses")
        self.hospital_table.heading("nooftablets",text="Number of Tablets")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("furinfo",text="Further Info")
        self.hospital_table.heading("bp",text="Blood Pressure")
        self.hospital_table.heading("storage",text="Storage Advice")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("pid",text="Patient ID")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        ##functionalities Declaration


    def iPrescription(self):
        if self.NameofTablet.get() == "" or self.RefNO.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="MyData")#Be Sure to Change it According to your System Settings
                my_cursor = conn.cursor()
                sql_query = "INSERT INTO Hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

                values = (
                    self.NameofTablet.get(),
                    self.RefNO.get(),
                    self.NoofDoses.get(),
                    self.NumberOfTablets.get(),
                    self.IssueDate.get(),
                    self.DailyDose.get(),
                    self.SideEffect.get(),
                    self.FurInfo.get(),
                    self.BP.get(),
                    self.Storage.get(),
                    self.PName.get(),
                    self.PID.get(),
                    self.DOb.get(),
                    self.Address.get(),
                    None
        
                )

                my_cursor.execute(sql_query, values)
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Data inserted successfully!")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")

            finally:
                my_cursor.close()
                conn.close()
    def exit_application(self):
        messagebox.showwarning("Confirmation","Bye Bye")
        root.destroy()
    def clear_application(self):
        self.NameofTablet.set(""),
        self.RefNO.set(""),
        self.NoofDoses.set(""),
        self.NumberOfTablets.set(""),
        self.IssueDate.set(""),
        self.DailyDose.set(""),
        self.SideEffect.set(""),
        self.FurInfo.set(""),
        self.BP.set(""),
        self.Storage.set(""),
        self.PName.set(""),
        self.PID.set(""),
        self.DOb.set(""),
        self.Address.set("")
        self.txtPresciptionText.delete("1.0",END)
        
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="MyData")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from Hospital")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                    conn.commit()
        finally:
            conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.NameofTablet.set(row[0]),
        self.RefNO.set(row[1]),
        self.NoofDoses.set(row[2]),
        self.NumberOfTablets.set(row[3]),
        self.IssueDate.set(row[4]),
        self.DailyDose.set(row[5]),
        self.SideEffect.set(row[6]),
        self.FurInfo.set(row[7]),
        self.BP.set(row[8]),
        self.Storage.set(row[9]),
        self.PName.set(row[10]),
        self.PID.set(row[11]),
        self.DOb.set(row[12]),
        self.Address.set(row[13])
        self.record_id=row[14]

    def update_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="MyData")
            my_cursor = conn.cursor()
            query = """
            UPDATE Hospital 
            SET NameofTablets=%s, ref=%s, doses=%s, nooftablets=%s, issuedate=%s, dailydose=%s, sideeffect=%s, furinfo=%s, bp=%s, storage=%s, pname=%s, pid=%s, dob=%s, address=%s
            WHERE id=%s
        """
            params = (
                self.NameofTablet.get(),
                self.RefNO.get(),
                self.NoofDoses.get(),
                self.NumberOfTablets.get(),
                self.IssueDate.get(),
                self.DailyDose.get(),
                self.SideEffect.get(),
                self.FurInfo.get(),
                self.BP.get(),
                self.Storage.get(),
                self.PName.get(),
                self.PID.get(),
                self.DOb.get(),
                self.Address.get(),
                self.record_id  
            )
            my_cursor.execute(query, params)
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Data Updated Successfully")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            my_cursor.close()
            conn.close()

    def show_data(self):
        self.txtPresciptionText.insert(END,"Name of Tablets:\t\t\t"+self.NameofTablet.get()+"\n")
        self.txtPresciptionText.insert(END,"Reference Number:\t\t\t"+self.RefNO.get()+"\n")
        self.txtPresciptionText.insert(END,"No. Of Doses:\t\t\t"+self.NoofDoses.get()+"\n")
        self.txtPresciptionText.insert(END,"Number of Tablets:\t\t\t"+self.NumberOfTablets.get()+"\n")
        self.txtPresciptionText.insert(END,"Issue Date:\t\t\t"+self.IssueDate.get()+"\n")
        self.txtPresciptionText.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPresciptionText.insert(END,"Side Effects:\t\t\t"+self.SideEffect.get()+"\n")
        self.txtPresciptionText.insert(END,"Further Information:\t\t\t"+self.FurInfo.get()+"\n")
        self.txtPresciptionText.insert(END,"Blood Pressure:\t\t\t"+self.BP.get()+"\n")
        self.txtPresciptionText.insert(END,"Patient Name:\t\t\t"+self.PName.get()+"\n")
        self.txtPresciptionText.insert(END,"Patient ID:\t\t\t"+self.PID.get()+"\n")
        self.txtPresciptionText.insert(END,"Patient DOB:\t\t\t"+self.DOb.get()+"\n")
        self.txtPresciptionText.insert(END,"Address:\t\t\t"+self.Address.get()+"\n")
        self.txtPresciptionText.insert(END,"Serial Number:\t\t\t"+str(self.record_id)+"\n")
    def delete_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Abcd@1234", database="MyData")
        my_cursor = conn.cursor()
        my_cursor.execute("delete from hospital where id=%s",(self.record_id,))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete", "Record Deleted Successfully")

root=Tk()
ob=Hospital(root)
root.mainloop()