class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people = sorted(people, key = lambda x : (-x[0],x[1]))
        ordered = []
        for person in people:
            ordered.insert(person[1],person)
        return ordered
                
                