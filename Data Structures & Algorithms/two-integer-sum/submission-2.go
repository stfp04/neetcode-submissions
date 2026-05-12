func twoSum(nums []int, target int) []int {
    var sums map[int]int = make(map[int]int)

	for i,v := range nums{
		var j, ok = sums[v]
		if ok{
			return []int{j,i}
		}else{
			sums[target - v] = i
		}
	}

	return make([]int, 0, 2)
}
