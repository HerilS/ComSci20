class BloodType:
    def __init__(self, bloodType):
        self.allBloodTypes = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if bloodType not in self.allBloodTypes:
            raise ValueError("ERR: Valid blood type not provided")
        self.bloodType = bloodType
        self.antigens = self.destructureBloodType(bloodType)

    def destructureBloodType(self, bloodType):
        # turn every character in bloodType into a list iterable
        bloodTypeList = list(bloodType)
        # O is not a valid antigen, so it is removed from beginning
        if 'O' in bloodTypeList:
            bloodTypeList.pop(0)
        # + automatically turns into D antigen / Rh factor
        if '+' in bloodTypeList:
            bloodTypeList[-1] = 'D'
        # - means that D antigen / Rh factor is simply not present, so it is removed from list
        if '-' in bloodTypeList:
            bloodTypeList.pop()
        return bloodTypeList

    def composeBloodType(self, destructuredBloodType):
        # do opposite of destructureBloodType
        if 'D' in destructuredBloodType:
            destructuredBloodType[-1] = '+'
        else:
            destructuredBloodType.append('-')

        # if destructuredBloodType only contains '+' or '-', append 'O' antigen at the beginning of the array
        if set(destructuredBloodType) == set(['-']) or set(destructuredBloodType) == set(['+']):
            return ''.join(['O'] + destructuredBloodType)

        return ''.join(destructuredBloodType)

    def getAllDestructuredBloodTypes(self):
        destructureBloodTypeList = []
        for bloodType in self.allBloodTypes:
            destructureBloodTypeList.append(self.destructureBloodType(bloodType))
        return destructureBloodTypeList

    def getBloodType(self):
        return self.bloodType

    def getAntigens(self):
        return 'Antigens include: {0}'.format(', '.join(self.antigens))

    def getAntibodies(self):
        antibodies = ['A', 'B', 'D']
        for antigen in self.antigens:
            if antigen in antibodies:
                antibodies.remove(antigen)
        return 'Antibodies include: {0}'.format(', '.join(antibodies))

    def canGiveBloodTo(self):
        destructuredBloodTypes = self.getAllDestructuredBloodTypes()
        canGiveBloodToList = []
        for i in destructuredBloodTypes:
            if set(self.antigens).issubset(set(i)):
                canGiveBloodToList.append(self.composeBloodType(i))
        return '{0} people can give blood to people who have these blood types: {1}'.format(self.bloodType, ', '.join(canGiveBloodToList))

    def canRecieveBloodFrom(self):
        destructureBloodTypeList = self.getAllDestructuredBloodTypes()
        canRecieveBloodFrom = []
        for i in destructureBloodTypeList:
            if set(i).issubset(set(self.antigens)):
                canRecieveBloodFrom.append(self.composeBloodType(i))

        return '{0} people can recieve blood from people who have these blood types: {1}'.format(self.bloodType, ', '.join(canRecieveBloodFrom))




APositive = BloodType("A-")
print(APositive.canRecieveBloodFrom())



