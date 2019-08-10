import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def clicked(value):
	
	if value == "First Fit":

		print("First Fit")
		root.withdraw()
		FF = Toplevel()
		FF.title("First Fit")
		FF.geometry("700x500+400+200")


		#=====================================def
		def home():
			FF.withdraw()
			root.deiconify()

		def quit():
			y = messagebox.askyesno("Memory Allocation System","Want to exit ?")
			if y > 0:
				root.destroy()
				FF.destroy()

		def calculate():
			def firstFit(blockSize,processSize):	
				FF.withdraw()
				m = 5
				n = 5
				print(blockSize)
				print(processSize)
				allocation = [-1]*n
				print(allocation)
				for i in range(n):
					for j in range(m):
						if blockSize[j] >= processSize[i]:
							allocation[i] = j
							blockSize[j] = 0
							break
				print(" Process No. Process Size      Block no.")
				for i in range(n):
					print(" ", i + 1, "      ", processSize[i],"      ", end = " ")
					if allocation[i] != -1:
						print(allocation[i] + 1)
						
					else:
						print("Not Allocated")
				 

				v1.set(processSize[0])
				v2.set(processSize[1])
				v3.set(processSize[2])
				v4.set(processSize[3])
				v5.set(processSize[4])
				
				for i in range(0,n):
					if allocation[i] == -1:
						allocation[i] = "Not Allocated"
					else:
						allocation[i] = allocation[i]+1
				t1.set(allocation[0])
				t2.set(allocation[1])
				t3.set(allocation[2])
				t4.set(allocation[3])
				t5.set(allocation[4])
			#=====================================	

			blockSize = [m1.get(),m2.get(),m3.get(),m4.get(),m5.get()]
			processSize = [p1.get(),p2.get(),p3.get(),p4.get(),p5.get()]
			
			
			result = Toplevel()
			result.title("First Fit")
			result.geometry("500x500+400+200")
			tf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			tf.place(x = 0,y = 0)
			#======================================Label
			l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
			l1.place(x = 200,y = 0)
			mf = Frame(result,width = 500,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
			mf.place(x = 0,y = 80)
			bf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			bf.place(x = 0,y = 420)
			p_Label = Label(mf,text = "Processs No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =5,y = 10)
			p1_Label = Label(mf,text = "Processs Size.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p1_Label.place(x =150,y = 10)
			p_Label = Label(mf,text = "Block No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =360,y = 10)
			p_Label1 = Label(mf,text = "1",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label1.place(x =45,y = 50)
			p_Label2 = Label(mf,text = "2",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label2.place(x =45,y = 100)
			p_Label3 = Label(mf,text = "3",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label3.place(x =45,y = 150)
			p_Label4 = Label(mf,text = "4",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label4.place(x =45,y = 200)
			p_Label5 = Label(mf,text = "5",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label5.place(x =45,y = 250)
			#==========================================Declaration
			v1 = StringVar()
			v2 = StringVar()
			v3 = StringVar()
			v4 = StringVar()
			v5 = StringVar()
			t1 = StringVar()
			t2 = StringVar()
			t3 = StringVar()
			t4 = StringVar()
			t5 = StringVar()
			

			#==========================================Entries
			p_Entry1 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v1)
			p_Entry1.place(x = 170,y = 50)
			p_Entry2 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v2)
			p_Entry2.place(x = 170,y = 100)
			p_Entry3 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v3)
			p_Entry3.place(x = 170,y = 150)
			p_Entry4 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v4)
			p_Entry4.place(x = 170,y = 200)
			p_Entry5 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v5)
			p_Entry5.place(x = 170,y = 250) 
			p_Entry1.configure(state = "disabled")
			p_Entry2.configure(state = "disabled")
			p_Entry3.configure(state = "disabled")
			p_Entry4.configure(state = "disabled")
			p_Entry5.configure(state = "disabled")
			m_Entry1 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t1)
			m_Entry1.place(x = 310,y = 50)
			m_Entry2 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t2)
			m_Entry2.place(x = 310,y = 100)
			m_Entry3 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t3)
			m_Entry3.place(x = 310,y = 150)
			m_Entry4 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t4)
			m_Entry4.place(x = 310,y = 200)
			m_Entry5 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t5)
			m_Entry5.place(x = 310,y = 250) 
			m_Entry1.configure(state = "disabled")
			m_Entry2.configure(state = "disabled")
			m_Entry3.configure(state = "disabled")
			m_Entry4.configure(state = "disabled")
			m_Entry5.configure(state = "disabled")
			
			#=========================Back
			def back():
				result.withdraw()
				FF.deiconify()


			#================Button
			Back_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Back",background = "cyan", bd = 3,command = back).place(x = 100,y = 5)
			Quit_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 300,y = 5)
			firstFit(blockSize,processSize)
			


            


		#===========================Frames=======================
		tf = Frame(FF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		tf.place(x = 0,y = 0)
		l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
		l1.place(x = 300,y = 0)
		mf1 = Frame(FF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf1.place(x = 0,y = 80)
		mf2 = Frame(FF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf2.place(x = 350,y = 80)
		bf = Frame(FF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		bf.place(x = 0,y = 420)
		#======================================Proceeses =========================================
		p_Label = Label(mf1,text = "Processes ID",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		p_Label.place(x = 80,y = 5)
		p1_Label = Label(mf1,text = "Process 1",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p1_Label.place(x = 25,y = 70)
		p2_Label = Label(mf1,text = "Process 2",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p2_Label.place(x = 25,y = 120)
		p3_Label = Label(mf1,text = "Process 3",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p3_Label.place(x = 25,y = 170)
		p4_Label = Label(mf1,text = "Process 4",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p4_Label.place(x = 25,y =220)
		p5_Label = Label(mf1,text = "Process 5",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p5_Label.place(x = 25,y = 270)
		#=====================================Declation======================================
		p1 = IntVar()
		p1.set("0")
		p2 = IntVar()
		p2.set("0")
		p3 = IntVar()
		p3.set("0")
		p4 = IntVar()
		p4.set("0")
		p5 = IntVar()
		p5.set("0")
		m1 = IntVar()
		m1.set("0")
		m2 = IntVar()
		m2.set("0")
		m3 = IntVar()
		m3.set("0")
		m4 = IntVar()
		m4.set("0")
		m5 = IntVar()
		m5.set("0")

		#=====================================processes Entry
		p1_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p1)
		p1_Entry.place(x = 200,y = 70)
		p2_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p2)
		p2_Entry.place(x = 200,y = 120)
		p3_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p3)
		p3_Entry.place(x = 200,y = 170)
		p4_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p4)
		p4_Entry.place(x = 200,y = 220)
		p5_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p5)
		p5_Entry.place(x = 200,y = 270)
		#=======================================Memory Label=========================
		m_Label = Label(mf2,text = "Memory Partition",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		m_Label.place(x = 40,y = 5)
		m1_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m1_Label.place(x = 25,y = 70)
		m2_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m2_Label.place(x = 25,y = 120)
		m3_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m3_Label.place(x = 25,y = 170)
		m4_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m4_Label.place(x = 25,y =220)
		m5_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m5_Label.place(x = 25,y = 270)
		#=====================================Memory Entry
		m1_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m1)
		m1_Entry.place(x = 200,y = 70)
		m2_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m2)
		m2_Entry.place(x = 200,y = 120)
		m3_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m3)
		m3_Entry.place(x = 200,y = 170)
		m4_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m4)
		m4_Entry.place(x = 200,y = 220)
		m5_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m5)
		m5_Entry.place(x = 200,y = 270)
		
		#=====================================Buttton===============================
		H_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Home",command = home,background = "cyan", bd = 3).place(x = 10,y = 5)
		R_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Result",command = calculate,background = "cyan", bd = 3).place(x = 300,y = 5)
		Q_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 550,y = 5)



	elif value == "Best Fit":
		print("Best Fit")
		root.withdraw()
		BF = Toplevel()
		BF.title("Best Fit")
		BF.geometry("700x500+400+200")


		#=====================================def
		def home():
			BF.withdraw()
			root.deiconify()

		def quit():
			y = messagebox.askyesno("Memory Allocation System","Want to exit ?")
			if y > 0:
				root.destroy()
				BF.destroy()

		def calculate():
			def BestFit(blockSize,processSize):	
				BF.withdraw()
				m = 5
				n = 5
				print(blockSize)
				print(processSize)
				allocation = [-1]*n
				print(allocation)
				for i in range(n):
					bestIdx = -1
					for j in range(m):
						if blockSize[j] >= processSize[i]:
							if bestIdx == -1:
								bestIdx = j
							elif blockSize[bestIdx] > blockSize[j]:
								bestIdx = j

					if bestIdx != -1:
						allocation[i] = bestIdx
						blockSize[bestIdx] = 0
				


				print(" Process No. Process Size      Block no.")
				for i in range(n):
					print(" ", i + 1, "      ", processSize[i],"      ", end = " ")
					if allocation[i] != -1:
						print(allocation[i] + 1)
						
					else:
						print("Not Allocated")
				 

				v1.set(processSize[0])
				v2.set(processSize[1])
				v3.set(processSize[2])
				v4.set(processSize[3])
				v5.set(processSize[4])
				
				for i in range(0,n):
					if allocation[i] == -1:
						allocation[i] = "Not Allocated"
					else:
						allocation[i] = allocation[i]+1
				t1.set(allocation[0])
				t2.set(allocation[1])
				t3.set(allocation[2])
				t4.set(allocation[3])
				t5.set(allocation[4])
			#=====================================	

			blockSize = [m1.get(),m2.get(),m3.get(),m4.get(),m5.get()]
			processSize = [p1.get(),p2.get(),p3.get(),p4.get(),p5.get()]
			
			
			result = Toplevel()
			result.title("First Fit")
			result.geometry("500x500+400+200")
			tf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			tf.place(x = 0,y = 0)
			#======================================Label
			l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
			l1.place(x = 200,y = 0)
			mf = Frame(result,width = 500,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
			mf.place(x = 0,y = 80)
			bf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			bf.place(x = 0,y = 420)
			p_Label = Label(mf,text = "Processs No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =5,y = 10)
			p1_Label = Label(mf,text = "Processs Size.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p1_Label.place(x =150,y = 10)
			p_Label = Label(mf,text = "Block No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =360,y = 10)
			p_Label1 = Label(mf,text = "1",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label1.place(x =45,y = 50)
			p_Label2 = Label(mf,text = "2",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label2.place(x =45,y = 100)
			p_Label3 = Label(mf,text = "3",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label3.place(x =45,y = 150)
			p_Label4 = Label(mf,text = "4",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label4.place(x =45,y = 200)
			p_Label5 = Label(mf,text = "5",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label5.place(x =45,y = 250)
			#==========================================Declaration
			v1 = StringVar()
			v2 = StringVar()
			v3 = StringVar()
			v4 = StringVar()
			v5 = StringVar()
			t1 = StringVar()
			t2 = StringVar()
			t3 = StringVar()
			t4 = StringVar()
			t5 = StringVar()
			

			#==========================================Entries
			p_Entry1 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v1)
			p_Entry1.place(x = 170,y = 50)
			p_Entry2 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v2)
			p_Entry2.place(x = 170,y = 100)
			p_Entry3 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v3)
			p_Entry3.place(x = 170,y = 150)
			p_Entry4 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v4)
			p_Entry4.place(x = 170,y = 200)
			p_Entry5 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v5)
			p_Entry5.place(x = 170,y = 250) 
			p_Entry1.configure(state = "disabled")
			p_Entry2.configure(state = "disabled")
			p_Entry3.configure(state = "disabled")
			p_Entry4.configure(state = "disabled")
			p_Entry5.configure(state = "disabled")
			m_Entry1 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t1)
			m_Entry1.place(x = 310,y = 50)
			m_Entry2 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t2)
			m_Entry2.place(x = 310,y = 100)
			m_Entry3 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t3)
			m_Entry3.place(x = 310,y = 150)
			m_Entry4 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t4)
			m_Entry4.place(x = 310,y = 200)
			m_Entry5 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t5)
			m_Entry5.place(x = 310,y = 250) 
			m_Entry1.configure(state = "disabled")
			m_Entry2.configure(state = "disabled")
			m_Entry3.configure(state = "disabled")
			m_Entry4.configure(state = "disabled")
			m_Entry5.configure(state = "disabled")
			
			#=========================Back
			def back():
				result.withdraw()
				BF.deiconify()


			#================Button
			Back_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Back",background = "cyan", bd = 3,command = back).place(x = 100,y = 5)
			Quit_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 300,y = 5)
			BestFit(blockSize,processSize)
			


            


		#===========================Frames=======================
		tf = Frame(BF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		tf.place(x = 0,y = 0)
		l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
		l1.place(x = 300,y = 0)
		mf1 = Frame(BF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf1.place(x = 0,y = 80)
		mf2 = Frame(BF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf2.place(x = 350,y = 80)
		bf = Frame(BF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		bf.place(x = 0,y = 420)
		#======================================Proceeses =========================================
		p_Label = Label(mf1,text = "Processes ID",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		p_Label.place(x = 80,y = 5)
		p1_Label = Label(mf1,text = "Process 1",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p1_Label.place(x = 25,y = 70)
		p2_Label = Label(mf1,text = "Process 2",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p2_Label.place(x = 25,y = 120)
		p3_Label = Label(mf1,text = "Process 3",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p3_Label.place(x = 25,y = 170)
		p4_Label = Label(mf1,text = "Process 4",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p4_Label.place(x = 25,y =220)
		p5_Label = Label(mf1,text = "Process 5",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p5_Label.place(x = 25,y = 270)
		#=====================================Declation======================================
		p1 = IntVar()
		p1.set("0")
		p2 = IntVar()
		p2.set("0")
		p3 = IntVar()
		p3.set("0")
		p4 = IntVar()
		p4.set("0")
		p5 = IntVar()
		p5.set("0")
		m1 = IntVar()
		m1.set("0")
		m2 = IntVar()
		m2.set("0")
		m3 = IntVar()
		m3.set("0")
		m4 = IntVar()
		m4.set("0")
		m5 = IntVar()
		m5.set("0")

		#=====================================processes Entry
		p1_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p1)
		p1_Entry.place(x = 200,y = 70)
		p2_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p2)
		p2_Entry.place(x = 200,y = 120)
		p3_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p3)
		p3_Entry.place(x = 200,y = 170)
		p4_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p4)
		p4_Entry.place(x = 200,y = 220)
		p5_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p5)
		p5_Entry.place(x = 200,y = 270)
		#=======================================Memory Label=========================
		m_Label = Label(mf2,text = "Memory Partition",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		m_Label.place(x = 40,y = 5)
		m1_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m1_Label.place(x = 25,y = 70)
		m2_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m2_Label.place(x = 25,y = 120)
		m3_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m3_Label.place(x = 25,y = 170)
		m4_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m4_Label.place(x = 25,y =220)
		m5_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m5_Label.place(x = 25,y = 270)
		#=====================================Memory Entry
		m1_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m1)
		m1_Entry.place(x = 200,y = 70)
		m2_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m2)
		m2_Entry.place(x = 200,y = 120)
		m3_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m3)
		m3_Entry.place(x = 200,y = 170)
		m4_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m4)
		m4_Entry.place(x = 200,y = 220)
		m5_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m5)
		m5_Entry.place(x = 200,y = 270)
		
		#=====================================Buttton===============================
		H_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Home",command = home,background = "cyan", bd = 3).place(x = 10,y = 5)
		R_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Result",command = calculate,background = "cyan", bd = 3).place(x = 300,y = 5)
		Q_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 550,y = 5)


	elif value == "Worst Fit":
		print("Worst Fit")
		root.withdraw()
		WF = Toplevel()
		WF.title("First Fit")
		WF.geometry("700x500+400+200")


		#=====================================def
		def home():
			WF.withdraw()
			root.deiconify()

		def quit():
			y = messagebox.askyesno("Memory Allocation System","Want to exit ?")
			if y > 0:
				root.destroy()
				WF.destroy()

		def calculate():
			def worstFit(blockSize,processSize):	
				WF.withdraw()
				m = 5
				n = 5
				print(blockSize)
				print(processSize)
				allocation = [-1]*n
				for i in range(n):
					wstIdx = -1
					for j in range(m):
						if blockSize[j] >= processSize[i]:
							if wstIdx == -1:
								wstIdx = j
							elif blockSize[wstIdx] < blockSize[j]:
								wstIdx = j 
					if wstIdx != -1:
						allocation[i] = wstIdx
						blockSize[wstIdx] = 0
				

				print(" Process No. Process Size      Block no.")
				for i in range(n):
					print(i + 1, "       ",processSize[i], end = "    ")
					if allocation[i] != -1:
						print(allocation[i] + 1)
						
					else:
						print("Not Allocated")
				 

				v1.set(processSize[0])
				v2.set(processSize[1])
				v3.set(processSize[2])
				v4.set(processSize[3])
				v5.set(processSize[4])
				
				for i in range(0,n):
					if allocation[i] == -1:
						allocation[i] = "Not Allocated"
					else:
						allocation[i] = allocation[i]+1
				t1.set(allocation[0])
				t2.set(allocation[1])
				t3.set(allocation[2])
				t4.set(allocation[3])
				t5.set(allocation[4])
			#=====================================	

			blockSize = [m1.get(),m2.get(),m3.get(),m4.get(),m5.get()]
			processSize = [p1.get(),p2.get(),p3.get(),p4.get(),p5.get()]
			
			
			result = Toplevel()
			result.title("First Fit")
			result.geometry("500x500+400+200")
			tf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			tf.place(x = 0,y = 0)
			#======================================Label
			l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
			l1.place(x = 200,y = 0)
			mf = Frame(result,width = 500,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
			mf.place(x = 0,y = 80)
			bf = Frame(result,width = 500,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
			bf.place(x = 0,y = 420)
			p_Label = Label(mf,text = "Processs No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =5,y = 10)
			p1_Label = Label(mf,text = "Processs Size.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p1_Label.place(x =150,y = 10)
			p_Label = Label(mf,text = "Block No.",font = ("Helvetica",15,"bold"),fg = "blue",bg = "powder blue")
			p_Label.place(x =360,y = 10)
			p_Label1 = Label(mf,text = "1",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label1.place(x =45,y = 50)
			p_Label2 = Label(mf,text = "2",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label2.place(x =45,y = 100)
			p_Label3 = Label(mf,text = "3",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label3.place(x =45,y = 150)
			p_Label4 = Label(mf,text = "4",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label4.place(x =45,y = 200)
			p_Label5 = Label(mf,text = "5",font = ("Helvetica",17,"bold"),fg = "blue",bg = "powder blue")
			p_Label5.place(x =45,y = 250)
			#==========================================Declaration
			v1 = StringVar()
			v2 = StringVar()
			v3 = StringVar()
			v4 = StringVar()
			v5 = StringVar()
			t1 = StringVar()
			t2 = StringVar()
			t3 = StringVar()
			t4 = StringVar()
			t5 = StringVar()
			

			#==========================================Entries
			p_Entry1 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v1)
			p_Entry1.place(x = 170,y = 50)
			p_Entry2 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v2)
			p_Entry2.place(x = 170,y = 100)
			p_Entry3 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v3)
			p_Entry3.place(x = 170,y = 150)
			p_Entry4 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v4)
			p_Entry4.place(x = 170,y = 200)
			p_Entry5 = Entry(mf,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = v5)
			p_Entry5.place(x = 170,y = 250) 
			p_Entry1.configure(state = "disabled")
			p_Entry2.configure(state = "disabled")
			p_Entry3.configure(state = "disabled")
			p_Entry4.configure(state = "disabled")
			p_Entry5.configure(state = "disabled")
			m_Entry1 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t1)
			m_Entry1.place(x = 310,y = 50)
			m_Entry2 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t2)
			m_Entry2.place(x = 310,y = 100)
			m_Entry3 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t3)
			m_Entry3.place(x = 310,y = 150)
			m_Entry4 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t4)
			m_Entry4.place(x = 310,y = 200)
			m_Entry5 = Entry(mf,width = 12,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = t5)
			m_Entry5.place(x = 310,y = 250) 
			m_Entry1.configure(state = "disabled")
			m_Entry2.configure(state = "disabled")
			m_Entry3.configure(state = "disabled")
			m_Entry4.configure(state = "disabled")
			m_Entry5.configure(state = "disabled")
			
			#=========================Back
			def back():
				result.withdraw()
				WF.deiconify()


			#================Button
			Back_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Back",background = "cyan", bd = 3,command = back).place(x = 100,y = 5)
			Quit_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 300,y = 5)
			worstFit(blockSize,processSize)
			


            


		#===========================Frames=======================
		tf = Frame(WF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		tf.place(x = 0,y = 0)
		l1 = Label(tf,text = "First Fit",font =("Helvetica",30,"bold"),fg = "blue",pady = 5,bg = "powder blue")
		l1.place(x = 300,y = 0)
		mf1 = Frame(WF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf1.place(x = 0,y = 80)
		mf2 = Frame(WF,width = 350,height = 340,bd = 7,relief = "ridge",bg = "powder blue")
		mf2.place(x = 350,y = 80)
		bf = Frame(WF,width = 700,height = 80,bd = 7,relief = "ridge",bg = "powder blue")
		bf.place(x = 0,y = 420)
		#======================================Proceeses =========================================
		p_Label = Label(mf1,text = "Processes ID",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		p_Label.place(x = 80,y = 5)
		p1_Label = Label(mf1,text = "Process 1",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p1_Label.place(x = 25,y = 70)
		p2_Label = Label(mf1,text = "Process 2",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p2_Label.place(x = 25,y = 120)
		p3_Label = Label(mf1,text = "Process 3",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p3_Label.place(x = 25,y = 170)
		p4_Label = Label(mf1,text = "Process 4",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p4_Label.place(x = 25,y =220)
		p5_Label = Label(mf1,text = "Process 5",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		p5_Label.place(x = 25,y = 270)
		#=====================================Declation======================================
		p1 = IntVar()
		p1.set("0")
		p2 = IntVar()
		p2.set("0")
		p3 = IntVar()
		p3.set("0")
		p4 = IntVar()
		p4.set("0")
		p5 = IntVar()
		p5.set("0")
		m1 = IntVar()
		m1.set("0")
		m2 = IntVar()
		m2.set("0")
		m3 = IntVar()
		m3.set("0")
		m4 = IntVar()
		m4.set("0")
		m5 = IntVar()
		m5.set("0")

		#=====================================processes Entry
		p1_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p1)
		p1_Entry.place(x = 200,y = 70)
		p2_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p2)
		p2_Entry.place(x = 200,y = 120)
		p3_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p3)
		p3_Entry.place(x = 200,y = 170)
		p4_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p4)
		p4_Entry.place(x = 200,y = 220)
		p5_Entry = Entry(mf1,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = p5)
		p5_Entry.place(x = 200,y = 270)
		#=======================================Memory Label=========================
		m_Label = Label(mf2,text = "Memory Partition",font = ("Helvetica",23,"bold"),fg = "blue",bg = "powder blue")
		m_Label.place(x = 40,y = 5)
		m1_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m1_Label.place(x = 25,y = 70)
		m2_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m2_Label.place(x = 25,y = 120)
		m3_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m3_Label.place(x = 25,y = 170)
		m4_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m4_Label.place(x = 25,y =220)
		m5_Label = Label(mf2,text = "Memory size",font = ("Helvetica",20,),fg = "blue",bg = "powder blue")
		m5_Label.place(x = 25,y = 270)
		#=====================================Memory Entry
		m1_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m1)
		m1_Entry.place(x = 200,y = 70)
		m2_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m2)
		m2_Entry.place(x = 200,y = 120)
		m3_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m3)
		m3_Entry.place(x = 200,y = 170)
		m4_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m4)
		m4_Entry.place(x = 200,y = 220)
		m5_Entry = Entry(mf2,width = 7,font = ("Helvetica",15),bd = 6,relief = "ridge",textvariable = m5)
		m5_Entry.place(x = 200,y = 270)
		
		#=====================================Buttton===============================
		H_Btn = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Home",command = home,background = "cyan", bd = 3).place(x = 10,y = 5)
		R_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Result",command = calculate,background = "cyan", bd = 3).place(x = 300,y = 5)
		Q_Btn  = Button(bf,font  = ("georgia",12,"bold"),width = 9,height = 2,relief = RIDGE,text = "Quit",background = "cyan", bd = 3,command = quit).place(x = 550,y = 5)




	
	
root = Tk()
root.title("Memory Allocation System")

top = Frame(root, width = 400,height = 50, bd = 6, relief  = "ridge")
top.pack(anchor = S)
title = Label(top,font = ("Helvetica",16,"bold"),fg = "blue",text = "Memory Allocation System")
title.pack(anchor = S)
bottom = Frame(root, width = 400,height = 350,bd = 6,relief = "ridge")
bottom.pack(anchor = S) 
label = Label(bottom,font = ("Helvetica",13,"bold"),fg = "blue",text = "Which System you want to load ?").pack(anchor = S)

MODES = [("First Fit","First Fit"),("Best Fit","Best Fit"),("Worst Fit","Worst Fit"),]
fit = StringVar()
fit.set("First Fit")
for text,mode in MODES:
	Radiobutton(bottom,text = text,font = ("Helvetica",13,),variable = fit,value = mode).pack(anchor = S)


#radio_1 = Radiobutton(bottom,text = "First Fit",font = ("Helvetica",13,),value = 1).place(x = 130,y = 70)
#radio_2 = Radiobutton(bottom,text = "Best Fit",font = ("Helvetica",13,),value = 2).place(x = 130,y = 90)
#radio_3 = Radiobutton(bottom,text = "Worst Fit",font = ("Helvetica",13,),value = 3).place(x = 130,y = 110)
EnterBtn = Button(bottom,font  = ("georgia",12),width = 5,relief = RIDGE,text = "Enter",background = "cyan", bd = 3,command =lambda: clicked(fit.get())).pack(anchor = S)
label = Label(bottom,font = ("Helvetica",2,"bold"),fg = "blue",text = "").pack(anchor = S)
def quit():
	y = messagebox.askyesno("Memory Allocation System","Want to Exit the System ?")
	if y >0:
		root.destroy()
ExitBtn = Button(bottom,font  = ("georgia",12),width = 5,relief = RIDGE,text = "Exit",background = "cyan", bd = 3,command = quit)
ExitBtn.pack(anchor = S)

root.mainloop()
