class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        senior_citizens = 0
        if len(details) == 0:
            return 0
            
        for detail in details:
            if int(detail[11:13]) > 60:
                senior_citizens += 1
        return senior_citizens