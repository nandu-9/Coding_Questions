
# Defining the class

class reassemble:

    def __init__(self, seg_list):
        self.seg_list = seg_list

    def get_start_seg(self, L):

        # Loop for identifying the starting segment of the whole word
        for ref in L:

            # Setting up the start and end flags for the given reference word segment
            end_flag = False
            start_flag = False

            for item in L:
                if ((ref[-1] == item[0])):
                    end_flag = True

                if ((ref[0] == item[-1])):
                    start_flag = True

            if ((start_flag == False) & (end_flag == True)):
                start_seg = ref
                break
        return start_seg

    def get_assembled_word(self):

        # getting the pre-requisites
        L = self.seg_list
        start_seg = self.get_start_seg(L)

        # Assembling the word
        M = L[0:]
        assembled = start_seg
        while (len(M) > 1):
            for i in range(len(L)):
                if (assembled[-1] == L[i][0]):
                    assembled = assembled[:-1] + L[i]
                    M.remove(L[i])
        return assembled


# Test Cases Check Up
# Specify the inputs
ip1 = ["mput", "Com", "ter"]
ip2 = ["wab", "lesSchw", "ion", "TheCharl", "bCorpor", "rati"]

# Instantiating objects
inp_1 = reassemble(ip1)
inp_2 = reassemble(ip2)

print("\n")
print("Results -------------------------------------\n")
print(inp_1.get_assembled_word(), "\n")
print(inp_2.get_assembled_word(), "\n")
print("End of Results ------------------------------\n")
