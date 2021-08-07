class MaxSubarray:
    def getMaxSubarray(self, arr: [])->int:
        """
        create a function to hold the state/result:
                sum[i][j] = sum with start index i and j is length
        Relation between states:
              sum
        base case:
              sum[i][1] = num[i] for i =

        :param arr:
        :return:
        """
        if len(arr)==0:
            return 0
        maxi = con_sub_arr = arr[0]
        for i in range(1, len(arr)):
            num = arr[i]
            con_sub_arr = max(num, con_sub_arr+num)
            maxi = max(con_sub_arr, maxi)
        return maxi

if __name__ == "__main__":
    ma = MaxSubarray()
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(ma.getMaxSubarray(arr))