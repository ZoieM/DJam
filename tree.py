
#TEST TEST TES

def printLevelByLevel(self, root):
	currLevel = [root]

	while(currLevel):
		newLevel = []
		for n in currLevel:
			print n.value
		if root.left != None:
			newLevel.append(root.left)
		if root.right != None:
			newLevel.append(root.right)
		currLevel = newLevel

def averageOfLevels(self, root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    currLevel = [root]
    result = []
    
    while currLevel: 
        newLevel = []
        len_level = len(currLevel)
        temp = []
        for n in currLevel:
            temp.append(n.val)
        sum_level = sum(temp)
        result.append(sum_level/len_level)
        if root.left != None:
            newLevel.append(root.left)
        if root.left != None: 
            newLevel.append(root.right)
        currLevel = newLevel
    return result

