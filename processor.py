import sys
import fileinput
from userdata import UserData 


myInput = fileinput.input() if len(sys.argv) is 1 else open(sys.argv[1]) #Read from stdin or fileinput

class Processor:
	def __init__(self):
		self.myDB = {}

	def luhncheck(self, cardNum):
		total = 0
		for index,item in enumerate(cardNum, 1):
			if index % 2 is 0:
				total += int(item)
			else:
				total += sum([int(digit) for digit in str(2*int(item))])	
		return total % 10 == 0

	def processInput(self):
		for line in myInput:
			commandList = line.strip("\n").split(" ")
			operation, user = commandList[0], commandList[1]

			if operation == "Add":
				cardNum, limit = commandList[2], commandList[3]
				self.addCard(user,cardNum,limit)

			elif operation == "Charge":
				charge = commandList[-1]
				self.chargeCard(user, charge)

			elif operation == "Credit":
				credit = commandList[-1]
				self.creditCard(user, credit)
		
		self.printDatabase()


	def addCard(self, user, cardNum, limit):
		if self.luhncheck(cardNum) and int(limit.replace("$","")) >= 0:
			self.myDB[user] = UserData(cardNum, int(limit.replace("$","")))
		else:
			self.myDB[user] = UserData(cardNum, "error", "error")

	def chargeCard(self, user, charge):
		if type(charge) is str:
			charge = int(charge.replace("$",""))

		if self.myDB.get(user) and self.myDB.get(user).limit is not str and charge >= 0:
			#charges should not be negative
			if self.myDB.get(user).balance + charge <= self.myDB.get(user).limit:
				#Only if the charge does not cause the user to go over their limit should we process
				self.myDB.get(user).balance += charge

	def creditCard(self, user, credit):
		if type(credit) is str:
			credit = int(credit.replace("$",""))

		if self.myDB.get(user) and type(self.myDB.get(user).limit) is not str and credit >= 0:
			#credits should not be negative
			self.myDB.get(user).balance -= credit

	def printDatabase(self):
		for key in sorted(list(self.myDB)):
			print key + ": " + ("$" if type(self.myDB[key].balance) is not str else "") + str(self.myDB[key].balance) 

if __name__ == '__main__':
	processor = Processor()
	processor.processInput()